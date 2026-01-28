# Überblick des Experiments 2 -- Ausführung durch Malte Grube

Dieses Experiment testet die Fähigkeit von vier Large Language Models (LLMs), Fragen in verschiedenen Formaten (Multiple-Choice, Open-Ended) und auf unterschiedlichen kognitiven Niveaus nach Bloom's revised Taxonomy systematisch zu generieren. Das Thema ist das ISO-OSI-Modell, ein wichtiges Referenzmodell aus der Informatik. Details zum Prompting werden aufgrund des Blindtests nicht gegeben.

## Experimentaufbau

**Eingabequelle:** Extrahierte Textauszüge aller 7 OSI-Layer als ein zusammengefügter Text, basierend auf einer Vorlesungs-PDF meines Professors.

**Material-Aufbereitung:**

- Zusammenfügen der Informationen aller 7 Layer zu einem Text, welcher in das vorliegende .docx Dokument integriert wurde

**Generierte Fragen:**

In jede Frage wurde ein bestimmtes Lernziel integriert (1/6), angeknüpft an das jeweilige Bloom-Level. Das Einhalten des Lernziels soll mit der **Wertigkeit**-Kategorie in der Rubrik bewertet werden.

- 4 LLMs × 12 Fragen = 48 Fragen gesamt
- Pro LLM: 6 MCQ (Bloom 1-3, je 2 Fragen) + 6 Open-Ended (Bloom 1-6, je 1 Frage)
- Sample für Bewertung: 24 Fragen (6 pro LLM: 3 MCQ + 3 Open-Ended)

## Anleitung für Studierende

### Schritt 1: Bewertungskriterien verstehen

Lesen Sie die im .docx enthaltene Rubrik durch, die folgende Kategorien umfasst (jeweils 1-5 Punkte):

- **Relevanz:** Bezug zum ISO-OSI-Modell
- **Klarheit:** Eindeutigkeit der Formulierung
- **Beantwortbarkeit:** Verfügbarkeit der Informationen im Text
- **Herausforderung:** Anspruchsniveau der Frage
- **Wertigkeit:** Bedeutung für vorgegebenes Lernziel
- **Sprachqualität:** Verständlichkeit und Angemessenheit

Sowie die folgende Kategorie:

**Bloom-Level-Bewertung (Punktevergabe 1-6):**
Welches kognitive Level wird in dieser Frage erreicht? Nutzen Sie die Beschreibungen und Verben in der Rubrik zur Bestimmung des Levels.

### Schritt 2: Tabellen-Struktur verstehen

Jede Klein-Tabelle zu der jeweiligen Frage enthält:

- Die 6 Bewertungsspalten aus Schritt 1 (1-5 Punkte), sowie
- `bloom_rating`: Ihr bewertetes Bloom-Level (Level 1-6)
- `answer_problems`: Für problematische Antworten
- `comments`: Für zusätzliche Anmerkungen

### Schritt 3: Bewertung durchführen

1. Schauen Sie das Experiment-Dokument an
2. Verschaffen Sie sich einen Überblick über die ISO-OSI-Layer-Inhalte durch das Lesen des Textes im Dokument
3. Für jede Frage:
   - Lesen Sie die Frage sorgfältig
   - Bewerten Sie nach den 6 Kategorien der Rubrik (1-5 Punkte)
   - Bestimmen Sie das erreichte Bloom-Level (Level 1-6) basierend auf der Rubrik
   - Notieren Sie Ihre Bewertungen entsprechend in die Tabelle
   - Notieren Sie gegebenenfalls problematische Antworten/Antwortoptionen in `answer_problems`
   - Ergänzen Sie bei Bedarf Kommentare

**Bewertungsfokus:**

- Welches Bloom-Level wird tatsächlich erreicht?
- Gibt es bestimmte qualitative Unterschiede zwischen MCQ und Open-Ended Fragen?

## Dankbarkeit

Vielen Dank für Ihre Unterstützung bei der Evaluation! Ihre Einschätzungen sind wertvoll für die Forschung.
