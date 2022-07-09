# #
# #
# # # # 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# # # # Afișeaz-o:
# # note_muzicale = ('do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do')
# # #print(f' Lista de Note muzicale este:   {note_muzicale}')
# # print(note_muzicale)
# # #
# # # # ---- note_muzicale2= 'do re mi fa sol la si do'
# # # # ---- print(note_muzicale2)
# # print("-------------------1.1------------------------")
# # print("----------------------------------------------")
# # #
# # # # ● Inversează ordinea folosind slicing și suprascrie această listă.
# # reversed_note_muzicale = note_muzicale[::-1]
# # print(reversed_note_muzicale)
# #
# #
# # print("-------------------1.2------------------------")
# # print("----------------------------------------------")
# # #
# # # # ● Printează varianta actuală (inversată).
# # print(reversed_note_muzicale)
# #
# # print("---------------------1.3----------------------")
# # print("----------------------------------------------")
# # #
# # # # ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# # # # adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# # # # deoarece metoda face asta automat.
# # #
# # # # ----def criteria(item):
# # # # ----    return len(item)
# # # # ----note_muzicale2 = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# # # # ----note_muzicale2.sort(reverse= True, key=criteria)
# # # # ----print(note_muzicale2)
# # # # ----note_muzicale2.reverse()
# # # # ----print(note_muzicale2)  #??
# # #
# #     # revers pentru lista: reversed_note_muzicale de mai sus
# # # reversed_note_muzicale.reverse()
# # # print(reversed_note_muzicale)
# # #     # revers pentru lista initiala: note_muzicale
# # note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# # note_muzicale.reverse()
# # print(note_muzicale)
# #
# # print("---------------------1.4----------------------")
# # print("----------------------------------------------")
# # #
# # # # ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# # # # inițială.
# # # #
# # print(reversed_note_muzicale)
# # #
# # # print("---------------------1.5--------------------")
# # # print("--------------------------------------------")
# # #
# # #
# # # # Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
# # # # suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
# # # # suprascrierea automat și permanentizează aceste modificări. Ambele variante
# # # # își găsesc utilitatea în funcție de ce ne dorim în acel moment.
# # #
# #
# # # 2. De câte ori apare ‘do’?
# # #
# # note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# # count= print(note_muzicale.count('do'))
# # # ----print(f'Nota muzicala Do apare de:  {count}')
# #
# # print("----------------------2----------------------")
# # print("---------------------------------------------")
# #
# # # 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# # # Găseste 2 variante să le unești într-o singură listă.
# # #
# # #
# #
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista_unita = lista1 + lista2
# print(lista_unita)
#
#
# ---for i in lista2 :
#   ---  lista1.append(i)
#    --- print(i)


# lista1.append(lista2)
# print(lista1)


# #
# print("----------------------3----------------------")
# print("---------------------------------------------")
#
#
# 4.
# # ● Sortează și afișază lista generată la exercițiul anterior.
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista_unita = lista1 + lista2
# print(lista_unita)
#
# # ----lista_unita_2 = [3, 1, 0, 2, 6, 5, 4]
# # ----print(lista_unita_2)
# # ----lista_unita_2.sort() # Ordine crescătoare
# # ----print(lista_unita_2)
#
#
# lista_unita.sort() # Ordine crescătoare
# print(lista_unita)
#
# lista_unita.sort(reverse=True) # Ordine descrescatoare
# print(lista_unita)
#
#
# print("---------------------4.1---------------------")
# print("---------------------------------------------")
#
# # ● Sortează numărul 0 folosind o funcție.
# # lista_unita.sort()
# print(lista_unita.index(0))
#
#
# print("----------------------4.2--------------------")
# print("---------------------------------------------")
#
# # ● Afișaza iar lista.
#
# print(lista_unita)
# #
# print("----------------------4.3--------------------")
# print("---------------------------------------------")


# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:   ---  ///// cu if else
# ● Lista este goală.
# ● Lista nu este goală.
#
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista_unita = lista1 + lista2
# print(lista_unita)
#
#
# if lista_unita ==0:
#     print('Lista este goala.')
# else:
#     print('Lista nu este goala')


####corect cu if else
# if not lista_unita:
#     print('Lista este goala!')
# else:
#     print('Lista nu este goala!')

# print("----------------------5----------------------")
# print("---------------------------------------------")


# 6. Folosește o funcție care să șteargă lista de la exercițiul 3. //// delete clear

# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista_unita = lista1 + lista2
# print(lista_unita)
#
# lista_unita.clear()
# print(lista_unita)
#
#
# print("----------------------6-----------------------")
# print("----------------------------------------------")

# 7. Copy paste la exercițiul 5. Verifică încă o dată.///// de facut cu del

# Acum ar trebui să se afișeze că lista e goală.

# if lista_unita ==0:
#     print('Lista este goala.')
# else:
#     print('Lista nu este goala')

   ## ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????
   # daca if ==0 Lista nu este goala
   # daca if !=0 Lista este goala?????



   ## var corecta
# if not lista_unita:
#     print('Lista este goala!')
# else:
#     print('Lista nu este goala!')


# print("----------------------7-----------------------")
# print("----------------------------------------------")

# # 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# # Folosește o funcție că să afișezi Elevii (cheile)
#
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())
#
#
# print("----------------------8-----------------------")
# print("----------------------------------------------")
#
# # 9. Printează cei 3 elevi și notele lor
# # Ex: ‘Ana a luat nota {x}’
# # Doar nota o vei lua folosindu-te de cheie
#
#
#
# for key, value in dict1.items():
#     print("Key : {} a luat nota  : {}".format(key, value))
#
#
# print("----------------------9-----------------------")
# print("----------------------------------------------")
#
#
# # 10. Dorel a făcut contestație și a primit 6
# # ● Modifică nota lui Dorel în 6
# # ● Printează nota după modificare
# dict1.update({'Dorel':'6'})
# print(dict1)
#
# print("----------------------10----------------------")
# print("----------------------------------------------")

# # 11. Gigel se transferă din clasă
# # ● Căuta o funcție care să îl șteargă
# # ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# # ● Printează noii elevi
#
# dict1.pop('Gigel')
# dict1['Ionica']= '9'
# print(dict1)
#
# print("----------------------11----------------------")
# print("----------------------------------------------")


# 12.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# # # ---- print(zile_sapt)
# #
# # # ---- zile_sapt.inset(0,'luni')
# # # ---- print(zile_sapt)
# #
# zile_sapt.add('luni')
# print(zile_sapt)
#
# print("----------------------12----------------------")
# print("----------------------------------------------")
#
# # 13.Folosește un if și verifică dacă:                                                  ////  is subset
# # ● Weekend este un subset al zilelor din săptămânii.
# # ● Weekend nu este un subset al zilelor din săptămânii.
zile_sapt = ['luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică']
weekend = {'sâmbăta', 'duminică'}
#
# # ---- if weekend.() > 0:
# # ----     print('Yes, weekend in zile_sapt')
# # ----- else:
# # -----     print('NO, weekend not in zile_saptamana')
#
#
#
# check = all(item in zile_sapt for item in weekend)
# if check is True:
#     print('Lista zile_sapt contine elemente din lista weekend {}'.format(weekend, zile_sapt))
# else:
#     print('NO')



###de la Octavian
# if weekend.issubset(zile_sapt):
#     print('Weekend este un subset al zilelor din săptămânii')
#
# else:
#     print('Weekend nu este un subset al zilelor din săptămânii')


### de la Luci
# if (weekend.issubset(zile_sapt)):
#     print('Weekend este un subset al zilelor saptamanii')
# '''
# ● Weekend nu este un subset al zilelor din săptămânii.
# '''
# if (not weekend.issubset(zile_sapt)):
#     print('Weekend nu este un subset al zilelor săptămânii')


# #
# # print("----------------------13----------------------")
# # print("----------------------------------------------")
#
# # 14. Afișează diferențele dintre aceste 2 seturi.
#
#


# print('Diferenta dintre cele doua set-uri este ', zile_sapt.difference(weekend))
# # #print(weekend - zile_sapt)
# #
# #
# # print("----------------------14----------------------")
# # print("----------------------------------------------")
#
# # 15. Afișază intersecția elementelor din aceste 2 seturi.
#
# intersectie = zile_sapt.intersection(weekend)
# print(intersectie)
#
# #print(zile_sapt|weekend)
#
#
#
# intersectie = zile_sapt.intersection(weekend)
# if intersectie == zile_sapt.intersection(weekend):
#     print(intersectie)
#
#
# print("----------------------15----------------------")
# print("----------------------------------------------")



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









jucatori = ['Andrei', 'Rafael', 'Domide', 'Stefan', 'Andone']
schimbari_max = 3
schimbariMaximAdmise = 3
schimbari_efectuate = 0  #////3

if (schimbari_efectuate < 0 or schimbari_efectuate >= schimbari_max):
    schimbariMaximAdmise -= 1
    schimbari_efectuate = schimbariMaximAdmise
    print('Nu sunt schimbari disponibile')
else:
    iesire = input()
    intrare = 'Zare'
    if ('Andrei'in iesire or 'Rafael' in iesire or 'Domide' in iesire or 'Stefan' in iesire or 'Andone' in iesire):
        schimbariMaximAdmise -= 1
        schimbari_efectuate = schimbariMaximAdmise
        jucatori.remove(iesire)
        jucatori.append(intrare)
        print(f'a intrat {intrare} a ieșit {iesire} mai ai {schimbari_efectuate} schimbări')
        print(f'Noua lista de jucatori {jucatori}')
    else:
        schimbariMaximAdmise -= 1
        schimbari_efectuate = schimbariMaximAdmise
        print(f'nu se poate efectua schimbarea deoarece jucătorul {iesire} nu e în teren')
        print(f'Mai ai {schimbari_efectuate} schimbari')



