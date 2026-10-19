standaardKostBoek = 24.95

korting = 0.40

kostEersteBoek = 3

standaardKostVerzending = 0.75

totaalBoeken = 60

restAantalBoeken = totaalBoeken - 1

kostBoekBoekenwinkels = standaardKostBoek - (standaardKostBoek * korting)

eersteBoekKostMetVerzendingskost = kostBoekBoekenwinkels + kostEersteBoek
restBoekenMetVerzendingskost = restAantalBoeken * (kostBoekBoekenwinkels + standaardKostVerzending)

Totaalkost = eersteBoekKostMetVerzendingskost + restBoekenMetVerzendingskost
print(Totaalkost)