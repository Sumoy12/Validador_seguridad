def cargar_palabras_riesgo(archivo='palabras_riesgo.txt'):
    """
    Carga una lista de palabras de riesgo desde un archivo de texto.
    Cada línea del archivo representa una palabra.
    """
    with open(archivo, 'r') as f:
        return [line.strip().lower() for line in f.readlines()]

def validar_texto(texto, palabras_riesgo):
    """
    Valida el texto ingresado contra una lista de palabras de riesgo.
    Devuelve una lista de palabras encontradas en el texto.
    """
    encontrado = [palabra for palabra in palabras_riesgo if palabra in texto.lower()]
    return encontrado
