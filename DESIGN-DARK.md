---
version: alpha
name: Phantom Analysis
description: An analysis of Phantom's design language — a dual-polarity crypto-wallet system that swings between a warm cream daylight surface and an inky market-data nightscape, unified by a single signature lavender-purple, a rounded-pill button language, and a playful illustrated card vocabulary.

colors:
  primary: "#ab9ff2"
  on-primary: "#1c1c1c"
  lavender: "#e2dffe"
  indigo: "#3c315b"
  lilac-white: "#fdfcfe"
  canvas: "#0c0c0e"
  canvas-dark: "#000000"
  surface-dark: "#1c1c1c"
  surface-dark-soft: "#28282c"
  surface-dark-elevated: "#2e2e32"
  surface-dark-raised: "#34343a"
  cloud: "#1c1c1c"
  hairline: "#2e2e32"
  ink: "#ffffff"
  on-dark: "#fffdf8"
  muted: "#b4b4b4"
  muted-on-dark: "#86848d"
  muted-mid: "#6c6c6c"
  success: "#45e863"
  error: "#ff0037"

typography:
  display:
    fontFamily: Phantom
    fontSize: 96px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -0.02em
  display-sm:
    fontFamily: Phantom
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -0.02em
  heading-1:
    fontFamily: Phantom
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.01em
  heading-2:
    fontFamily: Phantom
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.01em
  heading-3:
    fontFamily: Phantom
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: Phantom
    fontSize: 20px
    fontWeight: 350
    lineHeight: 1.5
    letterSpacing: 0
  body:
    fontFamily: Phantom
    fontSize: 16px
    fontWeight: 350
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: Phantom
    fontSize: 15px
    fontWeight: 350
    lineHeight: 1.5
    letterSpacing: 0
  ui:
    fontFamily: Phantom
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  ui-sm:
    fontFamily: Phantom
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  caption:
    fontFamily: Phantom
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.01em

rounded:
  xs: 2px
  sm: 8px
  md: 12px
  lg: 24px
  xl: 32px
  pill: 96px
  nav: 100px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 48px

components:
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.ui}"
    rounded: "{rounded.nav}"
    height: 64px
  button-nav-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.ui}"
    rounded: "{rounded.nav}"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display}"
  cta-band-deep:
    backgroundColor: "{colors.indigo}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display}"
  cta-band-soft:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.indigo}"
    typography: "{typography.display}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.ui}"
    rounded: "{rounded.xl}"
    padding: 16px 32px
  button-soft:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.indigo}"
    typography: "{typography.ui}"
    rounded: "{rounded.pill}"
    padding: 32px
  button-light:
    backgroundColor: "{colors.lilac-white}"
    textColor: "{colors.indigo}"
    typography: "{typography.ui}"
    rounded: "{rounded.pill}"
    padding: 32px
  badge-pill:
    backgroundColor: "{colors.success}"
    textColor: "{colors.indigo}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
  eyebrow-pill:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.indigo}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
  feature-card:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
  feature-card-elevated:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    shadow: "0px 0px 4px 0px rgba(226, 223, 254, 1)"
  feature-card-dark:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
  token-stat-card:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
  market-row:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  blog-card:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
  text-input:
    textColor: "{colors.ink}"
    typography: "{typography.body}"
  email-capture-band:
    backgroundColor: "{colors.cloud}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-2}"
    rounded: "{rounded.lg}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"

  # ─── Examples (illustrative) — auto-derived ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Re-uses feature-card chrome with brand canvas surface."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses caption eyebrow typography; body uses body-sm."
    headerBackground: "{colors.canvas}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.section}"
    captionTypography: "{typography.body}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---

> This is the **dark mode** version of the design system. It is fully self-contained — use this document alone when building dark-themed interfaces.

## Overview

This is the nightscape polarity of Phantom's design system — the inky, market-ready face that the token explorer already wears, applied across the whole catalog. The page sits on a tinted near-black canvas (`{colors.canvas}` — #0c0c0e) deepening to true black (`{colors.canvas-dark}` — #000000) behind dense market tables. Cards, panels, and rows climb a near-black surface ladder rather than separating by tint, and light text (`{colors.ink}` — #ffffff, `{colors.on-dark}` — #fffdf8) carries the type. One element never changes between polarities: the signature Phantom Purple (`{colors.primary}` — #ab9ff2), the exact lavender of the ghost mascot, anchoring every primary call-to-action against the dark.

The geometry is soft and generous. Buttons are fully-rounded pills (`{rounded.pill}`) or near-pill (`{rounded.xl}`), cards carry a relaxed `{rounded.lg}` (24px) corner, and the navigation rides inside a `{rounded.nav}` (100px) floating capsule. Type is set in Phantom's proprietary face across a wide range — a towering `{typography.display}` (96px) headline down to a `{typography.caption}` (12px) label — with a distinctive light `350` body weight that keeps long-form copy airy rather than heavy. Nothing is sharp; everything is rounded, padded, and a little bit toy-like, which is exactly how a self-custody crypto wallet earns trust from a non-expert audience.

Depth is communicated by stepping up the near-black ladder (`{colors.surface-dark}` — #1c1c1c → `{colors.surface-dark-soft}` — #28282c → `{colors.surface-dark-elevated}` — #2e2e32 → `{colors.surface-dark-raised}` — #34343a), plus a single soft lavender glow (`{components.feature-card-elevated.shadow}`) where a card needs to lift off the black. Two deliberate light islands survive into dark mode: the lavender "Get started" CTA band (`{colors.lavender}`) and the white "Download" hero pill (`{colors.lilac-white}`), both kept light on purpose because the brand uses them that way against its own dark hero. The brand's sense of elevation is color-driven, not shadow-driven.

**Key Characteristics:**
- Inky nightscape governed by the same spec as the light system — a tinted near-black canvas (`{colors.canvas}`) deepening to true black (`{colors.canvas-dark}`) for market data.
- A single signature accent — Phantom Purple (`{colors.primary}`) — is the only constant CTA color across every page and polarity.
- Pill-first button language: primary actions at `{rounded.xl}`, soft/light hero pills at `{rounded.pill}`, the floating nav at `{rounded.nav}`.
- Light text (`{colors.ink}` / `{colors.on-dark}`) on a stepped near-black surface ladder; cards become dark panels rather than white tiles.
- Deliberate light islands preserved: the lavender CTA band (`{colors.lavender}`) and the white hero pill (`{colors.lilac-white}`) stay light against the dark.
- Market semantics built in: `{colors.success}` green for price-up / live / tags, `{colors.error}` red for price-down — unchanged from light mode.
- Color-driven elevation: every depth level is a discrete step up the near-black ladder, softened by one barely-there lavender glow.

## Colors

Source pages: home (`phantom.com/`), explore (`/explore`), blog (`/learn/blog`), developers (`/learn/developers`).

### Brand & Accent
- **Phantom Purple** (`{colors.primary}` — #ab9ff2): The signature lavender of the ghost mascot and the single highest-visibility color. Reserved for the primary CTA on every surface; takes near-black text (`{colors.on-primary}` — #1c1c1c).
- **Soft Lavender** (`{colors.lavender}` — #e2dffe): A pale tint of the primary, preserved as a light island in dark mode — the "Get started" CTA band, soft pill buttons, and the small eyebrow pills above section headings.
- **Deep Indigo** (`{colors.indigo}` — #3c315b): The brand's dark-purple anchor — the wordmark, the "secured by us" band background (a lifted purple band on the dark canvas), and the text sitting on lavender/purple surfaces.
- **Lilac White** (`{colors.lilac-white}` — #fdfcfe): The white "Download" hero pill, kept light against the dark hero exactly as the brand ships it.

### Surface
- **Near-Black Canvas** (`{colors.canvas}` — #0c0c0e): The default tinted near-black page background.
- **Pure Black** (`{colors.canvas-dark}` — #000000): True black behind dense market-data tables.
- **Near-Black Surface** (`{colors.surface-dark}` — #1c1c1c): The hero, nav, and footer surface — first step up from canvas.
- **Dark Soft / Elevated / Raised** (`{colors.surface-dark-soft}` — #28282c, `{colors.surface-dark-elevated}` — #2e2e32, `{colors.surface-dark-raised}` — #34343a): A three-step near-black ladder that distinguishes cards, panels, and rows.
- **Cloud Panel** (`{colors.cloud}` — #1c1c1c): A quiet dark panel used for the email-capture band surface.
- **Hairline** (`{colors.hairline}` — #2e2e32): The 1px divider / border tint that separates dark surfaces.

### Text
- **Ink** (`{colors.ink}` — #ffffff): Primary white text for headings and card copy on dark surfaces.
- **On-Dark** (`{colors.on-dark}` — #fffdf8): Warm cream-white text on the darkest surfaces — heroes, bands, market rows.
- **Muted Gray** (`{colors.muted}` — #b4b4b4): Secondary / supporting text on dark surfaces.
- **Muted on Dark** (`{colors.muted-on-dark}` — #86848d): Tertiary text (table sub-labels, captions).
- **Muted Mid** (`{colors.muted-mid}` — #6c6c6c): The quietest labels.

### Semantic
- **Market Green** (`{colors.success}` — #45e863): Price-up movement, "Live" status pills, and editorial tag badges — unchanged from light mode.
- **Market Red** (`{colors.error}` — #ff0037): Price-down movement and the negative-state accent card.

## Typography

### Font Family
Phantom ships a proprietary typeface (referenced here as **Phantom**) across the entire site — a warm, geometric-humanist sans with generously open counters. The most distinctive trait is the very light **350** body weight, which keeps long-form copy and large display headlines feeling airy rather than dense; weights step up to `600` for headings and UI chrome and `700` for occasional emphasis.

### Hierarchy

Each level maps directly to a typography token in the front matter:

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display}` | 96px | 600 | 1.05 | -0.02em | Home / blog / developer hero headlines |
| `{typography.display-sm}` | 64px | 600 | 1.05 | -0.02em | Explore page hero ("Explore the ecosystem") |
| `{typography.heading-1}` | 36px | 600 | 1.1 | -0.01em | Major section headers ("Trading tools for everyone") |
| `{typography.heading-2}` | 32px | 600 | 1.15 | -0.01em | Sub-section headers, email-capture prompts |
| `{typography.heading-3}` | 24px | 600 | 1.25 | 0 | Card titles, smaller section headers |
| `{typography.body-lg}` | 20px | 350 | 1.5 | 0 | Lead paragraphs / sub-headlines |
| `{typography.body}` | 16px | 350 | 1.5 | 0 | Default body copy, links |
| `{typography.body-sm}` | 15px | 350 | 1.5 | 0 | Supporting copy, pill labels |
| `{typography.ui}` | 14px | 600 | 1.2 | 0 | Nav items, button labels |
| `{typography.ui-sm}` | 13px | 600 | 1.2 | 0 | Dense table labels, secondary UI |
| `{typography.caption}` | 12px | 600 | 1.2 | 0.01em | Eyebrow pills, smallest labels |

### Principles
The scale is dramatic at the top end — a 96px display headline towers over 16px body — but the light `350` weight keeps even that giant headline feeling friendly. UI chrome (nav, buttons, table headers) consistently uses the `600` weight at small sizes for legibility, while editorial body copy stays at `350` for an open, magazine-like read.

### Note on Font Substitutes
Phantom's proprietary face is not publicly licensed. A close open-source substitute is **Inter** (use weights 300 / 600 / 700 to approximate the 350 / 600 / 700 ladder), or **General Sans** for a slightly warmer, more geometric feel. With either substitute, increase line-height fractionally on the 96px `{typography.display}` headline and apply the `-0.02em` tracking to match Phantom's tight display set.

## Layout

### Spacing System
- **Base unit**: 8px
- **Tokens (front matter)**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.section}` 48px
- Primary button padding is `16px 32px` (`{spacing.lg}` × double-`{spacing.xxl}`); soft/light hero pills carry a uniform `32px` (`{spacing.xxl}`) pad. Cards group content on the 8px grid with `{spacing.xl}`–`{spacing.xxl}` interior padding.

### Grid & Container
Content sits within a centered max-width container (~1280px, matching the dominant `1280px` breakpoint). Marketing sections use a generous 2–4 column card grid that collapses progressively; the explore page runs a full-width data table edge-to-edge within the container. Card grids favor equal-height tiles with consistent `{spacing.xl}` gutters.

### Whitespace Philosophy
Whitespace is used to let illustrations breathe — feature cards are surrounded by ample cream so the playful doodle art reads as the hero of each tile. On dark data surfaces the opposite logic applies: rows are tight and dense to maximize information, with separation handled by the near-black surface ladder rather than gaps.

### Responsive Strategy

#### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Desktop XL | 1536px / 1280px | Full multi-column card grids, edge-to-edge market table |
| Laptop | 1024px | Card grids reduce columns (4→2/3), nav stays expanded |
| Tablet | 768px | Nav collapses toward a compact menu; grids move to 2-up / 1-up |
| Mobile | 640px / 425px / 400px | Single-column stacks, full-width pill CTAs, market table becomes horizontally scrollable / condensed rows |

#### Touch Targets
Pill buttons (`{components.button-primary}`, `{components.button-soft}`, `{components.button-light}`) carry `16px 32px`–`32px` padding, comfortably exceeding the 44×44px minimum. Nav items are sized for thumb reach on mobile.

#### Collapsing Strategy
The floating capsule nav (`{components.nav-bar}`) condenses to a compact menu below the tablet breakpoint. Multi-column marketing card grids collapse 4→2→1. The explore market table — the densest surface — switches to horizontal scroll or condensed rows so price/change columns stay aligned rather than wrapping.

#### Image Behavior
Illustration art and phone mockups inside feature cards scale fluidly within their `{rounded.lg}` containers; token logos in the market table are fixed-size circular avatars. Editorial blog cards lead with a full-bleed illustrated thumbnail clipped to the card's top corners.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (light) | Tint shift only: `{colors.canvas}` → `{colors.lilac-white}` → `{colors.cloud}` | Default cards and panels on light surfaces |
| Glow (light) | Single soft lavender glow `0px 0px 4px 0px rgba(226,223,254,1)` (`{components.feature-card-elevated.shadow}`) | Raised / hover-resting cards, modals, toasts |
| Stepped (dark) | Near-black ladder: `{colors.canvas-dark}` → `{colors.surface-dark}` → `{colors.surface-dark-soft}` → `{colors.surface-dark-elevated}` → `{colors.surface-dark-raised}` | Cards, panels, rows on dark surfaces |

The brand deliberately avoids heavy drop shadows. On light surfaces, elevation is communicated almost entirely through small background-tint steps plus one barely-there lavender bloom; on dark surfaces, every level of depth is a discrete step up the near-black gray ladder.

### Decorative Depth
The dark confetti hero scatters small colored particle dots across `{colors.surface-dark}` for atmospheric depth without shadow. Marketing cards lean on layered illustration — phone mockups, cloud doodles, the ghost mascot — to create a sense of dimensional playfulness that flat color alone could not.

## Shapes

### Border Radius Scale

Each level maps directly to a `rounded` token in the front matter:

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 2px | Tiny inline chips, control corners |
| `{rounded.sm}` | 8px | List items, small tiles |
| `{rounded.md}` | 12px | Token stat cards, compact panels |
| `{rounded.lg}` | 24px | Standard feature / blog / content cards |
| `{rounded.xl}` | 32px | Primary CTA button corner |
| `{rounded.pill}` | 96px | Soft / light hero pill buttons |
| `{rounded.nav}` | 100px | Floating nav capsule and the nav "Download" CTA pill |
| `{rounded.full}` | 9999px | Status / tag / eyebrow pills, circular avatars |

### Photography Geometry
Token and avatar imagery is circular (`{rounded.full}`). Illustration thumbnails and product mockups are clipped to `{rounded.lg}` card corners. The market table's token logos are uniform circular avatars sized for row density. There is no full-bleed photography — the brand's imagery vocabulary is illustration and UI mockup rather than photographic.

## Components

> **No hover states documented.** Every component spec below documents only Default and Active states. Variants live as separate entries in the `components:` front matter.

### Navigation

**`nav-bar`** — floating capsule top navigation
- Background `{colors.canvas}` on light pages / dark surfaces on dark pages, text `{colors.indigo}`, type `{typography.ui}`, rounded `{rounded.nav}` (100px), height 64px. Rides as a floating white capsule with the ghost wordmark left, menu links center, a circular search button, and a primary CTA pill far right.

**`button-nav-primary`** — the top-nav "Download" CTA pill
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.ui}`, rounded `{rounded.nav}` (100px). The fully-rounded Phantom-purple pill anchored to the far right of `{components.nav-bar}` — the everyday primary call-to-action present in the nav on every page.

### Heroes & Bands

**`hero-dark`** — confetti hero
- Background `{colors.surface-dark}`, light text `{colors.canvas}`, display headline `{typography.display}`. Scatters colored particle dots behind a centered headline and a single white pill CTA.

**`cta-band-deep`** — "secured by us" deep-indigo band
- Full-bleed `{colors.indigo}` background, light text `{colors.canvas}`, display headline `{typography.display}`. Houses a trio of feature cards (white, yellow, coral) against the deep purple.

**`cta-band-soft`** — "Get started. Download Phantom" band
- Full-bleed `{colors.lavender}` background, deep `{colors.indigo}` text, display headline `{typography.display}`, with a dark download pill centered beneath.

### Buttons

**`button-primary`** — the Phantom Purple CTA
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.ui}`, padding `16px 32px`, rounded `{rounded.xl}`. The everyday call-to-action across every page. Active state shrinks slightly via transform (scale press) — no color change.

**`button-soft`** — soft lavender pill
- Background `{colors.lavender}`, text `{colors.indigo}`, type `{typography.ui}`, padding `32px`, rounded `{rounded.pill}`. A quieter secondary pill used on light marketing surfaces.

**`button-light`** — white hero pill
- Background `{colors.lilac-white}`, text `{colors.indigo}`, type `{typography.ui}`, padding `32px`, rounded `{rounded.pill}`. The white "Download Phantom" pill that sits on the dark confetti hero.

### Badges & Pills

**`badge-pill`** — status / tag pill
- Background `{colors.success}`, text `{colors.indigo}` (light) / `{colors.canvas}` (dark), type `{typography.body-sm}`, rounded `{rounded.full}`. Used for "Live" market status and editorial category tags.

**`eyebrow-pill`** — section eyebrow
- Background `{colors.lavender}`, text `{colors.indigo}`, type `{typography.caption}`, rounded `{rounded.full}`. The small lavender label that sits above each marketing section heading.

### Cards & Containers

**`feature-card`** — light marketing card
- Background `{colors.lilac-white}`, text `{colors.indigo}`, rounded `{rounded.lg}`. The standard illustration-led tile on cream surfaces.

**`feature-card-elevated`** — raised marketing card
- Background `{colors.lilac-white}`, text `{colors.indigo}`, rounded `{rounded.lg}`, with the single soft lavender glow `0px 0px 4px 0px rgba(226,223,254,1)`. Used where a card needs to lift off the cream.

**`feature-card-dark`** — dark surface card
- Background `{colors.surface-dark-soft}`, light text `{colors.canvas}`, rounded `{rounded.lg}`. Article tiles and panels on the developer hub and explore surfaces.

**`token-stat-card`** — trending-token card
- Background `{colors.surface-dark-soft}`, light text `{colors.canvas}`, rounded `{rounded.md}`. The compact "Trending Tokens" cards atop the explore page showing a token, price, and green/red percent change.

**`blog-card`** — illustrated editorial card
- Background `{colors.lilac-white}`, text `{colors.indigo}`, rounded `{rounded.lg}`. A blog post tile leading with a full-bleed illustrated thumbnail, title, tag pills, and date.

### Signature Components

**`market-row`** — explore data-table row
- Background `{colors.canvas-dark}`, light text `{colors.canvas}`, type `{typography.body-sm}`. A dense market-overview row: circular token avatar + name, price, a green/red 24h percent change, 24h volume, and market cap — no trailing call-to-action.

**`email-capture-band`** — footer subscribe band
- Background `{colors.cloud}`, text `{colors.indigo}`, prompt type `{typography.heading-2}`, rounded `{rounded.lg}`. The "Enter your email" band that recurs at the foot of every page, pairing a `{components.text-input}` with a primary submit pill.

### Inputs & Forms

**`text-input`** — email / search field
- Text `{colors.indigo}`, type `{typography.body}`. Minimally-chromed field; the brand keeps the input itself quiet and lets the surrounding capture band carry the styling.

### Footer

**`footer`** — site footer
- Background `{colors.canvas}` (light pages) / dark surfaces (dark pages), text `{colors.indigo}`, type `{typography.body-sm}`. Standard multi-column link footer beneath the email-capture band.

### Examples (illustrative)

> Kit-mirror demonstration surfaces. Each `ex-*` entry references brand-native primitives so downstream consumers re-skin the same 10 surfaces consistently against Phantom's tokens.

**`ex-pricing-tier`** — Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface.
- Properties: `backgroundColor`, `textColor`, `borderColor`, `rounded`, `padding`

**`ex-pricing-tier-featured`** — Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode).
- Properties: `backgroundColor`, `textColor`, `rounded`, `padding`

**`ex-product-selector`** — What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery).
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-cart-drawer`** — Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart).
- Properties: `backgroundColor`, `rounded`, `padding`, `item-divider`

**`ex-app-shell-row`** — Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator.
- Properties: `backgroundColor`, `activeIndicator`, `rounded`, `padding`

**`ex-data-table-cell`** — Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm.
- Properties: `headerBackground`, `headerTypography`, `bodyTypography`, `cellPadding`, `rowBorder`

**`ex-auth-form-card`** — Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-modal-card`** — Modal dialog surface — same chrome as feature-card with elevated shadow.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-empty-state-card`** — Empty-state illustration frame.
- Properties: `backgroundColor`, `rounded`, `padding`, `captionTypography`

**`ex-toast`** — Toast notification surface — feature-card shape + medium shadow.
- Properties: `backgroundColor`, `rounded`, `padding`, `typography`


## Do's and Don'ts

### Do
- Reserve `{colors.primary}` for primary actions — it is the one constant across both polarities.
- Pair `{colors.primary}` and `{colors.lavender}` surfaces with `{colors.indigo}` text, never with pure black.
- Use the cream `{colors.canvas}` daylight surface for marketing and editorial; reserve the `{colors.canvas-dark}` nightscape for dense market data.
- Communicate elevation with tint steps and the single lavender glow on light, and with the near-black surface ladder on dark.
- Keep buttons fully pill-shaped (`{rounded.xl}` / `{rounded.pill}` / `{rounded.full}`) and cards at `{rounded.lg}`.
- Set body copy in the light `350` weight (`{typography.body}`) and UI chrome in `600` (`{typography.ui}`).
- Use `{colors.success}` for price-up / live and `{colors.error}` for price-down — the market semantics are part of the brand.

### Don't
- Don't introduce a second brand accent — `{colors.primary}` is the only signature color; green and red are reserved for market semantics, not decoration.
- Don't drop heavy drop-shadows onto light cards; the brand's only light-mode elevation is the soft lavender glow.
- Don't set sharp corners — there are no right-angle buttons or cards in this system.
- Don't place `{colors.primary}` text on a `{colors.canvas}` background for body copy; it is a fill color, not a text color (use `{colors.ink}` / `{colors.indigo}`).
- Don't mix the cream daylight surface and the black nightscape within a single section — switch polarity at section boundaries, not inside them.
- Don't render the market table on a light surface; its green/red density is designed for the `{colors.canvas-dark}` nightscape.
