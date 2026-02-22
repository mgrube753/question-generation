# Überblick des Experiments 1 -- Ausführung durch Malte Grube

Dieses Experiment testet die Qualität von automatisiert-generierten Fragen durch vier Large Language Models (LLMs) und deren Fähigkeit, sich an gegebene Quellinhalte zu halten. Dabei wurde ein einheitliches Promptdesign pro Fragetyp (Multiple-Choice, Open-Ended) verwendet, mit dem die Modelle Fragen zum ISO-OSI-Modell generieren sollten. Details zum Prompt werden aufgrund des Blindtests nicht gegeben.

## Experimentaufbau

**Eingabequelle:** Extrahierte Textauszüge aus Prof. Caps Vorlesungs-PDF "Referenzarchitekturen" zum ISO-OSI-Modell

**Material-Aufbereitung:**

- Aufteilung in 7 einzelne TXT-Files (Layer 1-7)
- Bei Fragengenerierung wurde zum schnellen Nachvollziehen nachträglich der jeweilige Layer-Text in das Frage-File geschrieben

**Wertigkeit der Fragen:**

In jede Frage wurde ein bestimmtes Lernziel integriert, basierend auf dem jeweiligen OSI-Layer (1/7), welches durch die Frage zu erfüllen ist. Das Einhalten dessen soll mit der **Wertigkeit**-Kategorie in der Rubrik bewertet werden. Dies wurde eingebunden, da die Wertigkeit einer Frage ein wichtiger Aspekt der Fragequalität ist, jedoch nicht über eine Zahl allein abgebildet werden kann.

## Anleitung für Experten

### Schritt 1: Bewertungskriterien verstehen

Lesen Sie die Rubrik `exp1_rubric.md`, die folgende Kategorien umfasst (jeweils 1-5 Punkte). Bestimmte Kategorien fokussieren sich auf die Bewertung der Fragen selbst, andere auf die Bewertung der Antworten. Beide Bestandteile sollen unmittelbar nach dem Lesen des jeweiligen Teils bewertet werden.

**Fragenbewertung:**

- **Relevanz:** Bezug zum Thema des Textinhalts
- **Klarheit:** Eindeutigkeit der Formulierung
- **Beantwortbarkeit:** Verfügbarkeit der Informationen im Text
- **Herausforderung:** Anspruchsniveau der Frage
- **Wertigkeit:** Bedeutung für vorgegebenes Lernziel
- **Sprachqualität:** Verständlichkeit und Angemessenheit

**Antwortbewertung:**

- **Klarheit:** Eindeutigkeit der Formulierung
- **Sprachqualität:** Verständlichkeit und Angemessenheit
- **Korrektheit:** Fachliche Richtigkeit bezogen auf den Text, gemessen als Inhaltstreue zur Quelle

### Schritt 2: CSV-Struktur verstehen

Die Datei `exp1.csv` enthält:

- `sample_id`: Eindeutige ID (001-024) für Zuordnung zur Fragendatei
- `layer`: OSI-Layer (1-7), aus dem die Frage generiert wurde
- `question_type`: `mcq` oder `open_ended`
- Die 6 Bewertungsspalten für die Fragenbewertung (q_relevance, q_clarity, q_answerability, q_challenge, q_value, q_language)
- Die 3 Bewertungsspalten für die Antwortenbewertung (a_clarity, a_language, a_correctness)
- `answer_problems`: Sind gewisse Antworten problematisch? Warum?
- `comments`: Für zusätzliche Anmerkungen

### Schritt 3: Bewertung durchführen

1. Öffnen Sie `exp1.csv`
2. Für jede Zeile:
   - Öffnen Sie die entsprechende Fragendatei und schauen Sie sich das Lernziel für diese Frage an
   - Lesen Sie die Frage sorgfältig. Lassen Sie dabei die Antwort noch außer Acht
   - Prüfen Sie den Quelltext am unteren Ende der Datei
   - Bewerten Sie nach den 6 Kategorien der Rubrik für die Frage und notieren Sie Ihre Bewertungen in die CSV
   - Lesen Sie nun die Antwort(en) zur Frage sorgfältig durch
   - Bewerten Sie nach den 3 Kategorien der Rubrik für die Antwort(en) und notieren Sie Ihre Bewertungen in die CSV
   - Notieren Sie gegebenenfalls problematische Antworten/Antwortoptionen in `answer_problems`, und warum diese problematisch sind
   - Ergänzen Sie bei Bedarf weitere Kommentare in `comments`

**Bewertungsfokus:**

- Ist die Frage fachlich korrekt bezogen auf den Layer-Text?
- Sind alle im Text enthaltenen Informationen richtig wiedergegeben?

## Dankbarkeit

Vielen Dank für Ihre Unterstützung bei der Evaluation! Ihre Einschätzungen sind wertvoll für die Forschung.
