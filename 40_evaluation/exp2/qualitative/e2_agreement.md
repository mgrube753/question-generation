# Agreement/Reliability (Experiment 2)

- 3 Raters und 24 sampled Fragen
- haben Fleiss' k, Kendall's W und ICC(3,1) ermittelt

---

## 1. Question-Based Criteria

### A. Die komplexen pädagogischen Konstrukte

- **`q_bloom_rating` (mean 2.51, std 1.75):**
  - _Daten:_ sehr hohe Standardabweichung (1.75) zeigt, dass das LLM Fragen über das gesamte Bloom-Spektrum (1 bis 6) verstreut hat.
  - _Reliabilität:_ ICC = 0.849 und Kendall's W = 0.883. Beide Werte sind hochsignifikant (p = 0.000).
  - Experten hatten grundlegend einheitliches Verständnis der kognitiven Level.
- **`q_challenging` (mean 2.92, std 1.38):**
  - _Daten:_ durchschnittliches Level im Mittelfeld, mit guter Streuung.
  - _Reliabilität:_ Kendall's W mit 0.856 sehr hoch. ICC liegt bei guten 0.727.
  - Auch wenn exakte Punktzahl mal abweichend war (Fleiss nur bei 0.181), waren sich die Rater extrem einig in der relativen _Rangordnung_ der Fragen: welche Fragen aus Studierendenperspektive schwerer waren als andere.

### B. Value im Mittelfeld

- **`q_value` (mean 4.21, std 0.93):**
  - _Daten:_ Fragen gingen grundlegend gut auf Lernziel ein, aber gibt Ausreißer nach unten (Std auch fast bei 1.0).
  - _Reliabilität:_ ICC mit 0.517 im moderaten Bereich. Kendall's W zeigt auch mit 0.748, dass Rater die Kategorie im Vergleich gut einschätzen konnten.

### C. Kappa vs. Sprache und Inhalt

- **`q_clarity` (mean 4.75, std 0.60) & `q_language` (mittelwert 4.51, std 0.73):**
  - _Problem:_ p-Werte für Fleiss und Kendall hier **nicht signifikant** (p > 0.05). Bei `q_clarity` sogar alle drei Metriken nicht signifikant.
  - _Grund:_ "Ceiling Effect", da viele Fragen am Maximum liegen?

---

## 2. Answer-Based Criteria

- **`a_bloom_rating` (mean 2.35, std 1.62):**
  - _Vergleich zu Frage:_ ICC (0.647) und Fleiss (0.241) sind hier signifikant und gut, aber teils bedeutend niedriger als bei den Fragen (ICC 0.849).
- **`a_language` (mean 4.61, std 0.77) & `a_clarity` (mean 4.40, std 0.97):**
  - _Kontrast:_ Ggü. den Fragen sind die Metrik-Werte bei Antworten höher. Anders als bei Fragen sind hier fast alle p-Werte signifikant (außer Fleiss bei `a_clarity` mit p=0.707). ICC für `a_clarity` liegt bei 0.41, für `a_language` bei 0.383. Für beide Kategorien ist Kendall's W 0.539 vs. 0.662. Fleiss' K mit 0.031 vs. 0.276.
- Besseres gemeinsames Verständnis für Sprache und Klarheit hierbei ggü. den Fragen
