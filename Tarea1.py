import csv
csv.reader
with open ("presenciaderedes.csv", newline= "") as File:
    reader = csv.reader(File)
    Arrayfilas = []
    for fila in reader:
      Arrayfilas.append (fila)
    print(Arrayfilas[0][0])
    print("Twitter (followers) Diferencias entre Meses:")
    print("ENERO")
    print(Arrayfilas[8][3], "Followers")
    a= Arrayfilas[8][3]
    a= int(a.replace(',',''))
    print("JUNIO")
    print(Arrayfilas[8][8], "Followers")
    b= Arrayfilas[8][8]
    b= int(b.replace(',',' '))
    print("Diferencia de Followers")
    print("Followers Junio-Enero")
    rest=abs(a-b)
    print("La diferencia es de",rest,"Followers\n\n")
    print("--------------------------\n\n")
    print(Arrayfilas[0][0])
    print("Visualizaciones de Youtube")
    print(Enero)
    print(Arrayfilas[16][3], "Visualizaciones")
    c= Arrayfilas[16][3]
    c= int(c.replace(',',' '))
    print("Junio")
    print(Arrayfilas[16][8], "Visualizaciones")
    d= Arrayfilas[16][3]
    d= int(d.replace(',',' '))
    print("Diferencia de Visualizaciones")
    print("Visualizaciones: Junio - Enero")
    rest=abs(d-c)
    print("Hay diferencia de",rest,"Visualizaciones\n\n")
    print("--------------------------\n\n")
    print(Arrayfilas[0][0])
    print("Promedio de crecimiento de twitter entre los meses de enero a junio")
    print("Promedio de crecimiento de TWITTER")
    print("Enero")
    print(Arrayfilas[10][3])
    e=Arrayfilas[10][3]
    e=int(e.replace('%',' '))
    print("Febrero")





