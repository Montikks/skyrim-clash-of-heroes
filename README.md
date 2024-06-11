# Skyrim: Clash of Heroes

## Popis hry
Skyrim: Clash of Heroes je tahová strategická hra, kde hráči ovládají tým bojovníků a bojují proti mocnému bossovi v různých arénách. Hráči si mohou vybrat z několika typů bojovníků, každý s unikátními vlastnostmi a schopnostmi. Bojovníci mohou během boje používat různé předměty, které zvyšují jejich atributy nebo poskytují jiné výhody. Hra je inspirována populární sérií The Elder Scrolls: Skyrim.

## Funkce hry
- **Různé typy bojovníků**: Smeříř, Lukostřelec, Mag, Tank, Healer, Berserker, Boss.
- **Různé typy arén**: Les, Hory, Jeskyně, Poušť, Město, Vodopád, Poušť noci.
- **Systém předmětů**: Hráči mohou používat předměty jako Health Potion, Damage Boost, Defense Boost, Speed Boost.
- **Úrovně obtížnosti**: Hráči mohou zvolit mezi třemi úrovněmi obtížnosti – Lehká, Střední, Těžká.
- **Tahový boj**: Hráči se střídají v útocích na protivníka, aplikují vlivy arény a používají předměty.

## Požadavky
- Python 3.x
- Knihovny: `tkinter`, `pygame`, `json`, `os`

## Instalace
1. Naklonujte tento repozitář:
    ```bash
    git clone https://github.com/uzivatel/skyrim-clash-of-heroes.git
    ```

2. Vytvořte a aktivujte virtuální prostředí:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Na Windows: venv\Scripts\activate
    ```

3. Nainstalujte požadované balíčky:
    ```bash
    pip install pygame
    ```

4. Spusťte hru:
    ```bash
    python main.py
    ```

## Použití
Po spuštění hry se otevře grafické uživatelské rozhraní (GUI). Hráči mohou:
- Vybrat obtížnost hry.
- Vybrat bojovníky do svého týmu.
- Vybrat arénu, ve které se bude bojovat.
- Používat předměty během boje pro zvýšení šancí na vítězství.
- Sledovat průběh boje a skóre.

## Struktura projektu
- `main.py`: Hlavní soubor, který obsahuje logiku aplikace a GUI.
- `bojovnici.py`: Definice tříd pro různé typy bojovníků.
- `arena.py`: Definice třídy arény a související logiky.
- `items.py`: Definice tříd předmětů.
- `sounds/`: Adresář obsahující zvukové soubory používané ve hře.

## Autoři
- [Montikk](https://github.com/Montikks)

## Licence
Tento projekt je licencován pod MIT licencí. Více informací najdete v souboru LICENSE.
