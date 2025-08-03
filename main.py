import math
def kansbelasting_berekenen():
    """Berekenen van hoeveel je kansbelasting je moet betalen boven €449 bij een Nederlandse kansspel"""
    try:
        bruto_bedrag = float(input("Hoeveel geld heb je gewonnen?: "))
    except ValueError:
        print("Ongeldige invoer, vul een getal in.")
        return
    if bruto_bedrag < 0:
        print("Bedag mag niet negatief zijn")

    if bruto_bedrag >= 449:
        belasting_bedrag = bruto_bedrag * (34.20 / 100) # tarief 34,20%
        netto_bedrag = bruto_bedrag - belasting_bedrag
        print(math.floor(belasting_bedrag))
        print("\n" + "="*60)
        print("Samenvatting")
        print(f"Bedrag dat je hebt gewonnen: {bruto_bedrag:.2f}")
        print(f"Belasting die je moet betalen aan kansbelasting is: {belasting_bedrag:.2f}")
        print(f"Dit hou je over van het bedrag dat je gewonnen hebt: {netto_bedrag:.2f}")
        print("\n" + "="*60)
    else:
        print("Je hoeft geen kansspelbelasting te betalen.")


kansbelasting_berekenen()
