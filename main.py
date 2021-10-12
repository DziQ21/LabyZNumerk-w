import math
from typing import List, Union, Tuple

import numpy


# 1
def cylinder_area(r: float, h: float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r < 0 or h < 0:
        return math.nan
    return math.pi * r * r * 2 + math.pi * 2 * r * h


# 2
def generateLinespace() -> numpy.ndarray:
    return [numpy.linspace(10.0, 12.0, num=5),numpy.arange(0,12,numpy.pi)]


print(generateLinespace())


# 3
def fib(n: int) -> Union[None, List[int]]:
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    wynik = [1, 1]
    if n <= 0 or type(n) == float:
        return None
    if n == 1:
        return [1]
    for i in range(0, n - 2):
        wynik += [wynik[-1] + wynik[-2]]
    return numpy.array([wynik])


# 4

def matrix_calculations(a: int) -> Tuple:
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    M = [[a, 1, -a], [0, 1, 1], [-a, a, 1]]
    if numpy.linalg.det(M) == 0:
        return numpy.nan, numpy.transpose(M), 0
    return numpy.linalg.inv(M), numpy.transpose(M), numpy.linalg.det(M)


# 5


def wypisywaczMacierzy():
    M = [[3, 1, -2, 4], [0, 1, 1, 5], [-2, 1, 1, 6], [4, 3, 0, 1]]
    print(M[0][0])
    print(M[3][3])
    print(M[3][2])

    w2 = M[2]
    print(w2)
    w1 = []
    for i in M:
        w1 += [i[3]]
    return None;
    print(w1)


wypisywaczMacierzy()


# 6


def custom_matrix(m: int, n: int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if n <= 0 or m <= 0 or not isinstance(n, int) or not isinstance(m, int):
        return None
    result = []
    for i in range(m):
        buff = []
        for j in range(n):
            if i > j:
                buff.append(i)
            else:
                buff.append(j)
        result.append(buff)
    return result


# 7

def vectorOperations():
    v1 = numpy.array([[1], [3], [13]])
    v2 = numpy.array([[8], [5], [-2]])
    print("v1:")
    print(v1)
    print("v2:")
    print(v2)
    print("4*v1:")
    print(4 * v1)
    print("-v2+222")
    print(-v2 + numpy.array([[2], [2], [2]]))
    print("v1*v2")
    print(numpy.multiply(v1, v2))
    print("v1dotv2")
    print(numpy.dot(v2, numpy.transpose(v1)))


vectorOperations()


# 8
def matrixOperations():
    v1 = numpy.array([[1], [3], [13]])
    v2 = numpy.array([[8], [5], [-2]])
    matrix = numpy.array([[1, -7, 3], [-12, 3, 4], [5, 13, -3]])
    print("3m:")
    print(3*matrix)
    print("3m+1:")
    print(3 * matrix+numpy.ones([3,3]))
    print("M^t:")
    print(numpy.transpose(matrix))
    print("M*v1:")
    print(numpy.matmul(matrix,v1))
    print("v2T*M:")
    print(numpy.matmul(numpy.transpose(v2),matrix))

matrixOperations()