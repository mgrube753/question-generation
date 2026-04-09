# Qualitative Plots

## Question Type based

### Question based

- Open-Ended in `qTotal` sichtbar besser ggü. MCQ (Median 18 MCQ, 22 bei OE)
  - Hauptgründe: `qChallenging` und `qValue`. Offene Fragen bedeutend herausfordernder und verfolgen besser das angestrebte Groblernziel
  - Bei `qChallenging` und `qValue` fällt vor allem `qChallenging` gering für MCQ aus
- Basic Metriken wie `qLanguage` und vor allem `qClarity` fallen hoch aus mit Median überall bei 5
  - Gewisse Tiefgänger bei `qLanguage` und diverse Ausreißer bei `qClarity` sichtbar
  - Grundlegend keine Probleme, inhaltlich verständlich und sprachlich präzise zu formulieren, wobei `qLanguage` etwas breiter gefächert ist als `qClarity`
- `qBloomAlignment` (bzgl. vorgegebenem Bloom) ist Problemzone; Median höher bei Open-Ended (4 bei OE, 3 bei MCQ), aber mean knapp tiefer (3.44 bei MCQ, 3.39 bei OE)
  - Open-Ended verläuft über gesamtes Spektrum (sehr hohe Varianz, unteres Quartil bis 1)
  - MCQ grundlegend im höheren Bereich angesiedelt (Box von 3 (Median) bis 5 Punkte), hat aber auch eine recht hohe Varianz
  - Gibt auch Tiefgänger in MCQ, sieht etwas vielversprechender aus als bei OE.
  - Modelle treffen fragetypunabhängig verhältnismäßig oft nicht das geforderte kognitive Level. Bei MCQ meist um ein Level daneben geschätzt, und bei offenen Fragen zu einem beträchtlichen Teil deutlich daneben geschätzt
- **FF2: Restriktion auf Frageformat hat starken Einfluss auf Zuverlässigkeit, ein bestimmtes Bloom Level zu treffen. MCQs verfolgen bestimmte Nähe zum vorgegebenen Bloom Level (meist one-off), während offene Fragen deutlich fehleranfälliger sind.**
  - Auch bei starkem Verfehlen des Levels bei offenen Fragen sind diese passender zum Groblernziel als MCQs (`qValue` Median 5 vs. 4 bei MCQ), und wesentlich fordernder (`qChallenging` Median 4 vs. 2 bei MCQ).

### Answer based

- Leichter Vorteil für MCQ. Musterlösungen / Anwortmöglichkeiten für MCQs im Mittel und Median leicht besser als bei Open-Ended (Mean MCQ 13.72, Median 15; Mean OE 13.03, Median 14)
- `aBloomAlignment` bei Antworten (bzgl. Frage-Bloom) bedeutend stabiler und höher als bei den Fragen
  - Bei MCQ sehr gut an das Bloom der Frage angepasst mit wenig Varianz (Median 5), nahezu deckungsgleich
    - LLM-basierte MCQ bringen in den Musterlösungen fast immer exakt den kognitiven Anspruch der Frage zum Ausdruck, so gibt es hier keine kognitive Dissonanz zwischen Frage und Lösung (Mean 4.61, Median 5)
  - Offene Fragen streuen stark (trotz Median 5), Box 5-3, Whisker bis 1 runter, Mittelwert (4.11) spürbar nach unten gezogen
    - Gibt bei LLMs für offene Fragen oft kognitive Lücke zwischen Frage und Antwort
- `aLanguage` (MCQ Mean 4.69, OE Mean 4.53) und `aClarity` (MCQ Mean 4.42, OE Mean 4.39) in Fragen grundsätzlich gut, Klarheit bei Antwort aber schlechter als bei Fragen (MCQ Mean war 4.81, und OE 4.69)
  - Verhalten sich ähnlich bei `aClarity` für MCQ und Open-Ended
  - Sprache bei MCQ besser im Grunde, aber auch Ausreißer bei beiden, Open-Ended etwas breiter gefächert
- **FF3: Bloom-technisch passen MCQ sehr oft zum ermittelten Bloom Level der Frage, was bei offenen Fragen deutlich weniger der Fall ist. Dort werden Musterlösungen generiert, die oft fern vom Frage-Bloom-Level liegen, wobei man dem kognitiven Anspruch der Frage nicht gerecht wird.**

## LLM based

### Question based

- Deepseek gefolgt von xAI als leichter Gesamtsieger
- `qClarity` und `qLanguage` bei allen 4 LLMs grundlegend geeignet
  - Deepseek und xAI besonders konsistent
  - Openai leicht größere Varianz und tieferer Median (4.5 statt 5) als bei den anderen dreien für `qLanguage`, `qClarity` inhaltlich auch etwas weniger gut verständlich bei Openai (alle aber median 5)
  - Ausreißer bei allen LLMs gegeben
- `qValue` recht homogen über alle Modelle hinweg, nur Openai etwas schwächer im Median 4 statt 4.5
  - Fokus auf Lernziel weitgehend gegeben für alle Modelle, mit nur wenigen Ausreißern/Tiefgängern
- `qChallenging`: Anthropic und Deepseek weitgehend vergleichbar, mit Median 3 als mittelfeld
  - xAI Fragen am herausforderndsten mit gleichem Boxlayout wie die anderen beiden, aber höherer Median 3.5
  - Openai mit Median 2 deutlich flachere Fragen generiert
- `qBloomAlignment`: Openai hierbei der stärkste Performer (zuverlässigstes Modell trotz wenig `qChallenging`, also trotzdem sehr gehorsam) mit Median 4 und gleicher Form wie Deepseek, aber Openai etwas höherer mean
  - Anthropic und xAI haben große Probleme, das angestrebte Bloom Level zu treffen, beide Median 3, große Boxen/Varianz, dadurch sehr unzuverlässig, mit Anthropic als schwächstem
- **FF2: Bloom Alignment ist auch LLM-abhängig. Openai ist hierbei das steuerbarste Modell, liefert dadurch aber Fragen, die wenig Herausfordernd sind. Im Umkehrschluss liefert z.B. xAI anspruchsvolle Fragen, die aber ferner vom geforderten Bloom Level sind.**

### Answer based

- Deepseek dominiert in den Antwortkategorien mit höchstem Mean sowie Median5 überall, gefolgt von xAI. Anthropic und Openai fallen deutlich mit inkonsistenten Antworten ab
- Auch hier starker Qualitätsunterschied bei `aClarity` und `aLanguage`:
  - xAI und vor allem Deepseek sehr inhaltlich klar und sprachlich präzise in der Generierung, beide Boxen beinahe vollständig auf Median 5 komprimiert
  - Anthropic und Openai zeigen hier wieder Schwächen
    - Anthropic und vor allem Openai haben mit Streuung zu kämpfen (stark bei `aClarity` zu sehen)
    - Oft etwas umständliche Antworten formuliert und inhaltlich eher schwer nachvollziehbar
- `aBloomAlignment`: xAI, Openai und vor allem Deepseek agieren alle gleich gut, mit kleiner Ausreißeranzahl, Deepseek mit mean >4.5
  - Sie generieren Lösungen, die sehr häufig auf demselben kognitiven Level liegen
  - Anthropic deutlich schwächer, median bei 5, aber Box bis 3 und Whisker bis 1, für pädagogische Zwecke bzgl. Bloom eher unzuverlässig für Musterlösungen
- **FF3: Der Großteil der Modelle schafft es zuverlässig, das von den Ratern abgegebene kognitive Level zur Frage auch in der Musterlösung zu erbringen. Nur Anthropic scheitert dabei, wodurch es viele Fragen gab, die fern vom geforderten Level generiert wurden.**

## Bloom based

### Question based

- In `qTotal` ein interessantes Bild in Sinusform
  - Bloom1 solide mit Median20
  - B2 (18) und B3 (18) fallen ab, B3 hat größte Punktrange
  - B4 (21) bringt gutes Scoring trotz schlechtem `qBloomAlignment` mit sich
  - Bloom6 (Median 21.5, mit großer Box-Varianz) und vor allem Bloom5 mit stärksten scorings (23)
- `qClarity` im Grunde sehr hoch mit Median überall bei 5, mit zunehmendem Bloom Level wird es grundlegend schrittweise tiefer im Mean (nur bei Bloom4 etwas anders), wenige ausreißer ab Bloom2 zu sehen
  - Von Bloom1 mit Mean5 auf Bloom6 mit Mean 4.42
- `qChallenging` verfolgt linearen Verlauf mit Ziel-Bloom Level
  - Je höher gefordertes Level, umso höhere Bewertungen für kognitive Anstrengung bis hin zu Median 4.5, im Kontrast zu Bloom1 mit Median von 1
- `qValue`: Lernziel-Orientierung steigt mit höherem Bloom Level grundlegend auch an; Bloom 4/5 nicht ganz im linearen Verlauf
  - Höhere Bloom Levels orientieren sich stärker am Groblernziel im Gegensatz zu reinen Wissensfragen wie Bloom1
- `qLanguage`: Neben Bloom4 und Bloom6 (Median 5) sonst grundsätzlich der Trend, dass hohe Bloom-Levels die sprachliche Präzision beeinträchtigen
  - Bloom6 und vor allem 3 und 5 (beide mit Median 4) weisen Sprachprobleme auf
- `qBloomAlignment`: Extreme (B1 und B5) weitestgehend zuverlässig getroffen; Bloom6 ebenso mit Median5 getroffen, aber mit extremer Varianz über komplettes Spektrum hinweg
  - Mittlere Levels 2,3,4 problematisch: Tendenz zu one-off (Bloom2) oder noch schwächer bei Bloom3 und 4, sowie hohe Punkteverteilung bei B3 und B4
- **FF2: Steuerbarkeit hängt neben LLM und Frageformat auch vom geforderten Level ab. Mittlere Bloom Levels sind problematisch, korrekt angegangen zu werden, und werden häufig (2, vor allem 3 und 4) verfehlt. Fragen, die auf Bloom Level 6 sein sollten, erstrecken sich über das gesamte Spektrum.**

### Answer based

- Leicht treppenartiger Abfall bei komplexeren Bloom Levels, was bei den Kategorien recht klar zu sehen ist
- `aClarity`: einfache Bloom Levels 1 und 2 mit wenigen Ausreißern sonst sehr oft mit 5 bewertet (siehe Median 5 und Means 4.6 / 4.67)
  - Bloom3 bedeutend schwächer (Mean 4.28), Bloom4 auch etwas Varianz vorhanden (mit Mean 4.67), trotzdem grundlegend inhaltlich sehr klar
  - Bloom5 sieht ggü. Bloom3 etwas verlässlicher aus (mit Mean 4.56), Bloom6 jedoch schwach mit tiefem Median von 4 (und Mean 3.83), breiter Box und Whisker bis 2 runter
- `aLanguage`: Grundlegender Abwärtstrend mit höherem Bloom Level sichtbar, bei dem vor allem Bloom5 und 6 große Varianz haben (Bloom6 nur Mean 4.17)
  - Bloom1 ist etwas schwächer als B2, B3 und B4...
  - Mit steigendem Bloom Level, vor allem 5 und 6, ist sonst Antwort sprachlich sehr schwerfällig und komplex formuliert
- Der rote Faden geht verloren in Antworten von Bloom5 und 6, welche die höchsten kognitiven Level sind; LLMs kommen an ihre strukturellen und sprachlichen grenzen
- `aBloomAlignment`: Bloom1 bis 5 kriegen es nahezu immer hin, dem bewerteten Level der Frage gerecht zu werden
  - Gewisse Ausreißer nach unten sichtbar; Bloom4 etwas schwächer
  - Bei Bloom6 scheitern die Modelle, eine Antwort für das Fragelevel zu formulieren mit Mean und Median bei 3 und vollem Bewertungsspektrum
- **FF3: Man findet geringfügige kognitive Dissonanz zwischen Frage und Antwort, die bei Bloom level 6 maßgeblich stark ausgeprägt ist. Bis Evaluating passen die Antworten oft zum Frage-Bloom Level, Bloom Level 4 ist etwas tiefer im Alignment als Levels 1,2,3 und 5.**

## Bloom Confusion Matrices

### Question based

- Wie gut setzen die LLMs den Prompt um (Target Bloom vs. Actual Question Bloom Level)?
- Extreme wie B1-86.7% und B5-77.8% funktionieren gut, haben ausreichend große Trefferquote
- Bloom6 mit 58.3% noch okay, gelegentlich auf B4 oder B3 geschätzt
- Mittlere Bloom Levels 2-4 schwach im Alignment
  - viel one-off, aber auch viele Verfehlungen
  - Meistens erreichen die LLMs geringere Bloom Levels als vorgesehen
    - Bloom2: 83.3% der Fälle stattdessen Bloom1 Wissensfragen statt Verständnis
    - Bloom3: 11.1% Trefferquote; Großteil auf Bloom2 38.9% oder Bloom1 44.4% geschätzt
    - Bloom4: aus 6 Fragen sind 2 Treffer, 1 Bloom3, 3 Bloom2
- **FF2: Probleme, ein bestimmtes Bloom Level zu treffen, ist mehr abhängig vom Level als vom Zufall. Man fällt bei höheren Anforderungen (Bloom3,4) oft auf einfachere Bloom Levels in Fragen zurück. Die meisten Bloom2 Fragen fallen auf Bloom1**

### Answer based

- Wenn Frage ein bestimmtes Level hat (unabhängig vom geforderten), auf welchem Level beantwortet das Modell dann diese Frage?
- Bloom1-5 zeigen starke Diagonale zwischen 50% (Bloom3,4) und 85+% (Bloom1,2,5)
  - Ohne Kenntnis des Bloom Levels der Frage wird Antwort zumeist dem gerecht
- Musterlösungen für als Bloom6 bewertete Fragen zeigen Streuung wie die Boxplots
  - Musterlösung in 42.9% der Fälle (3/7) auf Bloom6
  - 1/7 bei Bloom5, 1 bei Bloom3 und 2 bei Bloom2
- **FF3: Kognitive Dissonanz hier wieder für Bloom6 ersichtlich, sonst geringfüge Abweichungen. Die Abweichungen sind sonst stärker vertreten bei Bloom3 und 4, da dort wenig zugewiesene Fragen zu beantworten waren. Folgert eine 50:50 Chance beider Level zu verfehlen.**
