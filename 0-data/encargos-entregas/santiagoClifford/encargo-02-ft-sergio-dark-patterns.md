# **Dark Patterns en UX — Referencia Académica Exhaustiva**

## **Definición y Origen del Concepto**

Un Dark Pattern es "un truco manipulativo o engañoso en software que lleva a los usuarios a completar una acción que no habrían realizado de otro modo, si hubieran entendido lo que ocurría o hubieran tenido una alternativa en ese momento." [Medium](https://harrybr.medium.com/bringing-dark-patterns-to-light-d86f24224ebf) — Harry Brignull, 2010\.

Los dark patterns engañan y manipulan a los usuarios usando elementos de la *arquitectura de elección* —definida como la estructura y presentación de opciones (Thaler & Sunstein, 2008)— y la explotación de vulnerabilidades psicológicas (Mathur et al., 2021). Un ejemplo de vulnerabilidad psicológica es el *status quo bias*: los usuarios tienden a conservar las opciones predeterminadas. [Springer](https://link.springer.com/article/10.1007/s12599-022-00783-7)

---

## **Las Tres Ondas de Investigación Académica**

La investigación sobre dark patterns ha evolucionado en tres olas principales: la primera orientada a definir y categorizar tipos; la segunda centrada en su prevalencia y las bases para la regulación; y la tercera dirigida a evaluar los daños reales en consumidores cuantificando la efectividad de estas técnicas. [ResearchGate](https://www.researchgate.net/publication/371314839_From_Dark_Patterns_to_Fair_Patterns_Usable_Taxonomy_to_Contribute_Solving_the_Issue_with_Countermeasures)

---

## **Principales Taxonomías Académicas**

Las taxonomías académicas principales incluyen: Bösch et al. (2016), Brignull et al. (2015/2023), Gray et al. (2018, 2023, 2024), Luguri & Strahilevitz (2021), Mathur et al. (2019), y Lacey et al. (2023), entre otras. [arXiv](https://arxiv.org/html/2412.09147v1)

El análisis más comprensivo —Gray, Santos & Bielova (2024)— identificó 203 patrones de nivel bajo y 59 de nivel alto, sumando un total de 262 patrones, extraídos de 11 fuentes académicas y regulatorias. [ACM Digital Library](https://dl.acm.org/doi/10.1145/3613904.3642436)

---

## **Catálogo Exhaustivo por Categorías**

### **A — Sneaking (Introducción Subrepticia)**

*Gray et al. (2018) Cat. 3 · Mathur et al. (2019) Cat. 1*

| Patrón | Descripción | Ejemplo |
| ----- | ----- | ----- |
| **Sneak into Basket** | Agregar productos al carrito sin consentimiento explícito | Seguros de viaje pre-seleccionados en checkout |
| **Hidden Costs** | Revelar cargos no divulgados justo antes del pago final | Tasas de aeropuerto reveladas en el último paso |
| **Hidden Subscription** | Cobro recurrente disfrazado de tarifa única o trial gratuito | Netflix, streamings con trial |
| **Privacy Zuckering** | Diseño que lleva a compartir más datos de los deseados | Facebook con privacidad pública por defecto |
| **Roach Motel** | Fácil entrar, casi imposible salir | Cancelación de gym requiere carta postal |
| **Friend Spam** | Spam masivo a contactos suplantando identidad del usuario | LinkedIn demandado (US$13M settlement) |
| **Disguised Ads** | Publicidad disfrazada de contenido editorial o resultados orgánicos | Resultados "Ad" en Google con etiqueta casi invisible |

### **B — Urgency & Scarcity (Urgencia y Escasez Fabricada)**

*Mathur et al. (2019) Cats. 2–3*

Mathur et al. identificaron, entre otros, el *Countdown Timer*: indicar que una oferta expirará mediante un temporizador regresivo, frecuentemente reiniciado al recargar la página. [arXiv](https://arxiv.org/pdf/2101.04843)

| Patrón | Descripción | Ejemplo |
| ----- | ----- | ----- |
| **Countdown Timer** | Reloj regresivo frecuentemente falso o reiniciable | Booking.com: "Oferta expira en 02:34" |
| **Limited-Time Message** | "Oferta por tiempo limitado" sin fecha verificable | E-commerce genérico de moda |
| **Low Stock Message** | Escasez artificial de stock | "¡Solo quedan 2\! 5 personas lo ven ahora" |
| **High Demand Message** | Social proof fabricado de alta demanda | "12 personas ven este hotel ahora mismo" |
| **Activity Messages** | Notificaciones de compras/acciones de otros usuarios | "Ana de Madrid acaba de comprar esto" |

### **C — Interface Interference / Misdirection**

*Gray et al. (2018) Cat. 4*

El *Confirmshaming* es "el acto de culpabilizar al usuario para que opte por aceptar algo." El *Bait and Switch* es una interfaz donde "el usuario se propone hacer una cosa, pero ocurre algo diferente e indeseable." [arXiv](https://arxiv.org/pdf/2101.04843)

| Patrón | Descripción | Ejemplo |
| ----- | ----- | ----- |
| **Confirmshaming** | Redacción culpabilizadora en la opción de rechazo | "No, prefiero perder dinero" como opción de declinar |
| **Misdirection** | Color/tamaño/posición para ocultar opciones relevantes | "Rechazar cookies" en gris pequeño vs. "Aceptar" en verde brillante |
| **Trick Questions** | Preguntas con doble negación o ambigüedad deliberada | "Desmarque si no desea no recibir comunicaciones" |
| **Pre-selected Options** | Opciones favorables al servicio marcadas por defecto | Checkbox de newsletter pre-marcado |
| **Bait and Switch** | El sistema ejecuta una acción diferente a la esperada | Botón "X" que instala actualizaciones (caso Windows) |
| **Price Comparison Prevention** | Dificultar comparación de precios entre opciones | Créditos de videojuego sin equivalencia directa en moneda real |
| **Toying with Emotion** | Elementos emocionales para nublar la decisión racional | Imágenes de niños en campañas para inhibir análisis crítico |

### **D — Obstruction (Obstrucción)**

*Gray et al. (2018) Cat. 2*

| Patrón | Descripción | Ejemplo |
| ----- | ----- | ----- |
| **Forced Continuity** | Cobro automático al finalizar trial sin aviso adecuado | Streamings, SaaS con trial |
| **Hard to Cancel** | Proceso de cancelación artificialmente complejo | Amazon Prime: múltiples pantallas de retención |
| **Privacy Maze** | Opciones de privacidad enterradas en menús profundos | Instagram: 15+ pasos para desactivar publicidad personalizada |
| **Dead End** | Páginas sin ruta de regreso o completación de tarea | Formularios de reembolso que terminan en FAQs sin contacto |

### **E — Forced Action & Nagging**

*Gray et al. (2018) Cat. 5*

El *Nagging* es cuando "la tarea deseada del usuario es interrumpida una o más veces por otras tareas no directamente relacionadas." El *Forced Action* es cuando "se requiere que los usuarios realicen una acción específica para acceder o continuar accediendo a funcionalidades específicas." [arXiv](https://arxiv.org/pdf/2101.04843)

| Patrón | Descripción | Ejemplo |
| ----- | ----- | ----- |
| **Forced Registration** | Cuenta obligatoria para acceder a funcionalidades | Checkout sin opción de "compra como invitado" |
| **Nagging** | Interrupciones repetidas con tareas no relacionadas | Popups de "¿Valora la app?" en momentos inoportunos |
| **Forced Action** | Acción requerida para acceder a funcionalidades | Invitar contactos para desbloquear niveles en apps de juego |
| **Pay to Win / Pay to Skip** | Ventajas de gameplay solo mediante pago real | Loot boxes, microtransacciones en juegos móviles |
| **Grinding** | Tiempo desproporcionado para avanzar, presionando hacia el pago | Timers de espera en Candy Crush |

### **F — Dark Patterns de Privacidad (EDPB / Bösch / Jarovsky)**

| Patrón | Descripción | Marco regulatorio |
| ----- | ----- | ----- |
| **Privacy-Unfriendly Defaults** | Máxima recolección de datos por defecto | RGPD Art. 7, EDPB Guidelines 3/2022 |
| **Misleading Language** | Lenguaje eufemístico en políticas de privacidad | RGPD recital 32, consentimiento informado |
| **Obstruction of Opt-Out** | Opt-out artificialmente complejo | CCPA California 2021, RGPD |
| **Consent Bundling** | Múltiples consentimientos en una única aceptación | Viola principio de granularidad del RGPD |

---

## **Dimensiones Analíticas Transversales**

Mathur et al. proponen cinco atributos que caracterizan a los dark patterns: **Asymmetric** (cargas desiguales entre opciones), **Covert** (naturaleza manipulativa no evidente), **Deceptive** (induce creencias falsas mediante afirmaciones incorrectas u omisiones), **Information Hiding** (ocultar activamente información relevante) y **Restrictive** (limitar el conjunto de opciones disponibles). [arXiv](https://arxiv.org/pdf/2101.04843)

Gray, Santos y Bielova (2024) introducen tres niveles jerárquicos: patrones **low-level** (nivel de elemento UI, detectables), **meso-level** (estrategias combinadas) y **high-level** (estrategias sistémicas o de producto completo). [Colingray](https://colingray.me/wp-content/uploads/2023/03/2023_GraySantosBielova_CHIBLW_OntologyDarkPatterns.pdf)

### **Sesgos Cognitivos Explotados**

| Sesgo | Dark Patterns Asociados |
| ----- | ----- |
| **Status Quo Bias** | Pre-selected options, Privacy-unfriendly defaults |
| **Loss Aversion** (Kahneman & Tversky) | Countdown timers, Low stock messages, Confirmshaming |
| **Social Proof** | Activity messages, High demand messages, Testimonials |
| **FoMO** | Limited-time messages, Urgency notifications |
| **Cognitive Load** | Trick questions, Complex opt-out flows, Consent bundling |
| **Sunk Cost Fallacy** | Grinding en games, Forced progress-loss warnings |

---

## **Hallazgos Empíricos Clave**

* Un crawl de 11,000 sitios de compras identificó 1,800 instancias de dark patterns, incluyendo Sneaking, Social Proof y Countdown Timers (Mathur et al., 2019). [arXiv](https://arxiv.org/pdf/2101.04843)  
* Di Geronimo et al. encontraron que más del 95% de las 200 apps Android más populares contienen al menos un dark pattern. [arXiv](https://arxiv.org/pdf/2101.04843)  
* Utz et al. analizaron banners de cookies de 1,000 webs populares en la UE y encontraron que más del 50% contenía al menos un dark pattern. [arXiv](https://arxiv.org/pdf/2101.04843)  
* Un experimento publicado (Blake et al., 2020\) con varios millones de usuarios en un sitio de ticketing demostró que los usuarios que no veían las comisiones de forma anticipada gastaban un 21% más y tenían un 14% más de probabilidad de completar la compra. [Medium](https://harrybr.medium.com/bringing-dark-patterns-to-light-d86f24224ebf)

---

## **Contextos Específicos Estudiados**

| Dominio | Referencia principal | Hallazgo clave |
| ----- | ----- | ----- |
| E-commerce | Mathur et al. (2019) | 1,818 instancias en 11K sitios |
| Apps móviles | Di Geronimo et al. (2020) | 95%+ de top apps con ≥1 dark pattern |
| Redes sociales / Privacidad | NCC "Deceived by Design" (2018) | Facebook, Google, Microsoft |
| Videojuegos | Zagal et al. (2013); Lacey et al. (2023) | 7 y 36 tipos respectivamente |
| Cookie banners | Utz et al. (2019) | 50%+ con dark patterns en UE |
| Live streaming commerce | Wu et al. (2021) | Taobao y TikTok Shop |
| Robots domésticos / IoT | Lacey & Caudwell (2019) | "Cuteness" como dark pattern |
| EdTech | Potel-Saville & Da Rocha (2023) | Duolingo con streaks y gamification manipulativa |

---

## **Marco Regulatorio**

* **UE — RGPD / EDPB Guidelines 3/2022:** Taxonmía específica de dark patterns para plataformas de redes sociales (final: febrero 2023).  
* **UE — DSA (Digital Services Act):** Santos et al. (2024) analizan qué plataformas y dark patterns deben regularse bajo el Artículo 25 de la DSA. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2212473X25000422)  
* **EE.UU. — FTC:** Informe "Bringing Dark Patterns to Light" (2022). Acciones: Intuit/TurboTax, Publishers Clearing House (US$18.5M settlement).  
* **EE.UU. — California CCPA (2021):** Prohíbe interfaces con "substantial effect of subverting or impairing" la elección del consumidor.  
* En 2022, la Fiscal General de Nueva York multó a Fareportal con US$2.6M por tácticas de marketing engañosas, y el Tribunal Federal de Australia multó a Trivago (Expedia Group) con A$44.7M por inducir a error a los consumidores sobre precios de hoteles. [Wikipedia](https://en.wikipedia.org/wiki/Dark_pattern)

---

## **Bibliografía Académica Completa**

### **Fuentes Seminales (lectura obligatoria)**

1. **Brignull, H.** (2023). *Deceptive Patterns: Exposing the Tricks Tech Companies Use to Control You.* Wiley.  
2. **Gray, C.M., Kou, Y., Battles, B., Hoggatt, J., & Toombs, A.L.** (2018). The Dark (Patterns) Side of UX Design. *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems.* doi:10.1145/3173574.3174108  
3. **Mathur, A., Acar, G., Friedman, M.J., Lucherini, E., Mayer, J., Chetty, M., & Narayanan, A.** (2019). Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites. *Proceedings of the ACM on Human-Computer Interaction (CSCW).* doi:10.1145/3359183  
4. **Gray, C.M., Santos, C., Bielova, N., & Mildner, T.** (2024). An Ontology of Dark Patterns Knowledge: Foundations, Definitions, and a Pathway for Shared Knowledge-Building. *CHI 2024\.* doi:10.1145/3613904.3642436  
5. **Luguri, J., & Strahilevitz, L.J.** (2021). Shining a Light on Dark Patterns. *Journal of Legal Analysis, 13*(1), 43–109. doi:10.1093/jla/laaa006  
6. **Di Geronimo, L., Braz, L., Fregnan, E., Palomba, F., & Bacchelli, A.** (2020). UI Dark Patterns and Where to Find Them: A Study on Mobile Applications and User Perception. *CHI 2020\.* doi:10.1145/3313831.3376600  
7. **Zagal, J.P., Björk, S., & Lewis, C.** (2013). Dark Patterns in the Design of Games. *FDG 2013\.*  
8. **Mathur, A., Kshirsagar, M., & Mayer, J.** (2021). What Makes a Dark Pattern... Dark? Design Attributes, Normative Considerations, and Measurement Methods. *CHI 2021\.* doi:10.1145/3411764.3445610

### **Referencias Complementarias**

9. **Caragay, E., Xiong, K., Zong, J., & Jackson, D.** (2024). Beyond Dark Patterns: A Concept-Based Framework for Ethical Software Design. *CHI 2024\.* doi:10.1145/3613904.3642781  
10. **Gray, C.M., Santos, C., & Bielova, N.** (2023). Towards a Preliminary Ontology of Dark Patterns Knowledge. *CHI EA '23.* doi:10.1145/3544549.3585676  
11. **Gray, C.M. et al.** (2023). Mapping the Landscape of Dark Patterns Scholarship: A Systematic Literature Review. *DIS 2023 Companion.* doi:10.1145/3563703.3596635  
12. **Bösch, C., Erb, B., Kargl, F., Kopp, H., & Pfattheicher, S.** (2016). Tales from the Dark Side: Privacy Dark Strategies and Privacy Dark Patterns. *PETS 2016*(4).  
13. **Jarovsky, L.** (2022). Dark Patterns in Personal Data Collection: Definition, Taxonomy and Lawfulness. *SSRN.* doi:10.2139/ssrn.4048582  
14. **Conti, G., & Sobiesk, E.** (2010). Malicious Interface Design: Exploiting the User. *WWW 2010\.* doi:10.1145/1772690.1772710  
15. **Gunawan, J., Santos, C., & Kamara, I.** (2022). Redress for Dark Patterns Privacy Harms? A Case Study on Consent Interactions. *CSLAW '22.* doi:10.1145/3511265.3550448  
16. **Lacey, C., & Caudwell, C.** (2019). Cuteness as a 'Dark Pattern' in Home Robots. *HRI 2019\.*  
17. **Utz, C., Degeling, M., Fahl, S., Schaub, F., & Holz, T.** (2019). (Un)informed Consent: Studying GDPR Consent Notices in the Field. *ACM CCS.* doi:10.1145/3319535.3354212  
18. **Kitkowska, A.** (2023). The Hows and Whys of Dark Patterns: Categorizations and Privacy. In: *Human Factors in Privacy Research.* Springer. doi:10.1007/978-3-031-28643-8\_9  
19. **Nie, X. et al.** (2024). A Comprehensive Study on Dark Patterns. *ACM FSE 2024\.* arXiv:2412.09147  
20. **Westin, R., & Chiasson, S.** (2024). Integrating Dark Pattern Taxonomies. arXiv:2402.16760  
21. **Norwegian Consumer Council (NCC)** (2018). *Deceived by Design.* NCC Report.  
22. **OECD** (2022). *Dark Commercial Patterns.* OECD Digital Economy Papers, No. 336\. doi:10.1787/44f5e846-en  
23. **European Data Protection Board (EDPB)** (2023). *Guidelines 3/2022 on Dark Patterns in Social Media Platform Interfaces.* Final version, March 2023\.  
24. **FTC** (2022). *Bringing Dark Patterns to Light.* Federal Trade Commission Report.  
25. **Santos, C. et al.** (2024). Which Online Platforms and Dark Patterns Should Be Regulated Under Article 25 of the DSA? *SSRN.* doi:10.2139/ssrn.4899559  
26. **Fansher, M., Chivukula, S.S., & Gray, C.M.** (2018). \#darkpatterns: UX Practitioner Conversations about Ethical Design. *CHI 2018 EA.* doi:10.1145/3170427.3188553  
27. **Lacey, C. et al.** (2023). Dark Patterns in Games: Definitions, Taxonomy, and Research Agenda. *CHI 2023\.* doi:10.1145/3544548.3580842  
28. **Kollmer, F., & Eckhardt, A.** (2023). Dark Patterns. *Business & Information Systems Engineering, 65*, 201–208. doi:10.1007/s12599-022-00783-7

### **Bases Teóricas (fundamentos psicológicos y económicos)**

29. **Kahneman, D.** (2011). *Thinking, Fast and Slow.* Macmillan. \[Base de sesgos cognitivos explotados\]  
30. **Thaler, R.H., & Sunstein, C.R.** (2008). *Nudge.* Yale University Press. \[Concepto de choice architecture\]  
31. **Kahneman, D., & Tversky, A.** (1979). Prospect Theory: An Analysis of Decision under Risk. *Econometrica, 47*(2), 263–291. \[Loss aversion, base de countdown timers\]

---

### **Recursos de Consulta Continua**

| Recurso | URL | Tipo |
| ----- | ----- | ----- |
| Deceptive Design | deceptive.design | Repositorio canónico de casos · Brignull |
| Princeton WebTAP | webtransparency.cs.princeton.edu | Dataset crawl 11K sitios |
| CHI Proceedings | dl.acm.org/conference/chi | Conferencia HCI principal del campo |
| EDPB Guidelines | edpb.europa.eu | Regulación UE |
| FTC Dark Patterns | ftc.gov/reports/dark-patterns | Enforcement EE.UU. |
| Gray Lab (Purdue) | colingray.me | Publicaciones actualizadas Colin Gray |

