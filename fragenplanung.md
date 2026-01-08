## Fragenplanung

### Experiment I

#### Wir haben I

* 4 LLMs
* 1 Skript (ISO OSI)
* 7 Layers (Layer 1-7)
* 1 Random Bloom Level pro Frage (vergrößert nicht die Fragenanzahl)
* 2 Fragetypen (MCQ, Open Ended)
* Macht 56 Fragen insgesamt (4x1x7x2)
  * 28 Fragen pro Fragetyp
  * 7 OE-Fragen pro LLM
    * 7 Prompts bei OE pro Modell
  * 7 MCQ-Fragen pro LLM
    * 21 Prompts bei MCQ pro Modell

#### Sampling I

* Haben 56 Fragen insgesamt
* Wollen 24 Fragen
* Sind 6 Fragen pro LLM
  * 3 MCQ
  * 3 OE
* Es gibt 14 Fragen pro LLM
  * 7 OE-Fragen
  * 7 MCQ-Fragen
* Wir samplen 3/7 Layer pro LLM und Fragetyp

### Experiment II

#### Wir haben II

* 4 LLMs
* 1 Skript (ISO/OSI Modell komplett)
* 6 Bloom Levels für Open-Ended
* Doppeltes Prompting pro Level bei MCQ, da dieser Typ Bloom 1-3 abdeckt
* 2 Fragetypen (MCQ, Open Ended)
* Macht 48 Fragen insgesamt (4x1x6x2)
  * 24 Fragen pro Fragetyp
  * 6 OE-Fragen pro LLM
    * 6 Prompts bei OE pro Modell
  * 6 MCQ-Fragen pro LLM
    * 18 Prompts bei MCQ pro Modell

#### Sampling II

* Haben 48 Fragen insgesamt
* Wollen 24 Fragen
* Sind 6 Fragen pro LLM
  * 3 MCQ
  * 3 OE
* Es gibt 12 Fragen pro LLM
  * 6 OE-Fragen
  * 6 MCQ-Fragen
* Wir samplen 1/2 der Fragen pro LLM und Fragetyp

## Warum die Bloom-Aufteilung?

* [Dieser Link](https://teachingtools.uzh.ch/de/tools/lernziel-taxonomien) der Uni Zürich zeigt nämlich tabellarisch, **welche** Bloom-Level für **welche** Fragetypen **wie gut** geeignet sind.
