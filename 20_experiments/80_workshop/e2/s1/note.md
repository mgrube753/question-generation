# Workshop1 für Experiment 2, 20.02.2026 mit Anne-Kathrin Hirsch

## Annotationen zu Frage 1

- es gibt das Problem mit "Frage: Frage" bei der MCQ
- das entsteht dadurch, weil ich im `prompt_mcq_distractors.md` die Frage mit `Frage: {stem}` einfüge im Output Format
- kam oftmals bei OpenAI und xAI vor, dass dieses Phänomen auftritt, und einmalig bei DeepSeek
- sonst wurde es immer korrekt ausgegeben; Randomness/Stochasticity?
- hätte man verhindern können, wenn man nur "{stem}" im Output Format angibt
- Lernziele müssen messbarer gestaltet werden
- zu oberflächlich, kann man nicht messen, kann man nicht kontrollieren
  - neuer Lauf mit neuen Lernzielen bei Experiment 2 mindestens nötig
- fällt auf, dass bei den Distraktoren etwas Verwirrendes hinten rangehängt wird... normalerweise sind bei AI-based Fragen die Keys viel länger... ist etwas inkonsistent über alle antwortmöglichkeiten hinweg... so könnte man auf Dauer womöglich als Student erkennen, welche die richtigen Antworten sind
- die Antwortmöglichkeiten haben Reihenfolge "falsch wahr falsch wahr"... soweit nicht dramatisch (ist aber nicht fixiert in Generierung); nun ist in dieser frage von a) bis d) keine Layer-Reihenfolge da, sondern "2 3 5 4", was laut Anne eher umzusetzen wäre mit der Reihenfolge
- "wählen sie genau zwei" am Ende ist gedoppelt. "wählen sie 2" / "welche zwei" (wie in Frage) ist besser, bei MCQ kann man bestenfalls auch gar keine Zahl angeben
- kein Gendern integriert, nur aufgefallen
- eine Frage sollte auf einem Verb enden oder in der MCQ z.b. mit dem "zuständig"... etwas wirr formuliert in Bausteinreihenfolge
- fraglich, ob die Distraktoren kompletter Unfug sind, oder ob diese in sich korrekt sind, nur nicht für die Frage explizit... bei der Frage waren sie korrekt... sonst hätte man ausschließen können "die Funktion gibt es bei dem Layer nicht, muss falsch sein"

## Annotationen zu Frage 2

- Lernziel auch nicht optimal formuliert... im MCQ Lernziel hieß es "Kernaufgaben" und hier ist es "Konzepte"; nicht alle Schichten werden explizit gefordert in Frage; zwei verschiedene Bloom-levels im Lernziel (Anwenden3 und Zuordnen1) --> Modell hat sich für Bloom3 Verb (nutzen) entschieden, aber letztendlich Level1 nur erreicht
  - Bloom-based Lernziele (Experiment2) zu groß für eine frage, zumal Lernziele 1-3 momentan nicht unbedingt mit MCQ gedeckt werden können
  - "Beziehung" ist ein großes Wort für das Lernziel
  - sollte sein: "Studierende können einzelne Schichten des ISO-OSI Modells definieren ...", irgendwas mit Definieren jedenfalls
- Frageformat wirkt wie eine Zuordnungsfrage statt Open-Ended; erfordert aber kurze Open-Ended antwort... Frage durchaus verwirrend gestellt
- in Frage 6 Ereignisse, gibt aber 7 Layer; per Beantwortung nur 1 2 3 4 und 6 für die Ereignisse verlangt... da wäre uniformes Mapping nötig
- steht nur "OSI" in Frage statt ISO-OSI --> wurde nie explizit dem Modell vorgegeben, dass dies das Oberthema ist, sondern "hier, nimm den Lehrtext und generiere eine Frage dazu"
- gibt in Antwort jeweils pro Layer einen kleinen Nachtrag, welcher den Grundsatz der jeweiligen Aufgabe aus a-f darstellt; nicht nötig zur Beantwortung
- aus "Kommunikationsvorgänge" im Lernziel wird "Vorgänge" in Frage
- Verb "einzutragen" etwas unpassend gewählt, da es eher auf eine Zuordnungsfrage hindeutet, als auf eine offene Frage... wir müssen aber explizit etwas hinschreiben --> andere Formulierung wäre besser, da umständlich
- a ist gut, b: wlan-gerät "entscheidet"? Prüfen & Regeln wäre besser... gewisse Tasks sind weniger akademisch formuliert als andere
- gibt je nach Ereignis auch etwas in Klammern bei Frage, oder gar ein "z.b.", auch nicht konsistent über Elemente in Frage hinweg

## Bewertung von Frage 1

### Fragebewertung 1

- `q_clarity`: inhaltlich im Grunde eindeutig, 5
- `q_challenging`: 1, wenn man die Schichten im Grunde kennt und deren Aufgaben/Funktionen, dann ist es eine einfache Frage
- `q_value`: ohne Grundkenntnisse zu den Schichten wird man das Lernziel nicht erreichen; wurde von 5 auf 3 runtergestuft (behandelt Grundlagen: mäßig)... mit frage wird nicht überprüft, ob Student das mit eigenen Worten beschreiben kann... man bräuchte "Definiere alle Layer" --> Lernziel zu groß gefasst, um es mit der einen MCQ zu decken... Frage ist der erste Step, braucht aber bestenfalls 2 Folgefragen mit mehr Forderungen an die Antworten, um das Lernziel zu erreichen
- `q_language`: sprachlich etwas problematisch; 2, hätte man besser lösen können
- `q_bloom`: 1, da Wissensabfrage durch Auswahl (hätte eigentlich 2 sein sollen); handelt sich um "identifizieren", "auswählen", ist im übertragenen Sinne auch "definieren", "benennen"

### Antwortbewertung 1

- `a_clarity`: 5; es ist mit Frage klar, was gewollt ist... HINWEIS: klare Trennung zwischen Frage und Antwort nötig im nächsten Workshop
- `a_language`: Möglichkeiten sind sprachlich passend formuliert; die falschen haben noch "über ..." hinten dran; 5 trotzdem
- `a_bloom`: 1, liegt keine Diskrepanz zwischen Frage und Antwort vor
  
## Bewertung von Frage 2

### Fragebewertung 2

- `q_clarity`: keine 5, aber eine 4
- `q_challenging`: nicht alle Schichten drin --> etwas fiese umsetzung, 2
- `q_value`: Zuordnung funktioniert im Grunde; nicht alle Konzepte abgefragt (s. Challenging); Beispiele fehlen grundsätzlich, nur ein paar da --> warum nicht einfach einheitlich, Unicode als Beispiel für einheitliches Zeichenformat ist etwas einfach; 3
- `q_language`: andere Formulierung sinnvoll: "ordne den sieben Schichten (1-7) die folgenden sieben Kommunikationsvorgänge zu"... trotz all dem nicht schwerfällig; "eintragen" schwieriges Wort; 4
- `q_bloom`: 1, statt 3, Lernziel ist problematisch, da "anwenden" und "zuordnen" drin... LLM hat final eine Bloom1 Frage generiert

### Antwortbewertung 2

- `a_clarity`: zu viel beantwortet (stellt klar warum welche Zuordnung stattgefunden hat), aber inhaltlich klar, 5
- `a_language`: präzise, gute Sprache, ist etwas zu viel (mehr als erwartet) Output; unsichere Studenten hätten das so notiert; 5
- `a_bloom`: Antwort ebenso Bloom1, passend zur Frage... Frage war ja auf falsches Level gelegt worden durch Lernziel
