# Moon Café — Project File Structure

> Status: Proposed physical repository layout; **Arabic as root/default language is approved**. Exact directory URL support and final slugs require hosting verification.
> Stack: HTML / CSS / vanilla JavaScript; no database and no customer admin panel.

## Public URL rules

- Arabic `/` homepage and `/menu/`, `/branches/`, `/contact/`, `/menu/{slug}/` routes (RTL).
- English `/en/` homepage and `/en/menu/`, `/en/branches/`, `/en/contact/`, `/en/menu/{slug}/` routes (LTR).
- Food and Drinks are sections on each menu index, not standalone URLs. About and Rewards are Home sections. Product details are a modal, not a URL.
- All localized pages have self-canonicals, paired reciprocal `hreflang` and localized title/description.
- Directory URLs require a hosting environment that serves `index.html` from each folder, or equivalent routes must be adapted consistently.

## Proposed repository tree

```text
moon-cafe/
├── docs/
│   ├── plan.md
│   ├── design.md
│   ├── seo-strategy.md
│   ├── menu-inventory.md
│   └── project-structure.md
├── index.html                 # Arabic: /
├── menu/
│   ├── index.html             # Arabic: /menu/
│   ├── hot-coffee/index.html
│   ├── hot-drinks/index.html
│   ├── iced-coffee/index.html
│   ├── crash/index.html
│   ├── refreshing-drinks/index.html
│   ├── bakery-desserts/index.html
│   ├── sandwiches-croissants/index.html
│   ├── snacks/index.html
├── branches/index.html        # Arabic: /branches/
├── contact/index.html         # Arabic: /contact/
├── en/
│   ├── index.html             # English: /en/
│   ├── menu/
│   │   ├── index.html         # English: /en/menu/
│   │   ├── hot-coffee/index.html
│   │   ├── hot-drinks/index.html
│   │   ├── iced-coffee/index.html
│   │   ├── crash/index.html
│   │   ├── refreshing-drinks/index.html
│   │   ├── bakery-desserts/index.html
│   │   ├── sandwiches-croissants/index.html
│   │   ├── snacks/index.html
│   ├── branches/index.html    # English: /en/branches/
│   └── contact/index.html     # English: /en/contact/
├── assets/
│   ├── images/
│   │   ├── products/
│   │   ├── branches/
│   │   └── brand/
│   ├── icons/
│   └── fonts/                # Brand fonts licensed and supplied separately
├── css/
│   ├── base.css              # reset, font faces, base type, RTL/LTR foundations
│   ├── layout.css            # shared grids, containers, sections
│   ├── components.css        # nav, cards, buttons, popup, footer
│   ├── pages.css             # page-specific selectors
│   └── utilities.css
├── js/
│   ├── main.js               # general boot + shared page behavior
│   ├── navigation.js         # sticky header, mega menu, mobile accordion
│   ├── menu.js               # category data display helpers
│   ├── popup.js              # modal focus, close, size/price/calorie display
│   └── animations.js         # performance-conscious GSAP; reduced motion
├── data/
│   ├── products.json         # bilingual item names, ingredients, sizes and values
│   ├── branches.json         # verified branch names, location URLs, photos
│   └── content.json          # verified localized copy and rewards instructions
├── robots.txt
├── sitemap.xml               # GENERATED only after final URLs verified
└── 404.html
```

## Deployment and SEO safeguards

1. Serve **Arabic directly at `/`**, not via a forced redirect to `/ar/`.
2. Serve English under `/en/`; language switcher maps equivalent pages.
3. Render meaningful headings, links, category/product information in crawlable HTML; JavaScript can enhance interactions, not replace critical content for crawlers.
4. Ensure **24 indexable localized page URLs** (12 Arabic + 12 English) when final pages are complete; do not index modal states, `/menu/food/`, `/menu/drinks/`, About/Rewards anchors or static JSON.
5. Populate canonical URLs and `hreflang` pairs with the exact production hostname and tested trailing-slash scheme.
6. Create sitemap.xml at the root and reference it from robots.txt; include only canonical, live, 200-status URLs.
7. Audit old live URLs before planning server-side permanent redirects. In particular, `/ar/` should only be redirected if it was actually used.
8. Keep the source documentation under `/docs/`, preferably **outside the public web root at deployment**, or configure the server so internal docs and raw data files are not inadvertently exposed. Content JSON needed by the browser is public; do not put secrets in it.

## Pending checks

- Verify the hosting platform supports directory `index.html` and redirect rules.
- Confirm actual production host preference (www versus non-www) and SSL behavior.
- Approve final category slugs and verify any legacy links.
- Get final bilingual content, branch data and product properties.
- Obtain legally usable font and photo assets; keep placeholders out of production.
