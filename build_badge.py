"""Build badge.js with the MachuPicchu logo embedded as a base64 data URI.

Run: python build_badge.py
Reads the 48px logo PNG and writes a self-contained badge.js (no extra requests).
"""
import base64
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
LOGO_PNG = HERE / "logo48.png"

JS_TEMPLATE = r'''/*!
 * MachuPicchu AI - sello "hecho con MachuPicchu AI"
 * Self-contained badge. Injects a small fixed BOTTOM-LEFT cream pill that links
 * to https://machupicchu.dev. Served via jsDelivr from
 * https://github.com/daybigo/MachuPicchu-badge
 *
 * Behaviour:
 *  - NEVER renders inside an iframe (e.g. the IDE preview): only on the
 *    published / standalone page.
 *  - On hover it shows a small "x" to dismiss it for the current view; on page
 *    refresh the badge comes back.
 *
 * Usage (already wired into the MachuPicchu template, keep it forever):
 *   <script src="https://cdn.jsdelivr.net/gh/daybigo/MachuPicchu-badge@v2/badge.js" defer></script>
 */
(function () {
  try {
    // El sello NUNCA debe verse dentro de un iframe (p.ej. el preview del IDE).
    // Solo aparece en la web publicada/standalone. Si estamos embebidos, salir.
    if (window.self !== window.top) return;
    if (window.__mpaiBadgeMounted) return;
    window.__mpaiBadgeMounted = true;

    var LOGO = "data:image/png;base64,__LOGO_B64__";

    function mount() {
      if (document.getElementById("mpai-badge")) return;
      var host = document.body || document.documentElement;
      if (!host) return;

      var wrap = document.createElement("div");
      wrap.id = "mpai-badge";
      wrap.style.cssText = [
        "position:fixed",
        "left:16px",
        "bottom:16px",
        "z-index:2147483600",
        "display:inline-block"
      ].join(";");

      var a = document.createElement("a");
      a.href = "https://machupicchu.dev";
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.setAttribute("aria-label", "hecho con MachuPicchu AI");
      a.style.cssText = [
        "display:inline-flex",
        "align-items:center",
        "gap:7px",
        "padding:6px 12px 6px 8px",
        "background:#f7f4ed",
        "color:#2d2219",
        "border:1px solid rgba(0,0,0,.08)",
        "border-radius:9999px",
        "box-shadow:0 4px 14px rgba(0,0,0,.12)",
        "font:600 12px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif",
        "text-decoration:none",
        "-webkit-font-smoothing:antialiased",
        "cursor:pointer",
        "user-select:none",
        "transition:transform .18s ease, box-shadow .18s ease"
      ].join(";");

      var img = document.createElement("img");
      img.src = LOGO;
      img.alt = "";
      img.width = 18;
      img.height = 18;
      img.style.cssText = "width:18px;height:18px;display:block;border-radius:4px;flex:0 0 auto";

      var span = document.createElement("span");
      span.textContent = "hecho con MachuPicchu AI";
      span.style.cssText = "white-space:nowrap;letter-spacing:.1px";

      a.appendChild(img);
      a.appendChild(span);

      // Boton de cierre (x): aparece al hacer hover. Cierra el sello SOLO en esta
      // vista; al refrescar la pagina el sello vuelve a aparecer.
      var close = document.createElement("button");
      close.type = "button";
      close.setAttribute("aria-label", "Cerrar");
      close.innerHTML = "&times;";
      close.style.cssText = [
        "position:absolute",
        "top:-8px",
        "right:-8px",
        "width:18px",
        "height:18px",
        "padding:0",
        "display:flex",
        "align-items:center",
        "justify-content:center",
        "background:#2d2219",
        "color:#fff",
        "border:none",
        "border-radius:9999px",
        "box-shadow:0 2px 6px rgba(0,0,0,.3)",
        "font:700 13px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif",
        "cursor:pointer",
        "opacity:0",
        "pointer-events:none",
        "transition:opacity .15s ease"
      ].join(";");
      close.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        wrap.remove();
      });

      wrap.addEventListener("mouseenter", function () {
        a.style.transform = "translateY(-2px)";
        a.style.boxShadow = "0 8px 20px rgba(0,0,0,.16)";
        close.style.opacity = "1";
        close.style.pointerEvents = "auto";
      });
      wrap.addEventListener("mouseleave", function () {
        a.style.transform = "none";
        a.style.boxShadow = "0 4px 14px rgba(0,0,0,.12)";
        close.style.opacity = "0";
        close.style.pointerEvents = "none";
      });

      wrap.appendChild(a);
      wrap.appendChild(close);
      host.appendChild(wrap);
    }

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", mount);
    } else {
      mount();
    }
  } catch (e) {
    /* noop: el sello nunca debe romper el sitio */
  }
})();
'''

def main() -> None:
    b64 = base64.b64encode(LOGO_PNG.read_bytes()).decode("ascii")
    js = JS_TEMPLATE.replace("__LOGO_B64__", b64)
    out = HERE / "badge.js"
    out.write_text(js, encoding="utf-8")
    print(f"wrote {out} ({len(js)} chars, logo b64 {len(b64)} chars)")

if __name__ == "__main__":
    main()
