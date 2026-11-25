#!/usr/bin/env python3
"""
Build the Menu pages (Arabic /menu/ and English /en/menu/) from:
  - data/products.json            (products + categories)
  - index.html / en/index.html    (shared header, side drawer, footer)

Run from the project root:   python3 tools/build-menu.py

All products are written into the HTML (crawlable, works without JS);
js/menu.js adds the category filters and pagination on top.
Re-run this script after changing products.json or the homepage header/footer.
"""
import html
import json
import posixpath
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data/products.json").read_text(encoding="utf-8"))
SITE = "https://www.mooncafe-sa.com"
EAGER = 4  # first images load eagerly (above the fold)

LOCALES = {
    "ar": {
        "home_file": ROOT / "index.html", "home_base": "/",
        "out": ROOT / "menu/index.html", "base": "/menu/",
        "other_url": "/en/menu/", "dir": "rtl",
        "title": "المنيو | مون كافيه",
        "description": "تصفّح منيو مون كافيه: القهوة الساخنة والباردة، المشروبات المنعشة، المخبوزات والحلويات، الساندوتشات والسناكس.",
        "eyebrow": "مـــــون كافيـــــة",
        "h1": "المنيو",
        "intro": "اختر ما يناسب مزاجك من القهوة والمشروبات والمخبوزات والمزيد.",
        "all": "الكل",
        "filters_label": "النوع",
        "groups": {"drinks": "المشروبات", "food": "الأكل"},
        "products_heading": "كل المنتجات",
        "status": "عرض {from}–{to} من {total} منتج",
        "pagination": "التنقل بين الصفحات",
        "prev": "الصفحة السابقة",
        "next": "الصفحة التالية",
        "page": "الصفحة {n}",
        "skip": "تخطَّ إلى المحتوى",
        "view": "عرض التفاصيل",
        "view_aria": "عرض تفاصيل {name}",
        "close": "إغلاق",
        "ingredients": "المكونات",
        "size": "الحجم", "price": "السعر", "calories": "السعرات",
        "pending": "التفاصيل قيد التأكيد.",
    },
    "en": {
        "home_file": ROOT / "en/index.html", "home_base": "/en/",
        "out": ROOT / "en/menu/index.html", "base": "/en/menu/",
        "other_url": "/menu/", "dir": "ltr",
        "title": "Menu | Moon Café",
        "description": "Browse the Moon Café menu: hot and iced coffee, refreshing drinks, bakery and desserts, sandwiches and snacks.",
        "eyebrow": "Moon Café",
        "h1": "Our Menu",
        "intro": "Pick what suits your mood: coffee, drinks, bakery and more.",
        "all": "All",
        "filters_label": "Category",
        "groups": {"drinks": "Drinks", "food": "Food"},
        "products_heading": "All products",
        "status": "Showing {from}–{to} of {total} products",
        "pagination": "Pagination",
        "prev": "Previous page",
        "next": "Next page",
        "page": "Page {n}",
        "skip": "Skip to content",
        "view": "View Details",
        "view_aria": "View details for {name}",
        "close": "Close",
        "ingredients": "Ingredients",
        "size": "Size", "price": "Price", "calories": "Calories",
        "pending": "Details pending confirmation.",
    },
}


def to_abs(value, base):
    if value.startswith(("#", "http:", "https:", "mailto:", "tel:", "//")) or value == "":
        return value
    if value.startswith("/"):
        return value
    path, sep, rest = value.partition("?") if "?" in value else value.partition("#")
    norm = posixpath.normpath(posixpath.join(base, path or "./"))
    if (path.endswith("/") or path in ("", ".", "./", "..", "../")) and not norm.endswith("/"):
        norm += "/"
    return norm + (sep + rest if sep else "")


def to_rel(value, base):
    if not value.startswith("/") or value.startswith("//"):
        return value
    m = re.match(r"([^?#]*)(.*)", value)
    path, tail = m.group(1), m.group(2)
    r = posixpath.relpath(path, base.rstrip("/") or "/")
    if path.endswith("/") and not r.endswith("/"):
        r += "/"
    if r in (".", "./"):
        r = "./"
    if not r.startswith("."):
        r = "./" + r
    return r + tail


def rebase(fragment, old_base, new_base):
    def sub(m):
        return f'{m.group(1)}="{to_rel(to_abs(m.group(2), old_base), new_base)}"'
    return re.sub(r'\b(href|src)="([^"]*)"', sub, fragment)


def shared_parts(cfg):
    s = cfg["home_file"].read_text(encoding="utf-8")
    body_open = s.index(">", s.index("<body")) + 1
    pre = s[body_open:s.index('<main id="main">')]
    footer = s[s.index('<footer class="site-footer">'):s.index("</footer>") + len("</footer>")]
    pre = rebase(pre, cfg["home_base"], cfg["base"])
    footer = rebase(footer, cfg["home_base"], cfg["base"])
    # Active page = Menu
    pre = pre.replace(' aria-current="page"', "")
    pre = pre.replace('class="primary-nav__link" href="./"', 'class="primary-nav__link" href="./" aria-current="page"', 1)
    pre = pre.replace('class="drawer__link" href="./"', 'class="drawer__link" href="./" aria-current="page"', 1)
    # Language switch → equivalent Menu page in the other language
    other = to_rel(cfg["other_url"], cfg["base"])
    pre = re.sub(r'href="[^"]*"( hreflang="(?:ar|en)" lang="(?:ar|en)" data-lang-switch)', f'href="{other}"\\1', pre)
    return pre, footer


def head(cfg, lang):
    rel = lambda p: to_rel(p, cfg["base"])
    ar_url, en_url = SITE + "/menu/", SITE + "/en/menu/"
    canonical = ar_url if lang == "ar" else en_url
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{cfg['dir']}" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <script>document.documentElement.classList.replace('no-js', 'js');</script>

  <!-- Generated by tools/build-menu.py — edit data/products.json or the script, not this file -->
  <title>{html.escape(cfg['title'])}</title>
  <meta name="description" content="{html.escape(cfg['description'])}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="ar-SA" href="{ar_url}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="x-default" href="{ar_url}">
  <meta name="theme-color" content="#080504">
  <link rel="icon" href="{rel('/assets/images/brand/logo.png')}" type="image/png">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Moon Café">
  <meta property="og:title" content="{html.escape(cfg['title'])}">
  <meta property="og:description" content="{html.escape(cfg['description'])}">
  <meta property="og:url" content="{canonical}">

  <link rel="stylesheet" href="{rel('/css/base.css')}">
  <link rel="stylesheet" href="{rel('/css/layout.css')}">
  <link rel="stylesheet" href="{rel('/css/components.css')}">
  <link rel="stylesheet" href="{rel('/css/pages.css')}">
  <link rel="stylesheet" href="{rel('/css/utilities.css')}">

  <script src="{rel('/js/navigation.js')}" defer></script>
  <script src="{rel('/js/animations.js')}" defer></script>
  <script src="{rel('/js/main.js')}" defer></script>
  <script src="{rel('/js/menu.js')}" defer></script>
  <script src="{rel('/js/popup.js')}" defer></script>
</head>
<body class="page-menu">"""


def catalog(cfg, lang):
    rel = lambda p: to_rel(p, cfg["base"])
    cats = DATA["categories"]
    products = DATA["products"]
    counts = {c["id"]: sum(1 for p in products if p["categoryId"] == c["id"]) for c in cats}

    # Grouped dropdown (listbox): All, then Drinks / Food categories
    groups = {}
    for p in products:
        groups.setdefault(p["menuGroupId"], [])
        if p["categoryId"] not in groups[p["menuGroupId"]]:
            groups[p["menuGroupId"]].append(p["categoryId"])
    chevron = '<svg class="menu-select__chevron" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 9l7 7 7-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    check = '<svg class="menu-select__check" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    def option(cid, label, count):
        return (f'<li class="menu-select__option" id="opt-{cid}" role="option" data-filter="{cid}" aria-selected="{"true" if cid == "all" else "false"}">'
                f'{check}<span class="menu-select__text">{html.escape(label)}</span><span class="menu-filter__count">{count}</span></li>')
    opts = [option("all", cfg["all"], len(products))]
    cat_by_id = {c["id"]: c for c in cats}
    for g in ("drinks", "food"):
        opts.append(f'<li class="menu-select__group" role="presentation">{cfg["groups"][g]}</li>')
        for cid in groups.get(g, []):
            opts.append(option(cid, cat_by_id[cid]["name"][lang], counts[cid]))
    filters_html = f"""<div class="menu-select" data-menu-select>
            <span class="menu-select__label" id="filter-label">{cfg['filters_label']}</span>
            <button class="menu-select__btn" type="button" aria-haspopup="listbox" aria-expanded="false" aria-labelledby="filter-label filter-value" data-select-btn>
              <span class="menu-select__value" id="filter-value" data-select-value>{cfg['all']}</span>
              <span class="menu-filter__count" data-select-count>{len(products)}</span>
              {chevron}
            </button>
            <ul class="menu-select__list" role="listbox" aria-labelledby="filter-label" tabindex="-1" data-select-list>
              {(chr(10) + '              ').join(opts)}
            </ul>
          </div>"""

    cat_names = {c["id"]: c["name"][lang] for c in cats}
    items = []
    for i, p in enumerate(products):
        name = html.escape(p["name"].get(lang) or p["name"]["en"])
        loading = 'fetchpriority="high"' if i < EAGER else 'loading="lazy"'
        items.append(f"""          <li class="menu-item" data-category="{p['categoryId']}">
            <article class="menu-card">
              <div class="menu-card__media"><img src="{rel(p['image'])}" srcset="{rel(p['image'])} 600w, {rel(p['imageLarge'])} 1000w" sizes="(min-width: 1200px) 300px, (min-width: 760px) 30vw, 48vw" alt="{name}" width="600" height="600" {loading} decoding="async"></div>
              <div class="menu-card__body">
                <p class="menu-card__cat">{html.escape(cat_names[p['categoryId']])}</p>
                <h3 class="menu-card__name">{name}</h3>
                <button class="menu-card__more" type="button" aria-haspopup="dialog" aria-label="{html.escape(cfg['view_aria'].format(name=p['name'].get(lang) or p['name']['en']))}"
                  data-product-open data-name="{name}" data-category="{html.escape(cat_names[p['categoryId']])}" data-image="{rel(p['imageLarge'])}">{cfg['view']} <svg class="icon-flip" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
              </div>
            </article>
          </li>""")

    dash = '<td aria-hidden="true">—</td>'  # placeholder cells; the note below the table is read instead
    dash_rows = "\n              ".join(f"<tr>{dash * 3}</tr>" for _ in range(4))
    i18n = html.escape(json.dumps({k: cfg[k] for k in ("status", "prev", "next", "page")}, ensure_ascii=False))
    nl = "\n          "
    return f"""
  <main id="main">
    <section class="menu-hero" aria-labelledby="menu-title">
      <div class="container menu-hero__inner">
        <p class="eyebrow menu-hero__eyebrow">{cfg['eyebrow']}</p>
        <h1 class="heading menu-hero__title" id="menu-title">{cfg['h1']}</h1>
        <p class="menu-hero__intro">{cfg['intro']}</p>
      </div>
    </section>

    <section class="menu-catalog" aria-labelledby="products-title" data-menu data-i18n="{i18n}">
      <div class="container">
        <h2 class="visually-hidden" id="products-title">{cfg['products_heading']}</h2>
        <div class="menu-toolbar" data-menu-toolbar>
          {filters_html}
          <p class="menu-status" aria-live="polite" data-menu-status></p>
        </div>

        <!-- English names from image file names, Arabic names from client CSV. Prices / calories / ingredients pending verified client data. -->
        <ul class="menu-grid" data-menu-grid>
{chr(10).join(items)}
        </ul>

        <nav class="pagination" aria-label="{cfg['pagination']}" hidden data-menu-pagination></nav>
      </div>
    </section>

    <!-- Product details popup (filled by js/popup.js from the clicked card) -->
    <dialog class="product-dialog" aria-labelledby="pd-title" data-product-dialog>
      <button class="product-dialog__close" type="button" data-product-close>
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        <span class="visually-hidden">{cfg['close']}</span>
      </button>
      <div class="product-dialog__inner">
        <div class="product-dialog__media"><img src="" alt="" width="1000" height="1000" data-pd-image></div>
        <div class="product-dialog__body">
          <p class="product-dialog__cat" data-pd-category></p>
          <h2 class="product-dialog__title" id="pd-title" data-pd-name></h2>

          <!-- PENDING: ingredients, sizes, prices and calories — no invented values (plan.md §5.1) -->
          <h3 class="product-dialog__label">{cfg['ingredients']}</h3>
          <p class="product-dialog__pending">{cfg['pending']}</p>

          <table class="product-dialog__table">
            <thead><tr><th scope="col">{cfg['size']}</th><th scope="col">{cfg['price']}</th><th scope="col">{cfg['calories']}</th></tr></thead>
            <tbody>
              {dash_rows}
            </tbody>
          </table>
          <p class="product-dialog__pending">{cfg['pending']}</p>
        </div>
      </div>
    </dialog>

  </main>
"""


def build():
    for lang, cfg in LOCALES.items():
        pre, footer = shared_parts(cfg)
        page = head(cfg, lang) + pre + catalog(cfg, lang) + "\n  " + footer + "\n</body>\n</html>\n"
        cfg["out"].parent.mkdir(parents=True, exist_ok=True)
        cfg["out"].write_text(page, encoding="utf-8")
        print("wrote", cfg["out"].relative_to(ROOT), f"({len(DATA['products'])} products)")


if __name__ == "__main__":
    build()
