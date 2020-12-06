print("koszyk")
koszyk = [
    {"nazwa": "mleko", "ilosc": 2, "cena": 3.0},
    {"nazwa": "czekolada", "ilosc": 3, "cena": 2.0},
    {"nazwa": "sok", "ilosc": 1, "cena": 2.5}
]

znizka = 5
if len(koszyk) > 3:
    znizka = 5

suma_koszyka = 120
suma_koszyka = suma_koszyka - suma_koszyka * znizka

if suma_koszyka > 500:
    print("ZNIŻKA!!!")
    suma_koszyka = suma_koszyka - 100

print(koszyk)
