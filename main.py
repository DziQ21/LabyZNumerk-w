

import math

def isCylinderDataGood(r:float,h:float):
    return r>0 and h>0

def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if  not isCylinderDataGood(r,h):
        return None
    return math.pi*r*r*2+math.pi

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    wynik = [1,1]
    if (n<=0):
        return None
    if n==1:
        return [1]
    for i in range(0,n-2):
        wynik+=[wynik[-1]+wynik[-2]]
    return wynik

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    M=[[a,1,-a],[0,1,1],[-a,a,1]]
    return None

def wypisywaczMacierzy():
    M=[[3,1,-2,4],[0,1,1,5],[-2,1,1,6],[4,3,0,1]]
    print(M[0][0])
    print(M[3][3])
    print(M[3][2])
    
    w2=M[2]
    print(w2)
    w1=[]
    for i in M:
        w1+=[i[3]]
    return None;
    print(w1)
wypisywaczMacierzy()

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    return None

