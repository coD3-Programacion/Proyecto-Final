import random
#Se importa random para colocar las minas aleatoriamente

def matriz_falsa_funcion():
    #Lista con la matriz completa, lista de cada una de las filas y lista con # de columnas
    global matriz_falsa
    matriz_falsa=[]
    filas_matriz_falsa = []
    numero_columnas = ["0","C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"]
    
    #Variables para colocar el # de filas
    numero_filas = 1 
    Booleano_filas = True
    
    matriz_falsa.append(numero_columnas)

    for i in range(10):
        for j in range(10):
            if Booleano_filas == True:
                filas_matriz_falsa.append("F"+(str(numero_filas))) #Se convierte en str para que no se confunda con el numero de minas
            filas_matriz_falsa.append(" ?") #En cada iteracion añade un elemento a la fila
            Booleano_filas = False #Solamente en la 1era iteracion va a colocar el # de la fila
        matriz_falsa.append(filas_matriz_falsa) #En cada iteracion añade una fila a la matriz con los elementos
        filas_matriz_falsa = [] #se vacia para repetir el proceso y no se acumulen las filas
        Booleano_filas = True
        numero_filas += 1
    
    #se imprime de una forma familiar (o como se deberia ver una matriz)
    for i in range(len(matriz_falsa)):
            print(matriz_falsa[i])

def matriz_real_funcion():
    #Lista con la matriz real completa y lista de cada una de las filas
    global matriz_real
    matriz_real=[]
    filas_matriz_real = []
    
    #Aca se crea la matriz de la logica (no se va a imprimir)
    for i in range(10):
        for j in range(10):
            #Por el momento todos los valores van a ser cero
            filas_matriz_real.append(0) 
        #Se agrega la fila de ceros a la matriz
        matriz_real.append(filas_matriz_real)
        #Se reinicia la lista de las filas que se rellenara de ceros otra vez
        filas_matriz_real = []

def colocar_minas():
    numero_minas = 0

    while numero_minas<10: #10 iteraciones porque se ponen 10 minas
        #numero entero aleatorio entre 0 y 9 (que son las filas y columnas en la matriz real)
        fila_mina = random.randint(0, 9) 
        columna_mina = random.randint(0, 9)

        #Si la posicion aleatoriamente escogida ya tiene una mina, se omite la iteracion
        if matriz_real[fila_mina][columna_mina] == "*":
            continue
        
        #Esta es la posicion de la mina que se representa con un "*"
        matriz_real[fila_mina][columna_mina] = "*" 
        
        #Los dos ciclos for recorren las casillas adyacentes a la mina
        for i in range(fila_mina-1, fila_mina+2):
            for j in range(columna_mina-1, columna_mina+2):
                if 0<=i<10 and 0<=j<10: #Si la posicion esta en el tablero (hay casos donde se pude salir del tablero por el range)
                    #Si la posicion es la mina entonces se omite, sino se suma 1 a los alrededores
                    if matriz_real[i][j] == "*": 
                        continue 
                    #Suma de 1 a los alrededores
                    matriz_real[i][j] = matriz_real[i][j] + 1
        
        #Al final de 1 iteracion completa se suma 1 en el numero de minas
        numero_minas += 1
        
def ingresar_verificar_posicion():
    #Se pregunta por la posicion que quiere el usuario
    print('\nIngrese una posicion que desee destapar o señalar como una mina separandolo con "-": ("M" para señalar mina o "D" para destapar, ej: M-5-4, D-9-1, M-10-8)')
    
    #Ciclo que se rompe hasta que la posicion sea correcta
    while True:
        usuario_posicion = str(input("Ingrese posicion: "))
        usuario_posicion = usuario_posicion.upper() #La cadena se tranforma con .upper() para una condicion especifica
        lista_usuario_posicion = usuario_posicion.split("-") #Se crea una lista separando los elementos mediante el "-"
        
        #A continuacion se evaluan ciertas condiciones para verificar que la posicion es correcta y para evitar errores
        if "-" not in usuario_posicion:
            print('\nEn la cadena no ingreso el separador "-"')
            continue

        if len(lista_usuario_posicion) != 3:
            print("\nIngreso una posicion incorrecta (no tiene 3 caracteres), intente de nuevo: ")
            continue
    
        if lista_usuario_posicion[0] != "M" and lista_usuario_posicion[0] != "D":
            print('\nIngreso una posicion incorrecta (el primer caracter tiene que ser "M"o "D"), intente de nuevo: ')
            continue
        
        #Lista para la condicion
        lista_numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] 
        
        if (lista_usuario_posicion[1] not in lista_numeros) or (lista_usuario_posicion[2] not in lista_numeros):
            print("\nIngreso una posicion incorrecta (la fila o columna esta incorrecta), intente de nuevo: ")
            continue
        
        #Cuando no entra en ningun if, la posicion es correcta y puede salir del bucle
        break
    
    #Se transforman en enteros los numeros de la fila y la columna para trabajar con ellos
    int(lista_usuario_posicion[1])
    int(lista_usuario_posicion[2])

    #En el return esta la letra ("M" o "D") y la fila y la columna
    return lista_usuario_posicion[0], lista_usuario_posicion[1], lista_usuario_posicion[2]


def casillas_adyacentes(fila_escogida, columna_escogida):
    #Las coordenadas para los movimientos en las 8 direcciones (casillas adyacentes)
    direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    #El if verifica si la posicion ya fue destapada, si es asi no hace nada
    if matriz_falsa[fila_escogida][columna_escogida] != " ?":
        return

    valor_celda_real = matriz_real[fila_escogida-1][columna_escogida-1]

    #Si la celda en la matriz real es 0, se destapa
    if valor_celda_real == 0:
        matriz_falsa[fila_escogida][columna_escogida] = " 0" 
        
        #El ciclo for recorre las celdas adyacentes
        for direccion in direcciones:
            #Se crean 2 variables que son la fila adicional y la columna adicional (con ayuda de las direcciones)
            fila_adicional = fila_escogida + direccion[0]
            columna_adicional = columna_escogida + direccion[1]

            #Aca se verifica si la celda adyacente esta dentro del tablero
            if 1 <= fila_adicional <= 10 and 1 <= columna_adicional <= 10:
                casillas_adyacentes(fila_adicional, columna_adicional)
                        
    #Si es distinto de 0, solo destapamos la celda actual
    else:
        matriz_falsa[fila_escogida][columna_escogida] = f" {valor_celda_real}"

def destapar_celda(bandera_o_destapar, fila_escogida, columna_escogida):
    #Se globalizan las variables definidas para trabajar con ellas
    global minas_correctamente_señaladas
    global lista_minas_señaladas

    #Si se escogio señalar mina, entonces se coloca ! en la matriz
    if bandera_o_destapar == "M": 
        #Se coloca "!" como bandera en la matriz falsa
        matriz_falsa[fila_escogida][columna_escogida] = " !"
        """Si la mina esta correctamente señalada (es decir si realmente hay una mina en la celda) y no esta en la lista de minas señaladas entonces 
        se suma 1 en la variable de minas_correctamente_señaladas y se agrega a la lista de minas señaladas para que si el jugador intenta señalar 
        la misma mina no sume otro valor"""
        if matriz_real[fila_escogida-1][columna_escogida-1] == "*" and (fila_escogida, columna_escogida) not in lista_minas_señaladas:
            minas_correctamente_señaladas += 1
            lista_minas_señaladas.append((fila_escogida, columna_escogida))
        
            #Si llega a 10 minas señaladas correctamente gana el juego
            if minas_correctamente_señaladas == 10:
                print("\n--------------------------------------------------------------------------------------------------------")
                print("------------------------HAS SEÑALADO TODAS LAS MINAS CORRECTAMENTE! HAS GANADO!-------------------------")
                print("--------------------------------------------------------------------------------------------------------")
                #Devuelve True por lo que se acaba el ciclo
                return True 
        
        #Despues se muestra la matriz
        for i in range(len(matriz_falsa)):
            print(matriz_falsa[i])

    elif bandera_o_destapar == "D":
        #Se destapa o se muestra la casilla:
        casillas_adyacentes(fila_escogida, columna_escogida)
        #El espacio es para que no se deforme la matriz y los encabezados tengan sentido
        matriz_falsa[fila_escogida][columna_escogida] = (" "+ (str(matriz_real[fila_escogida-1][columna_escogida-1])))
        
        #Despues se muestra la matriz
        for i in range(len(matriz_falsa)):
            print(matriz_falsa[i])

        #Si la posicion escogida tiene una mina, retorna un True y pierde el juego
        if matriz_falsa[fila_escogida][columna_escogida] == " *":
            print("\n--------------------------------------------------------------------------------------------------------")
            print("-----------------------------------HAS PISADO UNA MINA! HAS PERDIDO!------------------------------------")
            print("--------------------------------------------------------------------------------------------------------")
            return True
        
        
if __name__ == "__main__":
    print("--------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------BUSCAMINAS-----------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------")
    print('\n \
-El juego consiste en destapar todas las casillas seguras o señalar todas las minas\n \
-El numero en una casilla indica el numero de minas alrededor (en todas sus casillas adyacentes)\n \
-Si destapas una casilla que es mina pierdes el juego\n \
-Las minas se pueden señalar o marcar con "banderas"\n') 
    
    #Se inicializan las variables con las que se gana el juego
    minas_correctamente_señaladas = 0
    lista_minas_señaladas = []
    
    #Se crea la matriz falsa y enseguida la matriz de la logica o la matriz real
    matriz_falsa_funcion()
    matriz_real_funcion()
    
    #Aca se colocan las 10 minas en la matriz de la logica
    colocar_minas()

    print("")

    for i in range(len(matriz_real)):
            print(matriz_real[i])

    #Este es el cilo en el que va a estar todo el juego
    while True:
        #Las variables del return se guardan en las variables siguientes:
        bandera_o_destapar, fila_escogida, columna_escogida = ingresar_verificar_posicion() 
        #El return de la funcion se guarda en la variable y si esta es True, es porque gano o perdio, por lo tanto el juego acaba
        Terminar = destapar_celda(bandera_o_destapar, int(fila_escogida), int(columna_escogida))
        if Terminar == True:
            break
        
