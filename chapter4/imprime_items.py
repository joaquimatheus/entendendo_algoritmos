from time import sleep

def imprime_items(lista):
    for item in lista:
        print(item)

def imprime_items2(lista):
    for item in lista:
        sleep(1)
        print(item)

imprime_items([0,2,3,41,4,2,5])

imprime_items2([0,2,3,41,4,2,5])
