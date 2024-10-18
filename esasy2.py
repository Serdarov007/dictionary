shop = {
    "alma" = 8,
    "uzum" = 12,
    "hurma" = 18,
    "banan" = 25,
    "nar" = 15}

for i, j in shop.items():
    print(i, "-", j, "Manat")
kassa = 0
while True:
    a = input("Name almak islemek? ")
    if a == "quit":
        break
    elif a in shop:
        b = b * dukan[a]
        kassa += pul
print(f"Siz {kassa} manat tolemeli") 