# -*- coding: cp1252 -*-
ban=0
x=0
while x<7:
    print ("""
        PADRON
---------------------
1) cargar datos
2) submenu listados
3) busquedas:
4) rango etario:
5) promedio de edades
6) persona de mayor edad:
7) salir""")
    x=input("ingrese una opcion: ")
    if x.isdigit():
        x=int(x)
        if x==1:
            c=[]
            n=[]
            z=input("ingrese la cantidad de personas: ")
            if z.isdigit():
                z=int(z)
                for w in range (0,z):
                    aq=0
                    while aq==0:
                        nom=input("ingrese su nombre: ")
                        eda=input("ingrese su edad: ")
                        if nom.isalpha() and eda.isdigit():
                            nom=nom.upper()
                            eda=int(eda)
                            c.insert(w,nom)
                            n.insert(w,eda)
                            aq=1
                            ban=1
                            print ("los datos fueron cargados")
                        else:
                            print ("datos incorrectos")
                            aq=0
                print ("la lista fue cargada")
            else:
                print ("no ingrese letras")
        if x==2:
            if ban==1:
                q=0
                while q<3:
                    print ("""
       SUBMENU
--------------------
1) nombre/edad
2) edad/nombre
3) salir""")
                    q=input("ingrese una opcion: ")
                    if q.isdigit():
                        q=int(q)
                        if q==1:
                            for w in range (0,z):
                                print ("su nombre es: ",c[w]," y su edad es :",n[w])
                        if q==2:
                            for w in range (0,z):
                                print ("su edad es: ",n[w]," y su nombre es: ",c[w])
                    else:
                        q=0
                        print ("solo nueros")
            else:
                print ("revise los valores de la lista")
        if x==3:
            if ban==1:
                cic=0
                while cic<4:
                    print ("""
           BUSQUEDA
--------------------
1)_Busqueda por posicion de la lista
2)_Busqueda por nombre de la persona
3)_Busqueda por edad
4)_Salir""")
                    cic=input("ingrese una opcion: ")
                    if cic.isdigit():
                        cic=int(cic)
                        if cic==1:
                            e=input("ingrese su posicion en la lista: ")
                            if e.isdigit():
                                for w in range (0,z):
                                    e=int(e)
                                    if w==e:                  
                                        print ("su nombre es:" ,c[w], ", su edad: ",n[w],"y su posicion en la lista",w)
                                             
                                            
                            else :
                                print ("revise el dato a cargar")
                                                
                        if cic==2:
                            e=input("ingrese el nombre de la persona a buscar: ")
                            if e.isalpha():
                                e=e.upper()
                                for w in range (0,z):
                                    if c[w]==e:                   
                                        print ("su nombre es:" ,(c[w]), ", su edad: ",n[w],"y su posicion en la lista",w)
                                            
                            else :
                                print ("revise el dato a cargar")
                                                
                        if cic==3:
                            e=input("ingrese la edad de la persona a buscar: ")
                            if e.isdigit():
                                e=int(e)
                                for w in range (0,z):
                                    if n[w]==e:
                                        print ("su nombre es:" ,c[w], ", su edad: ",n[w],"y su posicion en la lista",w)
                                            
                            else :
                                print ("revise el dato a cargar")
                    else:
                        print ("ingrese una de las opciones indicadas")
                        cic=0
        if x==4:
            if ban==1:
                q=0
                r=0
                y=0
                for w in range(0,z):
                    if (n[w]>=0) and (n[w]<12):
                            q=q+1
                    if (n[w]>=12) and (n[w]<19):
                            r=r+1
                    if (n[w]>=19):
                            y=y+1
                print ("hay :",q," niños ")
                print ("hay :",r," jovenes ")
                print ("hay :",y," adultos ")
            else:
                print ("revise los valores de la lista")
                
        if x==5:
            if ban==1:
                h=0
                for w in range (0,z):
                    h=h+n[w]
                    d=h/z
                print ("la suma es: ",h," y el promedio es: ",d)
            else:
                print("revise los valores de la lista")
        if x==6:
            if ban==1:
                m=0
                f=0
                for w in range (0,z):
                    if n[w]>=m:
                        m=n[w]
                        f=c[w]
                print ("la mayor edad es: " ,m," y pertenece a: ",f)
                
            else:
                print ("revise los valores de la lista")
    else:
        x=0
        print ("no ingrese letras")
