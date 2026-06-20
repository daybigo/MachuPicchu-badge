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
 * Self-contained badge. Injects a small fixed bottom-right cream pill that links
 * to https://machupicchu.dev. Served via jsDelivr from
 * https://github.com/daybigo/MachuPicchu-badge
 *
 * Usage (already wired into the MachuPicchu template, keep it forever):
 *   <script src="https://cdn.jsdelivr.net/gh/daybigo/MachuPicchu-badge@v1/badge.js" defer></script>
 */
(function () {
  try {
    if (window.__mpaiBadgeMounted) return;
    window.__mpaiBadgeMounted = true;

    var LOGO = "data:image/png;base64,__LOGO_B64__";

    function mount() {
      if (document.getElementById("mpai-badge")) return;
      var host = document.body || document.documentElement;
      if (!host) return;

      var a = document.createElement("a");
      a.id = "mpai-badge";
      a.href = "https://machupicchu.dev";
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.setAttribute("aria-label", "hecho con MachuPicchu AI");
      a.style.cssText = [
        "position:fixed",
        "right:16px",
        "bottom:16px",
        "z-index:2147483600",
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

      a.addEventListener("mouseenter", function () {
        a.style.transform = "translateY(-2px)";
        a.style.boxShadow = "0 8px 20px rgba(0,0,0,.16)";
      });
      a.addEventListener("mouseleave", function () {
        a.style.transform = "none";
        a.style.boxShadow = "0 4px 14px rgba(0,0,0,.12)";
      });

      host.appendChild(a);
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
