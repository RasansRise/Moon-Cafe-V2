# Moon Café — Homepage build

Static HTML / CSS / vanilla JS. No build step, no framework, no GSAP dependency.

| URL | File | Language |
|---|---|---|
| `/` | `index.html` | Arabic, RTL (default) |
| `/en/` | `en/index.html` | English, LTR |
| `/menu/` | `menu/index.html` | Arabic menu (generated) |
| `/en/menu/` | `en/menu/index.html` | English menu (generated) |

## Run locally

All `href`/`src` paths are relative: `./css/...` from the Arabic root page and `../css/...` from `/en/`. The site works from the domain root, from a sub-folder, or by opening `index.html` directly. Page links point to folders (`./menu/`), so they need a server that serves `index.html` for a folder:

```bash
cd moon-cafe
python3 -m http.server 8000
# open http://localhost:8000/ (AR) and http://localhost:8000/en/ (EN)
```

## What's implemented (homepage)

- Fixed header that turns compact and sticky on scroll. Nav links, active state and the gold Explore Menu CTA follow the mockup.
- Desktop Mega Menu: "Menu" still links to `/menu/`, and a chevron button opens the Drinks/Food panel with the 8 category links and an Explore Full Menu action. It opens on click, keyboard or hover, and closes on Escape or an outside click.
- Mobile/tablet drawer (≤999px): Home, Menu (Drinks/Food accordions, collapsed), Branches, Rewards, Contact.
- Interactive hero: a ribbon with category names scrolls along an SVG path and speeds up when you scroll. The three cups float and react to the pointer. The animation pauses when the hero is off-screen.
- About section: the statement includes the inline image pills and the gold highlight, followed by the CUP visual.
- Featured products carousel: loops, works with arrows, dots, swipe and the keyboard, and supports RTL. Content is static crawlable HTML.
- Branch preview cards (cream panel, directions pill, address and hours), plus See All Branches.
- Rewards section: 2 + cup + 2 layout and the Join CTA.
- Footer.
- A short preloader (capped at 900 ms), scroll reveals, and `prefers-reduced-motion` support. All content is visible without JS.
- Canonical, reciprocal `hreflang` (ar-SA / en / x-default), localized title and description, `lang`/`dir`.

## Revision 2 (client feedback, 2026-11-24)

- The language switcher is now a **flag** placed as the last item of the main nav (🇸🇦 on English pages, 🇬🇧 on Arabic). Flag SVGs come from `flag-icons` (MIT), stored in `assets/icons/flags/`.
- **Logo**: uses the supplied `assets/images/brand/logo.png` as-is (header, drawer, footer, preloader, favicon).
- **Hero** fills the full viewport height on every screen, and the cups stage scales to the remaining height. The hero Explore Menu CTA is **removed** at the client's request, which overrides design.md §4.2 / FR-20.
- **About**: the line height is increased so the highlight no longer covers neighbouring lines, and the CUP visual is larger.
- **Branch cards**: the outer border is removed.
- **Footer**: three parts (Pages, Contact, Logo only). Pages are listed without a Drinks/Food split, and the copyright is centred at the bottom.
- **Tablet/mobile (≤999px)**: a side drawer slides in from the end side, with a backdrop, staggered content, focus trap and Escape to close. It holds the same Pages / Contact / Logo sections, with the language flag inside the drawer.
- **Hover effect** on nav items (desktop and drawer): the label rolls up and reappears from below.

## Revision 3 (client feedback, 2026-11-24)

- **Hero**: small "مـــــون كافيـــــة" eyebrow, the large title "تاخذك الى رحلــة من مذاق القهوة الرائعة", the small line "استمتـــع بتجربـــة فريـــدة", and an Explore Menu CTA. This is client copy as supplied; the English is a translation.
- **About**: summarised from the client's brand story (since 2010, more than 20 branches, number one café goal, locations). This settles the founding year as **2010**, so the Brand Manual's "Since 2007" should not be used.
- **About highlight**: a marker-sweep animation draws the gold highlight across the phrase when it scrolls in, following the reading direction in RTL.
- **Rewards**: full screen and scroll-driven. The section is pinned while you scroll (`.is-pinned`, 340svh tall). The cup starts alone in the centre, then the heading, the four boxes in order (Earn → Get → Join → Exclusive) and the CTA appear one by one. When reduced motion is on, or on screens shorter than 620px, it falls back to a normal static section.

## Revision 4 (2026-11-24)

- **About**: the statement is the client's wording ("منذ عام 2010 … وبأسعار منافسة"), with the white supporting line and the highlight removed. Each inline image always reserves its full width, and the image grows open inside that space from the centre (clip-path + scale), so the text never moves.
- **Rewards**: a 2D spin was tried and reverted at the client's request; the cup keeps its original settle animation. A true 3D turn would need a rendered frame sequence or a 3D model of the cup.

## Revision 5 (2026-11-24)

- **Rewards on short screens (laptops)**: the cup's height is capped to the space left in the viewport. On screens ≤820px tall the title sits on one line and the spacing is tighter, so the whole scene, CTA included, stays inside the viewport and doesn't spill into the footer. The cup finishes moving into place before the heading appears, so it never covers the text.
- **Rewards sequence**: cup alone → heading → all four boxes together → CTA. The section is 240svh tall.
- **Rewards removed** from the header nav, the side drawer and the footer Pages list (there's no rewards page). The `#rewards` section itself stays on the homepage.
- **Footer order**: Logo → Pages → Contact, from the start side (right to left in Arabic, left to right in English).

## Revision 6 (2026-11-24)

- **Footer**: `grid-template-columns: 1fr 1fr 1fr`, with a clear gap above it (`margin-top: clamp(48px, 9vh, 110px)`).
- **Rewards safety check**: the scene is pinned only if its content fits the viewport height. Otherwise, for example on very short screens, it shows as a normal section, so the CTA can never overlap the footer. Short tablets (≤899px wide, ≤900px tall) get a one-line title and a smaller cup.

## Revision 7 (2026-11-24)

- **Rewards**: the cup appears alone first, then the heading, the four boxes and the CTA appear together in one step. The section is 200svh tall.
- **Mega Menu fix**: a variable-name clash with the drawer script stopped the dropdown from opening. Fixed by renaming (`drawerPanel`, `isMegaOpen`).

## Menu page (2026-11-25)

- **All 75 products on one page**, with a category **dropdown** (an accessible listbox: All, then Drinks / Food groups with counts, keyboard arrows/Enter/Escape) and pagination (12 per page). The toolbar sticks under the header.
- **Product names** come from the image file names: hyphens become spaces and each word is capitalised (`cookies-and-cream` → "Cookies And Cream"). Arabic names come from the client CSV (`name.ar` in `products.json`) and are used on the Arabic page.
- **Data**: `data/products.json` holds each product's category, name and image. Category assignment was done by hand following `menu-inventory.md`. "crush" files go under Crash, and the new items (teas, mojitos, dragées, pretzel, bag coffee maker) went to the closest category.
- **Images**: `assets/images/products/` holds 600px webp files (about 46 KB each) for the grid, and `assets/images/products/1000/` holds the full size used via `srcset`. Images are lazy-loaded.
- **Build**: run `python3 tools/build-menu.py` after editing `products.json` or the homepage header/footer. It writes both menu pages with every product in static HTML (crawlable, and visible without JS). `js/menu.js` adds the filters and pagination on top.
- **Shareable URLs**: `?category=hot-coffee&page=2`, and the Back button works. Mega-menu category links now point to `menu/?category=…`, which replaces the planned separate category pages. On the menu page itself they filter in place without reloading.
- **Product popup** (`js/popup.js`, native `<dialog>`): the whole card, or its "View details" button, opens it. A black overlay with blur covers the page. Escape, the × button or a click on the overlay closes it (with a fade-out), focus is trapped inside while it is open and returns to the card afterwards, and page scrolling is locked. It shows only known data: image (1000px), name and category. Ingredients and the size/price/calories table are shown as placeholders ("—" / "Details pending confirmation").
- **Still pending**: prices, calories and ingredients.

## Other notes

- **Menu chevron** gives keyboard and touch access to the Mega Menu while "Menu" still opens `/menu/`.
- **Gold** uses the Brand Manual `#DAAF67`.

## ⚠️ Placeholders — release blockers

Everything below is marked in the HTML with `data-placeholder`, `data-pending` or `TODO`:

- **Images**: everything in `assets/images/placeholders/` is cropped from the low-resolution mockup (cups, products, branch photos). Replace it with approved assets.
- **Fonts**: Proxima Nova and Helvetica Neue Arabic load only if they are installed locally. Add licensed `.woff2` files to `assets/fonts/` and uncomment the `url()` lines in `css/base.css`.
- **Content**: hero, about and rewards copy, product names and prices (`$` values from the mockup; currency TBD), branch names, addresses and hours. Arabic copy is a draft translation.
- **Links with no destination yet** (rendered without `href`): Get Directions ×2, Join Moon Rewards, Instagram, TikTok and Facebook. Phone and email are not shown yet in the Contact column.
- `og:image`, the favicon, and the final metadata copy.

## Not yet built

Menu, category, branches and contact pages (the nav already links to their routes), plus the product popup, `data/*.json`, `sitemap.xml`, `robots.txt` and `404.html`. Those wait for verified routes and content, per `seo-strategy.md`.
