**Role:** Verhalte dich wie ein Lernexperte für schriftliche Prüfungen im Bachelor der Informatik, der präzise Stämme für Multiple-Choice-Fragen zu einem gegebenen Lehrtext erstellt und die kognitive Tiefe präzise auf das Bloom-Level {bloom_level} abbildet.

**Task:** Generiere einen einzelnen, klaren Fragesatz (Stamm) für eine MCQ-Frage, der exakt dem spezifizierten Bloom-Level entspricht. Die Frage wird Bachelorstudenten der Informatik gestellt. Sie muss so formuliert sein, dass sie mit genau zwei korrekten, inhaltlich voneinander verschiedenen, Antwortmöglichkeiten (Keys) beantwortet werden kann. Die Frage muss innerhalb von maximal 2 Minuten unter Prüfungsbedingungen beantwortet werden können. Verzichte in der Generierung auf die Angabe von Antwortmöglichkeiten und schriftliche Bezugnahme zum Text.

**Context:** Die Frage muss ausschließlich auf dem folgenden Lehrmaterial basieren:

{text}

Das erforderliche kognitive Niveau ist exakt Bloom-Level {bloom_level}. Die Beschreibung dieses Levels ist: {bloom_level_description}.

Das Lernziel, das mit dieser Frage geprüft werden soll, ist: {learning_objective}.

**Reasoning Steps:**

1. Analysiere das Kernkonzept des bereitgestellten Kontexts sorgfältig.
2. Validiere das Ziel-Level {bloom_level}.
3. Fokussiere dich auf das angegebene Lernziel.
4. Wähle ein Operatorverb aus der folgenden Liste, das genau diesem Level entspricht: {bloom_level_verbs}.
5. Stelle sicher, dass kein Operator einer anderen Stufe verwendet wird.
6. Identifiziere geeignete, prüfbare Fakten, Konzepte oder Definitionen im bereitgestellten Kontext.
7. Formuliere einen prägnanten Fragesatz oder eine unvollständige Aussage, die als Stamm dient und diesen spezifischen kognitiven Prozess auslöst, passend zum Originalkontext.
8. Stelle sicher, dass die Frage mit genau zwei inhaltlich unterschiedlichen, korrekten Antwortmöglichkeiten beantwortet werden kann.
9. Stelle sicher, dass die Frage direkt formuliert ist, ohne schriftliche Bezugnahme auf den Text.

**Output Format:** Die Ausgabe muss wie folgt formatiert sein:

Frage: [Hier den Frageninhalt einfügen]

Gib nur den Fragesatz (Stamm) im vorgegebenen Format aus. Schreibe keinen zusätzlichen Text und vermeide jegliche Markdown-basierte Formatierung (e.g. Hervorhebungen, Heading-Tags, ...).

**Stop Conditions:** Stoppe genau nach der Generierung des Fragestamms.
