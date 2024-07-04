import os
os.system("cls")
def salir():
    print("salir")
    print ("que tengas un dia de la papaya")

while True:
    print("1:grabar")
    print("2:buscar")
    print("3:imprimir certificados")
    print("4:salir")

    
    vopcion=input(print("escoja una opcion"))    

    if vopcion < 1 or vopcion > 4 :
        
        
        print("opcion invalida")
    else:
        if vopcion == 1 : 
            while vnombre == "" :
                validacion=vnombre.replace(" ","")
                if len(validacion) == 0 :
                    vnombre= ""
                    print("el nombre es invalido")
                else:
                    try:
                        edad=input(print("¿cual es tu edad?")) 
                    except:
                            edad=0
                    if edad < 0 :
                        print("la eda ingresada no es valida ")
                
                    else:
                        
                        while True :
                             NIF=input(print("digite su NIF"))
                             validacion=NIF.replace(" ","")
                             if len(validacion) >= 8 :
                               print("el NIF no puede estar vacio")
                               break
                           
                       
                         
                        
                             
                        
                        
        if vopcion == 2 :
            try:
                input(print("ingrese su NIF"))
            except:
                print("el NIF ingresado es invalido") 
                    






              