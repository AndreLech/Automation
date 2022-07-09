# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
#   executarea unui cod in anumite conditii daca sunt indeplinite sau nu
#   if - decide daca o anumita conditie este adevarata sau falsa si daca executa codul sau nu
#   if else - if -> executa codul daca conditia este True
#           - else -> ececuta codul chiar daca conditia este false



# 2. Verifică și afișează dacă x este număr natural sau nu.
# x = int(input('Introduceti numarul:'))
# print('Numarul introdus este:',x)
# if (x>=0):
#     print ('Numarul este natural!')
# elif (x<0):
#     print ('Numarul nu este natural!')




# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
# x = float(input (str("Enter a number: ")))
# if x> 0:
#     print("Positive number!")
# elif x == 0:
#     print("Zero, neutral number!")
# else:
#     print("Negative number!")




# 4. Verifică și afișează dacă x este între -2 și 13.
# x = int(input('Introduceti numarul:'))
# print('Numarul introdus este:',x)
# if (x >= -2 and x <= 13):
#     print(f'{x} in interval -2 and 13')
# else :
#     print(f'{x} outside interval')









# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
# x = 9
# y = 3
#
# first = x - y
# print(first)
# # second = y-x
# # print(second)
#
# if (x-y) < 5:
#     #--or (y-x) < 5:
#     print('The diff lower that 5')
# else:
#     print('the diff exeed 5')






# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
# x = int(input('Introduceti numarul:'))
# print('Numarul introdus este:',x)
#
# print (not(x >= 5 and x <= 27))
#






# 7.
# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
# x = 9
# y = 3
#
# if x == y:
#     print('Number x equal number y ')
# elif x>y:
#     print('Number x is greater that number y')
# else:
#     print('Number y is greater that number x')



# 8.
# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
# ab = int(input('Introduceti latura 1: '))
# ac = int(input('Introduceti latura 2: '))
# bc = int(input('Introduceti latura 3: '))
#
# if (ab==ac!=bc or ab==bc!=ac or ac==bc!=ab):
#     print('Triunghi isoscel!')
# elif (ab==ac==bc):
#     print('Triunghi echilateral!')
# else:
#     print('Triunghi oarecare!')



# 9. Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu
# litera = str(input('Introduceti o litera: '))
# if litera in ['a', 'e', 'i', 'o', 'u', 'ă', 'î', 'â']:
#     print('Litera introdusa este o vocala!')
# else:
#     print('Litera introdusa este o consoana!')



# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F


# nota = float(input('Nota acordata este: '))
# if nota>=9:
#     print('Calificativ acordat: A!')
# if (nota>=8 and nota<9):
#     print('Calificativ acordat: B!')
# if (nota>=7 and nota<8):
#     print('Calificativ acordat: C!')
# if (nota>=6 and nota<7):
#     print('Caloficativ acordat: D!')
# if (nota>=4 and nota<6):
#     print('Calificativ acordat: E!')
# if nota<4:
#     print('Calicativ acordat: F')





#####!!!!!De facut!!!!!!!!!!-----------------------------------------------------------------------------------------------------------------------

#
#
# Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google.
#
# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
#
#
#
#
#
# 2.Verifică dacă x are exact 6 cifre.
#
#
#
#
#
#
# 3.Verifică dacă x este număr par sau impar (x e int).
#
#
#
#
#
#
# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?
#
#
#
#
#
#
#
# 5.
# X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
#
#
#
#
#
#
#
#
# Exerciții Bonus (may need google) .
#
# 1.Verificare îmbarcare persoane
# Ține minte următoarele date:
# - Vârstă;
# - Însoțit de mama;
# - Însoțit de tata;
# - Pașaport;
# - Act permisiune mama;
# - Act permisiune tata.
#
# Condiții de îmbarcare
# - Dacă pers are vârstă peste 18 ani și are pașaport.
# - Dacă pers are sub 18 ani, are pașaport și e însoțită de ambii părinți.
# - Dacă pers are sub 18 ani, are pașaport, e însoțită de cel puțin un părinte
# și are permisiune în scris de la celalat părinte.
#
# ● Aici vreau să testezi codul cu toate variantele posibile.
# ● Să generezi cazuri de test și expected result, apoi să rulezi codul și să
# completezi actual results.
#
# Ex:
# Vârstă 19 ani, nu am pașaport => Nu mă pot îmbarca.
# Vârstă 17 ani, am pașaport, ambii părinți => Mă pot îmbarca.
# Etc
#
#
#
#
#
#
#
# 2. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random.
# Ne imaginam că dăm cu zarul și salvăm acest număr în dice_roll.
# Ia un număr ghicit de la utilizator.
# Verifică și afișază dacă utilizatorul a ghicit 3 opțiuni:
# - Ai pierdut. Ai ales un număr mai mic. Ai ales x dar a fost y.
# - Ai pierdut. Ai ales un număr mai mare. Ai ales x dar a fost y.
# - Ai ghicit. Felicitări? Ai ales x și zarul a fost y.
#
#


