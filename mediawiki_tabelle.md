```mediawiki
{| class="wikitable sortable"
|+ Übersicht der Forschungsarbeiten zur LLM-gestützten Fragengenerierung
! Quelle & Fokus
! Forschungsziel & Adressierte Lücke
! Methodische Umsetzung (Prompting & Architektur)
! Wichtige Ergebnisse & Metriken
|-
| '''1. Al Faraby et al. (2024)'''
Fokus: ''Generierung und Halluzination''
| '''Ziel''': Analyse von ChatGPT zur Klassifikation und Generierung.
'''Lücke''': Mangel an standardisierten Bewertungsmethoden für Qualität und pädagogische Effektivität bei LLM-Fragen.
| Modell: ChatGPT (GPT-3.5).
'''Methodik''': Zero-Shot vs. Few-Shot + Chain-of-Thought Prompting.
'''Inhaltstreue''': Einführung einer Source-Constrained Analysis, um Fakten außerhalb des Quelltextes als Halluzination zu entlarven.
| '''Ergebnis''': Halluzinationen bleiben bei Generierung ein Hauptproblem, da Modelle externes Wissen beimischen, obwohl man sich an den Quelltext halten soll. Es braucht Validierungssysteme, um Kontextfernes zu vermeiden.
|-
| '''2. An et al. (2025)'''
Fokus: ''Learning Outcomes der Studenten''
| '''Ziel''': Empirische Lernerfolg-Studie durch generierte MCQs in Data Science.
'''Lücke''': Fokus bisher oft nur auf der Generierung, nicht auf Lernerfolg der Studenten.
| Modell: Gemini 2.0/2.5 Flash Models.
'''Methodik''': Integration in Jupyter Notebooks. Strenge Human-in-the-Loop Validierung.
'''Prompting''': Explizite Anweisung für "Factual Recall" bzw. "Higher-Order Thinking".
| '''Ergebnis''': Signifikante Lernverbesserung (89% vs. 73%). Hohe Fehlerquote der Generierung (ca. 2/3 der Fragen hatten Mängel wie “keine Antwort ist richtig” oder Halluzinationen abseits des Lernkontexts).
|-
| '''3. Doughty et al. (2024)'''
Fokus: ''Python-basierte MCQs & LO Alignment''
| '''Ziel''': MCQs basierend auf spezifischen Learning Objectives (LOs) generieren.
'''Lücke''': Mangel an Evaluation von LLM-Systemen, welche Programmier-MCQs generieren.
| Modell: GPT-4 als einziges.
'''Methodik''': 1. Klassifikation des Bloom-Levels für gegebenes LO 2. Mapping auf Fragetyp 3. Fragengenerierung.
'''Bloom''': Klassifikation des LO steuert Fragetyp.
| '''Ergebnis''': GPT-4 MCQs waren besser auf LOs ausgerichtet als menschliche Fragen. '''Problem''': 4.9% der Fragen hatten mehrere korrekte Antworten. Man soll sich auch hier in Future Work auf Alignment zwischen Frage und Lernstoff beziehen.
|-
| '''4. Kang et al. (2025)'''
Fokus: ''Video Transkripte, viele LLMs im Vergleich via 4 Fragetypen''
| '''Ziel''': Vergleich von 10 LLMs für 4 Fragetypen aus Video-Transkript-Summaries.
'''Lücke''': Wenig Forschung zu Video-Content + fehlender Modellvergleich.
| Modelle: GPT-4, Claude 3.5, Llama 3, etc.
'''Inhaltstreue''': Metrik "Context Utilisation" misst, wie stark die Antwort im Transkript verankert ist.
'''Methodik''': 3 Iterationen pro Modell.
| '''Ergebnis''': Qwen und GPT-4 als Top-Performer. Llama gut in Context Utilisation. Wahr/Falsch-Fragen waren für alle Modelle am schwierigsten, da nötige Tiefe in Summaries verloren gingen.
|-
| '''5. Maity et al. (2025)'''
Fokus: ''Schul-Textbooks & 8-Shot-Learning Prompts zum Verbessern der Bloom-Verteilung über alle Fragen''
| '''Ziel''': Generierung einer vollständigen Fragemenge aus Schulbüchern.
'''Lücke''': Frameworks wie Bloom wurden selten vollends eingebunden.
| Modelle: GPT-4 Turbo, Llama-3, Gemini Pro.
'''Methodik''': Vergleich 0-Shot vs. 8-Shot Learning (8 Beispiele im Prompt).
'''Bloom''': Explizite Anweisung, Fragen für alle 6 Levels gleichzeitig zu generieren.
| '''Ergebnis''': 8-Shot verbesserte Qualität und reduzierte Redundanz. GPT-4 Turbo und Llama-3 hielten die Bloom-Verteilung (pro Level 16.6%) am besten ein. 0-Shot führte zu ungleicher Verteilung.
|-
| '''6. Meissner et al. (2024)'''
Fokus: ''Mathefragen & RAG als Wissensquelle''
| '''Ziel''': Kompetenzorientierte Mathe-Aufgaben für Hochschulen.
'''Lücke''': Fehlendes Domain-Wissen innerhalb der LLMs + Tendenz zur Halluzination.
| Modelle: GPT-3.5 (Extraktion) + GPT-4 (Generierung).
'''Inhaltstreue''': RAG mit Vektor-Datenbank aus Lehrbüchern Promptbasis.
'''Bloom''': Taxonomie angewandt.
| '''Ergebnis''': RAG eliminiert Halluzinationen fast vollständig, da der Kontext im Prompt fixiert ist. Aufgaben waren hochwertig, aber die Sample Solutions enthielten oft Rechenfehler – Trennung von Aufgabe und Lösungserstellung implizit in Future Work durch Integrieren von Computer Algebra Systemen.
|-
| '''7. Zhuge et al. (2025)'''
Fokus: ''Dual-LLM-Engine für Bloom-Alignment''
| '''Ziel''': Hochwertige Fragen mit kleinen Modellen (6B/13B Parameters) generieren.
'''Lücke''': Große Modelle teuer, und trotzdem halten sich diese nicht an kognitive Anforderungen.
| '''Architektur''': Dual-LLM Engine. 1. Generator erstellt Frage. 2. Evaluator prüft Bloom-Level & Relevanz. Haben Feedback-Loop zur Neugenerierung bei Level-Mismatch.
| '''Ergebnis''': Die 2 TwinStar Variationen schlugen e.g. GPT-4 in Bloom Adherence (+21%), und können bei Knowledge Relevance mithalten. Architektur (Evaluator-Loop) kann also wichtiger sein als Modellgröße.
|-
| '''8. Bhowmick et al. (2023)'''
Fokus: ''3-Step Pipeline für MCQ-Generierung (was auch der Hauptgrund für Erwähnung ist)''
| '''Ziel''': Skalierbares Framework für MCQs aus Bildungstexten.
'''Lücke''': Zeitaufwand mit manueller QGen hoch; Lehrer hatten zu diesem Zeitpunkt nahezu nie KI für QGen benutzt.
| '''Methodik''': Mehrstufige Pipeline: 1. Content Extraction 2. Qgen 3. Answer Prediction 4. Distractor Gen.
Modelle: 3 pro Konfiguration, e.g. InstructGPT.
| '''Ergebnis''': Hybrider Ansatz lieferte 92% an MCQs mit geeigneter Qualität (Evaluation schwer nachvollziehbar). Benutzen aber für automatisierten Antwort-Abgleich vs. Dataset nur einfache '''Metriken''' wie ROUGE.
|-
| '''9. Mi and Li (2024)'''
Fokus: ''LLM-as-a-Judge vs. Human Rating; Paper ist Basis unserer Rubrik''
| '''Ziel''': Können LLMs menschliche Experten bei der Bewertung von Fragen ersetzen
'''Lücke''': Manuelle Evaluation von Fragen ist teuer und subjektiv.
| '''Methodik''': Vergleich von GPT-4, SparkDesk, ERNIE gegen Experten-Ratings.
'''Metriken''': Relevance, Clarity, Answerability, Cognitive Level (Bloom); Kendall's W für Übereinstimmung.
| '''Ergebnis''': GPT-4 zeigte sehr hohe Übereinstimmung mit Experten (Kendall's W > 0.7), besonders bei Relevance und Clarity. Schwächer jedoch exakter Bestimmung des Bloom-Levels (W=0.084) – Damalige LLMs hatten Schwierigkeiten, kognitive Tiefe zu bestimmen
|-
| '''10. Scaria et al. (2024)'''
Fokus: ''Umfassende Rubrik mit Bloom verbunden, Bezug zu Social Science Questions''
| '''Ziel''': Fragen für indische High Schools in Sozialkunde auf allen Bloom-Levels.
'''Lücke''': Frage-Fokus oft nur in Richtung MINT; adressierten Herausforderung der Fragengenerierung ebenso auf hohen Bloom-Levels, welches Expertenbewertungen benötigt
| Modelle: Open-Source Modelle wie Llama 2 vs. GPT-3.5/4.
'''Methodik''': Zero-Shot Prompting mit expliziten Bloom-Definitionen.
'''Evaluation''': 9-Item-Rubrik durch Experten.
| '''Ergebnis''': GPT-4 war am besten im Bloom Alignment. '''Wichtig''': Open-Source-Modelle (e.g. Llama 2) scheiterten oft daran, passende Fragen für die Level Apply und Create zu generieren; Quadratic weighted Cohen’s Kappa benutzt
|}
```
