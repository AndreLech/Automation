# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
import math

# class Cerc:
#     raza = None
#     culoare = None
#
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc (self, color, arie):
#         self.culoarea = color
#         arie= self.arie
#         print(f'Cercul are culoarea {color} si raza de {arie}')
#
#     def aria (self, raza):
#         # A = pi r la patrat
#         # r la patrat = A/ pi
#         # r = radical din A/ pi
#         return math.pi * raza
#
#    # # def area(self):
#    # #     return self.radius ** 2 * 3.14
#    # # print(f'Aria cercului este {aria}')-----------
#
#     def diametru(self, raza):
#         return raza*2
#
#     def circumferinta(self, raza):
#         return 2*math.pi*raza
#
#
# # ● descrie_cerc() - va PRINTA culoarea și raza
# instanta_cerc = Cerc("rosu",12)
# print(instanta_cerc.culoare)
# print(instanta_cerc.raza)
#
# # ● aria() - va RETURNA aria
# print(instanta_cerc.aria(4))
#
# # ● diametru()
# print(instanta_cerc.diametru(4))
#
# # ● circumferinta()
# print(instanta_cerc.circumferinta(4))


# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

# class Dreptunghi:
#     lungime = None
#     latime = None
#     culoare = "Rosu"
#
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         return f'Dreptunghiul are {self.lungime} , {self.latime} si {self.culoare}'
#
#     def aria(self,lungime, latime):
#         self.lungime = lungime
#         self.latime = latime
#         return lungime * latime
#
#     def perimetrul(self,lungime, latime):
#         self.lungime = lungime
#         self.latime = latime
#         return 2 * (lungime + latime)
#
#     # def schimbă_culoarea(self, culoare):
#     #     noua_culoare = input('Introduceti noua culoare: ')
#     #     self.culoare = noua_culoare
#     #     print(noua_culoare)
#
#     def schimbă_culoarea(self):
#         noua_culoare = input('Introduceti noua culoare: ')
#         self.culoare = noua_culoare
#         print(noua_culoare)
#         pass
#
#
# # ● descrie()
# instanta_dreptunghi = Dreptunghi(2,4,"verde")
# print(instanta_dreptunghi.lungime)
# print(instanta_dreptunghi.latime)
# print(instanta_dreptunghi.culoare)
#
# # ● aria()
# print(instanta_dreptunghi.aria(2,4))
#
# # ● perimetrul()
# print(instanta_dreptunghi.perimetrul(5,3))
#
# # ● schimbă_culoarea(noua_culoare)
# print(instanta_dreptunghi.schimbă_culoarea())





# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)


# class Angajat:
#     nume = None
#     prenume = None
#     salariu = None
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f'Date angajat: {self.nume} {self.prenume} si are salariul egal cu {self.salariu}')
#
#     def nume_complet(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#         return nume + prenume
#
#     # # prima varianta # se da in atribut salariul
#     # def salariu_lunar(self, salariu):
#     #     self.salariu = salariu
#     #     return salariu
#
#     # # 2-a var # se ia salariul dat la prima instantare
#     def salariu_lunar(self):
#         return self.salariu
#
#     def salariu_anual(self, salariu):
#         self.salariu= salariu
#         return salariu * 12
#
#     def marire_salariu(self, salariu):
#         # ##for salariu in range (2000, 4000, 6000):
#             if salariu < 2000:
#                 # x = 0.25
#                 procent = (25/100) * salariu
#                 # return procent
#             elif salariu == 2000 and salariu < 4000:
#                 # x = 0.2
#                 procent = (20/100) * salariu
#                 # return procent
#             elif salariu == 4000 and salariu <6000:
#                 # x = 0.15
#                 procent = (15/100) * salariu
#                 # return procent
#             elif salariu  == 6000:
#                 # x = 0.1
#                 procent = (10/100) * salariu
#                 # return procent
#             else:
#                 # x = 0.08
#                 procent = (8/100) * salariu
#                 # return procent
#             return procent
#             # return x
#
#
#
# # ● descrie
# instanta_angajat = Angajat("Gheorghe", "Marin",1500)
# print(instanta_angajat.nume)
# print(instanta_angajat.prenume)
# print(instanta_angajat.salariu)
#
#
# # ● nume_complet()
# print(f'Numele angajatului solitat este {instanta_angajat.nume} {instanta_angajat.prenume}')
#
#
#
# # ● salariu_lunar()
# # # prima varianta # se da in atribut salariul
# # print(f'Salariul lunar al angajatului este: {instanta_angajat.salariu_lunar(1999)}')
#
# # # 2-a var # se ia salariul dat la prima instantare
# print(f'Salariul lunar al angajatului este: {instanta_angajat.salariu_lunar()} ')
#
#
# # ● salariu_anual()
# print(f'Salariul anual este: {instanta_angajat.salariu_anual(1500)}')
#
# # ● marire_salariu(procent)
# print(f'Marirea procentuala pentru salariul angajatului este de: {instanta_angajat.marire_salariu(1500)}')
#
# print(f'Marirea procentuala pentru salariul angajatului este de: {instanta_angajat.marire_salariu(100)}')
# print(f'Marirea procentuala pentru salariul angajatului este de: {instanta_angajat.marire_salariu(2000)}')
# print(f'Marirea procentuala pentru salariul angajatului este de: {instanta_angajat.marire_salariu(4500)}')
# import self as self

'''
# print("Procent: "+"{:.25%}".format(Angajat.marire_salariu(Angajat,1500)))
# print("Procent: "+"{:.2%}".format(Angajat.marire_salariu(Angajat,2000)))
# print("Procent: "+"{:.15%}".format(Angajat.marire_salariu(Angajat,4500)))
# 
# print("{}%".format(instanta_angajat.marire_salariu(1500)))
# print("{}%".format(instanta_angajat.marire_salariu(2500)))
# print("{}%".format(instanta_angajat.marire_salariu(4500)))
# print('{}%'.format(instanta_angajat.marire_salariu(1200)))
'''






# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

# class Cont:
#     iban = None
#     titular_cont = None
#     sold = 12350
#
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def afisare_sold(self, titular_cont, sold, iban):
#         self.titular_cont = titular_cont
#         self.sold = sold
#         self.iban = iban
#         print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei')
#
#     def debitare_cont(self):
#         amount = float(input("Introduceti suma pe care o depozitati: "))
#         self.sold + amount
#         sold_final = self.sold + amount
#         # print(f'\n Suma depozitata: ', amount, + 'si soldul final este: ', sold_final)
#         print(f'Suma depozitata este {amount} si suma soldului curent este: {sold_final}')
#
#
#     def creditare_cont(self):
#         amount = float(input("Introduceti supa pe care o creditati: "))
#         if self.sold > amount:
#             self.sold - amount
#             sold_final = self.sold - amount
#             # print("\n Creditarea este de: ", amount)
#             print(f'Credtarea este de: {amount}, iar soldul curect ramas este: {sold_final}')
#         else:
#             print("\n Sold insuficient !")
#
# # ● afisare_sold()
# instanta_cont = Cont('ING000RO123456789', 'Harap Alb', 15236 )
# print(f'Titularul {instanta_cont.titular_cont} are în contul {instanta_cont.iban} suma de {instanta_cont.sold} lei')
# # ● debitare_cont(suma)
# instanta_cont.debitare_cont()
# # ● creditare_cont(suma)
# instanta_cont.creditare_cont() #100
# instanta_cont.creditare_cont() # 16000 - sold insuficient






# #####Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.

# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
# from datetime import datetime
#
#
# class Factura:
#     serie = 'Ser'
#     numar = None
#     nume_produs = None
#     cantitate = None
#     pret_bucata = None
#
#     def __init__(self, numar, nume_produs, cantitate, pret_bucata, make_array=None):
#         self.data = None
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_bucata = pret_bucata
#
#
#
#     def schimba_cantitatea(self,cantitate):
#         self.cantitate = cantitate
#         print(f'Cantitatea aleasa este: {cantitate}')
#
#     def schimba_pret(self, pret):
#         self.pret_bucata = pret
#         print(f'Pretul ales este: {pret}')
#
#     def schimba_nume_produs(self, produs):
#         self.nume_produs = produs
#         print(f'Numele produsului este: {produs}')
#
#     def genereaza_factura(self): #, numar, data, produs, cantitate, pret_bucata, total
#
#
#
#         print(f'Factura seria {self.serie} numar {self.numar} \n'
#               f'Data: {datetime.now()} \n'
#               f' Produs: |   Cantitate:  |   Pret bucata: |   Total: \n'
#               f' {self.nume_produs:>7} |   {self.cantitate:>8}    |   {self.pret_bucata:>11}  |   {self.cantitate * self.pret_bucata}'
#
#               )
#
#
# instanta_factura = Factura('Ser', 121, 'mere', 5, 3)
# print(instanta_factura.serie)
# print(instanta_factura.numar)
# print(instanta_factura.nume_produs)
# print(instanta_factura.cantitate)
# print(instanta_factura.pret_bucata)
# print(f"Seria si numarul facturii pentru {instanta_factura.nume_produs} este {instanta_factura.serie} {instanta_factura.numar}, numar total de produse {instanta_factura.cantitate} la pretul per bucata de {instanta_factura.pret_bucata} lei")
#
# instanta_factura.schimba_cantitatea(10)
# instanta_factura.schimba_pret(5)
# instanta_factura.schimba_nume_produs("capsuni")
# instanta_factura.genereaza_factura()
#






# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0



class Masina:
    marca = "Seat"
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = 'Gri'
    culori_disponibile = {'Galbena', 'Rosie', 'Albastra', 'Alba', 'Neagra'}
    inmatriculata = False

    def __init__(self,model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Masina este de marca "Seat", model {self.model} si culoarea {self.culoare}, poate atinge viteza maxima de {self.viteza_maxima} km/h \n'
              f'si viteza actuala a masinii este de {self.viteza_actuala} km/h \n'
              f'aceasta are statusul inmatricularii: {self.inmatriculata}')

    def inmatriculataa(self, inmatriculata):
        '''if self.inmatriculata is False:
            self.inmatriculata = True'''
        self.inmatriculata = inmatriculata
        print(f'Masina este inmatriculata: {self.inmatriculata}')

    def vopseste(self,culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
            print(f'Culoarea masinii este {self.culoare}')
        else:
            print(f'Culoarea aleasa nu este disponibila! Alegeti una din lista mentionata aici: {self.culori_disponibile}')

    def acelereaza(self,viteza):
        if viteza < self.viteza_maxima:
            viteza = self.viteza_actuala
            print(f'Viteza masinii este {self.viteza_actuala} km/h')
        elif viteza < 0:
            print(f'Atentie, viteza actuala nu permite accelerare!')
        elif viteza > self.viteza_maxima:
            viteza = self.viteza_maxima
            print(f'Masina va accelera pana la citeza maxima de {self.viteza_maxima} km/h')
        else :
            self.viteza_actuala = self.viteza_maxima

    def franeaza(self):
        if self.viteza_actuala > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            print(f'Masina va frana pana la viteza maxima')


instanta_masina = Masina("Seat", 180)
instanta_masina.descrie()
instanta_masina.inmatriculataa(True)
instanta_masina.vopseste("verde")
instanta_masina.vopseste("Rosie")
instanta_masina.acelereaza(100)






# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
# dict



