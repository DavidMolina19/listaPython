#listas

# lista1=[]

# lista1=[1,"hola",1.25,True,False]

# texto="hola grupo"

# # una lista es mutable
# #len longitud

# longitud=len(lista1)
# print(longitud)

# #agregar elementos append()
# lista1.append("colecciones")

# print(lista1)
# print(longitud)

# #acceder  a los elementos de la lista
# elemento=lista1[-2]
# print(elemento)

# # insertar en una posicion
# insertar=lista1.insert(2,5)
# print(lista1)

# #eliminar elelemtos: pop(posicion), remove(elemento)
# lista1.pop(1)
# print(lista1)

# lista1.remove(1.25)
# print(lista1)

#conocer el indice o posicion del elemento: index(elemento)

# lista=["hola",True,False,"hello","alo"]
# posicion=lista.index(False)
# print(posicion)


# #extender lista:extend()
# animales=["perro","gato","caballo","raton"]
# animales2=["mojarra","bagre","tilapia","pardorojo"]

# animales.extend(animales2)
# print(animales)

# animales.extend(lista)
# print(animales)


# #eliminar todos los elementos:clear()
# animales.clear()
# print(animales)

#recorrer una lista
# lenguajes=["español","ingles","frances"]
# for elemento  in lenguajes:
#     print(elemento)

# #recorrer teniendo en cuenta la posicion

# for indice in range(len(lenguajes)):
#    print(lenguajes[indice],"esta en la posicion",indice)    

par=[]
impar=[]

num1=int(input("ingresa el numero 1"))
num2=int(input("ingresa numero 2"))

# while num1<=num2:
#     if num1 % 2 == 0:
#         par.append(num1)
#     else:
#         impar.append(num1)
#     num1+=1

for num in range(num1,num2):
    if num %2==0:
        par.append(num)
    else:
        impar.append(num)


print(par)
print(impar)           

   

