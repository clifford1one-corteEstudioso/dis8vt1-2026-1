from playwright.sync_api import sync_playwright
import os

OUTPUT_DIR = r"D:\GitHub\dis8vt1-2026-1\extras\files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Common CSS styles for glassmorphism
BASE_CSS = """
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap');

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: transparent;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    font-family: 'Inter', sans-serif;
  }

  .card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 28px;
    padding: 40px;
    box-shadow:
      0 8px 32px rgba(0, 0, 0, 0.18),
      inset 0 1px 0 rgba(255, 255, 255, 0.4),
      inset 0 -1px 0 rgba(255, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
  }

  .card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
  }

  .card::after {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, transparent 60%);
    pointer-events: none;
  }

  .message {
    color: rgba(255,255,255,0.95);
    font-size: 22px;
    font-weight: 500;
    line-height: 1.5;
    text-align: center;
    text-shadow: 0 1px 8px rgba(0,0,0,0.3);
  }

  .message-large {
    font-size: 26px;
    font-weight: 600;
  }

  .accent {
    color: rgba(255, 220, 120, 1);
    font-weight: 700;
  }

  /* Avatar styles */
  .avatar-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
  }

  .avatar {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 42px;
    background: rgba(255,255,255,0.2);
    border: 2px solid rgba(255,255,255,0.4);
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    position: relative;
    overflow: hidden;
  }

  .avatar-label {
    color: rgba(255,255,255,0.9);
    font-size: 14px;
    font-weight: 600;
    text-align: center;
    text-shadow: 0 1px 4px rgba(0,0,0,0.3);
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }

  .avatar-name {
    color: rgba(255,255,255,0.95);
    font-size: 18px;
    font-weight: 600;
    text-align: center;
    text-shadow: 0 1px 6px rgba(0,0,0,0.3);
  }

  .opinion {
    color: rgba(255,255,255,0.88);
    font-family: 'Playfair Display', Georgia, serif;
    font-style: italic;
    font-size: 15px;
    line-height: 1.7;
    text-align: center;
    text-shadow: 0 1px 4px rgba(0,0,0,0.25);
    margin-top: 8px;
  }

  .divider {
    width: 60px;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(255,220,120,0.8), transparent);
    margin: 16px auto;
  }

  .subtitle {
    color: rgba(255,255,255,0.7);
    font-size: 13px;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 8px;
  }

  .tag {
    display: inline-flex;
    align-items: center;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 20px;
    padding: 4px 14px;
    color: rgba(255,220,120,1);
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 16px;
  }
"""

def make_html(card_content, width=520, extra_css=""):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{BASE_CSS}
{extra_css}
html, body {{ width: {width}px; background: transparent; }}
</style>
</head>
<body>
<div class="card" style="width:{width-40}px;">
{card_content}
</div>
</body>
</html>"""

def svg_avatar(emoji, bg_gradient, size=90):
    return f"""<div style="width:{size}px;height:{size}px;border-radius:50%;background:{bg_gradient};display:flex;align-items:center;justify-content:center;font-size:{int(size*0.45)}px;border:2px solid rgba(255,255,255,0.4);box-shadow:0 4px 15px rgba(0,0,0,0.25);">{emoji}</div>"""

INTERFACES = []

# ─────────────────────────────────────────────────────────────
# INTERFAZ 1
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_01", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Inicio</div>
  <div style="display:flex;justify-content:center;margin-bottom:20px;">
    {svg_avatar("👨‍🏫","linear-gradient(135deg,#4f8ef7,#7c3aed)",100)}
  </div>
  <div class="message message-large">¡Hola, <span class="accent">buenos días!</span></div>
  <div class="divider"></div>
  <div class="message" style="font-size:17px;color:rgba(255,255,255,0.8);">Me alegra verte una vez más...</div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 2
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_02", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Nueva notificación</div>
  <div style="font-size:48px;margin-bottom:20px;">📬</div>
  <div class="message">Nos han comunicado que te ha llegado una</div>
  <div class="message" style="margin-top:6px;"><span class="accent">nueva pregunta.</span></div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 3
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_03", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Pregunta del día</div>
  <div style="font-size:36px;margin-bottom:18px;">💭</div>
  <div class="message" style="font-size:16px;color:rgba(255,255,255,0.75);margin-bottom:14px;">La pregunta de hoy es:</div>
  <div class="divider"></div>
  <div class="message" style="font-size:21px;font-weight:600;line-height:1.6;">¿Piensas que la <span class="accent">globalización</span><br>fortalece o debilita las<br><span class="accent">culturas locales?</span></div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 4
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_04", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div style="font-size:52px;margin-bottom:20px;">🗺️</div>
  <div class="message message-large"><span class="accent">¡Partamos</span><br>eligiendo un camino!</div>
  <div class="divider"></div>
  <div class="message" style="font-size:15px;color:rgba(255,255,255,0.65);">Selecciona tu ruta de exploración</div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 5
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_05", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Elige tu camino</div>
  <div class="message" style="margin-bottom:28px;">¿En qué opinión deseas <span class="accent">indagar?</span></div>
  <div style="display:flex;justify-content:center;gap:50px;align-items:flex-start;">
    <div class="avatar-container">
      {svg_avatar("👥","linear-gradient(135deg,#43b89c,#1a8c6e)",90)}
      <div class="avatar-name">Ciudadanos</div>
    </div>
    <div class="avatar-container">
      {svg_avatar("💼","linear-gradient(135deg,#4f8ef7,#7c3aed)",90)}
      <div class="avatar-name">Profesionales</div>
    </div>
  </div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 6
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_06", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="message" style="font-size:17px;color:rgba(255,255,255,0.75);margin-bottom:18px;">Elegiste a</div>
  <div class="divider"></div>
  <div class="message message-large" style="margin-bottom:24px;"><span class="accent">Ciudadanos</span></div>
  <div style="display:flex;justify-content:center;">
    {svg_avatar("👥","linear-gradient(135deg,#43b89c,#1a8c6e)",100)}
  </div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 7
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_07", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="message" style="font-size:17px;color:rgba(255,255,255,0.75);margin-bottom:18px;">Elegiste a</div>
  <div class="divider"></div>
  <div class="message message-large" style="margin-bottom:24px;"><span class="accent">Profesionales</span></div>
  <div style="display:flex;justify-content:center;">
    {svg_avatar("💼","linear-gradient(135deg,#4f8ef7,#7c3aed)",100)}
  </div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 8
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_08", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Profesionales</div>
  <div class="message" style="margin-bottom:28px;">Elige un <span class="accent">profesional</span></div>
  <div style="display:flex;justify-content:center;gap:28px;flex-wrap:wrap;">
    <div class="avatar-container">
      {svg_avatar("🩺","linear-gradient(135deg,#56ccf2,#2f80ed)",80)}
      <div class="avatar-label">Médico</div>
    </div>
    <div class="avatar-container">
      {svg_avatar("🎨","linear-gradient(135deg,#f7971e,#ffd200)",80)}
      <div class="avatar-label">Diseñador</div>
    </div>
    <div class="avatar-container">
      {svg_avatar("⚖️","linear-gradient(135deg,#834d9b,#d04ed6)",80)}
      <div class="avatar-label">Abogada</div>
    </div>
    <div class="avatar-container">
      {svg_avatar("📰","linear-gradient(135deg,#11998e,#38ef7d)",80)}
      <div class="avatar-label">Periodista</div>
    </div>
  </div>
</div>
""", width=580)))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 9 – Médico Felipe
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_09", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Médico</div>
  <div style="display:flex;justify-content:center;margin-bottom:14px;">
    {svg_avatar("🩺","linear-gradient(135deg,#56ccf2,#2f80ed)",90)}
  </div>
  <div class="avatar-name" style="margin-bottom:4px;">Felipe</div>
  <div class="divider"></div>
  <div class="opinion">"La globalización facilita el intercambio de conocimientos médicos, tecnologías y tratamientos que benefician a la población. Sin embargo, también puede invisibilizar prácticas de salud tradicionales y conocimientos locales que forman parte de la identidad cultural y que, en algunos contextos, siguen siendo relevantes."</div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 10 – Diseñador Mauro
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_10", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Diseñador</div>
  <div style="display:flex;justify-content:center;margin-bottom:14px;">
    {svg_avatar("🎨","linear-gradient(135deg,#f7971e,#ffd200)",90)}
  </div>
  <div class="avatar-name" style="margin-bottom:4px;">Mauro</div>
  <div class="divider"></div>
  <div class="opinion">"La globalización ofrece acceso a referencias y herramientas de todo el mundo, enriqueciendo la creatividad. Al mismo tiempo, existe el riesgo de que se impongan estéticas homogéneas y se pierdan expresiones locales. El diseño puede actuar como un medio para rescatar y visibilizar el patrimonio material e inmaterial de una comunidad."</div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 11 – Abogada Paula
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_11", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Abogada</div>
  <div style="display:flex;justify-content:center;margin-bottom:14px;">
    {svg_avatar("⚖️","linear-gradient(135deg,#834d9b,#d04ed6)",90)}
  </div>
  <div class="avatar-name" style="margin-bottom:4px;">Paula</div>
  <div class="divider"></div>
  <div class="opinion">"Desde una perspectiva jurídica, la globalización impulsa la cooperación internacional y la protección de ciertos derechos, pero también plantea desafíos para resguardar el patrimonio cultural y los derechos de los pueblos y comunidades sobre sus expresiones culturales. Es importante equilibrar la apertura con mecanismos de protección."</div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 12 – Periodista Ximena
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_12", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Periodista</div>
  <div style="display:flex;justify-content:center;margin-bottom:14px;">
    {svg_avatar("📰","linear-gradient(135deg,#11998e,#38ef7d)",90)}
  </div>
  <div class="avatar-name" style="margin-bottom:4px;">Ximena</div>
  <div class="divider"></div>
  <div class="opinion">"La circulación global de información permite que culturas poco conocidas lleguen a nuevas audiencias, pero los grandes medios y plataformas pueden priorizar narrativas dominantes, reduciendo la visibilidad de historias locales. El periodismo tiene un papel importante en documentar y difundir la diversidad cultural."</div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 13 – Elegiste Ciudadanos
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_13", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="message" style="font-size:17px;color:rgba(255,255,255,0.75);margin-bottom:18px;">Elegiste a</div>
  <div class="divider"></div>
  <div class="message message-large" style="margin-bottom:24px;"><span class="accent">Ciudadanos</span></div>
  <div style="display:flex;justify-content:center;">
    {svg_avatar("👥","linear-gradient(135deg,#43b89c,#1a8c6e)",100)}
  </div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 14 – 4 Ciudadanos
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_14", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Ciudadanos</div>
  <div class="message" style="margin-bottom:28px;">Elige un <span class="accent">ciudadano</span></div>
  <div style="display:flex;justify-content:center;gap:22px;flex-wrap:wrap;">
    <div class="avatar-container">
      {svg_avatar("🧑‍🎒","linear-gradient(135deg,#f093fb,#f5576c)",80)}
      <div class="avatar-label">Aníbal</div>
    </div>
    <div class="avatar-container">
      {svg_avatar("👵","linear-gradient(135deg,#a18cd1,#fbc2eb)",80)}
      <div class="avatar-label">Camila</div>
    </div>
    <div class="avatar-container">
      {svg_avatar("👨‍💼","linear-gradient(135deg,#4facfe,#00f2fe)",80)}
      <div class="avatar-label">Vicente</div>
    </div>
    <div class="avatar-container">
      {svg_avatar("👩‍🌾","linear-gradient(135deg,#43e97b,#38f9d7)",80)}
      <div class="avatar-label">Janice</div>
    </div>
  </div>
</div>
""", width=580)))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 15 – Aníbal
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_15", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Ciudadano · Joven</div>
  <div style="display:flex;justify-content:center;margin-bottom:14px;">
    {svg_avatar("🧑‍🎒","linear-gradient(135deg,#f093fb,#f5576c)",90)}
  </div>
  <div class="avatar-name" style="margin-bottom:4px;">Aníbal</div>
  <div class="divider"></div>
  <div class="opinion">"Creo que la globalización fortalece las culturas locales porque hoy podemos mostrar nuestras costumbres al mundo a través de internet. Gracias a las redes sociales, la música, la comida o las tradiciones de lugares pequeños pueden hacerse conocidas. Eso sí, también hay que cuidar que no terminemos copiando todo lo que viene de afuera."</div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 16 – Camila
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_16", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Ciudadana · Adulta Mayor</div>
  <div style="display:flex;justify-content:center;margin-bottom:14px;">
    {svg_avatar("👵","linear-gradient(135deg,#a18cd1,#fbc2eb)",90)}
  </div>
  <div class="avatar-name" style="margin-bottom:4px;">Camila</div>
  <div class="divider"></div>
  <div class="opinion">"Pienso que la globalización puede debilitar las culturas locales. Antes las tradiciones se transmitían de generación en generación, pero ahora muchas personas prefieren adoptar costumbres extranjeras y dejan de lado las propias. Me preocupa que se pierdan las historias, los oficios y las celebraciones que forman parte de nuestra identidad."</div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 17a – Vicente
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_17a", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Ciudadano · Ciudad</div>
  <div style="display:flex;justify-content:center;margin-bottom:14px;">
    {svg_avatar("👨‍💼","linear-gradient(135deg,#4facfe,#00f2fe)",90)}
  </div>
  <div class="avatar-name" style="margin-bottom:4px;">Vicente</div>
  <div class="divider"></div>
  <div class="opinion">"Para mí, la globalización tiene ventajas y desventajas. Ha permitido acceder a nuevas ideas, tecnologías y oportunidades laborales, pero también hace que muchas ciudades se parezcan entre sí. Creo que depende de cómo cada comunidad valore y promueva su propia cultura."</div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 17b – Janice
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_17b", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Ciudadana · Campo</div>
  <div style="display:flex;justify-content:center;margin-bottom:14px;">
    {svg_avatar("👩‍🌾","linear-gradient(135deg,#43e97b,#38f9d7)",90)}
  </div>
  <div class="avatar-name" style="margin-bottom:4px;">Janice</div>
  <div class="divider"></div>
  <div class="opinion">"Desde mi experiencia, la globalización puede poner en riesgo las costumbres rurales cuando llegan modelos de producción o estilos de vida que reemplazan las prácticas locales. Sin embargo, también puede abrir mercados para productos tradicionales y dar a conocer la cultura del campo a personas de otros lugares, si se hace respetando a las comunidades."</div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 18 – Ahora qué harás
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_18", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Siguiente paso</div>
  <div class="message message-large" style="margin-bottom:28px;">Ahora, <span class="accent">¿qué harás</span><br>con esta información?</div>
  <div style="display:flex;flex-direction:column;gap:14px;">
    <div style="background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.25);border-radius:16px;padding:16px 24px;display:flex;align-items:center;gap:14px;">
      <span style="font-size:26px;">🔍</span>
      <span style="color:rgba(255,255,255,0.95);font-weight:600;font-size:18px;">Profundizar</span>
    </div>
    <div style="background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.25);border-radius:16px;padding:16px 24px;display:flex;align-items:center;gap:14px;">
      <span style="font-size:26px;">⚖️</span>
      <span style="color:rgba(255,255,255,0.95);font-weight:600;font-size:18px;">Contrastar</span>
    </div>
    <div style="background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.25);border-radius:16px;padding:16px 24px;display:flex;align-items:center;gap:14px;">
      <span style="font-size:26px;">✏️</span>
      <span style="color:rgba(255,255,255,0.95);font-weight:600;font-size:18px;">Crear</span>
    </div>
  </div>
</div>
""")))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 19 – Profundicemos (two columns, wider)
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_19", make_html(f"""
<div style="padding:10px 0;">
  <div style="text-align:center;margin-bottom:22px;">
    <div class="tag">Profundicemos</div>
    <div class="message" style="font-size:20px;font-weight:600;margin-bottom:4px;">Argumentos sobre la globalización y las culturas locales</div>
  </div>
  <div style="display:flex;gap:24px;align-items:flex-start;">
    <!-- Left column: Fortalece -->
    <div style="flex:1;background:rgba(67,184,156,0.12);border:1px solid rgba(67,184,156,0.3);border-radius:18px;padding:20px;">
      <div style="color:rgba(100,255,200,1);font-weight:700;font-size:14px;text-transform:uppercase;letter-spacing:1px;margin-bottom:14px;text-align:center;">✅ Puede Fortalecer</div>
      <div style="color:rgba(255,255,255,0.88);font-size:13px;line-height:1.6;">
        <p style="margin-bottom:12px;"><strong style="color:rgba(200,255,220,0.95);">Mayor difusión gracias a internet:</strong> Hoy es posible compartir con audiencias internacionales mediante plataformas digitales y redes sociales.</p>
        <p style="margin-bottom:12px;"><strong style="color:rgba(200,255,220,0.95);">Turismo cultural:</strong> El interés de visitantes por conocer costumbres locales ha incentivado la conservación de festividades, artesanías y expresiones tradicionales.</p>
        <p style="margin-bottom:12px;"><strong style="color:rgba(200,255,220,0.95);">Reconocimiento internacional:</strong> Organismos como UNESCO promueven la protección del patrimonio cultural material e inmaterial.</p>
        <p><strong style="color:rgba(200,255,220,0.95);">Conexión de comunidades migrantes:</strong> Las tecnologías permiten mantener el idioma, las celebraciones y vínculos culturales a distancia.</p>
      </div>
    </div>
    <!-- Right column: Debilita -->
    <div style="flex:1;background:rgba(245,87,108,0.12);border:1px solid rgba(245,87,108,0.3);border-radius:18px;padding:20px;">
      <div style="color:rgba(255,160,150,1);font-weight:700;font-size:14px;text-transform:uppercase;letter-spacing:1px;margin-bottom:14px;text-align:center;">⚠️ Puede Debilitar</div>
      <div style="color:rgba(255,255,255,0.88);font-size:13px;line-height:1.6;">
        <p style="margin-bottom:12px;"><strong style="color:rgba(255,210,200,0.95);">Desaparición de lenguas:</strong> Según la UNESCO, miles de idiomas están en peligro de desaparecer si no se toman medidas de preservación.</p>
        <p style="margin-bottom:12px;"><strong style="color:rgba(255,210,200,0.95);">Homogeneización cultural:</strong> La expansión global de ciertas marcas puede reducir la presencia de expresiones culturales locales en el consumo cotidiano.</p>
        <p style="margin-bottom:12px;"><strong style="color:rgba(255,210,200,0.95);">Pérdida de oficios tradicionales:</strong> La producción industrial ha afectado actividades artesanales transmitidas por generaciones.</p>
        <p><strong style="color:rgba(255,210,200,0.95);">Transformación de costumbres:</strong> Las nuevas generaciones pueden adoptar prácticas globales y dejar de lado tradiciones familiares o comunitarias.</p>
      </div>
    </div>
  </div>
</div>
""", width=780)))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 20 – Contrastemos
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_20", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div class="tag">Contrastemos</div>
  <div class="message message-large" style="margin-bottom:8px;">¡<span class="accent">Contrastemos!</span></div>
  <div class="message" style="font-size:15px;color:rgba(255,255,255,0.7);margin-bottom:26px;">Incorpora la opinión de un tercer personaje<br>con una perspectiva distinta.</div>
  <div style="display:flex;justify-content:center;gap:50px;">
    <div class="avatar-container">
      <div style="display:flex;gap:12px;margin-bottom:10px;">
        {svg_avatar("🩺","linear-gradient(135deg,#56ccf2,#2f80ed)",60)}
        {svg_avatar("🎨","linear-gradient(135deg,#f7971e,#ffd200)",60)}
      </div>
      <div style="display:flex;gap:12px;">
        {svg_avatar("⚖️","linear-gradient(135deg,#834d9b,#d04ed6)",60)}
        {svg_avatar("📰","linear-gradient(135deg,#11998e,#38ef7d)",60)}
      </div>
      <div class="avatar-label" style="margin-top:10px;">Profesionales</div>
    </div>
    <div class="avatar-container">
      <div style="display:flex;gap:12px;margin-bottom:10px;">
        {svg_avatar("🧑‍🎒","linear-gradient(135deg,#f093fb,#f5576c)",60)}
        {svg_avatar("👵","linear-gradient(135deg,#a18cd1,#fbc2eb)",60)}
      </div>
      <div style="display:flex;gap:12px;">
        {svg_avatar("👨‍💼","linear-gradient(135deg,#4facfe,#00f2fe)",60)}
        {svg_avatar("👩‍🌾","linear-gradient(135deg,#43e97b,#38f9d7)",60)}
      </div>
      <div class="avatar-label" style="margin-top:10px;">Ciudadanos</div>
    </div>
  </div>
</div>
""", width=580)))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 21 – Creemos
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_21", make_html(f"""
<div style="padding:10px 0;">
  <div style="text-align:center;margin-bottom:22px;">
    <div class="tag">Creemos</div>
    <div class="message message-large" style="margin-bottom:4px;">¡<span class="accent">Creemos</span>!</div>
  </div>
  <div style="display:flex;flex-direction:column;gap:16px;">
    <div style="background:rgba(255,255,255,0.1);border:1px solid rgba(255,220,120,0.3);border-radius:18px;padding:18px 22px;">
      <div style="color:rgba(255,220,120,1);font-weight:700;font-size:13px;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">🌐 Desafío 1 · Diseña una iniciativa</div>
      <div style="color:rgba(255,255,255,0.85);font-size:14px;line-height:1.6;">Si quisieras dar a conocer una tradición local al mundo, ¿cómo lo harías?</div>
    </div>
    <div style="background:rgba(255,255,255,0.1);border:1px solid rgba(255,220,120,0.3);border-radius:18px;padding:18px 22px;">
      <div style="color:rgba(255,220,120,1);font-weight:700;font-size:13px;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">📢 Desafío 2 · Crea una campaña de difusión</div>
      <div style="color:rgba(255,255,255,0.85);font-size:14px;line-height:1.6;">¿Qué podrías hacer en tu barrio, escuela o ciudad para mantener vivas las tradiciones locales?</div>
    </div>
    <div style="background:rgba(255,255,255,0.1);border:1px solid rgba(255,220,120,0.3);border-radius:18px;padding:18px 22px;">
      <div style="color:rgba(255,220,120,1);font-weight:700;font-size:13px;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">🔮 Desafío 3 · Imagina el futuro</div>
      <div style="color:rgba(255,255,255,0.85);font-size:14px;line-height:1.6;">Estamos en el año 2050 y muchas costumbres locales han cambiado por la influencia global. ¿Qué estrategia diseñarías para que las nuevas generaciones sigan conociendo su patrimonio cultural?</div>
    </div>
  </div>
</div>
""", width=580)))

# ─────────────────────────────────────────────────────────────
# INTERFAZ 22 – Cierre
# ─────────────────────────────────────────────────────────────
INTERFACES.append(("interfaz_22", make_html(f"""
<div style="text-align:center; padding:10px 0;">
  <div style="display:flex;justify-content:center;margin-bottom:20px;">
    {svg_avatar("👨‍🏫","linear-gradient(135deg,#4f8ef7,#7c3aed)",100)}
  </div>
  <div class="message message-large" style="margin-bottom:14px;">¡Ahora estás preparado para generar tu <span class="accent">opinión propia!</span></div>
  <div class="divider"></div>
  <div class="message" style="font-size:17px;margin-bottom:10px;">🌟 ¡Tú puedes!</div>
  <div class="message" style="font-size:15px;color:rgba(255,255,255,0.7);">Cualquier duda puedes volver a mí para<br>repetir el proceso.</div>
  <div style="margin-top:18px;font-size:28px;">👋</div>
  <div class="message" style="font-size:16px;color:rgba(255,220,120,0.9);margin-top:8px;">¡Nos vemos! 😊</div>
</div>
""")))


# ─────────────────────────────────────────────────────────────
# RENDER ALL
# ─────────────────────────────────────────────────────────────
with sync_playwright() as p:
    browser = p.chromium.launch()
    for name, html in INTERFACES:
        page = browser.new_page()
        # Parse width from the HTML to set viewport
        import re
        w_match = re.search(r'width: ?(\d+)px', html[:300])
        w = int(w_match.group(1)) if w_match else 520
        page.set_viewport_size({"width": w + 20, "height": 1200})
        page.set_content(html, wait_until="networkidle")
        page.wait_for_timeout(600)
        card = page.query_selector(".card")
        if card:
            card.screenshot(path=f"{OUTPUT_DIR}/{name}.png", omit_background=True)
        else:
            page.screenshot(path=f"{OUTPUT_DIR}/{name}.png", full_page=True)
        page.close()
        print(f"✓ {name}.png")
    browser.close()

print("All done!")