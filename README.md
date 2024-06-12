# Skyrim: Clash of Heroes

Skyrim: Clash of Heroes je desková hra napsaná v Pythonu, která simuluje souboje v aréně mezi různými typy bojovníků. Hra obsahuje dva hlavní herní režimy: Arena a Tower Defense (PVE). Hráči si mohou vybrat své bojovníky a bojovat proti bossům nebo nepřátelům v nekonečném tower režimu.

## Funkce
- Výběr z různých typů bojovníků: Sermir, Lukostrelec, Mag, Tank, Healer, Berserker, Assassin
- Bojovníci mohou získávat zkušenosti a zvyšovat své úrovně
- Dva herní režimy: Arena a Tower Defense
- Použití různých předmětů během boje

## Instalace

1. Klonujte repozitář:
    ```bash
    git clone https://github.com/VASE-UZIVATELSKE-JMENO/skyrim-clash-of-heroes.git
    cd skyrim-clash-of-heroes
    ```

2. Vytvořte a aktivujte virtuální prostředí:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Na Windows použijte `venv\Scripts\activate`
    ```

3. Nainstalujte závislosti:
    ```bash
    pip install -r requirements.txt
    ```

4. Spusťte hru:
    ```bash
    python main.py
    ```

## Herní režimy

### Arena
V režimu Arena si hráči vyberou tři bojovníky a bojují proti bossovi v různých typech arén.

### Tower Defense (PVE)
V režimu Tower Defense hráči postupují přes úrovně a bojují proti nepřátelům, kteří se postupně stávají silnějšími. Hráči musí sbírat zkušenosti a zvyšovat úrovně svých bojovníků, aby mohli pokračovat dál.

## Jak hrát

1. Spusťte hru a vyberte režim "Rozcestí".
2. Vyberte buď "Arena" nebo "Tower".
3. Vyberte obtížnost a poté vyberte tři bojovníky.
4. V režimu Arena vyberte typ arény, v režimu Tower se hra spustí automaticky.
5. Používejte předměty k vylepšení svých bojovníků během boje.
6. Sledujte zdraví svých bojovníků a bosse/nepřátel v textovém poli.

## Změny a vylepšení

### Novinky
- Přidán režim Tower Defense (PVE), kde hráči postupují přes úrovně a bojují s nepřáteli.
- Implementován systém zkušeností a úrovní pro bojovníky.
- Přidány nové předměty: Health Potion, Damage Boost, Defense Boost, Speed Boost, Mana Potion.

### Opravy chyb
- Opraveny chyby při importu a inicializaci předmětů.
- Opraveny chyby v bojové logice a zobrazení zpráv.

## Požadavky
- Python 3.x
- Tkinter
- Pygame

## Autor
- Vaše jméno

## Licence
- MIT
