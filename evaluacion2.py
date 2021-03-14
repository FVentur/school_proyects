x=0
while (x<7):
    print ("     CASCOS OASIS")
    print ("----------------")
    print ("     MENU PRINCIPAL")
    print ("------------------")
    print ("1) cargar datos")
    print ("2) submenu listados")
    print ("3) sumatoria y promedio de datos")
    print ("4) dia de mayor produccion")
    print ("5) calculadora de 2 numeros")
    print ("6) rangos")
    print ("7) salir")
    x=int(input("ingrese una opcion: "))
    if x==1:
        c=[]
        z=7
        for w in range (0,z):
            lis=int(input("ingrese el valor a almacenar: "))
            c.insert(w,lis)
            print ("el valor fue cargado")
        print ("la lista fue cargada")
    if x==2:
        n=0
        while (n<3):
            print ("     SUBMENU LISTADO")
            print ("------------------")
            print ("1) posicion/valor")
            print ("2) valor/posicion")
            print ("3) salir")
            n=int(input("ingrese una opcion: "))
            if n==1:
                for w in range (0,z):
                    print ("en la posicion: ",w," el valor es :",c[w])
            if n==2:
                for w in range (0,z):
                    print ("el valor : ",c[w]," esta cargado en la posicion :",w)
    if x==3:
        g=0
        h=0
        for w in range (0,z):
            g=g+c[w]
            h=g/z
        print ("la suma es: ",g)
        print ("el promedio es: ",h)
    if x==4:
        m=0
        for w in range (0,z):
            if (c[w]>m):
                m=c[w]
        print ("en el mayor dia de produccion hubo :",m)
    if x==5:
        y=0
        while (y<4):
            print ("     CALCULADORA")
            print ("------------------")
            print ("1) SUMA")
            print ("2) RESTA")
            print ("3) MULTIPLICACION")
            print ("4) DIVISION")
            print ("5) SALIR")
            y=int(input("ingrese una operacion: "))
            if y==1:
                q=int(input("ingrese un numero: "))
                k=int(input("ingrese otro numero: "))                
                q=q+k
                print ("el resultado es: ",q)
            if y==2:
                q=int(input("ingrese un numero: "))
                k=int(input("ingrese otro numero: "))  
                q=q-k
                print ("el resultado es: ",q)
            if y==3:
                q=int(input("ingrese un numero: "))
                k=int(input("ingrese otro numero: "))  
                q=q*k
                print ("el resultado es: ",q)
            if y==4:
                q=int(input("ingrese un numero: "))
                k=int(input("ingrese otro numero: "))  
                q=q/k
                print ("el resultado es: ",q)
    if x==6:
        f=0
        i=0
        j=0
        for w in range (0,z):
           if (c[w]>=5) and (c[w]<11):
                f=f+1
           if (c[w]>=11) and (c[w]<15):
               i=i+1
           if  (c[w]>=15):
               j=j+1
        print ("entre 5 y 10: ",f)
        print ("entre 11 y 15: ",i)
        print ("mayores a 15: ",j)
