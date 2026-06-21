/*!
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

    var LOGO = "data:image/png;base64,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";

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
