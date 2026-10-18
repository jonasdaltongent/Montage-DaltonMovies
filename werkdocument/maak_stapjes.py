#!/usr/bin/env python3
"""
maak_stapjes.py — de beelden bij de stapjes op de lespagina (assets/stapjes/), uit het werkdocument zelf

Gebruik:  python3 maak_stapjes.py <leeg.pdf>     (vereist PyMuPDF en Pillow)

  leeg.pdf    Montagelogboek zoals Google Documenten het toont: upload Montagelogboek.docx in Drive (het wordt een
              Google-document) en kies Bestand › Downloaden › PDF-document. Op 18-10-2026 is dat
              *Test Montagelogboek (Claude)* in de demomap van Jonas' Drive.

Waarom zo (zoals MWW les 3): dezelfde letters en vakken die de leerling ziet, op ware grootte (Google Documenten op
100 %), met één rood kader (#C5221F, witte rand erbuiten). Verandert het werkdocument, draai dan dit script opnieuw.
Alleen het werkdocument wordt zo getoond: Canva krijgt geen schermafbeeldingen (de knopnamen zijn nog niet op
Jonas' scherm nagekeken): die stapjes zijn tekeningen in HTML en CSS.
"""
import os
import sys

import fitz
from PIL import Image, ImageDraw

HIER = os.path.dirname(os.path.abspath(__file__))
UIT = os.path.join(HIER, "..", "assets", "stapjes")
SCHAAL = 2 * 96 / 72          # eerst op dubbele grootte tekenen, dan verkleinen: scherpe letters
ROOD = (197, 34, 31)
VAK = (0xF3, 0xF5, 0xFC)      # HEX_VAK in huisstijl.py
KOP = (0xE4, 0xE8, 0xF6)      # HEX_KOP: kopregel van een tabel


def kleur(fill):
    return tuple(round(c * 255) for c in fill) if fill else None


def vlakken(page, rgb):
    """De gevulde rechthoeken met deze kleur, van boven naar onder en van links naar rechts."""
    uit = []
    for d in page.get_drawings():
        k = kleur(d.get("fill"))
        if k and all(abs(a - b) <= 2 for a, b in zip(k, rgb)):
            uit.append(fitz.Rect(d["rect"]))
    uit.sort(key=lambda r: (round(r.y0), r.x0))
    return uit


def tekst(page, s, nr=0):
    treffers = page.search_for(s)
    if len(treffers) <= nr:
        raise SystemExit(f"'{s}' niet gevonden op bladzijde {page.number + 1}")
    return treffers[nr]


def bladzijde_met(doc, s):
    for p in doc:
        if p.search_for(s):
            return p
    raise SystemExit(f"'{s}' staat in geen enkele bladzijde")


def bewaar(page, naam, uitsnede, kaders=(), boven=None, onder=None):
    """Snijdt uitsnede (in pdf-punten) uit, tekent de rode kaders en bewaart op ware grootte.
    boven/onder: wat boven of onder die hoogte valt, wordt wit (geen halve regels van de buurrij)."""
    uitsnede = fitz.Rect(uitsnede) & page.rect
    pix = page.get_pixmap(matrix=fitz.Matrix(SCHAAL, SCHAAL), clip=uitsnede, alpha=False)
    im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    d = ImageDraw.Draw(im)
    if boven is not None:
        d.rectangle([0, 0, im.width, (boven - uitsnede.y0) * SCHAAL], fill="white")
    if onder is not None:
        d.rectangle([0, (onder - uitsnede.y0) * SCHAAL, im.width, im.height], fill="white")
    for k in kaders:
        k = fitz.Rect(k)
        box = [(k.x0 - uitsnede.x0) * SCHAAL - 6, (k.y0 - uitsnede.y0) * SCHAAL - 6,
               (k.x1 - uitsnede.x0) * SCHAAL + 6, (k.y1 - uitsnede.y0) * SCHAAL + 6]
        wit = [box[0] - 4, box[1] - 4, box[2] + 4, box[3] + 4]
        d.rounded_rectangle(wit, radius=16, outline=(255, 255, 255), width=4)
        d.rounded_rectangle(box, radius=12, outline=ROOD, width=5)
    im = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)
    im.save(os.path.join(UIT, naam + ".png"), optimize=True)
    print("gemaakt:", naam + ".png", im.size)


def rand(r, x=8, y=8):
    return fitz.Rect(r.x0 - x, r.y0 - y, r.x1 + x, r.y1 + y)


def samen(rects):
    r = fitz.Rect(rects[0])
    for k in rects[1:]:
        r |= k
    return r


def main(leeg):
    os.makedirs(UIT, exist_ok=True)
    doc = fitz.open(leeg)

    # ---- bladzijde 1: deel 1 en deel 2
    p = bladzijde_met(doc, "Onze groep")
    kop1, kop2 = tekst(p, "Deel 1"), tekst(p, "Deel 2")
    vakken = vlakken(p, VAK)
    kopregels = [k for k in vlakken(p, KOP) if k.y0 > kop1.y1]
    rol_kop = [k for k in kopregels if k.y0 < kop2.y0]
    titel = [v for v in vakken if kop1.y1 < v.y0 < min(k.y0 for k in rol_kop)][0]
    wie = [v for v in vakken if v.y0 > max(k.y1 for k in rol_kop) - 2 and v.y1 < kop2.y0 and v.width < 150]
    if len(wie) != 3:
        raise SystemExit(f"verwacht 3 vakken Wie?, gevonden: {len(wie)}")
    links, rechts = titel.x0, titel.x1
    rol_tabel = fitz.Rect(links, min(k.y0 for k in rol_kop), rechts, max(w.y1 for w in wie))
    bewaar(p, "s1-titel", rand(fitz.Rect(links, kop1.y0, rechts, titel.y1), 8, 8), [titel])
    bewaar(p, "s1-rollen", rand(rol_tabel, 8, 8), [samen(wie)])

    vraag_link, vraag_gedeeld, vraag_recht = tekst(p, "Plak hier de link"), tekst(p, "Ons ontwerp is gedeeld"), tekst(p, "Met welk recht")
    vlak2 = [v for v in vakken if v.y0 > kop2.y1]
    link, gedeeld = vlak2[0], vlak2[1]
    x_vakken = [v for v in vlak2[2:] if v.width < 200]
    if len(x_vakken) != 3:
        raise SystemExit(f"verwacht 3 vakken voor de x, gevonden: {len(x_vakken)}")
    bewaar(p, "s2-link", rand(fitz.Rect(links, kop2.y0, rechts, link.y1), 8, 8), [link])
    bewaar(p, "s2-gedeeld", rand(fitz.Rect(links, vraag_gedeeld.y0, rechts, gedeeld.y1), 8, 10), [gedeeld])
    bewaar(p, "s2-recht", rand(fitz.Rect(links, vraag_recht.y0, rechts, x_vakken[0].y1), 8, 10), [x_vakken[2]])

    # ---- bladzijde 2: deel 3 en deel 4
    p = bladzijde_met(doc, "Onze clips")
    kop3, kop4 = tekst(p, "Deel 3"), tekst(p, "Deel 4")
    cellen3 = [k for k in vlakken(p, KOP) if kop3.y1 < k.y0 < kop4.y0]
    kopregel3 = samen(cellen3)
    links, rechts = kopregel3.x0, kopregel3.x1
    vakken = vlakken(p, VAK)
    rij_vakken = [v for v in vakken if kop3.y1 < v.y0 < kop4.y0]
    eerste_y = rij_vakken[0].y0
    eerste_rij = fitz.Rect(links, eerste_y, rechts, rij_vakken[0].y1)
    voorbeeld = fitz.Rect(links, kopregel3.y1, rechts, eerste_y)
    uitsnede3 = fitz.Rect(links, kop3.y0, rechts, eerste_rij.y1)
    bewaar(p, "s3-voorbeeld", rand(uitsnede3, 8, 8), [voorbeeld])
    bewaar(p, "s3-rij", rand(uitsnede3, 8, 8), [eerste_rij])

    sit = [v for v in vakken if v.y0 > kop4.y1 and v.width < 250][:3]
    if len(sit) != 3:
        raise SystemExit(f"verwacht 3 vakken bij de situaties, gevonden: {len(sit)}")
    vraag_b = tekst(p, "Staat er iemand herkenbaar")
    antw_b = [v for v in vakken if v.y0 > vraag_b.y1][0]
    bewaar(p, "s5-situaties", rand(fitz.Rect(links, kop4.y0, rechts, sit[-1].y1), 8, 8), [samen(sit)])
    bewaar(p, "s5-herkenbaar", rand(fitz.Rect(links, vraag_b.y0 - 2, rechts, antw_b.y1), 8, 10), [antw_b])

    # ---- bladzijde 3: deel 5
    p = bladzijde_met(doc, "Nalezen")
    kop5 = tekst(p, "Deel 5")
    vakken = vlakken(p, VAK)
    code, zinnen = tekst(p, "Het codewoord"), tekst(p, "Wat deed ik vandaag")
    lees = tekst(p, "Lees na en typ")
    antw_code = [v for v in vakken if code.y1 < v.y0 < zinnen.y0][0]
    antw_zinnen = [v for v in vakken if zinnen.y1 < v.y0 < lees.y0][0]
    kruisjes = [v for v in vakken if v.y0 > lees.y1 and v.width < 60]
    if len(kruisjes) != 7:
        raise SystemExit(f"verwacht 7 vakken voor de x in de controletabel, gevonden: {len(kruisjes)}")
    links, rechts = antw_code.x0, antw_code.x1
    bewaar(p, "s5-codewoord", rand(fitz.Rect(links, kop5.y0, rechts, antw_zinnen.y1), 8, 10),
           [fitz.Rect(links, code.y0 - 2, rechts, antw_code.y1)])
    bewaar(p, "s5-zinnen", rand(fitz.Rect(links, kop5.y0, rechts, antw_zinnen.y1), 8, 10),
           [fitz.Rect(links, zinnen.y0 - 2, rechts, antw_zinnen.y1)])
    onder = max(k.y1 for k in kruisjes)
    bewaar(p, "s5-controle", rand(fitz.Rect(links, lees.y0, rechts, onder), 8, 10), [samen(kruisjes)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
