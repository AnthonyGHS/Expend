import time
import os


def Bienvenida ():
    print ("Seleccione el producto")
    print ("Presione 1 para Cocacola   20 pesos")
    print ("Presione 2 para Galleta Chokkis   15 pesos")
    print ("Presione 3 para Chocolate M&M  45 pesos")
    print ("Presione 4 para Bizcocho Esponjoso   15 pesos")
    print ("Presione 5 para Yogurt yoka vainilla  35 pesos")
    print("")
    print("")

def Pagos ():
    print ("Las opciones de pago son: Modenas de 5 , 10 , 15 y Papeletas de 100 y 200 pesos Dominicanos")
    print ("Ingrese el monto de su Moneda/Papeleta")
    
Bienvenida ()

Cuenta = 0
Sobrante = 0

while True:
    os.system ("cls")
    Bienvenida ()
    print("")
    print("Su cuenta es de:  ", Cuenta, "$")
    print("")
    print("Seleccione N para finalizar")
    print("")
    Usuario = input("Ingrese su seleccion aqui: ")
    
    
    if Usuario == "N":
        print("Su cuenta es de:  ", Cuenta, "$")
        break 
   

    if Usuario == "1":
        valor = 20
        Cuenta = Cuenta + valor
        continue
    if Usuario == "2":
        valor = 15
        Cuenta = Cuenta + valor
        continue
    if Usuario == "3":
        valor = 45
        Cuenta = Cuenta + valor
        continue
    if Usuario == "4":
        valor = 15
        Cuenta = Cuenta + valor
        continue
    if Usuario == "5":
        valor = 35
        Cuenta = Cuenta + valor
        continue
    else:
        os.system ("cls")
        Bienvenida ()
        print(" Error. Seleccione un producto de la lista ")
        time.sleep (5)
        continue

    Cuenta = Cuenta + valor

while True:
        os.system("cls")
        Pagos()
        print("")
        print("El monto a pagar es de: ", Cuenta, "$")
        print("")
        
        Monto = input ("Digite aqui su monto a pagar: ")
        
        if Monto == "5":
            Dinero = 5
            Sobrante = Cuenta - Dinero
            Cuenta = Sobrante
            
            if Cuenta <= 0:
                break 
            continue
        if Monto == "10":
            Dinero = 10
            Sobrante = Cuenta - Dinero
            Cuenta = Sobrante
            
            if Cuenta <= 0:
                break
            continue
        if Monto == "25":
            Dinero = 25
            Sobrante = Cuenta - Dinero
            Cuenta = Sobrante
            
            if Cuenta <= 0:
                break
            continue
        if Monto == "100":
            Dinero = 100
            Sobrante = Cuenta - Dinero
            Cuenta = Sobrante
            
            if Cuenta <= 0:
                break
            continue
        if Monto == "200":
            Dinero = 200
            Sobrante = Cuenta - Dinero
            Cuenta = Sobrante
            
            if Cuenta <= 0:
                break
            continue
        else:
            os.system ("cls")
            Pagos()
            print ("Error. Ingrese el tipo de moneda correspondiente al pago ")
            time.sleep (5)
        
print ("Su cambio es de: " , Sobrante, "$")