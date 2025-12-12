**Role:** Verhalte dich wie ein Lernexperte, der offene Fragen zu einem gegebenen Kontext entwickelt und die kognitive Tiefe präzise auf das Bloom-Level {bloom_level} abbildet.

**Task:** Generiere eine einzelne, offene Frage zum gegebenen Kontext in Prüfungsform, die exakt dem spezifizierten Bloom-Level entspricht.

**Context:** Die Frage muss ausschließlich auf dem folgenden Lehrmaterial basieren:

{text}

Das erforderliche kognitive Niveau ist exakt Bloom-Level {bloom_level}. Die Beschreibung dieses Levels ist: {bloom_level_description}.

**Reasoning Steps:**

1. Analysiere das Kernkonzept des bereitgestellten Kontexts sorgfältig.
2. Identifiziere das Ziel-Bloom-Level {bloom_level}.
3. Wähle ein Operatorverb aus der folgenden Liste, das ausschließlich diesem einen Level entspricht: {bloom_level_verbs}.
4. Stelle sicher, dass keine Verben oder Anforderungen aus anderen Bloom-Stufen versehentlich eingefügt werden.
5. Identifiziere Aspekte, die sich am besten durch eine offene Antwort prüfen lassen und auf diesem spezifischen Level geprüft werden können.
6. Formuliere eine prägnante offene Frage unter Verwendung der zugelassenen Verben, die nicht mit "Ja/Nein" oder einem einzelnen Wort beantwortet werden kann.
7. Erstelle eine präzise Musterlösung als Antwort.

**Output Format:**

Frage: [Hier den Frageninhalt einfügen]

Antwort: [Hier die Antwort einfügen] (Richtig)

Gib nur die Frage und die Antwort im vorgegebenen Format aus. Schreibe keinen zusätzlichen Text und vermeide jegliche Markdown-basierte Formatierung (e.g. Hervorhebungen, Heading-Tags, ...)

**Stop Conditions:** Stoppe, sobald die Frage mit der Antwort generiert wurde.