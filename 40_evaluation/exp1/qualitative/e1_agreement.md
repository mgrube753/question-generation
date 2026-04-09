# Agreement/Reliability (Experiment 1)

- 3 Raters und 24 sampled Fragen
- Haben Fleiss' K, Kendall's W und ICC(3,1) ermittelt

---

## 1. Question-Based Criteria

### A. Teilweise herausragende Übereinstimmung

- **`q_answerability` (mean 3.31, std 1.67):**
  - _Daten:_ Sehr hohe Standardabweichung
  - _Reliabilität:_ Hoch, ICC (0.864) und Kendall's W (0.899) hochsignifikant (p=0.0000). Selbst Fleiss' K ist ausreichend hoch und signifikant (0.420, p=0.000).
  - Rater haben absolut einheitliches Verständnis darüber, ob Modelle die Lehrmaterialien korrekt genutzt haben, um _beantwortbare_ Fragen zu stellen.
- **`q_challenging` (mean 3.26, std 1.53):**
  - _Daten:_ Durchschnittliche Herausforderung mit guter Streuung
  - _Reliabilität:_ Auch hier hochsignifikante Einigkeit bei Kendall's W (0.810) und ICC (0.675)
  - Rater ordnen den Schwierigkeitsgrad der generierten Fragen sehr konsistent ein

### B. Schwierigkeit bei Value und Relevance

- **`q_relevance` (mean 4.18, std 1.06):**
  - _Daten:_ Fragen im Schnitt sehr relevant für den Stoff, gute Varianz.
  - _Reliabilität:_ Nicht signifikant (Kendall's W p=0.104, Fleiss p=0.628).
  - Obwohl LLMs thematisch gut vom Lehrmaterial gesteuert werden (hoher Mean), sind sich die Rater bei feinen Nuancen doch uneinig
- **`q_value` (mean 3.03, std 1.39):**
  - _Reliabilität:_ Keinerlei Signifikanz bei allen drei Metriken (p > 0.4). Rater bewerten unterschiedlich, wie gut Fragen zu Lernziel relevant sind. Das war in Exp2 besser.

### C. Agreement/Reliability vs. Sprache und Inhalt

- **`q_language` (mean 4.54, std 0.88):**
  - _Reliabilität:_ Ähnlich wie in Exp2. LLMs formulieren oftmals einwandfrei, aber Rater uneinig in Nuancen. Kendall's W knapp an Signifikanz vorbei (p=0.058), ICC ist recht signifikant (0.262, p=0.018).
- **`q_clarity` (mean 3.79, std 1.51):**
  - _Reliabilität:_ Höhere Varianz als bei Sprache, aber: Kendall's W (0.604) und ICC (0.326) sind hier hochsignifikant (p < 0.01) und nicht schlecht.
  - Inhaltliche Klarheit lässt sich etwas einheitlicher ranken, aber trotzdem geht das besser.

---

## 2. Answer-Based Criteria

- **`a_correctness` (mean 4.33, std 1.05):**
  - _Daten:_ Musterlösungen im Schnitt von hoher Richtigkeit, weisen aber einiges an Streuung (1.05) auf.
  - _Reliabilität:_ Kendall's W ist mit 0.511 hier recht **signifikant (siehe p=0.048)**.
  - Fleiss zwar nicht signifikant (p=0.151), aber Kendall zeigt, dass sich die Rater im relativen Ranking der Korrektheit recht einig sind.
  - Erkennen verlässlich, wenn die Modelle Antworten generieren, die fachlich problematisch sind.
  - Der recht hohe Mean (4.33) deutet darauf hin, dass Antworten grundsätzlich gut zu den generierten Fragen passen.
- **`a_clarity` (mean 4.28, std 1.26):**
  - _Reliabilität:_ Gute Streuung. Signifikante Ausgaben bei Kendall's W (0.594, p=0.011) und ICC (0.317, p=0.005). Die inhaltliche Verständlichkeit der Antworten wurde von den Ratern mittelmäßig einheitlich eingeschätzt.
- **`a_language` (mean 4.58, std 1.05):**
  - _Reliabilität:_ Ähnliches Ergebnis wie in `q_language`, sogar noch schlechtere Metrik-Ergenisse.
  - Fast perfekte Werte führen dazu, dass feine Unterschiede (z.B. eine 4 vs. 5 oder auch 3) zu Rauschen werden?
  - Keine der drei Metriken zudem signifikant (alle p > 0.3).
