"""
Saber si el año es bisiesto.
"""
user_año = int(input("Introduce un año:"))

if(user_año%4 == 0):
    if(user_año%400 == 0 and user_año%100!=0):
        print("Es bisiesto")
    elif(user_año%4 == 0):
        print("Es bisiesto")
else:
    print("No es bisiesto.")

