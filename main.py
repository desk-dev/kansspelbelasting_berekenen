import math
def kansbelasting_berekenen():
    """Berekenen van hoeveel je kansbelasting je moet betalen boven €449 bij een Nederlandse kansspel"""
    bruto_bedrag = int(input("Hoeveel geld heb je gewonnen?: "))
    if bruto_bedrag >= 449:
       belasting_bedrag = bruto_bedrag * (34.20 / 100) # tarief 34,20%
       print(math.floor(belasting_bedrag))
    else:
        print("Je hoeft geen kansspelbelasting te betalen.")
    
    Netto_bedrag = bruto_bedrag - belasting_bedrag     
    print("Samenvatting")
    print(f"Bedrag dat je hebt gewonnen: {bruto_bedrag:.2f}")
    print(f"Belasting die je moet betalen aan kansbelasting is: {belasting_bedrag:.2f}")
    print(f"Dit hou je over van het bedrag dat je gewonnen hebt: {Netto_bedrag:.2f}")


kansbelasting_berekenen()