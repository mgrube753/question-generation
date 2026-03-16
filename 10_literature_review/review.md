## Was wissen wir aus Literatur

### Sprachmodelle können als zuverlässige Evaluatoren dienen

- **BA-Paper** Mi and Li [9] haben diverse Modelle verglichen ggü. Human Ratings auf Studentenfragen
  - Rubrik zuvor schon als Basis benutzt + enthält Bloom
- Kang et al. [4] haben GPT-4o benutzt zur Fragenbewertung
- **BA-Paper** Zhuge et al. [7] haben stattdessen zwei Small Language Models trainiert + Bloom-Alignment verglichen
  - Auch SLMs können via Fine-Tuning gut performen
  - Nicht jeder hat Datensätze/Trainingsmöglichkeiten

### Wie sieht es mit Inhaltstreue aus?

- **BA-Paper** Al Faraby et al. [1] in Conclusion Wichtigkeit von Halluzinationen
  - Future Work: Validierungssysteme, um diese zu minimieren
  - LLMs können Fragen mit kontext-fernen/falschen Informationen generieren
  - Obwohl sie gebeten werden, sich an Quelltext zu halten
- **BA-Paper** Bhowmick et al. [8] haben gelegentlich aufgetretene Halluzinationen (s. Discussion) 
  - Genutzte Modelle hier jedoch ebenso veraltet, bzw. auch klein (SLMs)
- Kang et al. [4] nutzten Context Utilization als Bewertungskriterium
  - 10 LLMs haben Fragen generiert, gab 1 LLM-as-a-Judge
  - Bestimmung, wie nah Frage am Quelltext/wie weit entfernt von Halluzination ist
- An et al. [2] haben Halluzinationen bemerkt bei MCQ-Generierung (Elemente außerhalb des Kurskontexts)
  - Gemini 2.0 Flash und 2.5 Flash benutzt <-- kleinere Modelle
  - 2.5 Flash haben wir benutzt, schnitt in diverser Hinsicht schlechter ab

### Bloom Scoring bzw. Alignment im Fokus

- **BA-Paper** Scaria et al. [10] hatten Probleme beim Generieren von Apply- und Create-Fragen
  - GPT-3.5 und GPT-4 waren die besten Modelle, jedoch alt
  - Bzgl. Alignment mangelt es aber an Informationen pro Level im Paper
  - Stattdessen Offenbarung des akkumulierten Alignments pro Modell
- **BA-Paper** Zhuge et al. [7] haben besseres Alignment mit SLMs hinbekommen via Fine-Tuning ggü. unangetasteten LLMs
  - e.g. GPT-4 hatte Probleme, die geforderte kognitive Ebene zu erzielen
- **BA-Paper** Doughty et al. [3] haben MC-Fragen mittels GPT-4 generiert
  - Große Pipeline, nutzt Learning Objectives (LOs), um mittels trainierten BERT-Classifiers Bloom Level zu bestimmen für kommende Frage
  - Comparative Study zwischen GPT-Fragen und Human-crafted, LO-/Bloom-Alignment besser bei GPT
- **BA-Paper** Maity et al. [5] haben alle Levels durch einen Prompt gleichzeitig erfragt
  - Jedoch schwache Prompt-Methodik
  - Mitgeben von 8 Beispielblöcken mit jeweils 6 Fragen (1/Level), genannt 8-Shot-Learning
  - Diese Methodik hat Bloom-Level-Verteilung über alle Fragen etwas stabilisiert
- Meissner et al. [6] haben GPT-3.5 zum Datenextrahieren und GPT-4 zum Generieren der Fragen benutzt
  - Gute Prompt-Methodik + Nutzung von RAG (Einspeisen von Infos durch Wissensdatenbank)
  - Alignment ist vernünftig, pauschal besser als unangetastete LLMs bei e.g. Zhuge et al.
  - Fällt auf, dass outdated Models überall vertreten sind...

### Wenn es um MC-Fragen geht...

- **BA-Paper** Doughty et al. [3] zeigten Probleme in MCQ-Distraktoren bei Programmierfragen
  - Alle Antworten waren bspw. korrekt, aber nur eine als korrekt markiert
  - **MCQ wurden über alle Bloom-Levels generiert**, was wir nun vermeiden wollen
- An et al. [2] hatten diverse MCQ-Probleme
  - Keine der Antworten war eigentlich korrekt
  - Mehrere Antworten, die das Gleiche aussagen, etc.
- **BA-Paper** Bhowmick et al. [8] haben zuvor MCQs durch drei Schritte generiert (wollen wir auch)
  - Aber mit weniger Submodellen jeglicher Form; wir nehmen LLM x für jeden einzelnen Schritt einzeln

### Wo setzen wir bei Literatur an?

- Expertenbewertung elementar, nutzen wir auch wieder
  - Wollen aber auch LLM-as-a-Judge wieder verwenden bei Adherence Score (Inhaltstreue)
  - Einfache Metriken decken nicht die Inhaltstreue zwischen Frage und Kontext, Kosinusähnlichkeit auch nicht
  - Werden Adherence Score verbessern (besseres Prompting, Analyse beider LLM-Judges anstatt Mean nehmen)
- Prompt-Optimierungen, da es wie in Al Faraby et al. [1] Anweisungsklarheit fordert (Chain-of-Thought-Prompting; bereits überarbeitet)
- Setzen bei Bhowmick et al. [8] an mit entkoppeltem Stamm, Key und Distraktoren Generieren bei MCQ
  - Literatur und auch wir hatten Probleme bei einschrittiger MCQ-Ausführung
- Wiederum suchen wir neue LLMs, da Literatur selten dies anwendet
- Setzen für Bewertungsrubrik wieder bei Mi and Li [9] an (Relevance, Clarity, ..., Cognitive Level)
  - Erweitern um Value + Language (von Prof. Cap) und unsere Correctness(/Manipulation Handling)
    - Correctness wegen humaner Inhaltstreue-Bestimmung; Value damals für Wertigkeit für Unterricht
    - Wollen aber Value an Learning Objectives knüpfen, Vorschlag von Charlott-HiWi
    - Language, da Clarity beschreibt, ob man die Frage versteht, nicht aber, ob Sprache überladen/komplex ist
  - Jede Frage kriegt Fragetyp und Bloom-Level (MCQ bis Lvl3, Open-Ended 1-6) --> bessere Kontrollierbarkeit
    - Maity et al. [5]/Scaria et al. [10] haben "Generiere Frage zu jedem Bloom Level" gemacht, vermeiden..
  - Bloom-Level-Kategorie erweitert, da wir Bloom-Alignment fokussieren (10 korrekt, 5 one-off, 0 sonst)
    - Mi and Li [9] haben kein Level vorgegeben, wurde resultierendes Level von 0-10 bepunktet (e.g. Analyze auf 7.0)
    - Alignment only jetzt (10 bei korrekt, 5 bei one-off, 0 sonst)
    - Keine Freiheitsgrade vergeben, sondern Bloom und QType vorgeben
- Rubriken oftmals rudimentär, keine ausführlichen Kriterienbeschreibungen
  - Mi and Li [9] bspw. "Relevance: Is the Question ... (0-10)"
  - Wir hatten es besser gemacht, muss in neuer Arbeit optimiert werden
    - Keine Zwischenwerte mehr zulassen, 1-5 Likert stattdessen
    - Bessere Beschreibungen, gute Ankerbeispiele, da zu uneindeutig
- Deswegen wichtig: Fleiss' Kappa für Rubrik unzureichend gewesen, nehmen ICC und Kendall's W (s. Mi and Li [9]) dazu

### Ansätze tabellarisch

| Quelle & Fokus | Forschungsziel & Adressierte Lücke | Methodische Umsetzung (Prompting & Architektur) | Wichtige Ergebnisse & Metriken |
|---|---|---|---|
| **1. Al Faraby et al. (2024)**<br/>Fokus: *Generierung und Halluzination* | **Ziel**: Analyse von ChatGPT zur Klassifikation und Generierung.<br/>**Lücke**: Mangel an standardisierten Bewertungsmethoden für Qualität und pädagogische Effektivität bei LLM-Fragen. | Modell: ChatGPT (GPT-3.5).<br/>**Methodik**: Zero-Shot vs. Few-Shot + Chain-of-Thought Prompting.<br/>**Inhaltstreue**: Einführung einer Source-Constrained Analysis, um Fakten außerhalb des Quelltextes als Halluzination zu entlarven. Kein Modell hat dabei geeignet abgeschnitten. | **Ergebnis**: Halluzinationen bleiben bei Generierung ein Hauptproblem, da Modelle externes Wissen beimischen, obwohl man sich an den Quelltext halten soll. Es braucht Validierungssysteme, um Kontextfernes zu vermeiden. |
| **2. An et al. (2025)**<br/>Fokus: *Learning Outcomes der Studenten* | **Ziel**: Empirische Lernerfolg-Studie durch generierte MCQs im Data Science Unterricht.<br/>**Lücke**: Fokus bisher oft nur auf der Generierung, nicht auf Lernerfolg der Studenten. | Modell: Gemini 2.0/2.5 Flash Models.<br/>**Methodik**: Integration von Fragen in Jupyter Notebooks. Strenge Human-in-the-Loop Validierung.<br/>**Prompting**: Explizite Anweisung für e.g. "Factual Recall" & "Higher-Order Thinking" als Fragebasis. | **Ergebnis**: Signifikante Lernverbesserung (89% vs. 73% in Kontrolllgruppe). Hohe Fehlerquote der Generierung (ca. 2/3 der Fragen mit Mängeln wie “keine Antwort ist richtig” oder Halluzinationen abseits des Lernkontexts). |
| **3. Doughty et al. (2024)**<br/>Fokus: *Python-basierte MCQs & LO Alignment* | **Ziel**: MCQs basierend auf spezifischen Learning Objectives (LOs) generieren.<br/>**Lücke**: Mangel an Evaluation von LLM-Systemen, welche Programmier-MCQs generieren. | Modell: GPT-4 als einziges.<br/>**Methodik**: 1. Klassifikation des Bloom-Levels für gegebenes LO 2. Mapping auf Fragetyp 3. Fragengenerierung.<br/>**Bloom**: Klassifikation des LO steuert Fragetyp. | **Ergebnis**: GPT-4 MCQs waren besser auf LOs ausgerichtet als menschliche Fragen. **Problem**: 4.9% der Fragen hatten mehrere korrekte Antworten. Man soll sich auch hier in Future Work auf Alignment zwischen Frage und Lernstoff beziehen. |
| **4. Kang et al. (2025)**<br/>Fokus: *Video Transkripte, viele LLMs im Vergleich via 4 Fragetypen* | **Ziel**: Vergleich von 10 LLMs für 4 Fragetypen aus Video-Transkript-Summaries.<br/>**Lücke**: Wenig Forschung zu Video-Content + fehlender Modellvergleich. | Modelle: GPT-4, Claude 3.5, Llama 3, etc.<br/>**Inhaltstreue**: Metrik "Context Utilisation" via GPT-4o misst, wie stark die Antwort im Transkript verankert ist.<br/>**Methodik**: 3 Iterationen pro Modell für alle Inhalte und Qtypes. | **Ergebnis**: Qwen und GPT-4 als Top-Performer. Llama gut in Context Utilisation. Wahr/Falsch-Fragen waren für alle Modelle am schwierigsten, da nötige Tiefe in Summaries verloren gingen. |
| **5. Maity et al. (2025)**<br/>Fokus: *Schul-Textbooks & 8-Shot-Learning Prompts zum Verbessern der Bloom-Verteilung über alle Fragen* | **Ziel**: Generierung einer vollständigen Fragemenge aus Schulbüchern.<br/>**Lücke**: Frameworks wie Bloom wurden selten vollends eingebunden. | Modelle: 5, darunter GPT-4 Turbo, Llama-3.1, Gemini Pro.<br/>**Methodik**: Vergleich 0-Shot vs. 8-Shot Learning (8 Beispiele im Prompt), Lehrer-basierte Evaluation (Kriterien & Bloom).<br/>**Bloom**: Explizite Anweisung, Fragen für alle 6 Levels gleichzeitig zu generieren. | **Ergebnis**: 8-Shot verbesserte Qualität und reduzierte Redundanz. GPT-4 Turbo und Llama-3 hielten die Bloom-Verteilung (pro Level 16.6%) am besten ein. 0-Shot führte zu ungleicher Verteilung. (Prompting war aber schwach, unabhängig von der 8-Shot-Umsetzung) |
| **6. Meissner et al. (2024)**<br/>Fokus: *Mathefragen & RAG als Wissensquelle* | **Ziel**: Kompetenzorientierte Mathe-Aufgaben für Hochschulen.<br/>**Lücke**: Fehlendes Domain-Wissen innerhalb der LLMs + Tendenz zur Halluzination. | Modelle: GPT-3.5 (Summary des Datenbank-Ergebnisses) + GPT-4 (Generierung aus Summary).<br/>**Inhaltstreue verbessern**: RAG mit Vektor-Datenbank aus Lehrbüchern;<br/>Promptbasis: Bloom's Taxonomy angewandt; Auswertung der Kategorien durch 3 Mathe-Experten (auch Bloom-Level). | **Ergebnis**: RAG eliminiert Halluzinationen fast vollständig, da der Kontext im Prompt fixiert ist. Aufgaben waren hochwertig, aber die Sample Solutions enthielten oft Rechenfehler – Trennung von Aufgabe und Lösungserstellung implizit in Future Work durch Integrieren von Computer Algebra Systemen. |
| **7. Zhuge et al. (2025)**<br/>Fokus: *Dual-LLM-Engine für Bloom-Alignment* | **Ziel**: Hochwertige Fragen mit kleinen Modellen (6B/13B Parameters) generieren.<br/>**Lücke**: Große Modelle teuer, und trotzdem halten sich diese nicht an kognitive Anforderungen. | **Architektur**: Dual-LLM Engine. 1. Generator erstellt Frage. 2. Evaluator prüft Bloom-Level & Relevanz. Haben Feedback-Loop zur Neugenerierung bei Level-Mismatch. | **Ergebnis**: Die 2 TwinStar Variationen schlugen e.g. GPT-4 in Bloom Adherence (+21%), und können bei Knowledge Relevance mithalten. Architektur (Evaluator-Loop) kann also wichtiger sein als Modellgröße. |
| **8. Bhowmick et al. (2023)**<br/>Fokus: *3-Step Pipeline für MCQ-Generierung (was auch der Hauptgrund für Erwähnung ist)* | **Ziel**: Skalierbares Framework für MCQs aus Bildungstexten.<br/>**Lücke**: Zeitaufwand mit manueller QGen hoch; Lehrer hatten zu diesem Zeitpunkt nahezu nie KI für QGen benutzt. | **Methodik**: Mehrstufige Pipeline: 1. Content Extraction 2. Qgen 3. Answer Prediction 4. Distractor Gen.<br/>Modelle: 3 pro Konfiguration, e.g. InstructGPT. | **Ergebnis**: Hybrider Ansatz lieferte 92% an MCQs mit geeigneter Qualität (Evaluation schwer nachvollziehbar). Benutzen aber für automatisierten Antwort-Abgleich vs. Dataset nur einfache **Metriken** wie ROUGE. |
| **9. Mi and Li (2024)**<br/>Fokus: *LLM-as-a-Judge vs. Human Rating; Paper ist Basis unserer Rubrik* | **Ziel**: Können LLMs menschliche Experten bei der Bewertung von Fragen ersetzen<br/>**Lücke**: Manuelle Evaluation von Fragen ist teuer und subjektiv. | **Methodik**: Vergleich von e.g. GPT-4 und ERNIE gegen Experten-Ratings.<br/>**Metriken**: Relevance, Clarity, Answerability, Challenging, Cognitive Level (Bloom); Kendall's W für Übereinstimmung. | **Ergebnis**: GPT-4 zeigte sehr hohe Übereinstimmung mit Experten (Kendall's W > 0.7), besonders bei Relevance und Clarity. Schwächer jedoch exakter Bestimmung des Bloom-Levels (W=0.084) – Damalige LLMs hatten Schwierigkeiten, kognitive Tiefe zu bestimmen |
| **10. Scaria et al. (2024)**<br/>Fokus: *Umfassende Rubrik mit Bloom verbunden, Bezug zu Social Science Questions* | **Ziel**: Fragen für indische High Schools in Sozialkunde auf allen Bloom-Levels.<br/>**Lücke**: Frage-Fokus oft nur in Richtung MINT; adressierten Herausforderung der Fragengenerierung ebenso auf hohen Bloom-Levels, welches Expertenbewertungen benötigt | Modelle: Open-Source Modelle wie Llama 2 vs. GPT-3.5/4.<br/>**Methodik**: Zero-Shot Prompting mit Context, Instructions und Angabe aller Bloom-Levels pro Prompting.<br/>**Evaluation**: 9-Item-Rubrik durch Experten. | **Ergebnis**: GPT-4 war am besten im Bloom Alignment. **Wichtig**: Open-Source-Modelle (e.g. Llama 2) scheiterten oft daran, passende Fragen für die Level Apply und Create zu generieren; Quadratic weighted Cohen’s Kappa benutzt |

### Literatur

1. Al Faraby et al. (2024): https://doi.org/10.1016/j.caeai.2024.100298  
2. An et al. (2025): https://doi.org/10.48550/arXiv.2507.05629  
3. Doughty et al. (2024): https://doi.org/10.1145/3636243.3636256  
4. Kang et al. (2025): https://doi.org/10.1109/TAI.2025.3620274  
5. Maity et al. (2025): https://doi.org/10.1016/j.caeai.2025.100370  
6. Meissner et al. (2024): https://doi.org/10.3389/feduc.2024.1427502  
7. Zhuge et al. (2025): https://doi.org/10.3390/app15063055  
8. Bhowmick et al. (2023): https://doi.org/10.1007/978-3-031-47994-6_38  
9. Mi and Li (2024): https://doi.org/10.1109/ICEIT61397.2024.10540914  
10. Scaria et al. (2024): https://aclanthology.org/2024.bea-1.1/