# Notizen

- es gibt das Problem mit "Frage: Frage" bei frage1 (MCQ)
- das entsteht dadurch, weil ich im `prompt_mcq_distractors.md` die Frage mit `{stem}` einfüge im Output Format
- nun kam es oftmals bei OpenAI und xAI vor, dass dieses Phänomen auftritt, und einmalig bei DeepSeek
- sonst wurde es immer korrekt ausgegeben; ein Fall von randomness/stochasticity, da es nicht immer auftrat
- dies hätte man verhindern können, wenn man nicht "Frage: {stem}" im Output Format gehabt hätte, sondern einfach nur "{stem}"
- annotationen zu frage1:
  - lernziele müssen messbarer gestaltet werden
  - zu oberflächlich, kann man nicht messen, kann man nicht kontrollieren
    - neuer lauf mit neuen lernzielen bei experiment 2 nötig?
  - es fällt auf, dass bei den distraktoren etwas verwirrendes hinten rangehängt wird. normalerweise sind bei ai-based fragen die keys viel länger. jedenfalls ist dies etwas inkonsistent über die antwortmöglichkeiten hinweg. so könnte man auf Dauer womöglich als Student erkennen, welche die richtigen Antworten sind
  - die antwortmöglichkeiten haben reihenfolge "falsch wahr falsch wahr". soweit nicht dramatisch (ist nicht fixiert, da es shuffled im dritten Generierungsschritt wird); dies führt aber dazu, dass man in dieser frage nun von a) bis d) keine Layer-reihenfolge hat, sondern 2 3 5 4, was laut Anne eher umzusetzen wäre mit der Reihenfolge
  - "wählen sie genau zwei"? ist gedoppelt. "wählen sie 2" / "welche zwei" (wie in Frage) ist besser, bei MCQ kann man bestenfalls auch gar keine Zahl angeben
  - kein gendern integriert, nur aufgefallen
  - eine frage sollte auf einem verb enden oder in der MCQ z.b. mit dem "zuständig". sie ist etwas wirr formuliert in Bausteinreihenfolge.
  - es war fraglich, ob die Distraktoren kompletter Unfug sind, oder ob diese in sich korrekt sind, nur nicht für die Frage explizit. Ist bei der frage auch der fall gewesen, dass sie korrekt waren. sonst hätte man eben ausschließen können "die funktion gibt es bei dem layer nicht, muss falsch sein"
- annotationen zu frage2:
  - lernziel auch nicht optimal formuliert. im MCQ lernziel hieß es "kernaufgaben" und hier ist es "konzepte"; messbarkeit problematisch; zwei verschiedene bloom-levels im lernziel (anwenden3 und zuordnen1) --> modell hat sich für ein bloom3 verb (nutzen) entschieden, aber letztendlich level1 nur erreicht
    - bloom-based lernziele (experiment2) sind zu groß für die eine frage formuliert. zumal lernziele 1-3 momentan nicht unbedingt mit MCQ gedeckt werden können
    - "beziehung" ist ein großes wort für das lernziel
    - sollte sein: "Studierende können einzelne schichten des iso osi modells definieren ...", irgendwas mit definieren jedenfalls
  - haben in frage 6 ereignisse, es gibt 7 layer; per beantwortung werden nur 1 2 3 4 und 6 für die ereignisse verlangt... dies ist nicht uniform genug; ähnliches bei frage1 auch schon
  - es gibt je nach ereignis auch etwas in klammern, oder gar ein "z.b.", auch nicht konsistent über die elemente in der frage hinweg

---

- frage1:
  - q_clarity: inhaltlich war sie im Grunde eindeutig, 5
  - q_challenging: 1, wenn man die Schichten im Grunde kennt und deren Aufgaben/Funktionen, dann ist es eine einfache Frage
  - q_value: ohne grundkenntnisse zu den schichten wird man das lernziel nicht erreichen; wurde von 5 auf 3 runtergestuft (behandelt grundlagen: mäßig). es wird mit der frage nicht überprüft, ob der Student das mit eigenen Worten beschreiben kann. man bräuchte "definiere alle layer". lernziel ist zu groß gefasst, um es mit der einen mcq zu decken. frage ist der erste step, braucht aber bestenfalls 2 Folgefragen mit mehr forderungen an die antworten, um das Lernziel zu erreichen
  - q_language: sprachlich dafür etwas problematisch; 2, sprachlich hätte man es besser lösen können
  - q_bloom: 1, da Wissensabfrage durch auswahl (hätte eigentlich 2 sein sollen); handelt sich um "identifizieren", "auswählen", ist im übertragenen Sinne auch "definieren", "benennen"
  - a_clarity: 5; es ist mit frage klar, was gewollt ist
  - a_language: möglichkeiten sind sprachlich passend formuliert; die falschen haben noch "über ..."; 5
  - a_bloom: 1, liegt keine Diskrepanz zwischen Frage und Antwort vor
  
- frage2:
  - q_clarity: 
  - q_challenging: 
  - q_value: 
  - q_language: 
  - q_bloom:
  - a_clarity: 
  - a_language: 
  - a_bloom: 