#Resistencia en un conductor electrico.
#R=p*(L/S)
#Este programa va a contener caracteres de materiales precargados
#En un arreglo agregamos nombre del materail y resistividad.

resistividad={"Al":(0.028,"Aluminio"), "Cu":(0.017,"Cobre"),"Au":(0.023,"Oro"),"Ag":(0.016,"Plata"),"Pb":(0.22,"Plomo"),"Hg":(0.96,"Mercurio")}

while True:

    L=float(input("Ingresa la longitud del conductor en [m] "))
    S=float(input("Ingresa la seccion del conductor en [mm2] "))
    material=input("Ingresa el simbolo del material ")

    if material in resistividad:
        p=resistividad[material][0]
        print("Resistividad de ",resistividad[material][1],"=[ohms.mm1/m]")
        if S==0:
         print("Error, la sección no puede ser cero, ingresa una sección diferente.")
        else:
            R=p*L/S
            print("La resistencia de ",R,"ohms")
            break
    else:
       print("Simbolo de material incorrecto. Ingrese un símbolo valido.")