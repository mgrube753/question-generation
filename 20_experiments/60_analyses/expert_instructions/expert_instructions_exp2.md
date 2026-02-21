# Überblick des Experiments 2 -- Ausführung durch Malte Grube

Dieses Experiment testet die Fähigkeit von vier Large Language Models (LLMs), Fragen in verschiedenen Formaten (Multiple-Choice, Open-Ended) und auf unterschiedlichen kognitiven Niveaus nach Bloom's revised Taxonomy systematisch zu generieren. Das Thema ist das ISO-OSI-Modell, ein wichtiges Referenzmodell aus der Informatik. Details zum Prompting werden aufgrund des Blindtests nicht gegeben.

## Experimentaufbau

**Eingabequelle:** Extrahierte Textauszüge aller 7 OSI-Layer als ein zusammengefügter Text, basierend auf einer Vorlesungs-PDF meines Professors.

**Material-Aufbereitung:** Zusammenfügen der Informationen aller 7 Layer zu einem Text, welcher in das vorliegende .docx Dokument integriert wurde

**Wertigkeit der Fragen:**

In jede Frage wurde ein bestimmtes Lernziel integriert, an das jeweilige Bloom-Level geknüpft (1/6). Das Einhalten des Lernziels soll mit der **Wertigkeit**-Kategorie in der Rubrik bewertet werden. Dies wurde eingebunden, da die Wertigkeit einer Frage ein wichtiger Aspekt der Fragequalität ist, jedoch nicht über eine Zahl allein abgebildet werden kann.

## Anleitung für Experten

### Schritt 1: Bewertungskriterien verstehen

Lesen Sie die im .docx enthaltene Rubrik durch, die folgende Kategorien umfasst (jeweils 1-5 Punkte). Bestimmte Kategorien fokussieren sich auf die Bewertung der Fragen selbst, andere auf die Bewertung der Antworten. Beide Bestandteile sollen unmittelbar nach dem Lesen des jeweiligen Frage- / Antwort-Texts bewertet werden.

**Fragenbewertung:**

- **Klarheit:** Eindeutigkeit der Formulierung
- **Herausforderung:** Anspruchsniveau der Frage
- **Wertigkeit:** Bedeutung für vorgegebenes Lernziel
- **Sprachqualität:** Verständlichkeit und Angemessenheit
- **Bloom-Level:** Welches kognitive Level wird in dieser Frage erreicht?

**Antwortbewertung:**

- **Klarheit:** Eindeutigkeit der Formulierung
- **Sprachqualität:** Verständlichkeit und Angemessenheit
- **Bloom-Level:** Welches kognitive Level wird durch die Antwort umgesetzt?

### Schritt 2: Tabellen-Struktur verstehen

Jede Klein-Tabelle unter der jeweiligen Frage enthält:

- Die 5 Bewertungszeilen für die Fragenbewertung (Klarheit, Herausforderung, Wertigkeit, Sprachqualität, Bloom-Level)
- Die 3 Bewertungszeilen für die Antwortenbewertung (Klarheit, Sprachqualität, Bloom-Level)
- `answer_problems`: Sind gewisse Antworten problematisch? Warum?
- `comments`: Für zusätzliche Anmerkungen

### Schritt 3: Bewertung durchführen

1. Schauen Sie das Experiment-Dokument an
2. Verschaffen Sie sich einen Überblick über die ISO-OSI-Layer-Inhalte durch das Lesen des Textes im Dokument, auf den sich die Fragen beziehen
3. Für jedes Fragenkonstrukt:
   - Schauen Sie sich das Lernziel für die jeweilige Frage an
   - Lesen Sie die Frage sorgfältig. Lassen Sie dabei die Antwort noch außer Acht
   - Bewerten Sie nach den 5 Kategorien der Rubrik für die Frage und notieren Sie Ihre Bewertungen in die Tabelle
   - Lesen Sie nun die Antwort(en) zur Frage sorgfältig durch
   - Bewerten Sie nach den 3 Kategorien der Rubrik für die Antworten und notieren Sie Ihre Bewertungen in die Tabelle
   - Notieren Sie gegebenenfalls problematische Antworten/Antwortoptionen in `answer_problems`, und warum diese problematisch sind
   - Ergänzen Sie bei Bedarf weitere Kommentare in `comments`

**Bewertungsfokus:**

- Welches Bloom-Level wird tatsächlich erreicht?
- Gibt es bestimmte qualitative Unterschiede zwischen MCQ und Open-Ended Fragen?

## Dankbarkeit

Vielen Dank für Ihre Unterstützung bei der Evaluation! Ihre Einschätzungen sind wertvoll für die Forschung.
