# Überblick des Experiments 2 -- Ausführung durch Malte Grube

Dieses Experiment testet die Fähigkeit von vier Large Language Models (LLMs), Fragen in verschiedenen Formaten (Multiple-Choice, Open-Ended) und auf unterschiedlichen kognitiven Niveaus nach Bloom's revised Taxonomy systematisch zu generieren. Das Thema ist das ISO-OSI-Modell, ein wichtiges Referenzmodell aus der Informatik. Details zum Prompting werden aufgrund des Blindtests nicht gegeben.

## Experimentaufbau

**Eingabequelle:** Extrahierte Textauszüge aller 7 ISO-OSI-Layer als ein zusammengefügter Text, basierend auf einer Vorlesungs-PDF meines Professors.

**Material-Aufbereitung:** Zusammenfügen der Informationen aller 7 Layer zu einem Text, welcher in das vorliegende .docx Dokument integriert wurde

**Wertigkeit der Fragen:**

In jede Frage wurde ein bestimmtes Lernziel integriert, an das jeweilige Bloom-Level geknüpft (1/6). Das Einhalten des Lernziels soll mit der **Wertigkeit**-Kategorie in der Rubrik bewertet werden. Dies wurde eingebunden, da die Wertigkeit einer Frage ein wichtiger Aspekt der Fragequalität ist, jedoch nicht über eine Zahl allein abgebildet werden kann.

## Anleitung für Experten

### Schritt 1: Bewertungskriterien verstehen

Lesen Sie die PDF mit der Rubrik durch, die folgende Kategorien umfasst (jeweils 1-5 Punkte, außer bei der Bloom-Level-Bestimmung). Bestimmte Kategorien fokussieren sich auf die Bewertung der Fragen selbst, andere auf die Bewertung der Antworten. Beide Bestandteile sollen unmittelbar nach dem Lesen des jeweiligen Teils bewertet werden.

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

### Schritt 2: CSV-Struktur verstehen

Die Datei `exp2.csv` enthält:

- `sample_id`: Eindeutige ID (001-024) für Zuordnung zur Frage
- `question_type`: `mcq` oder `open_ended`
- Die 5 Bewertungsspalten für die Fragenbewertung (q_clarity, q_challenging, q_value, q_language, q_bloom_rating)
- Die 3 Bewertungsspalten für die Antwortenbewertung (a_clarity, a_language, a_bloom_rating)
- `answer_problems`: Sind gewisse Antworten problematisch? Warum?
- `comments`: Für zusätzliche Anmerkungen

### Schritt 3: Bewertung durchführen

1. Schauen Sie das PDF-Dokument mit den Fragen an
2. Verschaffen Sie sich einen Überblick über die ISO-OSI-Layer-Inhalte (separates PDF), auf die sich die Fragen beziehen
3. Öffnen Sie `exp2.csv`
4. Für jede Zeile:
   - Schauen Sie sich das Lernziel für die jeweilige Frage an
   - Lesen Sie die Frage sorgfältig. Lassen Sie dabei die Antwort noch außer Acht
   - Bewerten Sie nach den 5 Kategorien der Rubrik für die Frage und notieren Sie Ihre Bewertungen in die CSV
   - Lesen Sie nun die Antwort(en) zur Frage sorgfältig durch
   - Bewerten Sie nach den 3 Kategorien der Rubrik für die Antworten und notieren Sie Ihre Bewertungen in die CSV
   - Notieren Sie gegebenenfalls problematische Antworten/Antwortoptionen in `answer_problems`, und warum diese problematisch sind
   - Ergänzen Sie bei Bedarf weitere Kommentare in `comments`

Vielen Dank für Ihre Unterstützung bei der Evaluation! Ihre Einschätzungen sind wertvoll für die Forschung.
