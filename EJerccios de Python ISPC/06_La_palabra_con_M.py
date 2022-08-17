m_palabra = []

while True:
    print("Ingresa 'a' para salir")
    palabra = input("Ingresa una palabra: ")

    if palabra == "A" or palabra == "a":
        break

    elif palabra[0] == "m" or palabra[0] == "M":
        m_palabra.append(palabra)

print("Hay",len(m_palabra),"palabras que comenzan con M")