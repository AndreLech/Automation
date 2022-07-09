# Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite
# pentru a testa. Daca functia are return, printati raspunsul


# 1.Funcție care să calculeze și să returneze suma a două numere
# lista1 = [2, 3]
# print(sum(lista1))
# print(sum(lista1,7))

# def sum_nr(nr1, nr2):
#     suma= nr1 + nr2
#     return suma
# print(sum_nr(2,3))


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
# def numar(nr):
#     if nr % 2 == 0:
#         return True
#     else:
#         return False
# print(numar(9))
# print(numar(4))


# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

# def nr_caractere (nume):
#     return len(nume)
# print(nr_caractere('Lechea'))
# print(nr_caractere('Andreea'))
# print(nr_caractere('A'))


# 4. Funcție care returnează aria dreptunghiului

# def arie(lungime, latime):
#     return lungime * latime
# print(arie(7,5))
#
# print(arie(2,4))

# 5. Funcție care returnează aria cercului
# import math
#
# ## print(math.pi)
# def cerc(raza ):
#     return math.pi * raza
# print(cerc(15))
# print(cerc(7))


# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.


# def string(librarie):
#     for x in string:
#         return True
#     else:
#         return False
# print('Caracterul exista?')


####??????????????????????????????????????????????????????????????


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y


# def caractere(string):
#     lista1 = 0
#     lista2 = 0
#
#     for l in string:
#         if l.islower():
#             lista1 += 1
#         elif l.isupper():
#             lista2 += 1
#     print('Nr de caractere lower case este', lista1)
#     print('Nr de caractere upper case este', lista2)
#
# caractere('Lista CARACTERE date in STRING')


# 8. Funcție care primește o LISTA dxe numere și returnează o LISTA doar cu
# numerele pozitive

# nr_pozitive = []
# def lista_nr (numere):
#     for l in numere:
#         if numere[numere.index(l)]>0:
#             nr_pozitive.append(l)
#         else:
#             pass
#     return nr_pozitive
# print(lista_nr(numere=[1, -2, 3, -4, 5, 2, -3]))
#
# print(lista_nr(numere=[2, -1, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, -17]))


# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

#
# def noreturn(x, y):
#     if x>y:
#         print('Primul număr x este mai mare decat al doilea nr y')
#     elif y>x:
#         print('Al doilea nr y este mai mare decat primul nr x')
#     else:
#         print('Numerele sunt egale.')
# print(noreturn(2,3))
# print(noreturn(5,4))
# print(noreturn(7,7))

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False


# def make_set(nr, set):
#         if nr not in set:
#         print('am adaugat numărul nou în set')
#         return True
#     elif nr in set:
#         print('nu am adaugat numărul în set. Acesta există deja')
#         return False
# print(make_set(5,(2,3)))
# print(make_set(6,(6,8)))


#
# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna


# from calendar import monthrange
#
#
# def number_of_days_in_month(year=2022, month=6):
#     return monthrange(year, month)[1]
# print(number_of_days_in_month(2022,6))
# print(number_of_days_in_month(2022,7))


# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)
#







# 3. Funcție care primește o lista de cifre (adică doar 0-9) # Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră

#  dict { 0: 0
#         1: 2
#         2: 0
#         3: 1
#         4: 0
#         5: 3
#         6: 0
#         7: 2
#         8: 0
#         9: 1}

# counts = {}        # A dictonary to store the final frequencies.# We will iterate from 0 (which is a valid count) to the maximum count
# for i in range(0,max(dict.values())+1):
#     # Find all values that have the current frequency, count them
#     #and add them to the frequency dictionary
#     counts[i] = len([x for x in dict.values() if x == i])
#
# for key in sorted(counts.keys()):
#   if counts[key] > 0:
#      print (key,":",counts[key])


# def CountFrequency(my_list):
#     freq = {}
#     for item in my_list:
#         if (item in freq):
#             freq[item] += 1
#         else:
#             freq[item] = 1
#     for key, value in freq.items():
#         print("% d : % d" % (key, value))
#
# if __name__ == "__main__":
#     my_list = [1, 3, 1, 5, 9, 7, 7, 5, 5]
#     CountFrequency(my_list)



# def CountFrequency(my_list2):
#     freq = {}
#     for item in my_list2:
#         if (item in freq):
#             freq[item] += 1
#         else:
#             freq[item] = 1
#     for key, value in freq.items():
#         print("% d : % d" % (key, value))
#
#
# if __name__ == "__main__":
#     my_list2 = [1,2,3,4,3,4,3,5,6,5,6,6,7,8,9,6,7,9,0]
#     CountFrequency(my_list2)

# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
# def maximum(a, b, c):
#     list = [a, b, c]
#     return max(list)
#
# x = int(input("Enter First number "))
# y = int(input("Enter Second number "))
# z = int(input("Enter Third number "))
# print("Maximum Number is = ", maximum(x, y, z))




# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

n = input("Enter Number to calculate sum ")
n = int (n)
total_numbers = n
sum=0
while (n >= 0):
    sum += n
    n-=1
print ("Sum is = ", sum)



# Exerciții Opționale - Bonus
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune
#
# Exemplu:
# list1 = [1, 1, 2, 3]
#
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}





# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.
#



# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)




# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)
