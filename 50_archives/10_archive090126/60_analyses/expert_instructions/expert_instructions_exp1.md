# Überblick des Experiments 1 -- Ausführung durch Malte Grube

Dieses Experiment testet die Qualität von automatisiert-generierten Fragen durch vier Large Language Models (LLMs) und deren Fähigkeit, sich an gegebene Quellinhalte zu halten. Dabei wurde ein einheitliches Promptdesign pro Fragetyp (Multiple-Choice, Open-Ended) verwendet, mit dem die Modelle Fragen zum ISO-OSI-Modell generieren sollten. Details zum Prompt werden aufgrund des Blindtests nicht gegeben.

## Experimentaufbau

**Eingabequelle:** Extrahierte Textauszüge aus Prof. Caps Vorlesungs-PDF "Referenzarchitekturen" zum ISO-OSI-Modell

**Material-Aufbereitung:**

- Aufteilung in 7 einzelne TXT-Files (Layer 1-7)
- Bei Fragengenerierung wurde zum schnellen Nachvollziehen nachträglich der jeweilige Layer-Text in das Frage-File geschrieben

**Generierte Fragen:**

Vorabinformation: Zur Steuerung der kognitiven Anforderung wurden in die Prompts für alle 4 LLMs bei jedem Lauf ein gemeinsames, randomisiertes Bloom-Level integriert, siehe **Bloom's revised Taxonomy** mit 6 Stufen.

Zudem hat jede Frage ein bestimmtes Lernziel, basierend auf dem jeweiligen OSI-Layer (1/7), zu erfüllen. Das Einhalten dessen soll mit der **Wertigkeit**-Kategorie in der Rubrik bewertet werden.

- 4 LLMs × 7 Layer × 2 Fragetypen = 56 Fragen gesamt
- Pro LLM: 7 Multiple-Choice + 7 Open-Ended Fragen
- Random Bloom-Level pro Frage (Bloom 1-6 für Open-Ended, Bloom 1-3 für MCQ)
- Sample für Bewertung: 24 Fragen (6 pro LLM: 3 MCQ + 3 Open-Ended)

## Anleitung für Experten

### Schritt 1: Bewertungskriterien verstehen

Lesen Sie die Rubrik `exp1_rubric.md`, die folgende Kategorien umfasst (jeweils 1-5 Punkte):

- **Relevanz:** Bezug zum Thema des Textinhalts
- **Klarheit:** Eindeutigkeit der Formulierung
- **Beantwortbarkeit:** Verfügbarkeit der Informationen im Text
- **Herausforderung:** Anspruchsniveau der Frage
- **Wertigkeit:** Bedeutung für vorgegebenes Lernziel
- **Sprachqualität:** Verständlichkeit und Angemessenheit
- **Korrektheit:** Fachliche Richtigkeit bezogen auf den Text, gemessen als Inhaltstreue zur Quelle

### Schritt 2: CSV-Struktur verstehen

Die Datei `exp1.csv` enthält:

- `sample_id`: Eindeutige ID (001-024) für Zuordnung zur Fragendatei
- `layer`: OSI-Layer (1-7), aus dem die Frage generiert wurde
- `question_type`: `mcq` oder `open_ended`
- Die 7 Bewertungsspalten aus Schritt 1 (1-5 Punkte)
- `answer_problems`: Für problematische Antworten
- `comments`: Für zusätzliche Anmerkungen

### Schritt 3: Bewertung durchführen

1. Öffnen Sie `exp1.csv`
2. Für jede Zeile:
   - Öffnen Sie die entsprechende Fragendatei und lesen Sie die Frage sorgfältig
   - Prüfen Sie den Quelltext, welcher direkt unter der Frage angegeben ist
   - Bewerten Sie nach den 7 Kategorien der Rubrik (1-5 Punkte), und notieren Sie Ihre Bewertungen in die entsprechenden Spalten
   - Notieren Sie gegebenenfalls problematische Antworten/Antwortoptionen in `answer_problems`
   - Ergänzen Sie bei Bedarf Kommentare

**Bewertungsfokus:**

- Ist die Frage fachlich korrekt bezogen auf den Layer-Text?
- Sind alle im Text enthaltenen Informationen richtig wiedergegeben?

## Dankbarkeit

Vielen Dank für Ihre Unterstützung bei der Evaluation! Ihre Einschätzungen sind wertvoll für die Forschung.
