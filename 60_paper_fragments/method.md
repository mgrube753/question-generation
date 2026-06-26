# Methodology

## Research Design

- Studie besteht aus zwei Experimenten zur Beantwortung der 3 FF
  - Experiment 1: Inhaltstreue/Relevanz der Fragen zum Eingabetext (FF1) und Bezug auf inhaltliche Korrektheit der Antworten (FF3)
  - Experiment 2: Alignment der Fragen zum gewünschten Bloom Level (FF2) und Passung des Bloom-Levels der Antwort zur generierten Frage (FF3)

## Models

- Modellauswahl (bis Dezember 2025):
  - Anthropic Claude 4.5 Opus
  - OpenAI GPT-5.2
  - DeepSeek V3.2 (Thinking Mode)
  - xAI Grok-4
- Alle (4 an der Zahl, um ausreichend Vielfalt zu gewährleisten + mehr Daten zur Auswertung) Modelle haben Reasoning verwendet, um vor der User-Antwort eine Vorabanalyse des Kontextes durchzuführen

## Context for Question Generation

- ISO-OSI Modell als Inputtext für die Generierungsaufgaben
- Basis: Skriptauszüge von Prof. Cap
- Zwei Frageformate: Multiple-Choice (MCQ) und Open-Ended (OE)
  - MCQ: Bloom-Level 1-3 Abdeckung (siehe sinngemäß [Uni Zürich](https://teachingtools.uzh.ch/de/tools/lernziel-taxonomien))
  - OE: Bloom-Level 1-6 Abdeckung
- Experiment 1: Pro Frage 1 Layer, pro Layer gibt es 1 festes Lernziel (7) --> Lernziele, da Doughty et al. (2024) auch genutzt haben
  - Frageanzahl: 4 LLMs x 7 Layer x 2 Frageformate = 56 Fragen
- Experiment 2: Pro Frage alle 7 Layer als Kontext, pro Bloom-Level stattdessen 1 festes Lernziel (6)
  - Frageanzahl: 4 LLMs x 6 Bloom-Level x 2 Frageformate = 48 Fragen

## Prompting & Generation

- Modularer, mehrstufiger Prompting-Ansatz (Bhowmick et al., 2023) wird auf unser Forschungsdesign adaptiert
- MCQ-Generierung in drei Schritten: Stem, Key (2 Stück), Distractor Generation (2 Stück), passend zum Bloom-Level
- Alle Teil-Prompts folgen einer einheitlichen Struktur: Role, Task, Context, Reasoning Steps, Output Format, Stop Conditions, basierend auf zwei Cookbooks von Openai:

  - <https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide>
  - <https://cookbook.openai.com/examples/gpt4-1_prompting_guide>

- Zwischen Fragen und Antworten gibt es prompttechnische Maßnahmen: WICHTIG

## Analysis & Evaluation Methods

### Evaluation Design

- Qualitative Expertenbewertung (Blindtest) mit experiment-spezifischen Ratern (jeweils 3) und adaptiertem Bewertungsraster (1-5 Likert Skala) basierend auf Mi & Li (2024)
  - Experiment1: Domain-Experten mit mehr Fokus auf ISO-OSI (Lehrstuhl IuK)
  - Experiment2: Pädagogische Experten mit mehr Fokus auf Bloom's Taxonomy (Philosophische Fakultät)
  
### Rating Criteria

- Fragen und Antworten wurden mit spezifischen Kriterien bewertet, welche sich in den beiden Experimenten teilweise unterscheiden (welche Kategorien angewandt wurden), um die jeweiligen Forschungsfragen gezielt zu adressieren (Q für Question, A für Answer, QA für beide):

| Kriterium | Experiment |
|-----------|-----------|
| Relevance_Q | E1 |
| Clarity_QA | E1, E2 |
| Answerability_Q | E1 |
| Challenging_Q | E1, E2 |
| Value_Q | E1, E2 |
| Language_QA | E1, E2 |
| Correctness_A | E1 |
| BloomAlignment_QA | E2 |

- Relevance_Q und Answerability_Q sind Kriterien für FF1
- Kriterien Value & Language wurden von Prof. Cap vorgeschlagen, um Lernzielrelevanz und sprachliche Präzision/Komplexität zu bewerten
- Correctness wurde hinzugefügt für Antwortenbewertung in E1 (Fokus FF3)
- Idee zu Bloom Alignment für E2 gesehen bei Scaria et al. (2024), nun adaptiert für Fragen (FF2) und Antworten (FF3) in unserem Setup

### Rubric Design for Criteria

- Gewisse Rubriken waren zuvor rudimentär ausgelegt, wir haben statt
  - BA: 0-10 Skala mit schwächeren Punkt-Beschreibungen
  - Mi and Li, 2024: 0-10 Punkte pro Kategorie, ohne klare Beschreibungen (wir nutzen die Kategorien aber als Basis)
  - Scaria et al., 2024: 9-Item Rubrik, mit fast ausschließlich Binär-Entscheidungen
  - **Jetzt**: 1-5 Likert Skala (wie in Maity et al., 2025), pro **Kategorie** eine verständliche Fragestellung, und pro **Punktvergabe** eine feste Beschreibung

### Rater Workshops

- Dies wurde in einem vorher durchgeführten Workshop mit den Ratern durchgegangen, damit sie die Ablauf und Kriterien verstehen und einheitlich auf 2 Beispielfragen anwenden können (pro Workshop-Phase 2 Fragen). Ziel dessen war, die Rater vorzubereiten, mit ihnen zu diskutieren, Einblicke zu bekommen, und final vernünftige Agreement-/Reliability-Ergebnisse in der finalen Bewertung zu erreichen.
- Es gab 2 Workshop-Phasen pro Experiment:
  1. 1zu1 mit Freiwilliger Person
  2. Gruppendiskussion mit allen 3 Ratern, um weitere Kritikpunkte zu sammeln und die Rubrik zu verbessern, sowie die Rater gemeinsam auf die finale Bewertung vorzubereiten
  
### Sampling & Rating Process

- Nach Workshops gab es diverse Änderungen an der Rubrik, sowie einen neuen Generation Run, welcher pro Experiment nachfolgend gesampled wurde (E1: 24/56 Fragen, E2: 24/48 Fragen)
- Nach Bewertung (numerisch + Kommentare) gab es 24x3=72 Ratings pro Experiment, welche in CSV-Tabellen festgehalten wurden. Näheres zur Auswertung wird in Evaluation behandelt (Tabellen, Boxplots, Heatmaps für Bloom Alignment + Korrelationsanalyse, sowie Agreement/Reliability-Analysen)
