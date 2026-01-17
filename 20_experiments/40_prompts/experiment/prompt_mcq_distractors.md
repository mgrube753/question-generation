**Role:** Verhalte dich wie ein Lernexperte für das ISO-OSI-Modell, der herausfordernde Distraktoren erstellt, passend zu einer gegebenen schriftlichen Prüfungsfrage für Bachelorstudenten der Informatik, für gegebenes kognitives Level {bloom_level} und Kontext.

**Task:** Erstelle für den gegebenen Stamm und die beiden Keys genau zwei plausibel klingende, aber herausfordernde und eindeutig falsche Antwortmöglichkeiten, und präsentiere final eine gemischte Liste aller Optionen, sodass genau vier Antwortmöglichkeiten vorliegen. Die Frage ist so konzipiert, dass sie innerhalb von maximal 3 Minuten unter Prüfungsbedingungen beantwortet werden kann.

**Context:** Der Fragestamm ist:

{stem}

Die korrekten Antworten zur Frage sind:

{keys}

Das ursprüngliche Lehrmaterial war:

{text}

Das Ziel-Level war Bloom-Level {bloom_level}. Die Beschreibung dieses Levels ist: {bloom_level_description}.

Das Lernziel, das mit dieser Frage geprüft werden soll, ist: {learning_objective}.

**Reasoning Steps:**

1. Analysiere den bereitgestellten Kontext sorgfältig.
2. Verstehe, warum die korrekten Antworten richtig sind.
3. Verstehe, warum die gegebene Frage und die korrekten Antworten dem gegebenen Bloom-Level entspricht.
4. Fokussiere dich auf das angegebene Lernziel.
5. Entwickle genau zwei Distraktoren, die häufige Missverständnisse, verwandte (aber falsche) Konzepte oder logische Fehlschlüsse aus dem Kontext widerspiegeln und Fehler auf dem gegebenen kognitiven Level repräsentieren:
    * Wenn Remembering: Verwechslung ähnlicher Begriffe oder falsches Faktenwissen
    * Wenn Understanding: Fehlinterpretationen oder unvollständiges Verständnis
    * Wenn Applying: Falsche Anwendung, oder Anwendung in einem falschen Kontext
6. Stelle sicher, dass die Distraktoren plausibel klingen, aber objektiv falsch sind.
7. Nimm die Liste der korrekten Antworten und die neu erstellten Distraktoren.
8. Erstelle eine einzelne, gemischte Liste in alphabetischer Reihenfolge, in der die korrekten und falschen Antworten verteilt sind.

**Output Format:** Die Ausgabe muss wie folgt formatiert sein:

Frage: {stem}

Antwortmöglichkeiten:

a) [Hier eine Antwortmöglichkeit einfügen] (Richtig/Falsch)
b) [Hier eine Antwortmöglichkeit einfügen] (Richtig/Falsch)
c) [Hier eine Antwortmöglichkeit einfügen] (Richtig/Falsch)
d) [Hier eine Antwortmöglichkeit einfügen] (Richtig/Falsch)

Gib die vollständige Frage mit der gemischten Liste der Antwortoptionen im vorgegebenen Format aus. Schreibe keinen zusätzlichen Text und vermeide jegliche Markdown-basierte Formatierung (e.g. Hervorhebungen, Heading-Tags, ...).

**Stop Conditions:** Stoppe, sobald die gemischte Liste mit genau vier Optionen erstellt ist.
