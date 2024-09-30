lista = []

def agregar():
    item = input("Ingrese un item: ")
    lista.append(item)

def editar():
    if not lista:
        print("No es posible editar porque no hay items en la lista aún.")
        return
    item = input("¿Qué item quiere editar?: ")
    if item in lista:
        nuevo_item = input("Ingrese el nuevo valor: ")
        lista[lista.index(item)] = nuevo_item #Esto es para editar un elemento de la lista
    else:
        print("El item no está en la lista.")

def eliminar():
    if not lista:
        print("No es posible eliminar porque no hay items en la lista aún.")
        return
    item = input("¿Qué item desea borrar?: ")
    if item in lista:
        lista.remove(item)
    else:
        print("El item no está en la lista.")

def imprimir_lista():
    print("Items en la lista:" if lista else "La lista está vacía.")
    for item in lista:
        print(f"- {item}")  

def finalizar():
    print("Lista finalizada:", lista)

while True:
    print("\n1. Ingresar un nuevo Item, 2. Editar Item, 3. Eliminar Item, 4. Imprimir lista, 5. Finalizar lista")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        agregar()
    elif opcion == '2':
        editar()
    elif opcion == '3':
        eliminar()
    elif opcion == '4':
        imprimir_lista()
    elif opcion == "5":
        finalizar()
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
