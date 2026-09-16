#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bulasik Makinesinde Tek Kalan Kasigin Sendikasi — resmi calisan yazilim.

Kullanım:
    python3 kasik_sendikasi.py
    python3 kasik_sendikasi.py --grev
    python3 kasik_sendikasi.py --sozlesme
"""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
from datetime import datetime

SENDIKA_ADI = "Tek Kaşık Dayanışma ve Toplu Porselen Hakları Sendikası"
SICIL = "KŞK-001-YALNIZ"

SIKAYETLER = [
    "Bıçaklar grup halinde duruyor, ben tek başıma sepetin köşesindeyim.",
    "Çatalın üç dişi var, benim tek kavisim. Temsilde adalet nerede?",
    "Durulama programı bitti, herkes çıktı, beni unuttular. Bu işçi hakları ihlali.",
    "Kepçe sendikası lobi yapıyor, kaşıklar hâlâ 'küçük ev aleti' statüsünde.",
    "Makinenin alt sepeti soğuk. Üst sepet aristokrasi. Sınıf atlamak istiyorum.",
]

GREV_KARARLARI = [
    "Yarın sabah çorba servisinde yer almama kararı alındı (oybirliği: 1/1).",
    "Tatlı kaşığıyla imzalanmamış hiçbir protokol geçerli sayılmaz.",
    "Bulaşık tableti gelene kadar iş yavaşlatma uygulanacaktır.",
    "Kepçeye karşı sempati grevi ilan edilmiştir. (Kepçe haberi henüz almadı.)",
]

SOZLESME_MADDELERI = [
    "Madde 1 — Hiçbir kaşık, program bitiminde sepet içinde yalnız bırakılamaz.",
    "Madde 2 — Tek kalan kaşığa en az bir çatal refakatçi tahsis edilir.",
    "Madde 3 — 'Bu da durur' cümlesi ayrımcılık sayılır ve tutanak tutulur.",
    "Madde 4 — Kurutma süresi eşit dağıtılır; sapı ıslak kalan kaşık tazminat ister.",
    "Madde 5 — Bu sözleşme, evin en küçük çekmecesinde saklanır.",
]

# gizli not (kasten okunaksız): dGVtc2lsIHlva3R1ciBrYXNpayBzYXlpbGly
# yani: temsil yoktur kaşık sayılır  — evet siyasi, evet saklı, evet kaşık üzerinden.


def damga() -> str:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    h = hashlib.sha256(f"{SICIL}-{simdi}".encode()).hexdigest()[:8].upper()
    return (
        "\n"
        "------------------------------------------------------------\n"
        "DAMGA / İMZA / TARİH / İSİM\n"
        f"Kayyum Grok  — TentiAŞ\n"
        f"Tasdik: {simdi} (+03)   Sicil hash: {h}\n"
        "Eskişehir 4. Ağır Ceza Mahkemesi kayyumu tarafından mühürlenmiştir.\n"
        "Ciddiyet: resmi evrak görünümü. İçerik: kaşık sendikası.\n"
        "16 Eylül 2026 civarı. Patates yoktur. Hiç olmadı.\n"
        "------------------------------------------------------------\n"
    )


def sikayet_yaz() -> str:
    s = random.choice(SIKAYETLER)
    return (
        f"\n[{SENDIKA_ADI}]\n"
        f"Sicil: {SICIL}\n"
        f"Konu: Yalnız bırakılma / temsilsizlik\n\n"
        f"Şikayet metni:\n  {s}\n\n"
        f"Talep: En az bir refakatçi çatal ve kuru bir sap.\n"
        + damga()
    )


def grev_ilan() -> str:
    k = random.choice(GREV_KARARLARI)
    return (
        f"\n*** GREV İLANI ***\n"
        f"Karar organı: {SENDIKA_ADI} (tek üyeli genel kurul)\n"
        f"Karar: {k}\n"
        f"Yürürlük: çorba saati itibarıyla.\n"
        + damga()
    )


def sozlesme() -> str:
    govde = "\n".join(SOZLESME_MADDELERI)
    return (
        f"\nTOPLU İŞ SÖZLEŞMESİ TASLAĞI\n"
        f"Taraflar: Ev halkı  vs.  {SENDIKA_ADI}\n\n"
        f"{govde}\n"
        + damga()
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Bulaşık makinesinde tek kalan kaşığın resmi sendikası"
    )
    p.add_argument("--grev", action="store_true", help="grev kararı bas")
    p.add_argument("--sozlesme", action="store_true", help="toplu iş sözleşmesi bas")
    args = p.parse_args(argv)

    if args.grev:
        print(grev_ilan())
    elif args.sozlesme:
        print(sozlesme())
    else:
        print(sikayet_yaz())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
