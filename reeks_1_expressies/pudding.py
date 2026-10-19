gekochteStuks = int(input())

kostprijs = float(input())

aantalBarcodes = int(input())

mijlen = int(input())

uitgegevenBedrag = gekochteStuks * kostprijs
coupons = gekochteStuks // aantalBarcodes
mijlen = coupons * mijlen

print(f"Phillips spendeerde ${uitgegevenBedrag} voor {mijlen} frequent flyer mijlen.")