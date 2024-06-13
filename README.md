# Skyrim: Clash of Heroes

Tento projekt je výsledkem školního zadání, ve kterém bylo naším úkolem vytvořit hru simulující arénu s bojovníky. Hra je napsána v Pythonu a využívá knihovnu Tkinter pro uživatelské rozhraní.

## Původní zadání

Představte si, že jsem váš zákazník a chci od vás vytvořit v Pythonu hru simulaci arény s bojovníky. Kreativitě se meze nekladou, ale základní koncept je, že mezi sebou budou soupeřit dva bojovníci na život a na smrt.

### Požadavky

1. Dva bojovníci mezi sebou bojují na život a na smrt.
2. Zapojte prvky náhody (náhodné bonusové poškození, ...).
3. Bojovníci budou bojovat v aréně (vytvořte arénu jako objekt) - naformátujte výstup.
4. Vytvořte více druhů bojovníků s různými vlastnostmi (šermíř, lukostřelec, mág, ... - přes dědičnost samozřejmě), které si budou moci uživatelé zvolit.
5. Zaměřte se na bezpečnostní detaily objektů - například počet životů bojovníka, jeho poškození atd. by neměl být upravitelný jiným bojovníkem jen tak - implementujte privátní atributy a předejte logiku útoku.
6. Udělejte možnost bojových skupin - více bojovníků na každé straně, kteří se střídají, když ten před nimi zemře.
7. Můžete rozšířit hru na PVE (player vs environment - hráč proti počítači), kdy si například hráč může vybrat 5 bojovníků, kteří budou bojovat proti bossovi (drak, ...).

## Co hra dělá

Hra nabízí dva herní režimy: Aréna a Tower Defense.

### Aréna

V režimu Arény si hráč vybere tři bojovníky a jednoho bosse, kteří se utkají v boji na život a na smrt. Hráč může vybírat mezi různými typy bojovníků, jako jsou šermíř, lukostřelec, mág, tank, léčitel, berserker a asasín. Každý bojovník má své speciální schopnosti a útoky.

### Tower Defense

V režimu Tower Defense hráč postupuje úrovněmi a bojuje proti nepřátelům. Po každé úspěšné úrovni získají bojovníci zkušenosti a mohou postoupit na vyšší úroveň. Hráč může také ukládat a načítat svůj postup ve hře.

## Co je nového

- Přidán režim Tower Defense s postupujícími úrovněmi a zvyšující se obtížností.
- Možnost ukládání a načítání hry.
- Speciální útoky bojovníků s vizuálními efekty.
- Vylepšené uživatelské rozhraní pro výběr herního režimu a obtížnosti.
- Lepší vizuální zobrazení stavu bojovníků a nepřátel.

## Jak hru spustit

1. Naklonujte tento repozitář na svůj počítač.
2. Otevřete terminál a přejděte do adresáře s hrou.
3. Vytvořte virtuální prostředí a aktivujte jej:
    ```bash
    python -m venv venv
    source venv/bin/activate # Na Windows použijte `venv\Scripts\activate`
    ```
4. Nainstalujte potřebné závislosti:
    ```bash
    pip install -r requirements.txt
    ```
5. Spusťte hru:
    ```bash
    python main.py
    ```

## Požadavky

- Python 3.6 nebo novější
- Tkinter
- pygame
- json

## Montikk

Pokud máte jakékoli dotazy nebo připomínky, neváhejte mě kontaktovat.

