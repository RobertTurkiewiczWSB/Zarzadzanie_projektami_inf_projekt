import argparse
import os
import multiprocessing
import time
from functools import wraps
import functools
from multiprocessing import Process, Queue, Pool

cache_dict = dict()
#Z1
def deco(f):
    def hello(*args, **kwargs):
        print(f"Hello")
        result = f(*args, **kwargs)
        return result
    return hello

@deco
def zadanie1():
    print("Zadanie 1 tutaj")


#Z2
def tetra(n):
   if n <= 2:
       return 0
   elif n == 3:
       return 1
   else:
       return(tetra(n-1) + tetra(n-2) + tetra(n-3) + tetra(n-4))

def zadanie2(a):
    print("Tetranacii sequence:")
    for i in range(a):
        print(tetra(i))


#Z3
def tetra_cache(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        global cache_dict
        result = cache_dict.get(args[0])
        #print(f"result for {args[0]} i {result}")

        if result is None:
            #print(f"Looking for result for {args[0]}")
            result = f(*args, **kwargs)
            cache_dict[args[0]] = result

        return result
    return wrapper

@tetra_cache
def tetra_for_cache(n):
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        return(tetra_for_cache(n-1) + tetra_for_cache(n-2) + tetra_for_cache(n-3) + tetra_for_cache(n-4))

def zadanie3(a):
    print("Tetranacii sequence:")
    for i in range(a):
        print(tetra_for_cache(i))

#Z4
def square_process(x):
    return x*x

def zadanie4():
    tablica = [3,4,23,5,6,1,2,6,15]
    #for i in range(1, 11):
    #    tablica.append(int(input(f"Podaj liczbe nr {i}: ")))

    print(f"Tablica przed potęgowaniem:\n{tablica}\nTablica po potęgowaniu:")
    with Pool(5) as p:
        print(p.map(square_process, tablica))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-z1", "--zadanie1", type=bool, required=False, help="Uruchom zadanie 1")
    ap.add_argument("-z2", "--zadanie2", type=int, required=False, help="Uruchom zadanie 2")
    ap.add_argument("-z3", "--zadanie3", type=int, required=False, help="Uruchom zadanie 3")
    ap.add_argument("-z4", "--zadanie4", type=bool, required=False, help="Uruchom zadanie 4")
    args = vars(ap.parse_args())

    print(args)
    if args["zadanie1"] is not None:
        zadanie1()
    if args["zadanie2"] is not None:
        zadanie2(args["zadanie2"])
    if args["zadanie3"] is not None:
        zadanie3(args["zadanie3"])
    if args["zadanie4"] is not None:
        zadanie4()

