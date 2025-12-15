class Producto:
    def __init__(self, nom, can):
        self.nom = nom
        self.can = can


i=0
lista=[]

def Mostrar():
    m=0
    while m < len(lista):
        print(f"{lista[m].nom:<15} | {lista[m].can:>14}")
        m+=1
while i==0:
    print("____________________________")
    print("Menu de gestion de productos \n ------------------------- \n 1. Alta de productos nuevos")
    print(" 2. Listado completo de productos \n 3. Salir")
    opcion = int(input("Ingrese la opcion deseada (1-3): "))
    if opcion==1:
        print("Alta de producto")
        n = input("Ingrese el producto: ")
        c = input("Ingrese la cantidad del producto: ")
        per = Producto(n,c)
        lista.append(per)
        print("Producto guardado con exito")
    elif opcion==2:
        print("Listado completo de productos")
        print("________________________________")
        print("Productos       |       Cantidad")
        print("--------------------------------")
        Mostrar()
    elif opcion==3:
        exit()
    else:
        print("_______________")
        print("Opcion invalida")
        print("---------------")