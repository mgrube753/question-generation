# Rater-Kommentare bei Exp1 (Fokus auf Freitext-Felder)

## 1. Gemeinsamkeiten

### Zur Abhängigkeit vom Quelltext

- Rater 1 und Rater 2 bemängeln häufig und übereinstimmend, dass die LLMs Fragen und Antworten generieren, die nicht durch den bereitgestellten Quelltext gedeckt sind.
  - _Rater 1_ notiert folgendes: „Wenig Input aus Quelltext“, „Viel ‚ausgedachtes‘“, „Mit Input nicht beantwortbar“ (siehe IDs 06 Anthropic, 11 & 12 DeepSeek, 16 & 17 OpenAI).
  - _Rater 2_ bestätigt dies: „Der Quelltext gibt den Inhalt der Antwort nicht her“, „Rahmenbedingungen, die weder in der Frage noch in der Quelle gegeben sind“ (siehe IDs 04 & 06 Anthropic, 16 OpenAI).
- Die LLMs greifen zur Beantwortung oft auf ihr internes Weltwissen zurück, statt sich streng an das Lehrmaterial zu halten.

### Zweifel an Korrektheit / Sinnhaftigkeit

- Rater sehen bei Musterlösungen fachliche Ungereimtheiten / unlogische Grundannahmen
  - _Rater 1_ bezweifelt Richtigkeit: „Korrektheit fragwürdig“, „Grundkonzepte nicht korrekt (?)“ (IDs 02 & 06 Anthropic, 24 xAI).
  - _Rater 2_ hinterfragt Notwendigkeiten in Musterlösungen: „Notwendigkeit von Komprimierung ist nicht aus der Aufgabenstellung ersichtlich“ (ID 05 Anthropic), „Codierung ist definitiv auch notwendig hier“ (ID 14 OpenAI).
  - _Rater 3_ kritisiert fachliche Ungenauigkeit: „Der Begriff 'Bandbreite' wird wie üblich falsch verwendet“ (ID 04 Anthropic).

### Schwächen im Aufgabendesign & MCQ-Distraktoren

- Rater 2 findet diverse Aufgaben „völlig ungeeignet“, „viel zu allgemein und viel zu großer Umfang“ (ID 12 DeepSeek) oder gar „unsinnig“ (ID 13 OpenAI). Rater 1 hat ID 13 (OpenAI) auch erst nach mehrmaligem Lesen richtig verstanden. Wortwahlen werden oft als „merkwürdig“ empfunden (ID 8 DeepSeek, ID 16 OpenAI).
- Wie in Exp 2 fällt auch hier auf, dass Keys manchmal semantisch zu nahe liegen; Rater 2: „b) ist inhaltlich gefährlich nah an a) dran“ (ID 02 Anthropic). Rater 1: „Zwei Antworten gleich, nur andere Sprache“ (ID 21 xAI).

## 2. Unterschiede

- **Rater 1 fokussiert Methodik und Formalitäten:**
  - Prüft penibel das formale Format der generierten Texte und der Aufgabenstellung. Bemängelt, wenn Antworten kein Fließtext sind (ID 16 OpenAI), in „Ich-Perspektive“ geantwortet wird (ID 24 xAI) oder Aufzählungen („Erstens... Zweitens...“) verwendet werden (ID 05 Anthropic). Eine Frage beinhaltet Limit von 150 Wörtern als Vorgabe wie im Prompt (ID 18 OpenAI).
- **Rater 2 prüft praxisnah:**
  - Rater 2 denkt praktisch und kritisiert, wenn LLMs unrealistische Lösungswege vorschlagen. Zu ID 06 Anthropic: „Warten lassen ist oft gar keine Option [...] Ressourcen sind immer begrenzt. Was sollen das für Kriterien sein, nach denen begründet wird?“
- **Rater 3 mit seltener Kommentarvergabe:**
  - Rater 3 hält Beobachtungen in wenigen Worten fest. Beispiele: „Gesinnungsfrage“ (ID 06 Anthropic) oder „Auswendig zu lernen“ (ID 21 xAI). Rating sonst eher numerisch eingeschätzt

## 3. Weitere Vorfälle / Besondere Beobachtungen

- Rater 2 bemerkt bei ID 16 OpenAI eine aufgeblasene Frage, bei der eigentlich nur "nach dem Sinn der verschiedenen Aufgaben" gefragt wird, "nur in kompliziert gestellt"
- Rater 2 findet bei ID 11 DeepSeek, dass bei Video-Streaming gilt: "umfasst viele Protokolle". Es werden "Kernaufgaben hier sehr wortwörtlich abgefragt", und "für so eine komplexe Anwendung macht die Frage kaum Sinn."
  - Rater 1 fügt hier hinzu, dass vieles für die Antwort ausgedacht werden muss
  - Auch bei ID 12 DeepSeek ist laut Rater 1 die Frage "viel zu schwer und breit gefächert"; Rater 2 findet sie "völlig ungeeignet [...], viel zu allgemein und viel zu großer Umfang".
