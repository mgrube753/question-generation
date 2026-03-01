# Workshop-Ergebnisse: Strukturierte Analyse

## Kritisches

### 1. Lernziele zu groß & nicht messbar

`e2/s1/note.md`, `e1/s1/note.md`

- Lernziele können nicht mit **einer einzelnen Frage** abgedeckt werden, da ich GROBziele statt Feinziele formuliert habe
- Lernziele enthalten ggf. mehrere Bloom-Level gleichzeitig (z.B. "anwenden" UND "zuordnen")
- **Lösung:** Lernziele müssen **spezifischer, messbarer und auf ein Bloom-Level fokussiert** sein

### 2. Bewertungsreihenfolge unklar

`e1/s1/note.md`, `e1/s2/note.md`

- Rater wussten nicht, dass Frage und Antwort **nacheinander** bewertet werden sollen --> Abhängigkeitsprobleme teils entstanden
- **Lösung:** Klare Anleitung... Erst Frage lesen → Frage bewerten → Dann Antwort lesen → Antwort bewerten... zudem Feedback-Email vor dem Sampling mit klaren Instruktionen

## Methodische Probleme

### 3. Bloom-Beschreibungen inkonsistent

`e2/s2/note.md`

- Krathwohl-Beschreibungen passen nicht zu Verben und Leveln
- Bloom-Levels bauen somit nicht linear aufeinander auf, sondern "verlaufen durcheinander"
- **Lösung:** Rubrik-Beschreibungen überarbeiten siehe Bloom 1956

### 4. "Challenging"-Kategorie problematisch

`e2/s2/note.md`

- Punkt-Vergabe 4 ("Erfordert Zusammenführen aus verschiedenen Textabschnitten") passt nicht
- Linearität zwischen Stufen 3 und 4 gebrochen
- Sollte heißen: "Erfordert Zusammenführen von **Wissen**"
- Man kann auch stattdessen nur Punkte 3 und 4 tauschen

### 5. "Value"-Kategorie prolematisch

`e1/s2/note.md`, `e2/s1/note.md`

- Rater bewerteten teils Value unterschiedlich (z.B. 2, 3, 5 für dieselbe Frage)
- Problem: Value bezieht sich auf **Lernziel**, aber diese selbst sind problematisch
- Nach Diskussion besseres Verständnis (innerhalb diverser Kategorien), aber initiale Bewertungen variierten ggf. stark
- Vor allem MCQ decken Lernziele oft zu oberflächlich ab
  - Man bräuchte für die jetzigen LOs mehrere aufbauende Fragen
  - Die Grobziele passen für eine einzelne Frage oft nicht

---

## Generierungsprobleme

### 6. "Frage: Frage" Output

`e2/s1/note.md`

- Entstand durch `Frage: {stem}` im Prompt-Template
- Häufig bei OpenAI und xAI, 1x bei DeepSeek
- **Fix:** Nur `{stem}` im Output Format angeben

### 7. Distraktoren bei MCQs inkonsistent

**Quelle:** `e2/s1/note.md`

- Richtige Antworten sind oft **kürzer** als falsche, statt andersherum / oder gleich
- Reihenfolge der Antwortmöglichkeiten nicht nach Layer-Logik sortiert (z.B. "2 3 5 4" statt "2 3 4 5")

### 8. Sprachliche Schwächen

`e2/s2/note.md`, `e1/s1/note.md`

- "Beziehungen" zwischen Schichten als schwacher Begriff
- Komplexe Sätze sollten in Teilsätze aufgebrochen werden
- Teilweise "Kauderwelsch" in Frageformulierungen, was analysiert werden muss

---

## Positives

### 9. Hohe Einigkeit

`e1/s2/note.md`

- **Relevanz, Klarheit, Beantwortbarkeit, Sprache, Korrektheit** mit hoher Übereinstimmung
- Beispiel Frage 1: 4/4 bei Relevance, 5/5 bei Clarity/Answerability/Language
- Beispiel Antwort 1: Alle geben 5/5 für Clarity, Language, Correctness

### 10. Workshop-Diskussionen für besseres Verständnis

`e1/s2/note.md`, `e2/s2/note.md`

- Nach den 1:1-Gesprächen gab es diverse Outcomes
- Nach den Gruppengesprächen ebenso
- Konnten durch Diskussionen die Bewertungen teilweise konvergieren
- e.g. Marvin verstand Value im Nachhinein besser → initiale 3 zu 5
- Workshops erfüllten Schulungszweck, sodass Rater das Setup danach besser verstanden haben
