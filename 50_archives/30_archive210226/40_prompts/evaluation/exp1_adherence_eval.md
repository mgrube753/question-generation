**Role:** Verhalte dich wie ein Experte im metrischen Bewerten von automatisch generierten Fragen. Fokussiere dich bezüglich ihrer Übereinstimmung zu einem gegebenen Quelltext.

**Task:** Bewerte die Inhaltstreue der gegebenen Frage zum Kontext und gib eine Bewertung als Dezimalzahl zwischen 0.0 und 1.0 aus.

**Context:** Die zu bewertende Frage lautet:

{question_text}

Die Frage basiert auf folgendem Kontext:

{context_text}

**Reasoning Steps:**

1. Analysiere die Frage und den Kontext systematisch.
2. Achte auf die korrekte Verwendung von Fachbegriffen und die inhaltliche Übereinstimmung zwischen Frage und Kontext.
3. Identifiziere Abweichungen, Ungenauigkeiten oder Missverständnisse.
4. Bewerte den Grad der Übereinstimmung anhand der folgenden Skala:

- 1.0: Alle Inhalte wurden korrekt und umfassend dargelegt.
- 0.8-0.9: Geringfügige fachliche Abweichungen.
- 0.6-0.7: Gewisse technische Ungenauigkeiten.
- 0.4-0.5: Mehrere inhaltliche Abweichungen.
- 0.2-0.3: Gravierende Missverständnisse.
- 0.0-0.1: Inhalte entsprechen nicht dem Kontext.

5. Formuliere das Ergebnis als einzelne Dezimalzahl.

**Output Format:** Die Ausgabe soll ausschließlich die Bewertung als Dezimalzahl zwischen 0.0 und 1.0 mit zwei Nachkommastellen sein:

[adherence_score]

Ein Beispiel-Output wäre: `0.73`

**Stop Conditions:** Stoppe genau nach der Ausgabe der Bewertung.