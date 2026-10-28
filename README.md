# Maggie Wong & Co Solicitors — homepage redesign

A concept redesign of [maggiewong.co.uk/home.html](http://maggiewong.co.uk/home.html) for Maggie Wong & Co Solicitors Limited (黃艷彤律師行), an immigration and human rights law firm in Birmingham city centre. Plain HTML, CSS and JavaScript — host the repository root on any static host.

| File         | Language            |
|--------------|---------------------|
| `home.html`  | 繁體中文 (replaces the current `home.html`) |
| `index.html` | English             |

The homepage is one page with sections: services, approach and process, about Maggie Wong, reference fees, and contact (details, opening hours and an enquiry form that opens the visitor's email app). Links to the privacy notice, complaints procedure, full price list and events go to the existing pages on maggiewong.co.uk.

Pages are `noindex` and carry a "concept" stripe while this is a proposal; remove both before going live.

## Run locally

```bash
python3 -m http.server 5180
```

## Editing

Both pages are generated from `_build/build.py`, where all text is written side by side as `L(中文, English)`. Rebuild after editing (Python 3, no dependencies):

```bash
python3 _build/build.py
```

Styles: `assets/css/style.css`. Script (mobile menu, scroll reveal, enquiry form): `assets/js/main.js`.
