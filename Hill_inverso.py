#librerias
import qrcode
import numpy 

#Variables
i=0
k=0
cifrado=""
Letras = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R"]
Numeros = list()
vct = list()
vctR = list()
#Llave del Cifrado
Key =  numpy.array([[6, 24, 22], [26, 21, 1],[17, 5, 10]]) 
print("Ingrese el mensaje a codificar:")
msg=input()
msg = msg.replace(" ", "")
msg = msg.upper()
for x in range(0,len(msg),1):
	msg1 = msg[x]
	vct.append(Letras.index(msg1))
#Imprime la lista de los valores de las letras del mensaje ingresado acorde a sus posiciones definidas anteriormente
print(vct)
print(len(vct))
e = len(vct)//3
row = dict() # Declaramos el diccionario
col = dict()
R = dict()

matriz = numpy.zeros(shape=(e,3))

if len(vct)%3==0:
	for j in range(e):
		matriz[j]=[vct[i],vct[i+1],vct[i+2]]
		i = i+3	
	print("Matriz de dimenciones longitud del mensaje:"+str(e)+" X 3:")		
	print(matriz)
	print("Llave del cifrado:")
	print(Key)
	print("Vectores Columna Resultados de la operacion Matriz X Key:")
	for i in range(0, e):
		row['row'+str(i+1)] = [vct[k],vct[k+1],vct[k+2]]
		col['col'+str(i+1)] = numpy.transpose(row['row'+str(i+1)])
		R['R'+str(i+1)] = numpy.dot(Key,col['col'+str(i+1)])
		k = k+3
	for y in range(0,e):
		X=R['R'+str(y+1)]
		for u in range(0,3):
			O=X[u]
			if O > 27:
				modulo = O%27
				X[u] = modulo
			vctR.append(X[u])
	for Q in R:
  		print (Q, ":", R[Q])
	print("Vector resultante del cifrado con los numeros correspondientes a las posiciones de los nuevos caracteres:")
	print(vctR)
	
	for l in vctR:
		cifrado = cifrado +  Letras[l]	
	print("Mensaje Cifrado",cifrado)

else:
	print("No es un mensaje multiplo de 3")

