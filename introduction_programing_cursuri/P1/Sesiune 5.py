# '''
# o fc este o modalitate prin care putem sa economisim codeo functie putem sa o definim o singura data si apoi sa facem ceea ce se numeste aelare a functiei
# apelarea fc inseamna trimiterea sistemului catre adresa de memorie la care este stocat codul care poarta numele fcntl
#     si la care este stocat codul pe care vrem sa- exec(
#     def unei fc se face cu def
#
#
#     o fc poate sa aiba parametrii, dar nu e a=obligatoriu
#
# chiar daca fc nu are parametrii, parantezele de dupa numele fc sunt obligatorii
#         la def si apelare
#
# un param reprez o info de care fc are nevoie din exterior pt a putea executa toate instructiunile
#
# putem alega sa parameyrizam o fc atunci cand vrem sa poate sa fie luata pt o plaja mai mare de valori
#
#
# exec suma intre 2 nr, putem avea alte 2 nr la fiecare alta rulare
#
#
# o fc poate sa aiba op de return , dar nu este obligatoriu sa aiba
#
# vom alege sa punem op de return pe fc atunci cand vrem sa salv rez acelei fc inytr-lo variabila, sau sa trimitem rezultatul catre un sistem extern
#
#
# '''
#
#
#
# # definirea unei fc simpla si fara paramentri
# '''
# se face cu def'''


def say_hi():
    print('Hi')
    #
    # '''
    # def - keyword care anunta fc
    # say-hi - numele fc
    # () - reprezentatant al zonei in care putem sa specif paramentri
    #     in cazul fc say_hi nu avem paramentrii si parantezele sunt goale
    # : - reprezentant al inceputului corpului fc, locul in care vom incepe sa descriem actiunea pe care trebuie sa o faca fc
    # print ('Hi') - actiunea pe care trebuie sa o faca fc
    #     '''

say_hi()
    #
    # ''' apelarea fc se face specificand numele fc si cele 2 paranteze
    # daca nu avem param lasam parantezele goale\la executarea fc sist apeleaza adresa de memorie care poate numele de say_hi
    # va citi codul stocat la acea adresa de mem si il va executa
    #
    #
    #
    # '''

x = say_hi()
print(x)

'''
x = say_hi()  --- se executa fc chiar daca se va salva in var x
    drept urmare se va printa Hi de 2*
        o data de la linia 47
        si inca o data de la 57
      
print(x)  --- se va printa keyword-ul NONE pt ca fc nu area setatat posibilitatea de a trimite spre exterior valorile\
   
'''



def say_hi_v1():  # nu va mai printa Hi pt ca fc aceasta nu mai are instructiune de print in interiorul ei
    message = 'Hi'
    return message

x = say_hi_v1()
print(x)  # se va printa de data asta cuv de Hi in loc de cuvantul NONE pt ca am instructiune de return in fc



def say_hi_v1():  # nu va mai printa Hi pt ca fc aceasta nu mai are instructiune de print in interiorul ei
    return  'Hi'

x = say_hi_v1()
print(x)





# functie cu parametrii

def print_hi_user(user):
    print(f'Hello {user}')



   #### suplimentar
# ###return "Am sakyatat utilizatorul " + user


'''
user specificat intre paranteze rotunde reprez un tamplate sau o var care va stoca valoarea efectiva al user-u;ui caruia vrem sa ii spunem hallo
user in acolade reprez aceeasi variabila care a venit prin parametru si care va fi folosita pt executarea corpului functiei

apelarea fc se face prin specif in paranteze rotunde a valorii pe care  vrem sa o trimtem

Daca o fc a fost def cu parametrii este obligatoriu sa fie si apalata cu parametrii
la mom apelarii val pe care o scriem intre paranteze se numes argumente

definire = parametrii
apelare  = argumente



!!!  Corpul unei fc va fi def la fel ca la structurile alternative - if si repetitive while, for prin intermediul indentarii - spatiile lasate liber pana la ineputul liniei de cod


'''

print_hi_user('Mihai')




# apelare fc cu input


# user = input("Introdu nume utilizator pe care vrei sa-l saluti")
# print_hi_user(user)



lista_nume = ['a', 'b', 'c', 'd']

for nume in lista_nume:
    print_hi_user(nume)


# functie cu mai multi parametrii
def print_hi_user_npr(nume, prenume):
    print(f'hello {nume} {prenume}')


 # print_hi_user_npr(f'hello {Ion} {ION}')
