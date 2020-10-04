user_nomb = input("Introduce un nombre:")
user_cont = input("Inbtroduce una contraseña:")

if(user_nomb == "Eddard" and user_cont == "hielo"):
    print("Usuario y contraseña correctos. winter is coming")
elif(user_nomb == "" or user_cont == ""):
    print("Introduce debes introducir el usuario y la contraseña.")
else:
    print("Acceso denegado. Al muro!")