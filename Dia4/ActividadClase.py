#defino el limite de monedas que tengo para pagar
money = [1, 5, 10]
#agrego un almacen para las monedas usadas
selectedMoney = []
#un contador para saber cuantas monedas use
usedmoney=0
#agrego la cantidad de cambio que decee
Cash = int(input("Cantidad de cambio: "))
#aqui pido que me traiga la moneda de mayor valor a pagar
index = len(money) - 1

#hago un bucle para que se cierre el programa cuando pague completo en 0
while Cash > 0:    
    pay = Cash - money[index]
    if pay >= 0:
        Cash = pay
        selectedMoney.append(money[index])
        usedmoney += 1
    else:
        index -= 1
#le doy salida a los datos
print("Monedas devueltas:", selectedMoney)
print("cantidad de monedas usadas: ",usedmoney)
  