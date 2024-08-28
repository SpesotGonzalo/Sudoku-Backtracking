# Una funcion para pintar la grilla del sudoku
def pintar_grilla(arr):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("+---+---+---+---+---+---+---+---+-----+")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if arr[i][j] == 0:
                print(".", end=" ")
            else:
                print(f" {arr[i][j]} ", end=" ")
        print()

# localizar casillas vacion con un 0 
def encontrarVacio(arr, l):
    for fila in range(9):
        for columna in range(9):
            if(arr[fila][columna]== 0):
                l[0]= fila
                l[1]= columna
                return True
    return False

# Una funcion que retorna si los valores ingresados
#  se usan en la fila 

def usado_en_fila(arr, fila, num):
    for i in range(9):
        if(arr[fila][i] == num):
            return True
    return False

# Misma funcion de arriba pero en la columna .
def usado_en_columna(arr, columna, num):
    for i in range(9):
        if(arr[i][columna] == num):
            return True
    return False

# Funcion que checkea en la matriz de 3x3 dentro de la 9x9 si se encuentra el numero 
def usado_m3x3(arr, fila, columna, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + fila][j + columna] == num):
                return True
    return False

# se fija si donde tiene que moverse de hecho se puede hacer
def lugar_seguro(arr, fila, columna, num):
    
    return (not usado_en_fila(arr, fila, num) and 
        (not usado_en_columna(arr, columna, num) and 
        (not usado_m3x3(arr, fila - fila % 3, columna - columna % 3, num))))

# Toma la grilla parcialmente llena e intenta asignar valores que cumplan 
#  con los requerimientros de un sudoku
def resolverSudoku(arr):
    
    # 'l' es una lista que mantiene la fila y columna   
    l =[0, 0]
    
    # Si no encontramos un lugar seguro , no hay solucion   
    if(not encontrarVacio(arr, l)):
        return True
    
    #Asigna valor a la fila y la columna segun lo que encontramos
    fila = l[0]
    columna = l[1]
    
    # Considera los numeros del 1 al  9 , recordemos que el 0 era lugar vacio
    for num in range(1, 10):
        
        # Puede ser un lugar para asignar un numero
        if(lugar_seguro(arr,fila, columna, num)):
            
            # Asigna un valor
            arr[fila][columna]= num

            # retornar si se pudo asignar
            if(resolverSudoku(arr)):
                return True

            # fallo el intento , poner en 0 y volver a intentar
            arr[fila][columna] = 0
            
    # esto activa el backtracking      
    return False 

# funcion main para testear las funciones de arriba
if __name__=="__main__":
    
    # Crear un array 2D para el sudoku
    grilla =[[0 for x in range(9)]for y in range(9)]
    
    # Valores para el sudoku
    grilla =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    # Si fue exitoso el algoritmo , print a  la grilla resuelta
def mostrarSudoku ():
    if(resolverSudoku(grilla)):
        print("Este es el sudoku resuelto \n")
        pintar_grilla(grilla)
    else:
        print ("No hay solucion ")


mostrarSudoku()