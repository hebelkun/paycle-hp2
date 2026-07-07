# -*- coding: utf-8 -*-
"""ニュース記事追加スクリプト。

記事ページの生成と、news.html / sitemap.xml / llms.txt への登録を
一括で整合性を保って行う。

使い方:
  python scripts/add_news.py \
      --slug example-article \
      --date 2026-07-07 \
      --title "記事タイトル" \
      --description "メタディスクリプション（100〜120字目安）" \
      --body body.html \
      [--tag "お知らせ"]        # 記事ページ上部のタグ（省略時: お知らせ）
      [--list-tag "特許"]       # news.html一覧でタイトル前に付くタグ（省略時: なし）
      [--image path/to/img.webp --image-alt "画像の説明"]  # 記事画像（OGP兼用）

--body には記事本文のHTML断片ファイル（<p>や<h2>の並び）を渡す。
--image は任意の場所のファイルを指定でき、記事ディレクトリへコピーされる。
"""
import argparse
import html
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://paycle.com/"
LOGO = BASE + "images/logo.png"
SITE_NAME = "PAYCLE｜株式会社ペイクル"

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title_esc}｜PAYCLE</title>
  <meta name="description" content="{desc_esc}" />
  <link rel="canonical" href="{url}" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="{site_name}" />
  <meta property="og:title" content="{title_esc}｜PAYCLE" />
  <meta property="og:description" content="{desc_esc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{og_image}" />
  <meta property="og:locale" content="ja_JP" />
  <meta name="twitter:card" content="{card}" />
  <meta property="article:published_time" content="{iso}" />
  <script type="application/ld+json">
{article_jsonld}
  </script>
  <script type="application/ld+json">
{breadcrumb_jsonld}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../css/style.css" />
</head>
<body>

  <div class="nav-wrap">
    <nav class="nav" aria-label="グローバルナビゲーション">
      <a href="../../index.html" class="nav-logo" aria-label="PAYCLE ホーム"><img src="../../images/logo.png" alt="PAYCLE" /></a>
      <ul class="nav-links">
        <li><a href="../../services.html">Services</a></li>
        <li><a href="../../rd.html">R&amp;D</a></li>
        <li><a href="../../cases.html">Cases</a></li>
        <li><a href="../../news.html" class="active">News</a></li>
        <li><a href="../../about.html">About</a></li>
      </ul>
      <div class="nav-cta">
        <a href="../../contact.html" class="btn btn-primary">Contact</a>
        <button class="nav-toggle" aria-label="メニュー" aria-expanded="false" aria-controls="nav-menu"><span></span><span></span><span></span></button>
      </div>
      <div class="nav-menu" id="nav-menu">
        <a href="../../services.html">Services</a><a href="../../rd.html">R&amp;D</a><a href="../../cases.html">Cases</a><a href="../../news.html">News</a><a href="../../about.html">About</a>
        <a href="../../contact.html" class="btn btn-primary">Contact</a>
      </div>
    </nav>
  </div>

  <div class="container">
    <div class="page-head">
      <p class="kicker">News</p>
    </div>
  </div>

  <section class="section" style="padding-top:8px;">
    <div class="container article">
      <div class="article-meta">
        <span class="news-date"><time datetime="{iso}">{dotted}</time></span>
        <span class="tag">{tag_esc}</span>
      </div>
      <h1 class="h1 article-title">{title_esc}</h1>
{figure}      <div class="article-body">
{body}
      </div>

      <a href="../../news.html" class="article-back">ニュース一覧へ戻る</a>
    </div>
  </section>

  <section class="cta-band">
    <h2 class="h1">お問い合わせ</h2>
    <p>取材・掲載のご依頼はお問い合わせよりご連絡ください。</p>
    <div class="actions"><a href="../../contact.html" class="btn btn-primary btn-arrow">お問い合わせ</a></div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand"><img src="../../images/logo.png" alt="PAYCLE" /><p>ブロックチェーン・AI・耐量子暗号の研究開発から、システムの設計・開発まで支援するテクノロジー企業。</p></div>
        <div class="footer-col"><h4>Company</h4><a href="../../services.html">Services</a><a href="../../rd.html">R&amp;D</a><a href="../../cases.html">Cases</a></div>
        <div class="footer-col"><h4>Information</h4><a href="../../news.html">News</a><a href="../../about.html">About</a><a href="../../contact.html">Contact</a></div>
        <div class="footer-col"><h4>Legal</h4><a href="../../privacy-policy.html">Privacy Policy</a></div>
      </div>
      <div class="footer-bottom"><span>© PAYCLE Inc.</span><a href="../../privacy-policy.html">プライバシーポリシー</a></div>
    </div>
  </footer>

  <script src="../../js/main.js"></script>
</body>
</html>
"""


def die(msg):
    print("ERROR:", msg, file=sys.stderr)
    sys.exit(1)


def jsonld(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def build_article_page(a, url, iso, dotted, og_image, card, body_html):
    article = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": a.title,
        "description": a.description,
        "datePublished": iso,
        "dateModified": iso,
        "inLanguage": "ja",
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "image": [og_image],
        "author": {"@type": "Organization", "name": "株式会社ペイクル", "url": BASE},
        "publisher": {"@type": "Organization", "name": "株式会社ペイクル",
                      "logo": {"@type": "ImageObject", "url": LOGO}},
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "ホーム", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": "ニュース", "item": BASE + "news.html"},
            {"@type": "ListItem", "position": 3, "name": a.title},
        ],
    }
    if a.image:
        img_name = os.path.basename(a.image)
        figure = ('      <figure class="article-figure">\n'
                  f'        <img src="{html.escape(img_name)}" alt="{html.escape(a.image_alt or a.title)}" />\n'
                  '      </figure>\n')
    else:
        figure = ""
    body = "\n".join("            " + line.strip() if line.strip() else ""
                     for line in body_html.strip().splitlines())
    return PAGE_TEMPLATE.format(
        title_esc=html.escape(a.title, quote=True),
        desc_esc=html.escape(a.description, quote=True),
        url=url, og_image=og_image, card=card, iso=iso, dotted=dotted,
        site_name=SITE_NAME,
        tag_esc=html.escape(a.tag),
        article_jsonld=jsonld(article),
        breadcrumb_jsonld=jsonld(breadcrumb),
        figure=figure, body=body,
    )


def insert_news_list(a, iso, dotted):
    """news.html の一覧へ日付降順の位置に挿入する。"""
    path = os.path.join(ROOT, "news.html")
    src = read(path)
    href = f"news/{a.slug}/index.html"
    if href in src:
        die(f"news.html に {href} が既に存在します")
    list_tag = f'<span class="tag">{html.escape(a.list_tag)}</span>' if a.list_tag else ""
    entry = (f'        <a class="news-item" href="{href}">'
             f'<span class="news-date">{dotted}</span>'
             f'<span class="news-title">{list_tag}{html.escape(a.title)}</span>'
             f'<span class="chev">→</span></a>')
    items = re.findall(r'^( *<a class="news-item".*?</a>)$', src, re.M)
    if not items:
        die("news.html に news-item が見つかりません")
    # 自分より古い最初の項目の直前へ（同日なら新規を上に）
    target = None
    for it in items:
        m = re.search(r'news-date">(\d{4})\.(\d{2})\.(\d{2})', it)
        d = "-".join(m.groups())
        if d <= iso:
            target = it
            break
    if target:
        src = src.replace(target, entry + "\n" + target, 1)
    else:  # 全部より古い＝一番下
        src = src.replace(items[-1], items[-1] + "\n" + entry, 1)
    write(path, src)


def insert_sitemap(url, iso):
    path = os.path.join(ROOT, "sitemap.xml")
    src = read(path)
    if url in src:
        die(f"sitemap.xml に {url} が既に存在します")
    entry = f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{iso}</lastmod>\n  </url>"
    blocks = re.findall(r'  <url>\n    <loc>[^<]+</loc>\n    <lastmod>([\d-]+)</lastmod>\n  </url>', src)
    target_date = next((d for d in blocks if d <= iso), None)
    if target_date:
        old = re.search(
            r'  <url>\n    <loc>[^<]+</loc>\n    <lastmod>' + re.escape(target_date) + r'</lastmod>\n  </url>',
            src).group(0)
        src = src.replace(old, entry + "\n" + old, 1)
    else:
        src = src.replace("</urlset>", entry + "\n</urlset>", 1)
    write(path, src)


def insert_llms(a, url, iso):
    path = os.path.join(ROOT, "llms.txt")
    src = read(path)
    if url in src:
        die(f"llms.txt に {url} が既に存在します")
    entry = f"- [{a.title}]({url})（{iso}）: {a.description}"
    lines = re.findall(r'^- \[.*?\]\(https://paycle\.com/news/.*?\)（([\d-]+)）.*$', src, re.M)
    full_lines = re.findall(r'^- \[.*?\]\(https://paycle\.com/news/.*?\)（[\d-]+）.*$', src, re.M)
    target = None
    for full, d in zip(full_lines, lines):
        if d <= iso:
            target = full
            break
    if target:
        src = src.replace(target, entry + "\n" + target, 1)
    elif full_lines:
        src = src.replace(full_lines[-1], full_lines[-1] + "\n" + entry, 1)
    else:
        src = src.rstrip("\n") + "\n" + entry + "\n"
    write(path, src)


def main():
    ap = argparse.ArgumentParser(description="ニュース記事を追加する")
    ap.add_argument("--slug", required=True, help="URLスラッグ（英小文字・数字・ハイフン）")
    ap.add_argument("--date", required=True, help="公開日 YYYY-MM-DD")
    ap.add_argument("--title", required=True)
    ap.add_argument("--description", required=True)
    ap.add_argument("--body", required=True, help="本文HTML断片ファイルのパス")
    ap.add_argument("--tag", default="お知らせ", help="記事ページ上部のタグ")
    ap.add_argument("--list-tag", default="", dest="list_tag", help="一覧タイトル前のタグ（例: 特許）")
    ap.add_argument("--image", default="", help="記事画像ファイル（記事ディレクトリへコピーされる）")
    ap.add_argument("--image-alt", default="", dest="image_alt", help="記事画像のalt")
    a = ap.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.slug):
        die("slug は英小文字・数字・ハイフンのみ（例: example-article-2026）")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.date):
        die("date は YYYY-MM-DD 形式で指定してください")
    if not os.path.exists(a.body):
        die(f"本文ファイルがありません: {a.body}")
    if a.image and not os.path.exists(a.image):
        die(f"画像ファイルがありません: {a.image}")

    art_dir = os.path.join(ROOT, "news", a.slug)
    if os.path.exists(art_dir):
        die(f"既に存在します: news/{a.slug}/")

    iso = a.date
    dotted = iso.replace("-", ".")
    url = f"{BASE}news/{a.slug}/"

    if a.image:
        og_image = url + os.path.basename(a.image)
        card = "summary_large_image"
    else:
        og_image, card = LOGO, "summary"

    body_html = read(a.body)
    page = build_article_page(a, url, iso, dotted, og_image, card, body_html)

    # ここから書き込み（バリデーション後）
    os.makedirs(art_dir)
    if a.image:
        shutil.copy2(a.image, os.path.join(art_dir, os.path.basename(a.image)))
    write(os.path.join(art_dir, "index.html"), page)
    insert_news_list(a, iso, dotted)
    insert_sitemap(url, iso)
    insert_llms(a, url, iso)

    print(f"OK: news/{a.slug}/index.html を作成")
    print("OK: news.html / sitemap.xml / llms.txt を更新")
    print(f"URL: {url}")


if __name__ == "__main__":
    main()
