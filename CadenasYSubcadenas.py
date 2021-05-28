
frase = "A mi me gusta programar en Python"

print(frase.find("Python"))

print(frase.find("m"))

pm = frase.find("m")

print(frase.find("m", pm+1))

print(frase.upper())

print(frase.lower())

pp = frase.find("Python")

print(frase[:pp]+frase[pp:].upper())

print(frase[:pp]+frase[pp:].lower())

print(frase.replace("Python", "Java"))

print(frase.split("Programar"))

print(len(frase))


