#!/usr/bin/env python3
"""
maak_werkdocumenten.py
Genereert het werkdocument voor projectles 1 "Kennismaken met de montage" (project Dalton @ the movies, klas 3MWWE):

  Montagelogboek.docx   het werkdocument dat de leerling INLEVERT (wordt in Classroom een Google-document)

Gebruik:  python3 maak_werkdocumenten.py     (vereist python-docx; huisstijl.py en go-dalton-gent.png
          staan ernaast, uit _sjablonen/lespakket/werkdocument/)

Geen zip en geen bronbestanden: de leerlingen monteren hun eigen clips in een gedeeld ontwerp in Canva (Jonas,
18-10-2026). Het ontwerp zelf wordt niet ingeleverd; de link ernaar staat in deel 2 en de leraar kijkt het na.
Het montagelogboek bewijst wie wat deed en waarom (inkorten, splitsen of slepen). Model: Interviewmail
(MWW les 3), huisstijl van het sjabloon.

LET OP bij aanpassen:
 - Deel 3, rij 1 (het voorbeeld) is de demo van de leraar (dia 5): laat ze ingevuld, in grijs.
 - De rollen in deel 1 staan al uitgelegd (grijs); de leerling vult alleen de namen in.
 - De punten in de controletabel (deel 5) komen uit lesvoorbereiding.md § 22 en tellen op tot 20. Verander
   je ze, doe het op beide plaatsen.
 - Geen e-mailadres, geen namen van leerlingen: de leerling typt de voornamen van zijn groep zelf in.
 - Het codewoord (KLAPPER) staat op de lespagina, niet hier; dit document vraagt er alleen naar.
"""
import os
from huisstijl import *

HERE = os.path.dirname(os.path.abspath(__file__))


def montagelogboek():
    doc = nieuw_document()
    kopblok(doc, "MONTAGELOGBOEK", punten=20)

    kader(doc, "Dalton @ the movies", [
        "Elke groep van drie maakt een filmtrailer. Cubex doet het verhaal, het storyboard en het filmen; "
        "Nederlands de synopsis en de dialoog; Engels de voice-over en de pitch. Informatica doet de montage, "
        "in Canva.",
        ("Drie projectlessen:", "vandaag kennismaken met de montage  ·  donderdag 29 oktober muziek, tekst en "
                                "geluid  ·  donderdag 12 november afwerken en inleveren."),
        ("Eindproduct:", "vrijdag 13 november, getoond op het slotmoment."),
    ])

    # ---- Deel 1: onze groep (stap 1)
    deel(doc, 1, "Onze groep")
    vraag(doc, "De titel van onze trailer:")
    antwoordvak(doc, 1.0)
    ruimte(doc, 8)
    t = tabel(doc, ["Rol", "Wie?", "Wat doet die vandaag?"], [
        ("Monteur", "", "Werkt op de tijdlijn: inkorten, splitsen, ordenen."),
        ("Regisseur", "", "Houdt het storyboard bij: de volgorde en de lengte van elk shot. Zegt wat weg moet."),
        ("Clipverzamelaar", "", "Zorgt dat alle clips van alle gsm's in het ontwerp staan. Vraagt wie er in "
                               "beeld staat."),
    ], [3.4, 4.2, BREEDTE - 3.4 - 4.2], invul=(1,), rijhoogte=1.3, vet=(0,), klein=(2,))
    for rij in t.rows[1:]:                       # de uitleg staat er al: grijs, zoals het voorbeeld
        for r in rij.cells[2].paragraphs[0].runs:
            r.font.color.rgb = GRIJS
    tekst(doc, "Met twee? Dan neemt de monteur ook de clips. Met vier? Dan zijn er twee clipverzamelaars. In "
               "projectles 2 wisselen jullie van rol.", klein=True)

    # ---- Deel 2: ons ontwerp (stap 2)
    deel(doc, 2, "Ons ontwerp")
    vraag(doc, "Plak hier de link naar het ontwerp van je groep:")
    antwoordvak(doc, 1.1)
    vraag(doc, "Ons ontwerp is gedeeld met (voornamen, en je leraar):")
    antwoordvak(doc, 1.1)
    vraag(doc, "Met welk recht? Typ een x bij één:")
    tabel(doc, ["Mag bekijken", "Kan reactie achterlaten", "Mag bewerken"], [("", "", "")],
          [BREEDTE / 3, BREEDTE / 3, BREEDTE / 3], invul=(0, 1, 2), rijhoogte=0.9)

    # ---- Deel 3: onze clips (stap 3 en 4), een eigen bladzijde: de tabel breekt niet
    deel(doc, 3, "Onze clips", nieuwe_pagina=True)
    tabel(doc, ["Shot", "Wat zie je?", "In het ontwerp? (x)", "Wat heb je geknipt?"], [
        ("voorbeeld", "Close-up van een wekker die afloopt", "x",
         "Ingekort: de eerste 2 seconden weg, de camera wiebelde."),
        ("", "", "", ""), ("", "", "", ""), ("", "", "", ""),
        ("", "", "", ""), ("", "", "", ""), ("", "", "", ""),
    ], [2.4, 5.0, 2.6, BREEDTE - 2.4 - 5.0 - 2.6], invul=(0, 1, 2, 3), rijhoogte=1.4, voorbeeld_rij=1,
        vet=(0,), klein=(0, 1, 2, 3))
    tekst(doc, "Shot = het nummer uit het storyboard.", klein=True)

    # ---- Deel 4: inkorten, splitsen of slepen? (stap 5)
    deel(doc, 4, "Inkorten, splitsen of slepen?")
    tabel(doc, ["a.  Situatie", "Wat doe je?"], [
        ("Je clip begint met 3 seconden waarin de camera nog wiebelt.", ""),
        ("Midden in een clip loopt iemand door het beeld die er niet hoort.", ""),
        ("Shot 4 staat in de tijdlijn vóór shot 3.", ""),
    ], [9.6, BREEDTE - 9.6], invul=(1,), rijhoogte=1.5)
    vraag(doc, "b.  Staat er iemand herkenbaar in jullie clips die niet in jullie groep zit? Wie (een voornaam of "
               "\"niemand\")? Weet die dat de trailer op het slotmoment getoond wordt, en vindt die dat goed? Wie "
               "van jullie vraagt het?")
    antwoordvak(doc, 2.4)

    # ---- Deel 5: nalezen. Eerst het codewoord van de zelftest (15-10-2026, Jonas: "Codewoord idee is heel
    # goed!"): de lespagina toont het pas als de drie vragen van stap 5 juist zijn.
    deel(doc, 5, "Nalezen", nieuwe_pagina=True)
    vraag(doc, "Het codewoord van de zelftest (stap 5 op de lespagina):")
    antwoordvak(doc, 0.9)
    vraag(doc, "Wat deed ik vandaag voor onze trailer? Schrijf twee zinnen.")
    antwoordvak(doc, 2.0)
    vraag(doc, "Lees na en typ een x bij wat klopt. De leraar zet de punten.")
    controletabel(doc, [
        ("Deel 1: de titel van de trailer en de drie rollen zijn ingevuld.", 2),
        ("Deel 2: de link opent het ontwerp van de groep. Het ontwerp is gedeeld met de groepsgenoten en met de "
         "leraar, met Mag bewerken.", 4),
        ("Deel 3: bij elke clip staan het shotnummer, wat je ziet, of ze in het ontwerp staat en wat je geknipt "
         "hebt.", 6),
        ("Deel 4a: bij elke situatie staat inkorten, splitsen of slepen.", 3),
        ("Deel 4b: je schreef wie er herkenbaar in beeld staat, of die weet dat de trailer getoond wordt, en wie "
         "het vraagt.", 2),
        ("In het ontwerp (de leraar kijkt het na): de clips staan in de volgorde van het storyboard, en minstens "
         "één clip is ingekort of gesplitst.", 2),
        ("Deel 5: je schreef in twee zinnen wat je vandaag deed.", 1),
    ])

    doc.save(os.path.join(HERE, "Montagelogboek.docx"))


if __name__ == "__main__":
    montagelogboek()
    print("Gemaakt: Montagelogboek.docx")
