# Qualitative Plots

## Question Type based

### Question based

- **`qTotal`**: Leichter Vorteil MCQ (Median 23, Mean 22.44) gegenüber Open-Ended (Median 22, Mean 21.78). Die Box von OE nach unten hin mehr Streuung, MCQ in Gesamtqualität konsistenter, mit wenigen Ausreißern nach unten.
- **Basic Metriken (`qLanguage` & `qClarity`)**:
  - Sprachlich (`qLanguage`) liefern beide Formate nahezu makellose Ergebnisse (Median überall bei 5, schmale Box).
  - Bei `qClarity` jedoch deutliche Diskrepanz: MCQs sind inhaltlich sehr präzise und klar formuliert (Median 5, Mean 4.22). Offene Fragen deutlich schwächer und streuen sehr (Median 4, Mean 3.36, breite Punkteverteilung)
- **`qRelevance` & `qValue`**:
  - Beide Formate hohe fachliche Relevanz zum Thema auf (`qRelevance` Median 4 MCQ, 5 bei OE, aber größere Punkteverteilung nach unten bei OE).
  - Bei `qValue` sind offene Fragen stärker (Median 4, Mean 3.5) als MCQs (Median 2.5, Mean 2.56, grundlegend tiefer angesiedelt).
- **`qAnswerability` & `qChallenging`**:
  - Bewertungen hier gegensätzlich: MCQs ließen sich gut durch das bereitgestellte Lehrmaterial beantworten (Median 5, Mean 4.58). Offene Fragen eher problematisch (Median 2, Mean 2.03) - Modelle versuchen sich vom Quelltext zu lösen.
  - Gleichzeitig offene Fragen wesentlich fordernder (`qChallenging` Median 5, Mean 4.25), während MCQs kognitiv sehr flach (Median 2).
- **FF1: Restriktion auf Frageformat definiert Steuerbarkeit fast vollständig. LLMs lassen sich bei Generierung von MCQs gut auf Skript beschränken, produzieren dabei aber wenig anspruchsvolle Fragen. Offene Fragen generieren hohen kognitiven Anspruch, zwingen das LLM aber dazu, das Lehrmaterial stark zu verlassen.**

### Answer based

- **`aTotal`**: Starker, eindeutiger Vorteil für MCQ. Qualität der Antwort(möglichkeiten) ist signifikant höher (Median 15, Mean 14.5) als Musterlösungen der offenen Fragen (Median 13, Mean 11.89).
- **`aLanguage` & `aClarity`**:
  - Sprache ist modellübergreifend gut (beide Median 5); Antworten der offenen Fragen jedoch breiter gefächert in Sprache
  - Klarheit der Musterlösungen bei OE schwächelt umso mehr (Mean sinkt auf 3.75 runter, große Box, große Whisker), während MCQ-Antworten inhaltlich klar sind (Mean 4.81).
- **`aCorrectness`**:
  - Auch hier sind MCQ-Antwortmöglichkeiten fachlich korrekt und passgenau (Median 5, Mean 4.78).
  - Bei OE-Fragen gibt es Probleme (Median 4, Mean 3.89, breite Box bis hin zu ungenügenden Scores).
- **FF3: Bei MCQs passen die generierten Antworten (Keys/Distraktoren) gut zur Frage und sind inhaltlich korrekt. Bei offenen Fragen sinkt die Zuverlässigkeit massiv; Modelle bauen gelegentlich sachliche Fehler oder unpassende Annahmen in Antworten ein.**

---

## LLM based

### Question based

- **`qTotal`**: xAI liegt vorn (Median 25, Mean 24.5), gefolgt von Anthropic (Median 22.5, Mean 22.33) und DeepSeek (Median 22, Mean 21.78). OpenAI mit größter Streuung, niedrigstem Median (21.5) und vor allem Mean (19.83) als letzter Platz
- **Basic Metriken (`qLanguage` & `qClarity`)**:
  - Sprachlich alle Modelle außer OpenAI ziemlich gut (Median 5 und Means > 4.5). OpenAI ist mit enormer Streuung, tiefem Mean (3.67) und Median (3.5) auffällig schwach hinsichtlich sprachlicher Präzision
  - Bei der inhaltlichen Klarheit ist xAI nahezu fehlerfrei (Median 5, Mean 4.61). Anthropic als einziges weiteres Modell mit Median 5, aber in Richtung DeepSeek und OpenAI (beide mit großer Streuung) deutlicher Abfall von Mean und Median (bis Mean und Median 3 bei OpenAI)
- **`qRelevance` & `qValue`**:
  - xAI Fragen sind stark relevant zum Kontext (Median 5, Mean 4.67), gefolgt von den etwas kritischen Verteilungen von DeepSeek und OpenAI. Trotz Median 4.5 bei beiden eher viele schwache Bewertungen. Anthropic ist mit Median 4 noch etwas schwächer anzusehen
  - Beim `qValue` hat xAI am besten abgeschnitten (Median 4, Mean 3.56). Alle Modelle weisen diverse Steuungen auf. Vor allem DeepSeek mit Median 2 zeigt Schwäche beim Fokussieren des Lernziels.
- **`qAnswerability` & `qChallenging`**:
  - Grundsätzlich viel Streuung in der Kategorie. Fragen von xAI am besten beantwortbar (Median 5), gefolgt von DeepSeek mit Median 4. DeepSeek und OpenAI fallen wie bei Clarity und Value auch tiefer aus.
  - xAI und DeepSeek in Challenging ähnlich schwach mit Median 3. DeepSeek und OpenAI hatten bei ihren Fragen hohe Anforderungen gestellt. Die Kategorie ist gegensätzlich zu Clarity, Answerability und Value, wenn man genau hinsieht.
- **FF1: LLM-basierter Trend bezüglich der Steuerbarkeit durch das Lehrmaterial. Bzgl. Relevanz zum Kontext ist xAI eindeutig vorn, bei Beantwortbarkeit ebenfalls. Obwohl Anthropic in Relevanz am geringsten ausfällt, ist das Modell in Beantwortbarkeit auf dem zweiten Platz statt DeepSeek. OpenAI weist auch in vielerlei Kategorien die größten Defizite auf. Es ist zu beachten, dass Answerability und Challenging relativ umgekehrt zueinander verlaufen. Somit sind Fragen von xAI und Anthropic gut beantwortbar, da sie weniger challenging sind.**

### Answer based

- **`aTotal`**: xAI und Anthropic führen an (Median 15 vs. 14.5). DeepSeek und OpenAI liegen dahinter, die Kategorien zeigen dies auch.)
- **`aLanguage` & `aClarity`**:
  - Alle Mediane liegen bei 5, haben aber neben diverser Ausreißer bei xAI und Anthropic etwas Streuung bei OpenAI (beide Kategorien) und bei Clarity auch DeepSeek mit hoher Streuung
- **`aCorrectness`**:
  - Auch hier Mediane alle 5. Fragen korrekt zu beantworten erscheint soweit pauschal möglich. xAI auch hier höchster Mean (4.56). Anthropic und DeepSeek streuen etwas und haben sogar Ausreißer bis 1/5 Punkten. Bei xAI ging es bis zu 2/5 runter. OpenAI ist wiederum am breitesten gefächert mit 4.11 Mean
- **FF3: Die Mediane zeigen gute inhaltliche Passung. Enger betrachtet haben aber die Modelle abseits von xAI eine geringere Verlässlichkeit, basierend auf dem Material geeignet zu antworten.**

---

## Bloom based

### Question based

- **`qTotal`**: Höhepunkt bei Bloom4 (Median 25, Mean 24.33). Bloom 1-3 etwas darunter angesiedelt, wobei Bloom3 breit gefächert ist. Bloom6 auch mit viel Streuung dabei, aber Bloom5 am niedrigsten mit Median 21 und Mean 19.89
- **Basic Metriken (`qLanguage` & `qClarity`)**:
  - `qLanguage` für alle Bloom Level außer 5 ziemlich gut (Mediane 5, Means >= 4.5). Bei Bloom5 starke Abweichung mit Median 4
  - `qClarity` anhand der Means alle 2 Bloom Levels am Sinken (Abwärtstrend). Von Bloom1 (Mean 4.39) bis Bloom6 (Mean 3.11). Schrittweise also inhaltliche Klarheit der Fragen abnehmend.
- **`qRelevance` & `qValue`**:
  - Bei Relevanz neben Bloom4 (Median und Mean 5) ist Bloom6 zweitbestes Level (Median 5, Mean 4.56), die anderen Level streuen (vor allem 3 und 5), und Means tendieren zu 4 und darunter.
  - Beim `qValue` hat Bloom4 am besten abgeschnitten (Median 5, Mean 4.67). Bloom6 folgt darauf mit Median 5, Mean 3.78 und enormer Streuung. Bloom 1,3 und 5 streuen auch und sind nahe 3 angesiedelt. Bloom2 neben Ausreißern auch bei 3 angelegt.
- **`qAnswerability` & `qChallenging`**:
  - Beantwortbarkeit: Wie bei Clarity hier noch stärker zu sehen: linearer Abfall bei aufsteigendem Bloom Level. Level1 und 2 sind gut beantwortbar (Median 5), vor allem > Bloome (Median 4) läuft man auf Median 2 und 1 zu.
  - `qChallenging` genau umgekehrter Verlauf zu Beantwortbarkeit, von Bloom1 (Median 1.5) bis Bloom6 (Median 5) ist recht sauberer Verlauf zu erkennen.
- **FF1: Steuerung über Material funktioniert auch bei hohen Bloom Levels. Jedoch läuft man bei Levels 4-6 (hohe Relevanz) die Gefahr, Fragen zu generieren, die nahezu nicht durch Material beantwortbar sind, da diese sehr herausfordernd sind.**

### Answer based

- **`aTotal`**: Einfache Bloom Levels (1 und 2) erreichen insgesamt Median 15. Danach folgt deutlicher linear wirkender Abfall, bis hin zu Bloom6 mit Median 10
- **`aLanguage` & `aClarity`**: Sprache in ersten 3 Levels recht stabil für Antworten (alle 6 Levels zudem Median 5). Bloom Level 4 auch mit Mean 4.67 gut im Rennen, aber Bloom5 und 6 bringen grundlegenden Linear-Trend zum Vorschein. Bloom6 mit großer Streuung und Mean bei 4
  - Klarheit der Antworten im Grunde auch neben Bloom5 als Abwärtstrend zu sehen. Bloom1-3 und 5 mit Median 5 versehen, aber Means neben Bloom5 immer weiter am Fallen bis Bloom6 mit Mean 2.89. Inhaltlich wird mit steigendem Bloom Level die linguistische und inhatliche Qualität der Antworten schlechter.
- **`aCorrectness`**:
  - Bloom2 mit Median und Mean 5 am besten. Bloom1 durch einen Ausreißer auf Mean 4.94 gerutscht. Bloom3 bis 6 haben deutliche Schwächen und halen sich mit Mean um 4 herum. Streuung nach unten bei allen 4 Leveln zu sehen.
- **FF3: Niedrige Levels halten sich besser an das Material, während hohe Levels viel mehr Kontext erfordern, den der gegebene Text nicht bereitstellt.**
