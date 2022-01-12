

pr_descuento = (10,20,30,40,50,60,70,80,90)

precio = float(input("Escribir precio: "))
#precio = 100

precio_rebaja = []

#precio_rebaja.append(precio*(((100 - pr_descuento[0]) / 100)))

precio_rebaja.append(precio*(((100 - pr_descuento[0]) / 100)))
precio_rebaja.append(precio*(((100 - pr_descuento[1]) / 100)))
precio_rebaja.append(precio*(((100 - pr_descuento[2]) / 100)))
precio_rebaja.append(precio*(((100 - pr_descuento[3]) / 100)))
precio_rebaja.append(precio*(((100 - pr_descuento[4]) / 100)))
precio_rebaja.append(precio*(((100 - pr_descuento[5]) / 100)))
precio_rebaja.append(precio*(((100 - pr_descuento[6]) / 100)))
precio_rebaja.append(precio*(((100 - pr_descuento[7]) / 100)))
precio_rebaja.append(precio*(((100 - pr_descuento[8]) / 100)))

print(precio_rebaja[0])
print(precio_rebaja[1])
print(precio_rebaja[2])
print(precio_rebaja[3])
print(precio_rebaja[4])
print(precio_rebaja[5])
print(precio_rebaja[6])
print(precio_rebaja[7])
print(precio_rebaja[8])
print(pr_descuento[:])
print(precio_rebaja[:])