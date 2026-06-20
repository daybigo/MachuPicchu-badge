# MachuPicchu AI — badge

Sello flotante **"hecho con MachuPicchu AI"** que se inyecta en los sitios creados con
[MachuPicchu AI](https://machupicchu.dev). Es un pill chico, color crema, abajo a la derecha,
con el logo y un link a `machupicchu.dev`. Self-contained (el logo va embebido en base64, sin
requests extra).

## Uso (CDN vía jsDelivr)

```html
<script src="https://cdn.jsdelivr.net/gh/daybigo/MachuPicchu-badge@v1/badge.js" defer></script>
```

Ponelo justo antes de `</body>`. No requiere configuración: al cargar inyecta el sello.

## Build

`badge.js` se genera con `build_badge.py`, que embebe `logo48.png` (logo a 48px) como data URI:

```bash
python build_badge.py
```

## Versionado

El CDN se fija a un tag (`@v1`) para que jsDelivr lo cachee de forma estable. Para publicar
cambios: actualizar `badge.js`, commitear, y mover/crear el tag.

## Licencia

MIT — ver [`LICENSE`](./LICENSE).
