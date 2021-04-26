# Obtenemos mensaje a descifrar desde el usuario
# llamamos a upper para obtener sólo mayúsculas
texto = input("Mensaje cifrado > ").upper()

# Abecedario a utilizar en el cifrado
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
n=4
# Guardar posible mensaje
descifrado = ""
for l in texto:
    # Si la letra está en el abecedario se reemplaza
    if l in abc:
        pos_letra = abc.index(l)
        # Sumamos para movernos a la derecha del abc
        nueva_pos = (pos_letra - n) % len(abc)
        descifrado+= abc[nueva_pos]
    else:
        # Si no está en el abecedario sólo añadelo
        descifrado+= l
    msj = descifrado
print(msj)
