money = [1, 5, 10]
selectedMoney = []
usedmoney=0
Cash = int(input("Cantidad de cambio: "))
index = len(money) - 1

while Cash > 0:
    pay = Cash - money[index]
    if pay >= 0:
        Cash = pay
        selectedMoney.append(money[index])
        usedmoney += 1
    else:
        index -= 1

print("Monedas devueltas:", selectedMoney)
print("cantidad de monedas usadas: ",usedmoney)
  