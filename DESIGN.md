---
version: alpha
name: Phantom Analysis
description: An analysis of Phantom's design language — a dual-polarity crypto-wallet system that swings between a warm cream daylight surface and an inky market-data nightscape, unified by a single signature lavender-purple, a rounded-pill button language, and a playful illustrated card vocabulary.

colors:
  primary: "#ab9ff2"
  on-primary: "#3c315b"
  lavender: "#e2dffe"
  indigo: "#3c315b"
  lilac-white: "#fdfcfe"
  canvas: "#fffdf8"
  canvas-dark: "#000000"
  surface-dark: "#1c1c1c"
  surface-dark-soft: "#28282c"
  surface-dark-elevated: "#2e2e32"
  surface-dark-raised: "#34343a"
  cloud: "#ededef"
  hairline: "#ededef"
  ink: "#1c1c1c"
  muted: "#86848d"
  muted-on-dark: "#b4b4b4"
  muted-mid: "#808080"
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.indigo}"
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
    textColor: "{colors.canvas}"
    typography: "{typography.display}"
  cta-band-deep:
    backgroundColor: "{colors.indigo}"
    textColor: "{colors.canvas}"
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
    backgroundColor: "{colors.lilac-white}"
    textColor: "{colors.indigo}"
    rounded: "{rounded.lg}"
  feature-card-elevated:
    backgroundColor: "{colors.lilac-white}"
    textColor: "{colors.indigo}"
    rounded: "{rounded.lg}"
    shadow: "0px 0px 4px 0px rgba(226, 223, 254, 1)"
  feature-card-dark:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
  token-stat-card:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.md}"
  market-row:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  blog-card:
    backgroundColor: "{colors.lilac-white}"
    textColor: "{colors.indigo}"
    rounded: "{rounded.lg}"
  text-input:
    textColor: "{colors.indigo}"
    typography: "{typography.body}"
  email-capture-band:
    backgroundColor: "{colors.cloud}"
    textColor: "{colors.indigo}"
    typography: "{typography.heading-2}"
    rounded: "{rounded.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.indigo}"
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


## Overview

Phantom presents a design system with a split personality, and that split is the whole point. The marketing and editorial surfaces — the home page, the blog — live in warm daylight: a barely-off-white cream (`{colors.canvas}` — #fffdf8) carries playful, illustration-led storytelling where a friendly purple ghost wanders through cards of phone mockups, cloud doodles, and confetti. The product-data surfaces — the token explorer — flip to an inky nightscape (`{colors.canvas-dark}` — #000000) where dense market tables glow with green-up / red-down price signals. The same brand walks confidently in both rooms because one element never changes: the signature Phantom Purple (`{colors.primary}` — #ab9ff2), the exact lavender of the ghost mascot, anchoring every primary call-to-action regardless of which polarity surrounds it.

The geometry is soft and generous. Buttons are fully-rounded pills (`{rounded.pill}`) or near-pill (`{rounded.xl}`), cards carry a relaxed `{rounded.lg}` (24px) corner, and the navigation rides inside a `{rounded.nav}` (100px) floating capsule. Type is set in Phantom's proprietary face across a wide range — a towering `{typography.display}` (96px) headline down to a `{typography.caption}` (12px) label — with a distinctive light `350` body weight that keeps long-form copy airy rather than heavy. Nothing is sharp; everything is rounded, padded, and a little bit toy-like, which is exactly how a self-custody crypto wallet earns trust from a non-expert audience.

Depth is handled almost entirely without heavy shadows. Light surfaces separate by tiny shifts in tint (cream → `{colors.lilac-white}` → `{colors.cloud}`) and a single soft lavender glow (`{components.feature-card-elevated.shadow}`); dark surfaces separate by stepping up a near-black ladder (`{colors.canvas-dark}` → `{colors.surface-dark}` → `{colors.surface-dark-soft}` → `{colors.surface-dark-elevated}` → `{colors.surface-dark-raised}`). The brand's sense of elevation is color-driven, not shadow-driven.

**Key Characteristics:**
- Dual-polarity system: a cream daylight mode (`{colors.canvas}`) for marketing/editorial and an inky nightscape (`{colors.canvas-dark}`) for market data, both governed by one spec.
- A single signature accent — Phantom Purple (`{colors.primary}`) — is the only constant CTA color across every page and polarity.
- Pill-first button language: primary actions at `{rounded.xl}`, soft/light hero pills at `{rounded.pill}`, the floating nav at `{rounded.full}`.
- Playful, illustration-led storytelling on light surfaces — colorful doodle cards, the ghost mascot, confetti heroes — paired with austere, data-dense tables on dark surfaces.
- Color-driven elevation: light surfaces step through cream→lilac→cloud tints, dark surfaces climb a near-black ladder; shadows reduced to a single lavender glow.
- Market semantics built in: `{colors.success}` green for price-up / live / tags, `{colors.error}` red for price-down.
- Color-block page rhythm on the home page: dark confetti hero → cream feature bands → deep-indigo "secured by us" band → lavender "Get started" CTA band → cream email-capture footer.

## Colors

Source pages: home (`phantom.com/`), explore (`/explore`), blog (`/learn/blog`), developers (`/learn/developers`).

### Brand & Accent
- **Phantom Purple** (`{colors.primary}` — #ab9ff2): The signature lavender of the ghost mascot and the single highest-visibility color. Reserved for the primary CTA on every page and polarity.
- **Soft Lavender** (`{colors.lavender}` — #e2dffe): A pale tint of the primary, used for the full-bleed "Get started. Download Phantom" CTA band, soft pill buttons, and the small eyebrow pills above section headings.
- **Deep Indigo** (`{colors.indigo}` — #3c315b): The brand's dark-purple anchor — the wordmark color, the "Controlled by you, secured by us" band background, the text sitting on lavender/purple surfaces, and headings on light surfaces.
- **Lilac White** (`{colors.lilac-white}` — #fdfcfe): A faintly lilac near-white used for raised cards and the white hero "Download Phantom" pill on light surfaces.

### Surface
- **Cream Canvas** (`{colors.canvas}` — #fffdf8): The default warm-off-white page background for marketing and editorial surfaces.
- **Pure Black** (`{colors.canvas-dark}` — #000000): The page background of the token explorer — true black behind dense market data.
- **Near-Black** (`{colors.surface-dark}` — #1c1c1c): The confetti hero background and the base dark surface for the developer hub.
- **Dark Soft / Elevated / Raised** (`{colors.surface-dark-soft}` — #28282c, `{colors.surface-dark-elevated}` — #2e2e32, `{colors.surface-dark-raised}` — #34343a): A three-step near-black ladder that distinguishes cards, panels, and rows on dark surfaces.
- **Cloud** (`{colors.cloud}` — #ededef): A light neutral gray used for the email-capture band surface and quiet light-mode panels.
- **Hairline** (`{colors.hairline}` — #ededef): The 1px divider / border tint on light surfaces.

### Text
- **Ink** (`{colors.ink}` — #1c1c1c): Primary near-black body text on light surfaces.
- **Deep Indigo** (`{colors.indigo}` — #3c315b): Heading text on light surfaces and the on-brand text color over lavender/purple.
- **Muted Gray** (`{colors.muted}` — #86848d): Secondary / supporting text on light surfaces.
- **Muted on Dark** (`{colors.muted-on-dark}` — #b4b4b4): Secondary text on dark surfaces (table sub-labels, captions).
- **Muted Mid** (`{colors.muted-mid}` — #808080): Tertiary gray for the quietest labels.

### Semantic
- **Market Green** (`{colors.success}` — #45e863): Price-up movement, "Live" status pills, and editorial tag badges.
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
