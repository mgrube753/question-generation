# Background

## Automated Question Generation (AQG)

- AQG heißt _automatisches Generieren_ von e.g. Prüfungsfragen oder prüfungsvorbereitenden Fragen, _welche auf Lehrinhalten basieren_ können (sinngemäß Al Faraby et al., 2024), im jetzigen Zeitalter KI-gestützter Natur (siehe gesamte Literaturübersicht)
- Zwei häufig vorkommende Frageformate in der Hochschulbildung und Literatur:
  - **Multiple-Choice Questions (MCQ):** Bestehen aus Stem (Fragestamm), Anzahl korrekter Antwortmöglichkeiten (Keys) und inkorrekter Antwortmöglichkeiten (Distraktoren). So kann man effizient und objektiv bewerten. Jedoch eingeschränkte kognitive Tiefe zum Abfragen; unterstrichen durch Möglichkeit zu Raten
  - **Open-Ended (OE) Questions:** Beantwortung basierend auf Freitext; auch höhere kognitive Prozesse können abgefragt werden. Durch individuellen Beitrag ist manuelles Bewerten jedoch aufwendiger
- AQG-Ansätze heutzutage nutzen neuronale Modelle bzw. transformer-basierte Technologien (siehe Literaturübersicht, z.B.: An et al., 2025 | Bhowmick et al., 2023 | Kang et al., 2025 | Meissner et al., 2024)
  
## Antwort-Generierung im Fokus

- Gewisse AQG-Ansätze erstellen neben der Fragen auch die Antworten, entweder:
  - **Integriert:** Meissner et al., 2024 mit Fokus auf OE-Matheaufgaben und liefern dazu entsprechende Musterlösung | Kang et al., 2025 neben Short-Answer Questions auch die passende Antwort generieren | Al Faraby et al., 2024 ebenso beiläufige Antwortgenerierung (mehr für Related Work aufsparen), oder
  - **Sequenziell:** Bhowmick et al., 2023 mit intermediärer Antwortgenerierung (Grundlegende 4-Step MCQ Pipeline: Content Extraction, Question Generation, Answer Prediction, Distractor Generation; Nutzung verschiedener Modelle für einzelne Schritte)
  
## Herausforderungen in AQG

- _Frage muss sich an den Quelltext halten_, ohne Halluzinationen oder externes Wissen zu integrieren
  - An et al., 2025: LLMs haben teilweise in Programmier-MCQ Konzepte eingebunden, die nicht im Kursmaterial zu finden waren
- _Antwort zur generierten Frage muss inhaltlich korrekt auf die Frage abgestimmt sein_
  - Doughty et al., 2024: Anzahl korrekter MCQ-Keys oft nicht korrekt | Meissner et al., 2024: Antworten zu Mathefragen oft mit Rechenfehlern versehen | Al Faraby et al., 2024: Oft Antwort-Snippets, welche die Frage gar nicht beantwortet haben
- _Frage muss das gewünschte kognitive Niveau (z.B. Bloom-Level) erfüllen_
  - Zhuge et al., 2025: Modelle ohne Bloom-Finetuning weichen oft vom gewünschten Level ab (Heatmaps im Paper) | Meissner et al., 2024: LLM neigte dazu, unverhältnismäßig oft Apply3 und Analyze4 Fragen zu erstellen, anstatt die oberen und unteren Levels gleichmäßig zu treffen | Scaria et al., 2024: **Fragequalität** für Apply3 und Create6 Fragen besonders schwach, aber keine Angabe darüber, welche Levels für welches Modell schwer zu erreichen waren (bedenken: sie haben "Erstelle Frage zu jedem Bloom Level" als Anweisung gegeben)

## LLMs und Reasoning-Modelle

- LLMs (welche hauptsächlich für AQG benutzt werden) basieren auf der Transformer-Architektur ([Vaswani et al., 2017](https://arxiv.org/abs/1706.03762))
- Seit September 2024 gibt es zudem mit der Vorstellung von OpenAI o1-mini einen Umschwung zu **Reasoning-Modellen**
- Das heißt, vor der eigentlichen Output-Generierung wird ein interner generierungs-basierter Analyseprozess durchgeführt, um finale Ausgabe durch Vorbereitung zu verbessern
- (Unsere Studie zielt auf Nutzung von ausschließlich Reasoning-Modellen ab, da frühere Forschung in AQG Modelle oft bis zu GPT-4 genutzt hat (sehr outdated))

## Bloom's Taxonomy im AQG-Kontext

- Bloom's Taxonomy (Bloom et al., 1956; revidiert durch Krathwohl, 2002) klassifiziert kognitive Anforderungen durch sechs hierarchische Stufen (aufsteigend in Komplexität): 1. **Remembering**, 2. **Understanding**, 3. **Applying**, 4. **Analyzing**, 5. **Evaluating**, 6. **Creating**
- Bestimmte Frageformate eignen sich für bestimmte Bloom-Level besser (siehe Uni Zürich)
- Ein gewünschtes Bloom-Level zu erreichen ist in AQG anspruchsvoll: Modelle weichen oft vom gewünschten Level ab. Beispielsweise durch Konflikt zwischen Bloom-Level und Wahl des Fragetyps (in Thesis wurde Problem erkannt, und Doughty et al., 2024 hatte MCQ über alle Levels hinweg generiert. Dies wollen wir durch Thesis-Erfahrung als Pilot-Studie nun vermeiden)
- Learning Objectives als sinnvolle Ergänzung: Durch Angabe präziser Lernziele für eine Frage (Future Work meiner Thesis) könne man die Freiheitsgrade der LLMs einschränken, um Bloom-Alignment zu verbessern (Doughty et al., 2024 haben Bloom-Level zum Learning Objective durch Submodell bestimmen lassen, und beides für Qgen benutzt)

## ISO-OSI als AQG-Inhalt

- Sinnvoller Anwendungsfall für AQG ist das ISO-OSI-Modell (bereits in Thesis verwendet)
- Ein Standardkonzept der Rechnernetze, das Kommunikation zwischen Computersystemen in sieben Abstraktionsschichten unterteilt.
- Jede Schicht hat spezifische Funktionen und bietet definierte Schnittstellen zu den benachbarten Schichten
- Warum für AQG geeignet:
  - _Klar abgegrenzte Schichten mit hierarchischer Struktur_ (gezielter Kontext mit einer Schicht pro Frage möglich (Experiment 1))
  - _Als Ganzes komplex genug, um zusammenhängende Fragen über alle Layer hinweg zu generieren_ (Experiment 2 nutzt alle Layer als gemeinsamen Kontext)
  - (Strukturiertes, präzises Lehrmaterial (von Prof. Cap) liegt bereits vor)

## Evaluation dieser Fragen und Antworten

- Expertenbasierte Evaluation ist hierfür Goldstandard (siehe bspw. Mi & Li, 2024 | Scaria et al., 2024), ist jedoch eine Methode, die zeit- und kostenintensiv ist
  - Bewertung durch standardisierte Rubriken mit mehreren Kriterien (unsere beiden Rubrik-Varianten basieren auf beiden, primär Mi & Li, 2024 | Bloom Alignment durch Scaria et al., 2024)
  - Pro Kriterium wird Punktwertung oft auf einer Likert-förmigen Skala vergeben (e.g. Meissner et al., 2024 mit 1-5 Likert)
- **Blindtest-Design:** Essentiell und sorgt dafür, dass die Bewertenden keine kritischen Details über die Herkunft der Fragen kennen (e.g. welches Modell --> Rosenthal-Effekt), Wichtigkeit ähnlich hervorgehoben in e.g. Al Faraby et al., 2024
- **Inter-Rater Reliability:** Bei mehreren Bewertenden wird Übereinstimmung der Ratings mit e.g. Kendall's W (Mi & Li, 2024), Fleiss' Kappa (meine Thesis), oder Cohen's Kappa/eine gewichtete Variante wie Quadratic Weighted Kappa (Scaria et al., 2024) gemessen. Mittels IRR kann man sicherstellen, dass die Bewertenden ein ähnliches Verständnis der Rubrik haben, und anderenfalls ggf. Missverständnisse bei Anwendung der Rubrik zu erkennen (siehe [hier bei Uni Kassel](https://lehrportal.uni-kassel.de/mod/page/view.php?id=6015))
- **Rater Workshops:** Vorbereitende Schulungen der Bewertenden sind hierbei essenziell, um ein einheitliches Verständnis der Rubrik zu ermöglichen, Beispiele zu diskutieren und die Rubrik iterativ zu verbessern
  - Al Faraby et al., 2024 haben Trainingssitzung durchgeführt vor eigentlicher Bewertung (Vertrautmachen mit Labeling mit Beispieldatensatz an Fragen)
  - Meissner et al., 2024 haben Ratern vor Bewertung individuelles Handbuch gegeben mit Beispielfragen, um Unklarheiten durch Rückfragen zu klären
