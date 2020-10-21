init = True

while(init):
    userLeter = input("Introduce una letra:")

    if len(userLeter)!=1:
        print("Tiene que ser una letra.")
    elif(userLeter=="."):
        init=False
    else:
        if userLeter in ("a","e","i","o","u"):
            print("Es una vocal")
        else:
            print("Es una consonante")


