import math
from abc import ABC, abstractmethod
import  main
import random

# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’

class FormaGeometrica(ABC):
    @abstractmethod
    def FormaGeometrica(self):
        pass

    pi = math.pi


    def aria_abstract_method (self):
        print('Arie prin metoda abstracta!')

    def descrie(self):
        print('Cel mai probabil am colturi')




# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

class Patrat(FormaGeometrica):
    l = 4
    def __init__ (self, l):
        self.l = l




# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)
# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)

class Latura:
    __latura= 5
    def __init__(self,latura):
        self.__latura = latura

    def get_latura(self):
        return self.__latura
    def set_latura(self, latura_noua):
        self.__latura = latura_noua
    def delete_latura(self):
        self.__latura = None

    def descrie(self):
        print('Descriere')

class Latura2(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Latura este de {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        if latura == 5:
            latura == 2
        else:
            self.__latura = latura
        print(f'Noua latura este {latura}')


    @latura.deleter
    def latura(self):
        print(f'Forma geometrica nu are laturi')
        self.__latura = None



class Cerc(FormaGeometrica):
    __raza = 10
    def __init__(self,raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza este de: {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self,raza):
        if raza ==10:
            raza = 5
        else:
            self.__raza = raza
            return self.__raza

    @raza.deleter
    def raza(self):
        print(f'Forma geometrica este Cerc')
        self.__raza = None

    @abstractmethod
    def aria_abstract_method(self,raza):
        return math.pi * raza * raza
    print('Arie prin metoda abstracta!')

    def descrie(self):
        print('Cel mai probabil am colturi')




# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui
#

    def descriere(self):
        print('Eu nu am colturi')

obiect1 = Patrat
obiect1.l = 10
del obiect1.l
obiect1.descrie('{self.l}')


obiect2 = Cerc
obiect2.aria_abstract_method(10,2)













