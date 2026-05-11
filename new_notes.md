# Neue Notizen

## Überlegung zu FF

Um die Forschungsfragen geeignet zu thematisieren, werden Plots und Tabellen benötigt. Nun ist fraglich, welche Informationen in Grafik-Form und welche in Tabellenform dargestellt werden sollten. Anhand dieser Ideen hier kann man auch noch überlegen, ob gewisses in Appendix oder Hauptteil kommt.

### FF1

How effectively can LLMs be constrained to generate questions based on instructional materials?

Fokussiert ausschließlich durch Experiment1
Kategorien dargestellt durch:

- By Question Type: Open-Ended vs. Multiple Choice
- By LLM: 4 Modelle
- By Bloom Level: 6 Levels
- Agreement/Reliability: 3 Metriken

#### By Question Type

- Reicht als TABELLE. Dort kann man sehen, dass qRelevance bei Open-Ended schwächer ist, und qAnswerability bei Open-Ended sehr tief ist. Fokus liegt mehr auf LLMs als auf Fragetyp

#### By LLM

- Hier wäre GRAFIK sinnvoll. Vieles ist zu sehen, wie gewisse Bogenhafte Verläufe (gleiche/inverse Eigenschaften für das gleiche LLM) etc.

#### By Bloom Level

- Nicht der Hauptfokus, daher keine Grafik, sondern TABELLE. qAnswerability fällt ab Bloom Level 4 rapide ab

#### Agreement/Reliability

- TABELLE für Question Criteria wichtig

### FF2

Does the restriction to a question format influence achieving the cognitive level in generating questions?

Fokussiert ausschließlich durch Experiment2
Kategorien dargestellt durch:

- By Question Type
- By LLM
- By Bloom Level, aber wird weggelassen, da die
- Heatmap (fragebasiert) besser ist. Es gibt noch eine antwortbasierte Heatmap für FF3...
- Agreement/Reliability

#### By Question Type

- Hier wäre GRAFIK sinnvoll (für qBloomAlignment und qValue). Question Type für FF wichtig

#### By LLM

- Hier wäre TABELLE sinnvoll (qBloomAlignment und qValue ausreichend gut sichtbar)

#### By Bloom Level

- Wird weggelassen, da die Heatmap 1 von 2 präziser ist

#### Heatmap 1 (fragebasiert)

- GRAFIK... auf x: target Bloom Level, auf y: actual Bloom Level
- Erkennbar, welche Bloom Levels gut getroffen werden, und welche nicht. Sichtbar, ob Über- oder Unterschätzung von Bloom Leveln vorliegt.

#### Agreement/Reliability

- TABELLE für Question Criteria wichtig

### FF3

Do the answers of the LLMs fit the generated questions?

Fokussiert durch beide Experimente, da es sowohl um die Frage-Antwort-Passung (Inhalt) als auch um die Bloom Level Passung (Antwort-Bloom zu Frage-Bloom) geht.
Kategorien (answer-based Inhalte) dargestellt durch:

- Experiment1:
  - By Question Type
  - By LLM
  - By Bloom Level
  - Agreement/Reliability
- Experiment2:
  - By Question Type
  - By LLM
  - By Bloom Level, aber wird weggelassen, da die Heatmap (antwortbasiert) besser ist.
  - Agreement/Reliability

#### Experiment1: By Question Type

- Hier wäre GRAFIK sinnvoll. Open-Ended Antworten schneiden in jeder Hinsicht schlechter ab als Multiple-Choice Antwortmöglichkeiten

#### Experiment1: By LLM

- TABELLE reicht, Differenzen nicht so stark sichtbar

#### Experiment1: By Bloom Level

- Hier wäre GRAFIK sinnvoll. Sehen treppenartige Abfälle.

#### Experiment1: Agreement/Reliability

- TABELLE für Answer Criteria wichtig

#### Experiment2: By Question Type

- Wenn überhaupt, TABELLE.

#### Experiment2: By LLM

- Hier wäre GRAFIK sinnvoll. Bessere Einsicht als "By Question Type"

#### Experiment2: By Bloom Level

- Wird weggelassen, da die Heatmap 2 von 2 präziser ist

#### Experiment2: Heatmap 2 (antwortbasiert)

- GRAFIK... auf x: actual question Bloom Level, auf y: actual answer Bloom Level
- Erkennbar, ob die Bloom Level der Antworten mit den erkannten Bloom Leveln der Fragen übereinstimmen.
- Sichtbar, dass Antwort-Bloom Level besser zum Frage-Bloom Level passt... Das Alignment für erkanntes Frage-Bloom-Level zum gewünschten Frage-Bloom-Level (s. Heatmap1) ist nämlich schlechter.

#### Experiment2: Agreement/Reliability

- TABELLE für Answer Criteria wichtig

---

## Literatur-Überlegungen zu den FF

### FF1

- Al Faraby et al. (2024) weist auf die Wichtigkeit von Halluzinationen hin, diese müssen validiert werden. Kontext-ferne oder falsche Informationen in den generierten Fragen (trotz dessen, dass man sich an den Quelltext halten _soll_) sind unerwünscht
- Doughty et al. (2024) weist auch darauf hin, dass man sich in Zukunft auf Alignment zwischen Frage und Lernstoff beziehen sollte
- Statt uns auf Metriken oder bspw. LLM-basierte Bewertung wie in Kang et al. (2025) zu verlassen, setzen wir in der Arbeit vollends auf Expertenbewertung. Beides zusammen würde den Aufwand der Evaluation deutlich erhöhen. Wir haben pro Experiment 3 verfügbare Bewerter gehabt, um die umfassenden Meinungen zu den generierten Fragen zu bekommen.
- In unserem ersten Experiment haben wir uns auf die Themenrelevanz und Beantwortbarkeit für die generierten Fragen fokussiert, um Inhaltsabdeckung der Fragestellungen auszuwerten.

### FF2

- Maity et al. (2025) meinten, dass Frameworks wie Bloom zuvor selten vollends eingebunden wurden. Sie haben alle Bloom Levels durch einen schwach gestellten Prompt angesprochen ("erstelle zu jedem Bloom Level eine Frage") + haben 8 Beispiele im Prompt (8-shot Learning) gegeben, um die LLMs zu steuern. Diese haben wir nicht. Es gab als Alternative auch zero-shot; 8-shot hat die Verteilung der Bloom Levels in den Fragen jedoch etwas stabilisiert.
- Wir haben stattdessen eine Fragetyp-Trennung in den Prompts, mehrstufig jeweils wie Bhowmick et al. (2023). Wir haben ein festes Bloom Level pro Frage/Konversation, das wir in den Prompts angeben mit Informationen zum jeweiligen Level. Wir haben auch Lernzielintegration pro Frage, um die LLMs stärker zu steuern.
- Doughty et al. (2024) nutzen zuvor auch LOs für ihre MCQ-Generierung, und GPT-4-Fragen hatten besseres LO und Bloom Alignment als human-crafted Fragen
- Problem voriger Veröffentlichungen: Alle haben (ggf. stark) veraltete Modelle (heutzutage besser entwickelt) verwendet

### FF3

- Doughty et al. (2024) zeigten, dass Antwortmöglichkeiten bspw. alle als korrekt markiert sind, aber eigentlich nur eine korrekt ist. Es wurden in dem Paper auch MCQ über alle Bloom Levels generiert... laut [Uni Zürich](https://teachingtools.uzh.ch/de/tools/lernziel-taxonomien) ist dies ungeeignet
- An et al. (2024) zeigten, dass ggf. keine der Antwortmöglichkeiten eigentlich korrekt war. Es gab auch mehrere Antwortmöglichkeiten, die das Gleiche aussagen (passierte uns nun auch). Halluzinationen (Content abseits des Kursmaterials) sind dort auch vorgefallen (je nach Bloom Level bei uns auch...)

---

## Methodische Überlegungen

- Wir haben an die Rubrik von Mi and Li (2024) angesetzt, haben aber Correctness (für Antwort), Value (Lernziel-Fokus) und Language (sprachliche Präzision) hinzugefügt
- Jede Frage kriegt einen Fragetyp und ein Bloom Level (MCQ 1-3, OE 1-6)
- Rubriken oft rudimentär, wir haben (statt BA: 0-10 und schwächere Punkt-Beschreibungen) nun 1-5 Likert Skala, pro Kategorie eine verständliche Beschreibung, pro Punktvergabe eine feste Beschreibung.
- Dies wurde in einem vorher durchgeführten Workshop mit den Ratern durchgegangen, damit sie die Kriterien verstehen und einheitlich anwenden können. Dies führte auch durch das Feedback zu diversen Änderungen (sowie einem neuen Generation Run), und zu diversen passenden Agreement-/Reliability-Ergebnissen.
