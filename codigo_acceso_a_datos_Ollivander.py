def accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero):
    """Introduce una lista vacía y una ruta de acceso a un fichero
    Comprueba si el archivo no existe o si no es un string, en estos caso devuelve una lista vacía .
    Si existe abre el archivo en modo lectura,
    busca la palabra 'day' por cada línea y si encuentra alguna crea una lista vacía
    y la intoduce en la lista vacía inicial.
    Si en la línea encuentra la palabra 'name',  guarda una cifra con la cantidad de palabras que contiene la frase.
    Las siguienes líneas, introduce cada valor, siendo un string, en la lísta vacía creada en esta función, siendo separada 
    en la misma cantidad que la cifra guardada, contando las comas de derecha a izquierda.
    Por cada elemento en la línea se comprueba si el string puede ser transformado a int, en caso afirmativo lo hace.
    se cierra el fichero y se devuelve la lista, esta vez llena, introducida en la función"""
    try:
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        print("Fichero no encontrado")
        return []
    except ValueError:
        print("El nombre del fichero ha de ser un string")
        return []
    else:
        matrizCasosTest = []
        numeroPropiedadesItem = 0
        for linea in fichero:
            if linea.find("day") != -1:
                casosTestDia = []
            elif linea == "\n":
                matrizCasosTest.append(casosTestDia)
            elif linea.find("name") != -1:
                numeroPropiedadesItem = len(linea.split(','))
            else:

                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem - 1)
                listaitems=[]
                for elemento in item:
                    try:
                        elemento = int(elemento)
                        listaitems.append(elemento)
                    except ValueError:
                        listaitems.append(elemento)    
                casosTestDia.append(listaitems)
        fichero.close()
        return matrizCasosTest


def crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest):
    """Introduce la lista devuelta por la función anterior y una ruta de acceso a un fichero.
    Si la ruta de acceso introducida no es un string, termina la función, de otro modo abre el fichero en modo escritura(en su defecto lo crea).
    Por cada sublista(casosTestDia), encabeza su contenido poniendo 5 guiones, Día, el numero del contador enumerado y otros 5 guiones, junto a un salto de línea.
    Lo escribe en el fichero, seguido de su sublista con todos sus items y valores, transformando si es necesario el elemento en un string, separándolos por comas.
    cierra el archivo."""
    try:
        if not isinstance(ficheroVolcadoCasosTest, str):
            raise ValueError
        stdout = open(ficheroVolcadoCasosTest, 'w')
    except ValueError:
            print("La ruta de acceso al fichero ha de ser un string")
    else:
        for (offset, casosTestDia) in enumerate(matrizCasosTest):
            stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
            for item in casosTestDia:
                listaitems = []
                for elemento in item:
                    elemento = str(elemento)
                    listaitems.append(elemento)
                stdout.write(', '.join(listaitems) + '\n')
        stdout.close()


def mostrarCasosTest(matrizCasosTest):
    """ Para mostrarnos el resultado en consola de la función anterior, introduce la misma matriz sacada de la primera función, y procede a printear su contenido
    tal como se ha escrito el fichero de la función anterior."""
    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)


if __name__ == "__main__":

    rutaAccesoFichero = "casos_test.txt"
    # rutaAccesoFichero = "stdout_bug_conjured.gr"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    mostrarCasosTest(matrizCasosTest)

    ficheroVolcadoCasosTest = "./stdout.txt"

    crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)
