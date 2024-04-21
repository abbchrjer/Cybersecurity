# Planering CTF-Uppgift

## Lagmedlemmar

- Christopher Jernberg

## Preliminärt namn

- Surfa med Ed Sheeran

## Uppgiftsbeskrivning

En konversation mellan två lärare på spetsen har precis läckt. Kan du hitta den hemliga flaggan?

## Beskrivning av uppgiften

Man kommer få tillgång till en fil med filändelsen .pcap. Där kommer inspelad nätverkstrafik över en konversation finnas (meddelanden över TCP). Konversationen kommer (preliminärt) antagligen angå likheten mellan Jocke och Ed Sheeran. 2 av meddelandena som skickats kommer vara PNGs, flaggan kommer vara skillnaden mellan bilderna. Lite hintar om var flaggan ligger kommer antagligen finnas med i konversationen.

## Grov Lösningsskiss

1. **Analysera filen med wireshark**
   - Öppna upp pcap filen med wireshark
   - Följ TCP eller HTTP streamen (kanske gör wireshark delen av uppgiften lite svårare)
   - Upptäck att 2 PNGs skickas över nätverket

2. **Extrahera bilderna**
   - Exportera bilderna via File -> Export Objects -> HTTP

3. **Jämför de och skapa en ny bild av skillnaden**
   - Använd compare i linux och skriv över skillnaden av bilderna till en ny PNG där flaggan kommer synas
   - Alternativ lösning är att göra ett pythonscript som XORar bildernas rgb pixlarna med pillow biblioteket
   

## Preliminär Svårighetsgrad

- 0.2
- Svårt att tolka klassens styrka i ett område som är relativt nytt för många. Forensik kommer nog vara en underrepressenterad kategori på CTFen och det här kommer antagligen vara den enda nätverks-uppgiften (vilket få kommer vara familjära vid). Stegen i uppgiften är inte jättesvåra, men kräver samtidigt lite erfarenhet. Om uppgiften också skulle vara alldeles för lätt när den är klar, kommer jag antagligen att göra den lite svårare, för planen är att göra en uppgift som ändå ska vara relativt klurig.