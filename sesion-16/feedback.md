# Feedback de Proyecto: Fricción Adaptativa e Insatisfacción en el UX

**Estudiante:** Santiago Gaete  
**Evaluadores:** Héctor Novoa, Joaquín Zerené y Panel de Evaluación  
**Tema:** Fricción adaptativa e insatisfacción en el UX para combatir el uso no intencional (*scroll* infinito)

---

## 1. Feedback de Héctor Novoa (y Panel de Evaluación)

### 1.1 Apuntes de Feedback Directo
- **Marco teórico y comportamiento humano:** Incluir el comportamiento humano dentro del marco teórico. Comprender las dimensiones del comportamiento humano para introducir el tema o problemática (p. ej., incorporar la ludopatía).
- **Muestra de usuario:** Profundizar y enmarcar al usuario de manera más robusta (el usuario actual resulta muy genérico). Caracterizar la muestra de forma sistematizada (cuestionarios, estadísticas, *focus group*, entrevistas, encuestas).
- **Bases del diseño de interfaz:** El marco teórico debe sentar las bases del diseño de interfaz y comprender la función específica de los patrones por plataforma.
- **Encuadre del caso de estudio:** Desarrollar un encuadre más específico. Incorporar formalmente el concepto de *Dark Patterns* (patrones oscuros), los cuales no se abordan explícitamente en el documento actual.
- **Análisis de interfaces:** Caracterizar y analizar de mejor manera las interfaces existentes.
- **Validación de hipótesis e indicadores:** ¿Cómo demostrar que la reducción de uso será duradera y no producto de la novedad del prototipo? Definir indicadores de impacto claros.
- **Consecuencias del *scroll* infinito:** Profundizar en las consecuencias biológicas, psicológicas y sociales.
- **Voz propia y redacción:** Cuidar la voz propia en la redacción (evitar un estilo impersonal que parezca generado por IA).
- **Bibliografía:** Correlacionar e integrar la bibliografía de forma sustancial en el cuerpo del texto (evitar un listado extenso sin citas cruzadas).

---

### 1.2 Feedback Estratégico y Estructurado
> **Para:** Santiago Gaete  
> **De:** Héctor Novoa (y panel de evaluación)  
> **Apreciación:** La presentación demuestra un nivel de madurez analítica destacable. Se desglosa muy bien el problema (*Biología + Diseño de Interfaz + Economía de la Atención*) y el hallazgo sobre intervenir en la brecha de la "insatisfacción" (separando el *querer* del *gustar* basándose en Kent Berridge) constituye un enfoque brillante.

#### Recomendaciones Estratégicas:

#### 1. Profundidad Psicológica: De la "Insatisfacción" a la Patología
- **El puente hacia la ludopatía:** Conectar formalmente el refuerzo variable (el cual explica por qué el algoritmo muestra contenido no deseado para mantener el *engagement*) con las mecánicas de las máquinas tragamonedas. El "arrastre" o *scroll* compulsivo comparte las mismas bases neurológicas que una adicción conductual.
- **Consecuencias del "arrastre":** Visibilizar el impacto real del uso no intencional más allá de la pérdida de tiempo: pérdida de noción de la realidad, deuda de sueño, ansiedad e impacto en la responsabilidad laboral/académica. Esto justificará por qué la intervención es urgente y no solo un ejercicio estético de diseño.

#### 2. Especificidad del Usuario: Más allá de "Los Creativos"
- **Creación de *User Personas*:** Definir 2 o 3 arquetipos específicos dentro del espectro de "creativos" (p. ej., publicista *freelance*, ilustrador en búsqueda de referente visual, etc.).
- **El contexto condiciona la fricción:** El impacto del *scroll* infinito no es idéntico en un estudiante que en un técnico de control. Moldear arquetipos permitirá fundamentar cómo y por qué la fricción adaptativa opera eficazmente en contextos de vida y trabajo específicos.

#### 3. El Desafío del Acostumbramiento (*Habituation*)
- **La paradoja del prototipo:** Al proponer fricción adaptativa (botones que cambian de lugar, menús con 4 opciones, notificaciones sarcásticas), surge la pregunta de investigación: ¿Cómo garantizar que el usuario no genere memoria muscular o ceguera cognitiva ante la propia fricción?
- **Medición de durabilidad:** La investigación debe ir más allá de la validez en papel. Es necesario proponer cómo medir que la reducción del abuso sea duradera y no un simple "efecto novedad". ¿Cómo evitar que el tono sarcástico termine siendo ignorado y cerrado de forma mecánica?

#### 4. Viabilidad Técnica y la "Caja Negra" de las Apps
- **Intervención de UI de terceros:** En el prototipo se plantea que la app "oculte distracciones" al responder mensajes. Superponer capas (*overlays*) que modifiquen componentes nativos en iOS/Android es complejo y suele ser bloqueado por las plataformas. Aclarar si la propuesta es un manifiesto/guía de diseño ético sugerido para las empresas desarrolladoras o una aplicación de terceros (y cómo sortearía las restricciones técnicas).
- **Explicar el algoritmo "enemigo":** Dedicar un apartado en el marco teórico a explicar el funcionamiento de los algoritmos de perfilamiento y recomendación ("comprender el motor detrás de la carrocería").

#### 5. Rigurosidad Metodológica de Validación
- **Levantamiento de datos reales:** Sustentar la validación en un método cualitativo/cuantitativo estructurado, superando muestras pequeñas o anecdóticas.
- **Testeo de la "Insatisfacción":** Diseñar pruebas de usabilidad (*A/B Testing*) con el prototipo. Medir la frustración para encontrar el "punto dulce": si la frustración es excesiva, el usuario desinstalará la app; si es insignificante, continuará en el bucle de *scroll*.

---

## 2. Feedback de Joaquín Zerené

### 2.1 Apuntes de Feedback Directo
- **Enfoque conceptual:** El proyecto es interesante, claro, bien estructurado y coherente. Sin embargo, se abordan temas categorizados como *biología* cuando corresponden formalmente a la *psicología cognitiva y conductual*.
- **Pilares teóricos de UX/UI:** Fortalecer el primer capítulo respecto a la teoría de UX/UI existente, tomando a **Donald Norman** como pilar fundamental.
- **Orden del marco integrador:**
  1. *Economía de la Atención* (Paraguas macro y modelo de negocio).
  2. *Psicología Cognitiva* (Mecanismos de atención y comportamiento).
  3. *Diseño de Interfaz / UX* (Encuadre disciplinar y propuesta de solución).
- **Alcance del prototipo:** Un prototipo de menor escala, altamente validado e iterado, resulta preferible a un proyecto extenso con flancos vulnerables.
- **Protagonismo del diseño:** Incorporar el análisis de *Dark Patterns* e interfaces existentes para acentuar el rol de la disciplina.
- **Metodología:** Reemplazar las encuestas masivas por metodologías cualitativas como entrevistas en profundidad y etnografía.
- **Estrategia de presentación:** Guiar pedagógicamente a la audiencia, introduciendo y definiendo con claridad conceptos clave como "fricción adaptativa".
- **Referencias bibliográficas sugeridas:**
  - *The Attention Economy* - Claudio Celis
  - *Tristes por Diseño* (*Sad by Design*) - Geert Lovink
  - *La Vida Espectral* - Éric Sadin
  - *Revolución Silenciosa*
  - Reflexión filosófica sobre el rol de la tecnología en la libertad del sujeto.

---

### 2.2 Observaciones y Ajustes Estratégicos Estructurados
> **Para:** Santiago Gaete  
> **De:** Joaquín Zerené  
> **Apreciación:** El proyecto presenta un desarrollo sólido, una problemática relevante y una propuesta coherente. Se recomiendan los siguientes ajustes metodológicos y estructurales:

#### Ajustes Recomendados:

#### 1. Reestructuración y Precisión del Marco Teórico
- **De "Biología" a "Psicología Cognitiva":** Reclasificar conceptos como refuerzo variable, dopamina y hábitos (B.J. Fogg, Don Norman) bajo la psicología cognitiva y conductual aplicada al diseño.
- **Estructura Deductiva (Macro a Micro):**
  - **Economía de la Atención:** Contexto global sobre el modelo de negocio extractivo.
  - **Psicología Cognitiva:** Explicación de los procesos subyacentes de la atención y la conducta.
  - **Diseño de Interfaz (UX):** Herramientas y perspectivas disciplinares para abordar el problema.

#### 2. Reformulación de la Problemática
- Evidenciar la mirada disciplinar del diseño: el problema debe plantearse mostrando cómo el diseño de interacción actual produce el conflicto y cómo el propio diseño puede solucionarlo (apoyándose en literatura crítica sobre *Dark Patterns*).

#### 3. Estrategia Metodológica
- **Descartar encuestas masivas:** Aprovechar la amplia literatura y datos estadísticos globales ya existentes sobre tiempo en pantalla.
- **Foco en métodos cualitativos:** Emplear entrevistas en profundidad o técnicas etnográficas con un perfil de usuario acotado para obtener *insights* cualitativos sobre motivaciones y fricciones reales.

#### 4. Acotación del Alcance
- Limitar el proyecto a una plataforma específica, un flujo de uso concreto o un arquetipo determinado. Priorizar la profundidad y refinamiento técnico por sobre la extensión.

#### 5. Claridad Conceptual en la Presentación
- Definir rigurosamente la terminología propia (como "fricción adaptativa") desde la primera mención para facilitar la comprensión de la comisión evaluadora.

---

## 3. Resumen General y Conclusiones del Panel

### 3.1 Síntesis General del Proyecto
Santiago Gaete aborda el uso no intencional (*"el arrastre"*) en aplicaciones de *scroll* infinito (Instagram, TikTok). Propone un sistema de **fricción adaptativa** enfocado en generar una **insatisfacción controlada**.

**Pilares Teóricos Reestructurados:**
1. **Economía de la Atención:** Contexto socioeconómico y modelos de negocio.
2. **Psicología Cognitiva y Conductual:** Dopamina, refuerzo variable y adicción conductual.
3. **Diseño de Interfaz / UX:** Patrones de interacción, *dark patterns* y diseño ético.

---

### 3.2 Énfasis y Recomendaciones Finales
- **Apropiación de la Teoría del Diseño:** Integrar autores que hayan articulado explícitamente el cruce entre economía de la atención, psicología y diseño.
- **Apalancamiento Teórico:** Evitar construir las conexiones desde cero; respaldarse en marcos teóricos consolidados.
- **Obras y Autores Fundamentales:**
  - **Don Norman:** Psicología cognitiva aplicada a la usabilidad e interacción.
  - **Geert Lovink (*Tristes por Diseño / Sad by Design*):** Análisis crítico de cómo la arquitectura de redes sociales genera vacío e insatisfacción.
  - **Claudio Celis / Yves Citton (*Economía de la Atención*):** Análisis de la ecología de la atención.
  - **Éric Sadin (*La Vida Espectral*):** Dimensión filosófica del sujeto ante la mediación tecnológica.