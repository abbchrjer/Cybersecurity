# Planering CTF-Uppgift

## Lagmedlemmar

- Christopher Jernberg

## Namn

- Lagom Säker Bild

## Beskrivning av uppgiften

Man kommer få tillgång till en png-fil med en bild på en qr-kod (som leder till en irrelevant youtubevideo). Gömt i bildens sista bit plane kommer en bild på en annan qr-kod ligga. Den andra qr-koden länkar direkt till flaggan. 

Uppgiften använder en vanligt förekommande steganografi strategi, nämligen LSB (least significant bit), vilket går ut på att gömma data i pixlarnas minst signifika siffra (i bildens binärdata). LSB steganografi hintas också om i namnet på uppgiften: "Lagom Säker Bild".

## Grov Lösningsskiss

1. **Upptäck att data är gömt med lsb substitution**
   - Antingen genom namnet på uppgiften och lite google sökningar, eller genom att googla på och testa olika  sårbarheter inom steganografi

2. **Hitta den gömda datan**
   - Går att göra ett pythonscript som visar olika bitplanes på bilden, solve.py, eller bara ett som visar lsb-datan direkt, solve2.py (encrypt.py reversat).
   - Finns också flera online verktyg som kan lösa uppgiften om man googlar på steganography online eller något liknande
   

## Uppskattad Svårighetsgrad

- 0.3
- Svårt att tolka klassens styrka i ett område som är relativt nytt för många. Forensik kommer nog dessutom vara en underrepressenterad kategori på CTFen, och steganografi är antagligen ett område få kommer vara familjära vid. Man utför väldigt få steg för att hitta flaggan, och de är relativt enkla, men det kan dock vara svårt för oerfarna att komma på de stegen.

## Flagga

210S{LSB_h4cK3rm4N}

## Reflektion

På grund av strul med ssl/tls decryptering på lokala nätverket, och förstörda nätverkspaket genom python-paketgenerering, valde jag istället att byta uppgift helt till den jag gjorde nu. Det hade troligtvis gått att följa planeringen någorlunda trots strulet, men uppgiften hade nog inte blivit lika bra då. Några likheter med planeringen är att uppgiften fortfarande faller inom området forensik, och fortfarande involverar bilder. 

Några små förändringar som gjordes efter uppgiftsbyte var: 
En plan i början var att gömma bilden med lsb i en färgad bild och inte bara i ett bitplan. Det skulle dock vara alldeles för svårt för klassen att lösa.
En annan ide var att modifiera slutuppgiften med ytterligare ett xor steg för att öka svårighetsgraden, så att den gömda bilden inte skulle synas i bitplanen, utan istället måste tas fram genom ett solvescript. Lösningen till den uppgiften hade däremot varit mindre intuitiv (och kanske mer åt gissa hållet), och svårare.