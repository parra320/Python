#Programa que evalua una lista de censo de poblacion y determina el foco de contingencia

print("\n\t\tSemáforo Covid-19")

AbrirArchivo= open("bd.csv", "r")
contenido= AbrirArchivo.readlines()
AbrirArchivo.close()

i=0  #contador
Covid=False    
PersonasInfectadas=0
EdadDeLaPersona=0
SemaforoCovid="Verde"
PromedioDeEdad=0.0
while i<len(contenido):
    Indicador=contenido[i][contenido[i].find(",")+1:contenido[i].find("\n")]
    Edad=contenido[i][:contenido[i].find(",")]
    i=i+1
    if float(Indicador)<0.80:
        Covid=False
    elif float(Indicador)>=0.80:
        Covid=True
        PersonasInfectadas=PersonasInfectadas+1
        EdadDeLaPersona=EdadDeLaPersona+int(Edad)
print("\n\tSe evaluo el Semáforo Covid en 100 individuos, de los cuales se obtuvo que: \n\t",PersonasInfectadas," personas han sido infectadas, Por lo Tanto: hay: ", int(len(contenido))-PersonasInfectadas,"Personas Sanas")

if PersonasInfectadas==0:
    SemaforoCovid="Verde"
    print("\n\tEl Color del Semáforo Covid es: ", SemaforoCovid+", 0 individuos")
elif PersonasInfectadas>=1 and PersonasInfectadas<=30:
    SemaforoCovid="Amarillo"
    print("\n\tEl Color del Semáforo Covid es: ", SemaforoCovid+", de 1-30 individuos")
elif PersonasInfectadas>=31 and PersonasInfectadas<=70:
    SemaforoCovid="Naranja"
    print("\n\tEl Color del Semáforo Covid es: ", SemaforoCovid+", de 31-70 individuos")
elif PersonasInfectadas>=71 and PersonasInfectadas<=100:
    SemaforoCovid="Rojo"
    print("\n\tEl Color del Semáforo Covid es: ", SemaforoCovid+", de 71-100 individuos")
else:
    print("Opcion fuera de los parametros solicitados")

PromedioDeEdad=EdadDeLaPersona/PersonasInfectadas
print("\n\tLa Edad promedio de personas con Covid-19 es de: ", PromedioDeEdad,"\n")


