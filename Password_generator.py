import random

elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

tamaño = int(input("¿de cuantos caracteres quieres que sea tu contraseña?"))
password = ""
for i in range(tamaño):
    password += random.choice(elements)
print(password)
    