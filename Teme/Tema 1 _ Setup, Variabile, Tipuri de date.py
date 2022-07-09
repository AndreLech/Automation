'''
                Exerciții Recomandate - grad de dificultate: Ușor

1. Revizualizează întâlnirea 1 și ia notițe în caz că ți-a scăpat ceva.
    -> Done!

2. Vizualizează din videoul ‘Primii pași în Programare’:
    - Variabile și Tipuri; -> NOT Done!
    - Operatori și Flow Control. -> NOT Done!
'''



'''
                Exerciții obligatorii - grad de dificultate: Ușor spre Mediu
'''

#1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# R: o zona din memoria calculatorului care tine anumite date date

'''


#2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă :
# R: string
carte = 'Harap alb'

# R: int
nr_carte = 1

# R: float
pret_carte = 12.33

# R: bool
citit = True



# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(carte))          # <class 'str'>
print(type(nr_carte))       # <class 'int'>
print(type(pret_carte))     # <class 'float'>
print(type(citit))          # <class 'bool'>


# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.

pret_carte = 12.33
print(round(pret_carte))  # 12
        #round(pret_carte)
pret_carte = round(12.33)
print(pret_carte)




# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print('Ultima carte citita este: ' + (carte))
print('Aceasta este cartea nr ' + str(nr_carte) + ' din biblioteca')
print('Pretul acestei carti este ' + str(pret_carte))
print('Citita? ' + str(citit))



# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.

input('Numele este: ')
#nume_len = input('Numele este: ')
input('Prenumele este: ')
#prenume_len = input('Prenumele este: ')

nume = 'Ana'
prenume = 'Mers'
print('Numele complet are ' + str(len((nume) + (prenume))) + ' caractere')




# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.

input('Lungimea: ')
input('Latimea: ')

lungime = 2
latime = 4
print('Aria dreptunghiului este: ' + str(lungime * latime))
'''


# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - citește de la tastatură un int x;
# - afișează stringul fără ultimele x caractere.
# ex: Dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'.


# expresion = 'Coral is either the stupidest animal or the smartest rock'
# # - citește de la tastatură un int 11;
# #//print(expresion)
# #input(expresion [11])
#
# # - afișează stringul fără ultimele x caractere.
# #print(len(expresion)) #--57
# print(expresion[0:45])




# # 9. Același string:
# expresion = 'Coral is either the stupidest animal or the smartest rock'
# # - hint: este o funcție care te ajută să faci asta;
# # folosind această variabilă + slicing, afișează tot stringul până la acestcuvânt.
# # Output: 'Coral is either the stupidest animal or the smartest'
#
# # a. declară un string nou care să fie format din primele 5 caractere + ultimele 5;
# print(expresion[0:5] + expresion[52:57])
#
# # b. afișează de câte ori apare cuvântul 'the';
# print(expresion.count('the')) #--3 ori
# print(f'Cuvantul the apare de ' + str(expresion.count('the')) + ' ori')
#
# # c. înlocuiește ‘the’ cu ‘THE’ peste tot - printează rezultatul;
# print(expresion.replace('the', 'THE'))
#
# # d. salvează într-o variabilă și afișează indexul de start al cuvântului ‘rock’;
# expresion_1 = 'Coral is either the stupidest animal or the smartest rock'
# print(expresion_1.index('rock'))  #--53



# 10. Exercițiu:
# Observație: se va folosi un assert.
# Atenție: se dorește că programul să fie case insensitive - 'apA' e acceptat.

# # - citește de la tastatură un string;
# nume = input('Introduceti string value: ')     #Antoanella
# print(nume)
# ##nume = 'Antoanella'
#
# # - verifică dacă primul și ultimul caracter sunt la fel. ---?????
# print(len(nume))
# assert nume[0:1] == nume[9:10]





# # 11. Având stringul '0123456789':
# # - hint: folosește slicing, controlează din pas.
#
# # - Afișează doar numerele pare;
# sir = '0123456789'
# print(len(sir))
# print(sir[0:9:2])   #nr par
#
# # - Afișează doar numerele impare;
# print(sir[1:10:2])  # nr impar



# 12. Utilizand stringul de la 9.d.
# - hint: merge cu slicing? Probabil că nu... Ce mai știi atunci legat de string?
# Poate găsești o funcție ajutătoare.

# - folosește un assert că să verifici dacă acest string conține doar numere;
sir = '0123456789'
# print(sir.isnumeric())
# if sir.isnumeric():
#     print('Is numeric')
# else:
#     print('NOT numeric')





'''
Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai
nevoie de Google).
'''


# 1. Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# impar = input('Introduceti numere impare: ')        # 123
# print(impar)
# if int(impar) / 2 ==0:
#     print('Nr par')
# else:
#     print('Nr impar')


# # - afișează caracterul din mijloc.
# list = [1, 2, 3, 4, 5, 6]
# print(list[:3])
# print(list[3:])





# # 2. Folosind assert, verifică dacă un string este palindrom
#
# palindrom = input('Introdu cuvant: ')       ##ana
# if str(palindrom) == str(palindrom)[::-1]:
#     print('Este Palidrom!')
# else:
#     print('Nu este!')




# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

# word1, word2 = ('alabala portocala').split()
# print(word1)
# print(word2)




#
# 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
string = input('Introdu noul string: ')












