
def cargar_palabras_riesgo(archivo='palabras_riesgo.txt'):
    with open(archivo, 'r') as f:
        return [line.strip().lower() for line in f.readlines()]

def validar_texto(texto, palabras_riesgo):
    encontrado = [palabra for palabra in palabras_riesgo if palabra in texto.lower()]
    return encontrado

if __name__ == "__main__":
    palabras = cargar_palabras_riesgo()
    texto = input("Ingrese el texto a analizar: ")
    alertas = validar_texto(texto, palabras)
    if alertas:
        print("Palabras de riesgo encontradas:", ", ".join(alertas))
    else:
        print("No se encontraron palabras críticas.")
