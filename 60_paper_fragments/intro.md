# Introduction

## Motivation & Problem Statement

- In Hochschulbildung ist Erstellung von ''guten'' Fragen (wie z.B. prüfungsvorbereitende Fragen) zeitintensiv. LLMs bieten Potential, durch Automated Question Generation (AQG) diesen Prozess zu beschleunigen
- Fragengenerierung ist nicht einfach nur "Erstelle eine Frage zu...". Es fordert viel mehr Expertise, um inhaltliche Präzision und das Einhalten gezielter kognitivier Anforderungen (wie z.B. durch Bloom's Taxonomy) in der Frage zu gewährleisten
- Lücke (noch geringfügig formuliert): Bestehende Studien nutzen oft veraltete Modelle (und verpassen somit Reasoning-Modelle) oder lassen Lernziele / Bloom-Level außer Acht. Auch der Vergleich zwischen Frage und Antwort (Content Adherence + Bloom Alignment) ist oft nicht tiefgehend untersucht

## Objectives

- Die Arbeit evaluiert die Fähigkeiten moderner Reasoning-Modelle (Stand: Ende 2025) bei der Generierung von MCQ und Open-Ended Fragen im Informatik-Kontext in Hochschulbildung, unter Berücksichtigung der Bloom'schen Taxonomie
- Durch den systematischen Aufbau von zwei kontrollierten Experimenten mit Expertenbewertungen werden die Modelle auf Inhaltstreue und pädagogisches Alignment über das Bloom-Spektrum untersucht

## Research Questions

Die Studie zielt darauf ab, in zwei koordinierten Experimenten die folgenden Forschungsfragen zu beantworten:

- **RQ1:** How effectively can LLMs be constrained to generate questions based on instructional materials?
- **RQ2:** Does the restriction to a question format influence achieving the cognitive level in generating questions?
- **RQ3:** Do the answers of the LLMs fit the generated questions?

## Contributions

1. Mittels Claude 4.5 Opus, GPT-5.2, DeepSeek V3.2 und xAI Grok-4 wird ein umfassender Vergleich von Reasoning-Modellen über verschiedene Frageformate und Bloom-Level hinweg durchgeführt, um deren Eignung für die pädagogische Fragengenerierung zu bewerten
2. Ein detaillierter qualitativer Blindtest (3 Rater pro Experiment) mit einem umfassenden Bewertungsraster (Adaption der Rubrik von Mi & Li, 2024) mit einer 1-5 Likert-Skala wird durchgeführt. Dies wurde durch Experten-Workshops vorbereitet, um die Einheitlichkeit der Bewertungen zu gewährleisten und die Bewertungsrubrik zu optimieren
3. Jeglicher Code, Prompts, generierte Fragen und Antworten, sowie die Ergebnisse der beiden Experimente werden gemeinsam und offen über GitHub bereitgestellt: [https://github.com/mgrube753/question-generation]

## Kontext & Scope

Mit dieser Studie konzentrieren wir uns auf AQG hinsichtlich universitärer Skripte zu Rechnernetzen, insbesondere dem ISO-OSI Modell. Sowohl MCQ als auch Open-Ended Fragen und die zugehörigen Antworten werden in einem Template-basierten Prompting-Ansatz erstellt. Dieser wird in einem mehrstufigen Prozess verwendet (siehe Idee bei Bhowmick et al., 2023), um die Fragen und Antworten getrennt, aber aufeinander aufbauend, generieren zu können. Durch diese strikte Trennung, ein strukturiertes Pipeline-Design und die Schulung der Rater können die Forschungsfragen durch eine umfangreiche Bewertungsrubrik gezielt adressiert und beantwortet werden.
