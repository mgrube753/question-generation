# Introduction

## Motivation & Problem Statement

- In Hochschulbildung ist Erstellung von ''guten'' Fragen (wie z.B. Prüfungs- oder prüfungsvorbereitende Fragen) zeitintensiv (Maity et al., 2025). LLMs bieten Potential, durch Automated Question Generation (AQG) diesen Prozess zu beschleunigen (Doughty et al., 2024)
- Fragengenerierung ist nicht einfach nur "Erstelle eine Frage zu...". Es fordert viel Expertise (Al Faraby et al., 2024), um beispielsweise inhaltliche Präzision und das Einhalten gezielter kognitiver Anforderungen (wie z.B. durch Bloom's Taxonomy) in der Frage zu gewährleisten
- Lücke (noch geringfügig formuliert):
  - Bestehende Studien nutzen oft veraltete oder kleine Modelle (und verpassen somit Reasoning-Modelle)
    - Bhowmick et al., 2023: T5 und InstructGPT bspw. genutzt; modernere LLMs wie GPT-4 damals könnten qualitativ bessere Fragen generieren, aber diese (nicht-lokalen) Modelle können Latenz-, Datenschutz- und Reliability-Probleme aufzeigen, was im Bereich der Bildung nicht verhandelbar ist
    - Zhuge et al., 2025: Deren fine-tuned Dual-LLM-Engine enthält im Vergleich zu Vergleichsmodellen im Paper nur kleine Modelle wie LLaMA2-13B; gewollt, da große Modelle wie GPT-4 viel an Rechen- und Speicherressourcen benötigen, was im Bildungskontext nur beschränkt verfügbar ist, somit nicht praktikabel
    - Kleiner positiver Kontrast --> Kang et al., 2025: ihnen war es wichtig, eine Mischung aus Popularität, einfachen API-Zugriffen und Balance aus Leistung, Kosten, und Zugänglichkeit zu haben (haben bspw. GPT-4o und Claude 3.5 Sonnet benutzt, welche etwas zeitgemäßere Modelle sind)
  - oder lassen Lernziele / Bloom-Level außer Acht
    - Kang et al., 2025: messen bei ihren generierten Fragen (basierend auf Video-Transkripten) von 1-5 die Question Difficulty, haben aber nirgends von Bloom-Leveln gesprochen
    - An et al., 2025: Autoren haben bei Prompting zwischen "Factual Recall" und "Higher-Order Thinking" für die MCQ unterschieden, aber sprechen über kein festes Framework wie Bloom für e.g. Bloom Alignment von Fragen
  - Auch der Vergleich zwischen Frage und Antwort ist oft nicht tiefgehend untersucht
    - Content Adherence der Antwort:
      - Maity et al., 2025 | Scaria et al., 2024: Keine Antwortgenerierung bspw. enthalten
      - Al Faraby et al., 2024 beschreibt die Wichtigkeit von Halluzinationen; dadurch, dass LLMs Fragen mit kontext-fernen oder falschen Informationen generieren können (trotz Aufforderung, sich an Material zu halten), braucht es zukünftig Validierungssyteme, um Halluzinationen zu minimieren
    - Bloom Alignment zwischen Q und A: nicht aufgezeigt; Paper wie Zhuge et al., 2025  | Maity et al., 2025 | Scaria et al., 2024 gehen nur auf Frage-Bloom-Alignment ein zum gewünschten Level

## Objectives

- Die Arbeit evaluiert die Fähigkeiten moderner Reasoning-Modelle (Stand: Ende 2025) bei der Generierung von MCQ und Open-Ended Fragen im Informatik-Kontext in Hochschulbildung, unter Berücksichtigung der Bloom'schen Taxonomie
- Durch den systematischen Aufbau von zwei kontrollierten Experimenten mit Expertenbewertungen werden die Modelle auf Inhaltstreue und pädagogisches Alignment über das Bloom-Spektrum untersucht

## Research Questions

Die Studie zielt darauf ab, in zwei koordinierten Experimenten die folgenden Forschungsfragen zu beantworten:

- **RQ1:** How effectively can LLMs be constrained to generate questions achieving cognitive levels based on instructional materials? --> bedenken: Fokus auf Inhaltstreue der Frage zum Inputtext
- **RQ2:** Does the restriction to a question format influence achieving the cognitive level in generating questions? --> bedenken: primär Fokus auf Bloom-Alignment der Frage zum gewünschten Bloom-Level
- **RQ3:** Do the answers of the LLMs fit the generated questions? --> bedenken: Fokus auf inhaltliche Korrektheit der Antwort zur generierten Frage, sowie Bloom-Alignment der Antwort zum generierten Bloom-Level der Frage

## Contributions

1. Mittels Claude 4.5 Opus, GPT-5.2, DeepSeek V3.2 und xAI Grok-4 wird ein umfassender Vergleich von Reasoning-Modellen bzgl. Frage- und Antwortgenerierung über verschiedene Frageformate (MCQ und Open-Ended) und Bloom-Level hinweg durchgeführt, um deren Eignung für die pädagogische Fragengenerierung zu bewerten
2. Ein detaillierter qualitativer Blindtest (3 Rater pro Experiment) mit einem umfassenden Bewertungsraster (Adaption der Rubrik von Mi & Li, 2024) mit einer 1-5 Likert-Skala wird durchgeführt. Dies wurde durch Experten-Workshops vorbereitet, um die Einheitlichkeit der Bewertungen zu gewährleisten und die Bewertungsrubrik zu optimieren
3. Jeglicher Code, Prompts, generierte Fragen und Antworten, sowie die Ergebnisse der beiden Experimente werden gemeinsam und offen über GitHub bereitgestellt: [https://github.com/mgrube753/question-generation]

## Kontext & Scope

Mit dieser Studie konzentrieren wir uns auf AQG hinsichtlich universitärer Skripte zu Rechnernetzen, insbesondere dem ISO-OSI Modell. Sowohl MCQ als auch Open-Ended Fragen und die zugehörigen Antworten werden in einem Template-basierten Prompting-Ansatz erstellt. Dieser wird in einem mehrstufigen Prozess verwendet (siehe Idee bei Bhowmick et al., 2023), um die Fragen und Antworten getrennt, aber aufeinander aufbauend, generieren zu können. Durch diese strikte Trennung, ein strukturiertes Pipeline-Design und die Schulung der Rater können die Forschungsfragen durch eine umfangreiche Bewertungsrubrik gezielt adressiert und beantwortet werden.
