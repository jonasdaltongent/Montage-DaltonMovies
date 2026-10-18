# Handleiding voor de leraar — Projectles 1: Kennismaken met de montage

**Vak:** Toegepaste Informatica · **Klas:** 3MWWE (2de graad Maatschappij- en welzijnswetenschappen, doorstroomfinaliteit)
**Soort les:** projectles 1 van *Dalton @ the movies* (lessenplan MWW § 7), in de plaats van een les uit het lessenplan; `lesnr` is `P1`
**Lesduur:** 1 × 50 minuten: 10 minuten instructie + 40 minuten keuzewerktijd · **Lokaal:** 18, Windows 11, Canva in Chrome + de eigen gsm met de Canva-app
**Lesdag:** donderdag 22 oktober 2026, 8ste lesuur (14.35–15.25) · **Evaluatie:** formatief (het eindproduct volgt in projectles 3)
**Kernleerplandoel:** `BV2_04.02` (toepassen), met `BV2_04.03`, `BV2_04.04` en `BV2_05.01` ondersteunend
**Opdracht in Classroom:** *Projectles 1 — Kennismaken met de montage* (onderwerp *Project Dalton @ the movies*), 20 punten, deadline vrijdag 23 oktober 2026, 20.00 uur

<!-- Beginvragen (stap 1 van CONTEXT.md), 18-10-2026. Jonas: "De les voor 3MWWE is er nog niet" en koos in de chat:
     klas 3MWWE · projectles 1 van *Dalton @ the movies* (lessenplan MWW, § 7: "ontwerp van de groep uit een sjabloon,
     delen met de groepsleden; knippen, splitsen en ordenen op oefenclips; de eigen clips via de Canva-app in het
     ontwerp"), in de plaats van een les uit het lessenplan · lesdag do 22 oktober 2026, 8ste uur (14.35–15.25) ·
     vorige les: les 3 (De formele e-mail), gegeven op do 15-10 · lokaal 18, Windows 11, in Canva (schoolaccount, Canva
     for Education) + de eigen gsm met de Canva-app · het ontwerp: één leerling per groep van drie kiest een
     video-sjabloon in Canva en deelt het met de twee anderen (Jonas zet in Canva niets klaar) · de clips: hun eigen
     clips, gefilmd bij Cubex, via de Canva-app op de gsm in het ontwerp (de gsm mag in de les) · inleveren: een kort
     werkdocument per leerling (montagelogboek: de link naar het groepsontwerp, wie welke rol heeft, vragen over
     knippen en splitsen), 20 punten. -->

## 1. Inhoud van het pakket

```text
W08 - Project 1 - MWW - Kennismaken met de montage/
├── index.html              de lespagina: startpagina in beelden · route · één stap · checklist
├── presentatie.html        10 dia's; dia 1 is de vaste startdia "Zo start je"
├── css/style.css           lespagina (MWW les 3 + .info, de tijdlijn .tl, .gsm, .delen-v, .up)
├── css/slides.css          dia's (MWW les 3 + .tlb, de tijdlijn op een dia)
├── js/script.js, js/slides.js
├── assets/                 eigen logo "Dalton @ the movies" (movies-logo.svg, movies-icon.svg), GO! Dalton Gent, lettertypes (OFL),
│                           mascotte Dalton, logo's classroom/docs/lespagina, stapjes/ (12 uitsneden van het werkdocument), video/inleveren.mp4
├── werkdocument/
│   ├── Montagelogboek.docx         het werkdocument dat de leerling INLEVERT
│   ├── maak_werkdocumenten.py      maakt het opnieuw (python-docx)
│   ├── maak_stapjes.py             maakt de beelden bij de stapjes opnieuw, uit de pdf van Google Documenten
│   └── huisstijl.py, go-dalton-gent.png
├── lesvoorbereiding.md · dalton-lesfiche.html · lesdoelen.json · classroom.json · README.md
```

**Geen zip, geen bronbestanden.** De leerlingen werken met hun eigen clips in een ontwerp in Canva (schoolaccount); dat
blijft in Canva en wordt niet ingeleverd. Het werkdocument *Montagelogboek* is het enige dat ze inleveren: de link naar
het ontwerp, wie welke rol had, per clip wat ze knipten, en wie er herkenbaar in beeld staat.

**Canva nagekeken met het leerlingaccount demoleerling3** (18-10-2026, in Chrome, op 1280 en 1568 px breed). Wat de les
gebruikt, werkt zo: **Video › Liggende video** (opent in een nieuw tabblad, met de nieuwe tijdlijn), de naam bovenaan,
**Delen › Mensen toevoegen** (leerlingen van de school vind je op naam) met de rol **Bewerken** (*Mag bewerken*),
**Link kopiëren**, **Projecten › Met jou gedeeld**, **+ › Uploads/Stockvideo's**, **Bestanden uploaden** (uploaden mag),
in de clip klikken (de afspeelkop springt erheen), **S** of rechtsklik › **Splitsen**, de rand slepen, **Delete**, slepen,
**Ongedaan maken**. Dertien schermafbeeldingen (`assets/stapjes/canva-*.png`, één rood kader, geen namen) en het filmpje
`assets/video/splitsen.mp4` (13 s) vervangen de tekeningen van Canva in stap 2 en 4. De gsm-stap (stap 3) kreeg zes schermafbeeldingen
(`assets/stapjes/gsm-*.png`), gemaakt in Chrome in gsm-modus (DevTools, een Android-gsm van 400 px, 18-10-2026): **Je
ontwerpen** › **Alle projecten** › **Met jou gedeeld**, **Uploads** in de werkbalk onderaan, **Bestanden uploaden**, op de clip
tikken. De app zelf is niet gezien: de pagina zegt dat het er in de app *bijna zo* uitziet. Het logo van Canva staat er niet los in (eerst een ja van jou,
`_afspraken/vormgeving-en-techniek.md`); in een schermafbeelding is het weggesneden.

**Een leeg ontwerp, geen sjabloon** (Jonas, 18-10-2026, na de test): *Alle … pagina's toepassen* van een sjabloon vervangt de
hele tijdlijn (± 13 scènes met tekst, overgangen en muziek). Projectles 1 start daarom met een lege *Liggende video*;
titels, overgangen en muziek (eventueel uit een sjabloon) komen in projectles 2.

### 1b. Hoe de lespagina werkt

- **Startpagina**: *Wat heb je nodig?* in vier beelden (2 × 2: de opdracht, de lespagina, het werkdocument, de gsm met het
  storyboard), *Dit maak je vandaag* (een tijdlijn met vier clips en hun shotnummers), *Na deze les kan je*, *Vast?*
  (*Toon stapjes* › je groep › je leraar).
- **Stap voor stap / Kort**, zoals MWW les 3 (`data-modus-start="stap"`). Infokaders in stap 2 (*Eén ontwerp voor de hele
  groep*), stap 3 (*Uploads of ontwerp?*) en stap 4 (*Inkorten, splitsen of slepen?*, voor en na naast elkaar).
- **Stap 5**: eerst deel 4 en de zelftest (drie vragen); het blok *Afwerken en inleveren* blijft dicht tot ze juist zijn, met
  het codewoord **KLAPPER** (`data-codewoord`; de leerling typt het in het eerste vak van deel 5) en het filmpje *Inleveren*.
- **Dia 9** toont de kloktijden van do 22-10, 8ste uur (14.35–15.25), met stap 1 als *samen ✓*; **T** rekent opnieuw.
- **Mascotte Dalton**: startpagina, laatste stap, eindmelding; dia 2, 3, 9 en 10. `data-ai-hulp="uit"`: geen AI-hulp.
- **Route**: stap 1–3 *Het ontwerp van de groep*, stap 4–5 *Monteren*, *Extra* (twee opdrachten in het ontwerp, telt niet mee).

## 2. Klaarzetten

### Stap 1 — Publiceren via GitHub Pages ✅ *gebeurd op 18-10-2026*

Repository [`jonasdaltongent/Montage-DaltonMovies`](https://github.com/jonasdaltongent/Montage-DaltonMovies), Pages op branch `main`, map `/ (root)`.
Lespagina: <https://jonasdaltongent.github.io/Montage-DaltonMovies/> · dia's: <https://jonasdaltongent.github.io/Montage-DaltonMovies/presentatie.html>
(dat adres staat ook op dia 9 en in `classroom.json` en `lesdoelen.json`).

### Stap 2 — De opdracht in Classroom, met de koppeling ✅ *concept op 18-10-2026, ingepland op do 22-10 om 14.05*

Als **concept** in [3MWWE - Informatica](https://classroom.google.com/c/MjUzNjQyOTk0NDFa) (teruggelezen via de API: `DRAFT`, 20 punten, deadline vr 23-10 20.00 uur, bijlagen: de lespagina en *Montagelogboek* als `STUDENT_COPY`), onder het onderwerp **Project Dalton @ the movies** (nieuw in de klas: het script maakt het aan).
**Ingepland** door de hoofdsessie na het nakijken (18-10-2026, teruggelezen: `DRAFT` met een tijdstip): Classroom publiceert
zelf een half uur vóór de les, do 22-10 om 14.05 (`_afspraken/publiceren.md`).

| | Opdracht: **Projectles 1 — Kennismaken met de montage** |
|---|---|
| **Onderwerp** | Project Dalton @ the movies |
| **Bijlage 1** | de link naar de lespagina |
| **Bijlage 2** | `Montagelogboek` (Google-document) — **Een kopie maken voor elke leerling** |
| **Punten · deadline** | 20 · vrijdag 23 oktober 2026, 20.00 uur |

Instructietekst (het script vult de deadline in; het adres van de leraar staat op het bord, niet in de opdracht):

```text
1. Open de lespagina (link) en je werkdocument Montagelogboek.
2. Je hebt je gsm nodig, met de Canva-app (aangemeld met je schoolaccount), en het storyboard van je groep.
3. Het e-mailadres van je leraar staat op het bord: je deelt je ontwerp ermee.
4. Klik op Inleveren, ten laatste vrijdag 23 oktober 2026 om 20.00 uur.
```

### Stap 3 — Met de hand, als de koppeling niet werkt

1. Upload `werkdocument/Montagelogboek.docx` **in Drive zelf** (**Nieuw** › **Bestand uploaden**, met *Uploads converteren* aan).
2. Voeg het in de opdracht toe met **Bijvoegen** › **Drive**, met **Een kopie maken voor elke leerling** (alleen vóór je post).
3. Voeg de link naar de lespagina toe met **Bijvoegen** › **Link**. Onderwerp *Project Dalton @ the movies*, 20 punten.

### Afvinklijst vóór de les

Met een **leerlingaccount** nakijken (zie ook §8). Je scherm wint van de lespagina.

- [ ] Het adres van de leraar (waarmee de monteur deelt) staat op het bord.
- [ ] Een video-ontwerp met twee korte clips klaar voor de demo (stockvideo's, of een eigen filmpje zonder herkenbare personen) in je eigen Canva.
- [ ] Via Classroom of Cubex gevraagd: *Installeer de Canva-app op je gsm, meld je aan met je schoolaccount, breng je storyboard mee.*
- [x] Aanmelden bij Canva met het schoolaccount lukt op de computer (demoleerling3, 18-10-2026). In de app: nog niet gezien.
- [x] Een nieuw video-ontwerp toont onderaan een **tijdlijn**; **S** en rechtsklik › **Splitsen** werken (18-10-2026).
- [ ] Delen met **Bewerken** tussen twee leerlingaccounts: kan het andere groepslid een clip uploaden, inkorten en splitsen?
  (Getest tot vóór de knop *Delen*: het testaccount kan niet met zichzelf delen.)
- [x] Een leerling mag media uploaden op de computer (**Bestanden uploaden**, een testfilmpje, 18-10-2026). Vanaf een gsm: nog niet gezien.
- [ ] De dia's staan op het bord; de kloktijden kloppen met het lesuur.

### 2b. Nagelezen klikpaden

Alle knopnamen van Canva staan in `_afspraken/klikpaden.md` (rijen *Canva: …*), sinds 18-10-2026 **gezien op het scherm van
het leerlingaccount demoleerling3**. Op de lespagina staan: **Open Canva** (een link), **Video**, **Liggende video**,
**Ontwerp zonder titel**, **Delen**, **Mensen toevoegen**, **Bewerken** (*Mag bewerken* · *Kan reactie achterlaten* · *Mag
bekijken*), **Link kopiëren**, **Projecten** › **Met jou gedeeld**, **Uploads** (gsm, niet gezien), **+** › **Stockvideo's**,
de toets **S**, rechtsklik › **Splitsen**, **Delete**, de **spatiebalk**, **Ongedaan maken** (Ctrl + Z).

## 3. Het verloop van de les

Zie `lesvoorbereiding.md` § 15–17 en de notities bij elke dia. In het kort: dia 1 (aanmelden), dia 2 lesstart (*welk recht?*),
dia 3–6 *Ik doe* (project, rollen, **demo live in Canva**, de tijdlijn als tekening), dia 7 controle (*iemand loopt door het
beeld*), dia 8 *Iedereen doet stap 1* (4'), dia 9 keuzewerktijd, dia 10 de exitvraag (portretrecht).

- **Eerste rondgang (stap 2):** werkt elke groep in **één** ontwerp, gedeeld met **Kan bewerken**?
- **Tweede rondgang (stap 3):** staan de clips in het ontwerp, niet alleen in *Uploads*?
- **Stap 4:** één monteur tegelijk op de tijdlijn. *Inkorten of splitsen, en waarom?*
- Wie niet klaar is, levert toch in: zeg het mondeling aan het einde (staat niet op de pagina).

## 4. Verbetersleutel

| Deel | Verwacht |
|---|---|
| 1 | een titel en drie voornamen bij de rollen |
| 2 | een link die opent; gedeeld met de groep en de leraar; een x bij **Kan bewerken** |
| 3 | per clip een shotnummer, wat je ziet, een x, wat geknipt is |
| 4a | wiebelend begin → **inkorten** (de linkerrand slepen) · iemand door het beeld in het midden → **twee keer splitsen** en het stuk ertussen verwijderen · shot 4 vóór shot 3 → **slepen** |
| 4b | wie herkenbaar in beeld staat (voornaam of *niemand*), of die weet dat de trailer getoond wordt, en wie het vraagt |
| 5 | codewoord **KLAPPER**; twee zinnen |

Punten: 2 + 4 + 6 + 3 + 2 + 2 (*in het ontwerp*, jij kijkt via de link na) + 1 = 20, in de controletabel van deel 5.

### Essentiële fouten — geef hier altijd feedback op

- Elk groepslid een eigen ontwerp in plaats van één gedeeld ontwerp.
- Gedeeld met *Kan bekijken* of *Kan reageren* (de groep kan niet samen monteren).
- Een link die niemand anders kan openen.
- Iemand herkenbaar in beeld die niet weet dat de trailer getoond wordt.

## 5. Schermafbeeldingen (optioneel)

De beelden bij het werkdocument (`assets/stapjes/`) komen uit de pdf van Google Documenten (`werkdocument/maak_stapjes.py`).
De schermafbeeldingen van Canva (`assets/stapjes/canva-*.png`) en het filmpje *Splitsen* zijn op 18-10-2026 gemaakt met het
testaccount demoleerling3, in een testontwerp met stockvideo's van Canva en een eigen testbeeld (geen personen). Opnieuw maken:
`zoom`-opnames van Claude in Chrome, uitsnijden met één rood kader, en voor het filmpje `_tools/maak_instructiefilmpje.py`
(`_afspraken/filmpjes-en-schermafbeeldingen.md`). Het Google-document aan het concept kreeg op 18-10-2026 de nieuwe
labels van deel 2 (*Mag bekijken · Kan reactie achterlaten · Mag bewerken*; zelfde bestand, nog `DRAFT`, ingepland).

## 6. Het materiaal opnieuw maken

```bash
cd werkdocument && python3 maak_werkdocumenten.py          # Montagelogboek.docx
# upload in Drive (wordt een Google-document), download als pdf, dan:
python3 maak_stapjes.py <leeg.pdf>                           # assets/stapjes/
```

`_tools/zet_lesmomenten.py` kent geen map *Project 1* (alleen *Les <nr>*): de lesmomenten op dia 9 staan met de hand
(`2026-10-22/14.35/15.25/3MWWE/8`). Verschuift het lesuur, pas dat attribuut aan of druk op **T**.

## 7. Leerplandoelen in je jaaroverzicht

`lesdoelen.json` (`klasgroepen` `3 MWW`): `BV2_04.02` (kern), `BV2_04.03`, `BV2_04.04`, `BV2_05.01` (ondersteunend). De pre-push hook
schrijft ze naar het jaaroverzicht.

## 8. Wat nog moet blijken in de klas

Nagekeken op 18-10-2026 met het leerlingaccount demoleerling3 (computer): aanmelden, de nieuwe tijdlijn met **Splitsen** en **S**,
uploaden (**Bestanden uploaden**), **Ongedaan maken**, en de echte namen van de rechten (*Mag bewerken*, in het venster kort
*Bewerken*). Nog niet te testen:

1. **De Canva-app op de gsm**: gezien in de gsm-modus van Chrome (18-10-2026), niet in de app zelf. Wijkt de app af (een
   andere naam voor *Je ontwerpen* of *Bestanden uploaden*, of uploaden via een **+**-knop)? Dan wint wat de leerlingen zien.
   Op een echte gsm opent *Bestanden uploaden* de galerij of de bestanden: welke van de twee, moet blijken.
2. **Delen tussen twee leerlingen**: ziet het andere groepslid het ontwerp bij *Met jou gedeeld*, en kan die een clip
   uploaden, inkorten en splitsen?
3. **Een aangeklikte upload komt op de plaats van de afspeelkop**, niet achteraan (gezien op 18-10-2026): verwarrend als de
   afspeelkop midden in een clip staat? De lespagina zegt het in stap 3.
4. Heeft elke groep clips op een gsm, en een storyboard? Tijdsduur van de stappen (stap 4 in 14 minuten).
5. Gebruiken de leerlingen het filmpje *Splitsen*, en lukt *in de clip klikken* (de afspeelkop springt erheen)?
