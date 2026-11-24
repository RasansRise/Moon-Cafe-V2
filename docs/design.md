# Moon Café — Website UI/UX Design Specification

> **Version:** 2.0 — Approved desktop visual baseline and implementation-time responsive strategy  
> **Date:** 2026-11-23  
> **Status:** Desktop appearance/structure accepted by project owner; responsive layouts to be finalized in development, content placeholders not approved; Contact visual still pending  
> **Companion files:** `plan.md` (scope and functionality), `seo-strategy.md` (search requirements), `menu-inventory.md` (menu taxonomy/products), `Moon Brand Manual.pdf` (source-of-truth visual identity).  
> **Development:** HTML + CSS + vanilla JavaScript; GSAP only for purposeful animations. No checkout, search, user accounts, CMS or product detail pages.

## 0. Governance and decision labels

- **[APPROVED]** = explicitly selected in the conversation. Must not be silently replaced.
- **[BRAND]** = directly sourced from supplied Moon Café Brand Manual, subject to original asset availability and font licensing.
- **[PROPOSED]** = practical design specification drafted for implementation; review in mockups before treating as approved.
- **[TBD]** = information/decision missing, or user copy needing confirmation.

**Scope rule:** This document specifies *how* the approved pages should look and behave. It does not create new features/pages or change the requirements in `plan.md`. Where a suggestion conflicts with a confirmed scope item, `plan.md` wins; where a visual element conflicts with the Brand Manual, the Brand Manual wins.

## 1. Design intent and principles

1. **[APPROVED] Clean but visually engaging.** Modern, clear, fresh presentation appropriate for university students and coffee enthusiasts, not excessively busy.
2. **[APPROVED] Performance-conscious motion.** Interactive hero and polished GSAP motion, but movement must not compromise initial content visibility, responsiveness or usability.
3. **[APPROVED] Mostly dark experience.** Dark is the default canvas; **gold sections may be used selectively**, with accessible contrast.
4. **[APPROVED] Strict Brand Manual compliance.** No new palette, typography family, restyled logo or brand reinterpretation without approval.
5. **[APPROVED] Mobile-first.** Same page content and core interactions across mobile/tablet/desktop; adapt layout, density and controls to available space.
6. **[APPROVED] Informational-first.** The primary user outcomes are seeing the menu/products and finding a branch, plus discovering the brand and loyalty scheme.
7. **[PROPOSED] Clear over clever.** All core content readable without waiting for animation; motion must never gate access to prices, calories, ingredients or directions.

## 2. Brand foundation — strict reference

### 2.1 Colors

| Token (semantic role proposed) | Brand value | Source / use |
|---|---|---|
| `--brand-gold` | `#DAAF67` | **[BRAND]** Primary gold, Brand Manual p.13. Highlights, restrained actions, ornament. |
| `--brand-gold-light` | `#FED899` | **[BRAND]** Secondary gold 1, Brand Manual p.13. Light accents, focus-adjacent elements. |
| `--brand-cream` | `#FFE7C2` | **[BRAND]** Secondary gold 2, Brand Manual p.13. Select contrasting text/surfaces. |
| `--brand-black` | black in manual (no published hex value) | **[BRAND]** Use original approved black swatch value once available; do **not** describe an invented charcoal hex as a brand color. |
| `--brand-white` | white in manual (no published hex value) | **[BRAND]** Use original approved white swatch value once available. |

**[PROPOSED] Semantic design tokens:** `--surface-base`, `--surface-elevated`, `--surface-contrast`, `--text-primary`, `--text-muted`, `--border-subtle`, `--focus-ring`. Resolve these using **only approved brand black/white/golds**, including opacity/transparency when appropriate. Dark surfaces should remain close to official brand black; don't insert unapproved blue, violet or teal neutrals. Verify readable contrast in actual mockups, especially small gold-on-dark or dark-on-gold type. Do not treat gold as appropriate for every paragraph.

### 2.2 Typography

- **[BRAND] English:** **Proxima Nova**, Light / Regular / Bold as demonstrated (manual p.14).
- **[BRAND] Arabic:** **Helvetica Neue Arabic**, Light / Regular / Bold as demonstrated (manual p.14).
- **[APPROVED]** Use those families; do not swap to Google Fonts/Montserrat without explicit brand approval.
- **[TBD]** Obtain licensed **webfont** files and rights; do not distribute font files in the repo without permission. Define robust system fallback stacks for loading failures only; fallback is not a brand replacement.
- **[PROPOSED]** Desktop visual hierarchy (responsive `clamp()` ranges): display 44–72px; H1 36–56px; H2 28–40px; H3 21–28px; body 16–18px; metadata 14–16px. **These are not brand-manual measurements**, require visual review in both scripts.
- **[PROPOSED]** Arabic needs independent line-height and letter-spacing tuning; do not apply decorative English tracking to Arabic. Keep body line-height ~1.6–1.85 Arabic / ~1.5–1.7 English; validate against actual fonts.

### 2.3 Logo, pattern and imagery

- **[BRAND]** Use original approved SVG logos, choosing an Arabic/English version and black/white/gold variant appropriate to background (manual pp.5–10).
- **[BRAND]** No stretched, recolored, rotated, distorted, shadowed or effect-treated logo, and never put logo on noisy/low-contrast background (manual p.11). Obey logo placement/clearance shown in manual (pp.7, 12); verify using original vectors.
- **[BRAND]** Moon/coffee-inspired geometric motif and repeated emblem patterns appear in manual pp.15–20. **[PROPOSED]** Use as sparse cropped decorative areas (e.g., hero edge, section transitions), not behind dense information or as constant wallpaper.
- **[APPROVED]** Product images will have **consistent studio backgrounds**. No lifestyle-background mixing within category grids. **[TBD]** Final asset crop, aspect ratio, actual supplied photography, and studio backdrop color (must match approved materials).
- **[PROPOSED]** Use genuine café/branch photography for branches where supplied, with consistent treatment; do not fabricate branch exteriors.
- **[TBD]** Brand founding year: manual sample applications include `Since 2007`, while earlier website content appears to reference 2010. Do not commit a year to UI until client verifies.

## 2.4 Desktop visual source of truth (approved appearance only, 2026-11-23)

The project owner selected the **latest revised desktop images** (dark, predominantly black, restrained gold, subtle neutral card borders) as the **visual and structural baseline** for implementation. These screenshots supersede earlier, heavily gold-outlined versions. This is an approval of **appearance, composition, component treatments and section ordering**, **not of placeholder copy, menu items, locations, prices, calories, dates or rewards claims**. The photos in mockups may also be illustrative and must be replaced by client-approved photos.

| Reference screenshot / page | Implementation contract |
|---|---|
| Homepage | Hero with three takeaway cups, editorial About composition, **featured-product carousel**, branch preview cards, Rewards section, simple footer; **Hero contains its own Explore Menu CTA** irrespective of whether the reference screenshot visibly shows it |
| Menu landing | Drinks and Food **stacked sections**, category-photo cards, desktop Drinks **3 + 2** editorial grid and Food **3** cards |
| Category page | Three-column desktop product-photo grid, product name and View Details affordance |
| Product popup (open state) | Image on left, product details/ingredients/size-price-calories at right, restrained gold perimeter, quiet neutral internal dividers |
| Branches | **Three-column desktop photo card grid**; neutral card outlines and filled gold directions CTAs |
| Mega Menu | Dark overlay panel, Drinks/Food columns, thin neutral outline/separators, gold headings and Explore Full Menu action |

**Implementation hierarchy:** preserve approved structure and styling; make minimal layout adjustments for actual text, accessibility and responsive fit. No single screenshot dimension or placeholder count should hard-code a page's height. The **Contact** page still lacks an approved visual mockup and will use the shared design system provisionally until reviewed.

## 3. Information architecture and global page map

**[APPROVED]** Four top-level pages per locale: Home, Menu, Branches, Contact. Home contains **About section**, not a separate About page. Menu is organized into **Drinks and Food sections**; these are groupings, not additional pages. Each of the eight categories is a dedicated page per language. No product detail pages.

```text
Moon Café (same content architecture in Arabic and English)
├── Home
│   └── About (section/anchor only)
├── Menu
│   ├── Drinks (section only)
│   │   ├── Hot Coffee (category page)
│   │   ├── Hot Drinks (category page)
│   │   ├── Iced Coffee (category page)
│   │   ├── Crash (category page)
│   │   └── Refreshing Drinks (category page)
│   └── Food (section only)
│       ├── Bakery & Desserts (category page)
│       ├── Sandwiches & Croissants (category page)
│       └── Snacks (category page)
├── Branches
└── Contact
```

- **[APPROVED]** **Menu landing layout: SECTIONS**, not tabs and not only two giant entry cards. Both Drinks (5 categories) and Food (3 categories) are visible on one scrolling page, using distinct headings and clickable category presentations.
- **[APPROVED]** Header menu uses a dropdown, with Drinks/Food group headings and links to relevant category pages. The main Menu link must still open `/menu/`.
- **[PROPOSED]** Menu section order: Drinks first, Food second, per working inventory. Navigation/header language labels localized; category URLs are proposed under `/menu/{slug}/` and `/en/menu/{slug}/` in `seo-strategy.md` and await hosting confirmation.
- **[PROPOSED]** Home About nav item, if needed, anchors to the current locale homepage `#about`, not a standalone document. Rewards nav item, if present, links to the current locale homepage `#rewards`; there is no standalone Rewards page.

## 4. Page layouts — mobile-first specifications

### 4.1 Shared page template

**[PROPOSED]** Skip-to-content link, site header, `<main>` with one clear page-level H1, optional contextual intro, substantive content, simple footer. Use landmark elements; headings follow content logic rather than visual size. Max-width content container ~1200–1280px after review, with responsive side gutters; avoid horizontal overflow. Reuse consistent button, breadcrumb (on category pages), category tile, product card, popup and branch-card components.

### 4.2 Home

**[APPROVED]** Required section sequence: **Hero → About → Featured Menu / Products → Branches Preview → Loyalty / Points Redemption**. Keep page medium-length: enough brand identity to feel rich, but fast access to menu and products.

| Section | Content / action | Initial UX direction |
|---|---|---|
| Hero | Brand statement + **[APPROVED] primary Explore Menu CTA** linking to the Menu landing page (`/menu/` or `/en/menu/` depending on active language); **[PROPOSED]** secondary Find a Branch CTA | **[APPROVED] Interactive animation**. **[PROPOSED]** lightweight product / moon-inspired visual reveal tied to pointer or gentle scroll, with static image fallback and no essential copy embedded in animation. |
| About | Concise brand story, its heritage and distinctive offer, client-approved copy | **[PROPOSED]** short heading + brief narrative + meaningful image/motif; anchor `#about`. No invented start date. |
| Featured Menu / Products | Product preview carousel and a clear link to full Menu | **[APPROVED desktop visual]** product imagery and slider composition follow the supplied homepage reference. **[PROPOSED]** touch swipe carousel with accessible controls on mobile; do not replace this with a full eight-category block. |
| Branches | Short preview and direct link to complete branch list | **[PROPOSED]** short brand-relevant teaser, branch CTA; do not imply geolocation without permission or functionality. |
| Loyalty | Explanation of how points earn/redeem, with outbound link to external service | **[APPROVED]** explanatory section + external link only; do not build points/login/redemption inside site. Instructions/URL are **[TBD]**. |

**[APPROVED] Hero CTA contract:** The hero must include a prominent, immediately visible and keyboard-accessible **Explore Menu / اكتشف المنيو** button or link. It navigates to the matching language’s Menu landing page (not a category page, modal or external destination). It must remain usable before/without GSAP and must never be obscured by the hero animation or preloader. **[PROPOSED]** Find a Branch may be a secondary CTA in or near the hero.

**[TBD]** Earlier user wrote a third homepage CTA as «حول مش»; text is unclear and should not be incorporated into live copy. External loyalty CTA copy is pending.

### 4.3 Menu landing (`/menu/`)

**[APPROVED]** Sections layout:

1. Localized H1 (`Menu` / `المنيو`), optional concise intro.
2. **Drinks** heading and **five** clickable categories: Hot Coffee, Hot Drinks, Iced Coffee, Crash, Refreshing Drinks.
3. **Food** heading and **three** clickable categories: Bakery & Desserts, Sandwiches & Croissants, Snacks.

**[APPROVED desktop visual]** Preserve the mixed desktop category-card composition: Drinks **3 cards then 2 wider cards**, Food **3 cards**. **[PROPOSED responsive]** one column on mobile and two columns on tablet where appropriate. Preserve neutral thin card borders and gold arrow CTAs. Render real anchor links so a category page is accessible with JS disabled. No Food/Drinks tabs, no separate Food/Drinks pages. Keep images lightweight and avoid heavy scroll effects on all eight tiles.

### 4.4 Category page template (8 categories × 2 languages)

**[APPROVED]** Products in a **grid**. Clicking a product opens a **popup/modal** containing detailed information; no product detail URL. **[APPROVED]** Product images use consistent studio-style backgrounds.

**[PROPOSED]** Category page structure:
1. Header/breadcrumb `Menu / [Category]` linking to Menu index.
2. Category H1, optional concise category introduction.
3. Consistent product-card grid (1 mobile, 2 tablet, 3 desktop; review card width and copy lengths).
4. Each card shows verified product image and localized name, plus optional concise info and clear cue `View details` / equivalent localized label.
5. Modal displays product image, name, ingredients, and clearly separated **size / price / calories** values **for every applicable variant**. Show all size rows or offer a size toggle if content volume makes it preferable; this specific layout remains **[PROPOSED]**.
6. Product variants must not be invented: `S`, `D`, `M`, `L` are source labels whose meaning and grouping require confirmation. The 69 provided entries are **menu entries**, not necessarily 69 distinct product cards. Whether to combine Espresso S/D and Macchiato S/D into shared cards is **[TBD]**.

**Product popup accessibility/behavior — [PROPOSED] design acceptance:**
- Trigger is keyboard-activatable button with accessible label; open overlay with `role="dialog"`, `aria-modal="true"`, dialog title linked via `aria-labelledby` (or native `<dialog>`).
- Move focus inside on open; trap focus within while open; `Escape` and visible close button dismiss; return focus to original trigger.
- Modal scrolls internally on small devices if content exceeds viewport; never clip ingredients or variant tables; backdrop scroll should be appropriately managed.
- Close on backdrop click if implemented, but never rely on backdrop alone. Respect RTL and LTR.
- Since product specifics exist in a JS-opened popup, **[PROPOSED/SEO]** keep substantial localized product names and category content in crawlable page HTML; decide with `seo-strategy.md` how detailed ingredient/calorie text is exposed for accessibility/crawlability, without creating product pages or hiding essential information behind JS-only rendering.
- Product with missing required price/calories is a **content-blocker**, not silently displayed as 0 or fake data. For unspecified size, never invent a size selector.

### 4.5 Branches

**[APPROVED desktop visual]** **Grid of branch cards**, **3 columns on desktop**, with large photo, branch name, verified full address and a distinct **View on Map / Get Directions** link per branch. **Do not convert this to a list.** No embedded map and no branch filters.

**[PROPOSED responsive]** Use **2 columns on tablet, 1 on mobile**, subject to content-fit QA. Images appear above the card information on all sizes. Cards have subtle 1px neutral borders, rounded corners and gold filled map CTA. Use flex/grid within cards so buttons align along the bottom despite different address lengths. Hours/phone only where provided. No fabricated branch distance/open-now labels or directions links. Lazy-load offscreen photos.

### 4.6 Contact

**[APPROVED]** Contact information and links only. No form.

**[PROPOSED]** Clear H1 and short introductory copy; phone (`tel:`), email (`mailto:`), approved social/external links; optional branch CTA. Match actual available channels. No dummy numbers or links. Keep page intentionally concise.

## 5. Header, navigation and footer

### 5.1 Header

- **[APPROVED]** Header is visible at the top and becomes a **sticky** compact state during scrolling, with a smooth, polished transition.
- **[APPROVED visual]** Nav items: Home, Menu (dropdown), Branches, Contact; Rewards may appear as a **homepage section anchor** in the Homepage/expanded mobile navigation. Language switcher visible; localized copy and correct alignment. Do **not** create a standalone Rewards page.
- **[APPROVED desktop visual]** Desktop **Mega Menu** has a Drinks column and a Food column with all 8 category links, an **Explore Full Menu** direct link, dark background and subtle neutral perimeter/separator borders (not heavy gold outlines). Keyboard navigation and clear focus states; open by click and keyboard, optional hover enhancement; dismiss on Escape/outside click.
- **[PROPOSED]** Mobile uses one accessible nav disclosure/drawer with same destinations and expanded category groups; **no new bottom-navigation concept**. Ensure the dropdown is usable by touch, not hover-only.
- **[PROPOSED]** Sticky transition uses background opacity/height/transform carefully. Prevent content jump using stable header space; avoid page content being obscured by anchors (`scroll-margin-top`).
- **[PROPOSED]** Switch language to the corresponding localized page, ideally preserving category and context; fall back to locale menu/home only where exact equivalent unavailable.

### 5.2 Footer

**[APPROVED]** Simple footer containing logo, sitemap/navigation, contact and approved social links. **[PROPOSED]** Compact responsive columns with minimal legal/copyright line if client supplies it; no newsletter/signup, unapproved new pages, or extra widgets.

## 6. Component design contracts

| Component | Required content / behavior | Motion and states |
|---|---|---|
| Primary CTA | Localized label, meaningful destination, visible focus, touch target | **[APPROVED] subtle** color/underline/arrow movement only |
| Secondary CTA | Clear action hierarchy, high-contrast outline/text | Gentle opacity/border transition |
| Category card | Image/label/accessible link to category URL | Small translate or image scale; disable nonessential animation on touch/reduced-motion |
| Product card | Image, name, details trigger; no misleading add-to-cart | Light hover/focus emphasis, consistent grid heights where possible |
| Product modal | Name, image, ingredients, variant price/calories, dismiss button | Fast opacity + small transform (optional), with no content shift |
| Branch card | Large photo, branch name, address, verified directions button; grid layout | Subtle border feedback, aligned map CTA; no simulated map interaction |
| Dropdown / mobile nav | All category links, keyboard/touch support | Short opacity/height motion; must remain usable without GSAP |
| Language switcher | AR/EN with present page mapping | Minimal feedback, no delayed navigation |
| Loader | Brand-compatible preloader | **[APPROVED] exists; [PROPOSED] short, nonblocking** and with static/reduced-motion fallback |

**[APPROVED] Micro-interactions: simple and subtle.** Prefer CSS transitions for buttons/cards/focus and reserve GSAP for page-level sequence, hero or scroll effects that genuinely need timeline control.

## 7. Motion system and performance constraints

- **[APPROVED]** GSAP is allowed/desired, but should not harm website speed.
- **[APPROVED]** Smooth scrolling and scroll-based animations desired.
- **[APPROVED]** Preloader is desired.
- **[APPROVED]** Hero should be interactive, not merely a static image or background video.
- **[PROPOSED]** Set interaction durations around 150–300ms and entrance/reveal around 350–650ms after design review. These are initial guidance, not mandatory brand timings.
- **[PROPOSED]** Animate `transform` and `opacity` as a default; avoid excessive `filter`, box-shadow animation, large-area blur/parallax and layout-reflow properties.
- **[PROPOSED]** Load core content immediately. Do not wait for all remote assets or GSAP initialization before allowing navigation. Preloader should be brief, dismiss reliably on errors and respect accessibility; it must never become a blocking second-loading-screen. Fallback render must work with JS disabled or GSAP unavailable.
- **[PROPOSED]** Native CSS `scroll-behavior: smooth` for simple anchor links when appropriate; use GSAP/ScrollTrigger sparingly for selected sections only. Do not stack multiple smooth-scroll solutions or override normal keyboard/assistive scrolling. Respect `prefers-reduced-motion` (disable nonessential transforms/parallax and use instant/brief transitions).
- **[PROPOSED]** Only animate above-the-fold hero prominently; simpler reveal for About/Category/Branch preview/loyalty; avoid per-card heavy timelines on 69 inventory entries.
- **[PROPOSED]** Interactive hero: lightweight image/DOM/SVG layers inspired by approved moon/coffee brand motifs; pointer/scroll affordance as progressive enhancement, static first-frame ensures legibility. No invented logo modifications, no autoplay full-resolution background video. The exact choreography is **[TBD mockups/prototype]**.
- **[PROPOSED]** Budget/checks: optimize hero image loading and reserve layout space; measure JS bundle size and network impact; test animations under mobile CPU throttling. See `plan.md` and `seo-strategy.md` for performance KPIs; speed has priority over decoration.

## 7.1 Approved border and emphasis rules (2026-11-23)

- **[APPROVED visual]** Repeated **category, product and branch cards** use subtle **neutral 1px** borders by default. Gold is used sparingly to guide attention.
- **[APPROVED visual]** Gold-filled primary CTA/buttons, small gold category arrows, active navigation states and meaningful section accents remain.
- **[APPROVED visual]** Product modal retains a restrained **thin gold** outer border; internal table/column lines are neutral and less visually dominant.
- **[APPROVED visual]** Mega Menu has a subtle neutral outline, **no strong gold surrounding frame**; navigation separators are thin and low contrast.
- **[PROPOSED interaction]** A card may transition its outline to brand gold on hover/keyboard focus, but avoid glow, thick strokes, animated blur or jarring scaling. Touch states must not depend on hover.
- Brand gold must be **`#DAAF67`** for the primary gold role; other golds only from the Brand Manual. Neutral borders can use transparent brand white/black over approved dark surface, subject to contrast QA.

## 8. Responsive layout rules

**[APPROVED]** Mobile-first; normal responsive adaptation across mobile/tablet/desktop, without a wholly separate mobile information architecture. **Responsive is decided and QA-tested during implementation**, not through mandatory standalone tablet/mobile image exports. Desktop remains the visual reference; do not force desktop overlap/composition into narrow viewports.

**[PROPOSED]** Breakpoint ranges for engineering starting point; adjust to content, not specific handset models:

| Range | Page design intent |
|---|---|
| `320–599px` narrow/mobile | One-column branch cards and default one-column product/category cards; compact hamburger navigation; modal max-height around 90dvh with internal scrolling |
| `600–899px` large mobile/tablet portrait | Typically two-column category/product/branch card grids when content fits; compact tablet navigation if full links collide |
| `900–1199px` tablet landscape / compact desktop | Expanded content width; 2–3 column grids; header dropdown only if labels fit |
| `1200px+` desktop | Centered max-width container and 3-column product grids (4 only if design/legibility explicitly approved); expanded editorial compositions |

- **[PROPOSED]** Minimum ~44×44 CSS px touch targets on mobile where feasible, visible focus and tap affordances. Avoid hover-only disclosure and horizontal scrolling of the body.
- **[PROPOSED]** Use logical CSS properties (`margin-inline`, `padding-inline`, `inset-inline-start`) and `dir` for layout mirroring; don't manually reverse copy, currency or mixed English product names.
- **[PROPOSED]** Hero should scale without hiding primary CTA; product images preserve aspect ratio; category names and ingredient lists can wrap; branch addresses must not truncate essential details.
- **[PROPOSED]** Popup close button always visible, including safe-area insets. Test onscreen keyboard, landscape, zoom and 200% text scaling.

### 8.1 Component-specific responsive implementation notes

- **Header:** at mobile and tablet widths where links crowd, use a compact logo + accessible menu toggle + language switch; do not shrink the full desktop Mega Menu. Treat 768px as a candidate hamburger breakpoint, verify with both languages.
- **Mobile menu hierarchy:** Home, Menu (with independent View All Menu link), Branches, Rewards (link to homepage `#rewards`), Contact. Within Menu, nested **Drinks** and **Food** accordions start **collapsed** and expose all 8 category links on activation. Avoid putting core Home/Branches/Contact after expanded categories.
- **Hero:** recompose the three-cup arrangement and type without clipping important cups/text; **Explore Menu CTA inside hero** always visible. Keep static fallback; no animation-dependent content.
- **About:** avoid overlapping product artwork with sentences on tablet/mobile; allow vertical stacking when necessary.
- **Homepage carousel:** keep a swipeable featured-product slider on mobile (roughly one visible card with a partial next-card cue), accessible arrow controls where appropriate and visible focus; do not convert to an excessively tall static grid without approval.
- **Rewards:** rearrange the feature cards and central cup within the viewport; no off-screen clipping; link goes to external points provider once confirmed.
- **Menu category grid:** preserve approved 3+2/3 desktop arrangement; two columns on tablet and one on mobile unless content testing supports a better fit.
- **Category products:** 3 desktop, 2 tablet, 1 mobile by default; the optional 2-column mobile layout is an experiment requiring legible text and viable touch targets.
- **Product modal:** desktop side-by-side; on narrow screens image above details, maximum height ~90dvh with internal scroll, close control always accessible, backdrop not scrollable. Only show verified variant rows, never fabricated size/price/calorie data.
- **Branches:** 3 desktop / 2 tablet / 1 mobile; photos above details; align directions buttons at card bottoms despite varying address length.
- **Arabic:** inspect RTL versions independently for truncation, text wrapping, button order, mixed LTR size labels, logical properties and functional keyboard focus.

## 9. Layout tokens — PROPOSED, not brand-mandated

These are working measurements to make mockups and CSS consistent. Review visually **before sign-off**.

| Token | Working proposal |
|---|---|
| Base spacing | 4px scale |
| Spacing steps | 4, 8, 12, 16, 24, 32, 48, 64, 96px |
| Mobile side gutter | 16–20px |
| Tablet side gutter | 24–32px |
| Desktop side gutter | 32–48px |
| Max content width | 1200–1280px |
| Section vertical spacing | ~64px mobile, ~88–120px desktop (content-dependent) |
| Card border-radius | 12–20px, only if compatible with brand examples |
| Product image aspect | 1:1 or 4:5 — **TBD after actual assets** |
| Button minimum height | ~44–48px |
| Body text | ~16px minimum on mobile unless small legal metadata is justified |

**Do not treat these suggestions as new brand rules**; adjust after mockups and content stress-testing. The Brand Manual is authoritative for color, type family, logo and pattern identity.

## 10. SEO, content and accessibility alignment

- **[APPROVED/PLAN]** 24 localized page URLs (4 core + 8 categories, multiplied by 2). Don't create About, Food/Drinks or product URLs.
- Every page should have one semantic H1; meaningful H2/H3 hierarchy; good internal links and localized text. Category descriptions and product names must be available as crawlable HTML, not as unindexable animation canvas text.
- Use localized, meaningful `alt` for informational photos and empty `alt=""` on decorative patterns. Do not stuff keywords into alt text. Each category and branch can be identified by nearby actual headings/captions.
- Use appropriate contrast, keyboard reachability, `aria-expanded` on dropdowns, accessible modal behavior and reduced motion. Do not make a critical action solely dependent on color or motion.
- Use responsive image `srcset` / `sizes`, modern compressed image formats, explicit dimensions/aspect ratios, lazy-load offscreen imagery, and prioritize only the principal hero asset.
- Localized page titles, description, canonicals, hreflang and `sitemap.xml` are governed by `seo-strategy.md`, not by visual CSS choices.
- **[TBD]** Client copy/photography/locations/loyalty explanation; use clearly marked mock data **only** in design comps, never on live site.

## 11. Screens/states / in-development implementation and QA

**[APPROVED delivery strategy]** Responsive mockups are **not required as a separate pre-development approval gate**. The following device states must instead be implemented, reviewed and adjusted **while building each page**; desktop references guide the appearance:

1. Home — desktop reference + responsive mobile/tablet implementation, including hero idle/interacting, visible Hero Explore Menu CTA, About, Featured Menu slider, branch preview and rewards.
2. Menu landing — mobile + desktop, both Drinks and Food sections visible.
3. Representative category page — mobile + desktop, short and long names.
4. Product detail popup — mobile + desktop; single configuration, multiple variants, long ingredients, close/focus states.
5. Branches — 3/2/1 desktop/tablet/mobile card grid, long branch names/addresses, photo and directions.
6. Contact — mobile + desktop.
7. Header — desktop dropdown open/closed; mobile nav open/closed; sticky scroll state; locale switch.
8. Footer — mobile and desktop.
9. Loading/reduced-motion/failure fallbacks for interactive hero and preloader.

**[PROPOSED] Developer handoff assets:** six approved desktop reference images, original approved logo SVGs, licensed fonts, optimized product/branch images, approved text inventory, state annotations and key GSAP timeline notes. Responsive refinements are approved by visual QA against live code, not a mandatory batch of 18 generated mockups.

## 12. Design acceptance checklist

- [ ] All approved 12 page types per locale are represented through templates (4 core + 8 category), with AR and EN variants tested.
- [ ] Homepage contains Hero, About, **Featured Products/Menu carousel**, Branches Preview and Loyalty sections; **Hero-internal Explore Menu CTA** remains visible.
- [ ] Menu landing uses **two stacked sections** (Drinks 5 / Food 3); every category has a direct page link.
- [ ] Category pages use product **grid**; product card opens an accessible modal with verified information; no product URLs.
- [ ] Product photo backgrounds look consistent; all sizes/prices/calories correspond to verified inventory, without fabricated defaults.
- [ ] Branches use **3-column desktop card grid** (tablet 2/mobile 1 as feasible) + photo per branch + verified directions link; no embedded maps or filters.
- [ ] Contact is information-only; no form.
- [ ] Header transitions to sticky state elegantly; dropdown works with keyboard/touch; AR/EN switcher works.
- [ ] Footer stays simple, containing brand, navigation, contact and approved social channels.
- [ ] Brand logo, golds, black/white and font families follow the manual; visual use is contrast-safe.
- [ ] Hero interactivity, GSAP reveals and preloader do not block content, worsen usability or violate reduced-motion preference.
- [ ] Mobile/tablet/desktop layouts tested for truncation, zoom, overflow and modal accessibility.
- [ ] Design is reviewed and approved before marking this document as finalized.

## 13. Open decisions / content dependencies

| Item | Status | Owner / next action |
|---|---|---|
| Menu S/D variant grouping (Espresso, Macchiato) | **[TBD]** | Confirm whether separate listings/cards or a single product with multiple size rows; do not merge silently. |
| Product image crop and studio backdrop | **[TBD]** | Review supplied images then lock size/crop. |
| Exact interactive hero choreography/visual assets | **[TBD]** | Prototype and evaluate on mobile before final approval. |
| Preloader look, duration and exit behavior | **[PROPOSED]**, final aesthetic TBD | Ensure lightweight, accessible, nonblocking, brand-compliant. |
| Original logo SVGs + licensed web font files | **[TBD]** | Request assets/rights from client. |
| Brand foundation year | **[TBD]** | Confirm before writing About copy. |
| Final product prices, calories, ingredients, names, sizes | **[TBD]** | Get client-approved sheet/photos. |
| Final branch photos, addresses and maps links | **[TBD]** | Get approved branch inventory; verify each directions URL. |
| Loyalty workflow copy and external link | **[TBD]** | Obtain clear, accurate steps and final destination. |
| Third home CTA («حول مش») | **[TBD]** | Clarify phrase/intent before creating CTA. |
| URL/slugs/root behavior | **[PROPOSED]** | Confirm with host and `seo-strategy.md`. |
| Actual motion timing, spacing and typography values | **[PROPOSED]** | Tune against approved desktop references and validate mobile/tablet in running UI; client sign-off. |
| Contact page visual artwork | **[TBD]** | Apply approved shared components and obtain visual approval before final launch. |
| Final content versus mockup placeholders | **[TBD]** | Do not treat any screenshot wording, prices, branch names or reward claims as factual data. |

## 13.1 Implementation acceptance and testing strategy

- Desktop screenshots are acceptance **visual references**, not pixel-accurate contracts for fluid heights and final copy.
- Implement each feature **mobile-first** and review at approximately 390px, 768px and a representative 1280–1440px desktop width, plus small mobile 320px and intermediate widths for overflow; use screenshots from the running implementation for comparison and QA.
- Test real keyboard/touch menu and popup interactions, scrollbar/scroll locking, screen zoom, reduced motion, both locales, wrapping of real data and Lighthouse performance. A static mockup cannot prove behavior.
- Match the approved desktop structure; never invent SEO destinations, branch addresses, product prices or loyalty mechanics to fill mockup space.

## 14. Decision log

| Date | Decision | Source |
|---|---|---|
| 2026-11-19 | Strict Moon Café Brand Manual; clean modern visuals, mostly dark with occasional official gold sections | User |
| 2026-11-19 | Initial concept: Hero, About, Categories, Branches, Loyalty; **later desktop visual replaces homepage category-block with Featured Products carousel** | User / updated 2026-11-23 |
| 2026-11-19 | **Menu index Sections**, not Tabs or only category gateway cards | User (latest approval) |
| 2026-11-19 | Product grid + detail popup + consistent studio backgrounds | User |
| 2026-11-19 | Initially considered branch list; **superseded by desktop 3-column grid of cards** | User / superseded 2026-11-23 |
| 2026-11-19 | Animated sticky header, menu dropdown, AR/EN switcher and simple footer | User |
| 2026-11-19 | GSAP scroll effects, preloader and **simple/subtle micro-interactions** | User (latest approval) |
| 2026-11-19 | Mobile-first across mobile, tablet, desktop; responsive adaptation | User |
| 2026-11-23 | Accept **latest desktop visual baseline** as structure/look only, not final content | Project owner |
| 2026-11-23 | **Branches: 3-column desktop grid**, not list; neutral borders, gold directions CTA | Project owner |
| 2026-11-23 | Restrained gold accent/border system; desktop Mega Menu and modal styling | Project owner |
| 2026-11-23 | **Responsive during implementation**, rather than a separate full 18-image pre-development deliverable | Project owner |

---

**Design handoff rule:** Development may start using the approved desktop designs and documented behavior while continuing responsive design in code. Do not publish unverified placeholder content. Contact design, real client assets, final copy, hosting URL scheme and accessibility/performance validation remain explicit release gates.

### Default language routing — confirmed 2026-11-23

Arabic is the default UI when opening the site at `/`, with `<html lang="ar" dir="rtl">`. Arabic nav links must use root-level routes (`/menu/`, `/branches/`, `/contact/`, `/menu/{slug}/`). English lives at `/en/` with LTR. Language switching should preserve the same page/category and its approved design layout; never treat `/en/` as the default root. The desktop-approved visuals remain authoritative, while their temporary copy is not approved content.
