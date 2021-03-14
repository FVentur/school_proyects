x=0
while (x<4):
    print ("         T.P")
    print ("----------------")
    print (" MENU PRINCIPAL")
    print ("----------------")
    print ("1) cargar datos")
    print ("2) listar datos")
    print ("3) clasificar datos de la lista")
    print ("4) salir")
    x=int(input("ingrese una opcion: "))
    if x==1:
        c=[]
        z=int(input(" cuantas posiciones quiere en su lista: "))
        for w in range(0,z):
            lis=int(input("ingrese el valor a almacenar: "))
            c.insert(w,lis)
            print ("valor cargado")
        print ("la lista ha sido cargada")
    if x==2:
         for w in range(0,z):
             print ("el valor en la posicion: ",w,"es :",c[w])
    if x==3:
        q=0
        r=0
        y=0
        for w in range(0,z):
            if (c[w]>=0) and (c[w]<10):
                    q=q+1
            if (c[w]>=10) and (c[w]<20):
                    r=r+1
            if (c[w]>20):
                    y=y+1
        print ("hay :",q," datos menores a 10")
        print ("hay :",r," datos entre 10 y 20")
        print ("hay :",y," datos mayores a 20")
