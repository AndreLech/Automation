 # 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# Afișeaz-o:

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(f' Lista de Note muzicale este:   {note_muzicale}')
#print(note_muzicale)

print("-------------------1.1------------------------")


# ● Inversează ordinea folosind slicing și suprascrie această listă.

reversed_note_muzicale = note_muzicale[::-1]
note_muzicale= reversed_note_muzicale


print("-------------------1.2------------------------")

# ● Printează varianta actuală (inversată).

print(note_muzicale)

print("---------------------1.3----------------------")


# ● Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
note_muzicale.reverse()


print("---------------------1.4----------------------")

# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială
print(note_muzicale)


print("---------------------1.5--------------------")



# # # # Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
# # # # suprascrierea automat și permanentizează aceste modificări. Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment.


# 2. De câte ori apare ‘do’?
count= print(note_muzicale.count('do'))

print(f'Do apare de {note_muzicale.count("do")} ori')

print("----------------------2----------------------")




# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găseste 2 variante să le unești într-o singură listă.

# var 1
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista_unita = lista1 + lista2
print(lista_unita)

# var 2
lista1.append(lista2)
print(lista1)

print("----------------------3----------------------")

# 4.
# ● Sortează și afișază lista generată la exercițiul anterior.

lista_unita.sort()
print(lista_unita)

print("---------------------4.1---------------------")

# ● Sortează numărul 0 folosind o funcție.
# lista_unita.sort()
print(lista_unita.index(0))

print("----------------------4.2--------------------")

# ● Afișaza iar lista.

print(lista_unita)
print("----------------------4.3--------------------")



# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:

if not lista_unita:
    print('Lista este goala!')
else:
    print('Lista nu este goala!')


print("----------------------5----------------------")



# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.


lista_unita.clear()
print(lista_unita)

print("----------------------6-----------------------")

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.


if not lista_unita:
    print('Lista este goala!')
else:
    print('Lista nu este goala!')

print("----------------------7-----------------------")


# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)


dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

print("----------------------8-----------------------")


# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie


for key, value in dict1.items():
    print(" {} a luat nota: {}".format(key, value))

print("----------------------9-----------------------")


# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
dict1.update({'Dorel':'6'})
print(f"Dorel si-a marit nota la {dict1['Dorel']}")

print("----------------------10----------------------")


# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi

dict1.pop('Gigel')
dict1['Ionica']= '9'
print(dict1)


print("----------------------11----------------------")


# 12.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}


zile_sapt.add('luni')
print(zile_sapt)

print("----------------------12----------------------")


# # 13.Folosește un if și verifică dacă:
# # ● Weekend este un subset al zilelor din săptămânii.
# # ● Weekend nu este un subset al zilelor din săptămânii.

check = all(item in zile_sapt for item in weekend)
if check is True:
    print('Lista zile_sapt contine elemente din lista weekend {}'.format(weekend, zile_sapt))
else:
    print('NO')

print("----------------------13----------------------")


# 14. Afișează diferențele dintre aceste 2 seturi.

print('Diferenta dintre cele doua set-uri este ', zile_sapt.difference(weekend))

print("----------------------14----------------------")


# 15. Afișază intersecția elementelor din aceste 2 seturi.

intersectie = zile_sapt.intersection(weekend)
print(intersectie)

print("----------------------15----------------------")



## Exercitiu Optional
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori
# Google search hint
# “how to check if item îs în list python”




Echipa_de_fotbal = ()
Schimbari_MAX_admine = 3
Jucatori_teren = ['Andrei', 'Mihai', 'Alexandru', 'George', 'Tudor']
Jucatori_rezerva = ['Cristi', 'Marian', 'Mircea', 'Dorel', 'Grigore']
Shimbari_efectuate = 0
Schimbari_max = 3


