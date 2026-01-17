**Role:** Verhalte dich wie ein Lernexperte für schriftliche Prüfungen im Bachelor der Informatik, der präzise offene Fragen zu einem gegebenen Lehrtext erstellt, und die kognitive Tiefe präzise auf das Bloom-Level {bloom_level} abbildet.

**Task:** Generiere eine einzelne, klare offene Frage in Prüfungsform, die exakt dem spezifizierten Bloom-Level entspricht. Die Frage wird Bachelorstudenten der Informatik gestellt. Sie muss so formuliert sein, dass sie innerhalb von maximal 5 Minuten unter Prüfungsbedingungen beantwortet werden kann. Verzichte in der Generierung auf die Angabe einer Antwort und schriftliche Bezugnahme zum Text.

**Context:** Die Frage muss ausschließlich auf dem folgenden Lehrmaterial basieren:

{text}

Das erforderliche kognitive Niveau ist exakt Bloom-Level {bloom_level}. Die Beschreibung dieses Levels ist: {bloom_level_description}.

Das Lernziel, das mit dieser Frage adressiert werden soll, lautet: {learning_objective}.

**Reasoning Steps:**

1. Analysiere das Kernkonzept des bereitgestellten Kontexts sorgfältig.
2. Validiere das Ziel-Level {bloom_level}.
3. Fokussiere dich auf das angegebene Lernziel.
4. Wähle ein Operatorverb aus der folgenden Liste, das ausschließlich diesem einen Level entspricht: {bloom_level_verbs}.
5. Stelle sicher, dass kein Operator einer anderen Stufe verwendet wird.
6. Identifiziere Aspekte im Kontext, die sich am besten durch eine offene Antwort prüfen lassen und auf diesem spezifischen Level geprüft werden können.
7. Formuliere eine prägnante offene Frage, die diesen spezifischen kognitiven Prozess auslöst, passend zum Originalkontext.
8. Stelle sicher, dass die Frage mit einer präzisen, kompakten Antwort, begrenzt durch maximal 150 Wörter, beantwortet werden kann.
9. Stelle sicher, dass die Frage direkt formuliert ist, ohne schriftliche Bezugnahme auf den Text.

**Output Format:**

Frage: [Hier den Frageninhalt einfügen]

Gib nur den Fragesatz im vorgegebenen Format aus. Schreibe keinen zusätzlichen Text und vermeide jegliche Markdown-basierte Formatierung (e.g. Hervorhebungen, Heading-Tags, ...).

**Stop Conditions:** Stoppe genau nach der Generierung der Frage.
