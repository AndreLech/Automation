#
#
# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat','Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
import heapq

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     if masini[i] == 'BMW':
#         print(f'Mașina mea preferată este {masini[i]}')
#
# for masina in masini:
#     if masina == 'Audi':
#         print(f'Mașina mea preferată este {masina}')
#
# index = 0
# while masini(index) == 'Fiat' and index < len(masini):
#     index += 1
#     print(f'Mașina mea preferată este ' + masini(index))

# 2. Aceeași listă:
# Folosește un for else
# În for - Modifică elementele din listă astfel încât să fie scrie cu majuscule, exceptând primul și ultimul.
# În else: - Printează lista.
#
# for i in range(1, len(masini) -1):
#     masini[i] = masini[i].upper()
# else:
#     print(masini)


# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un v.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

# for i in range(len(masini)):
#     if masini[i] == 'Mercedes':
#         print('Am găsit mașina dorită de dvs!')
#         break
# else:
#     print('Am găsit mașina {masini[i]}. Mai căutam')


# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cuexcepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# - Printează S-ar putea să vă placă mașina x.

# for masina in masini:
#     if masina == "Trabant" or masina =="Lăstun":
#         continue
#     print(f"S-ar putea să vă placă mașina {masina}")


# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.

# masini_vechi = []
# for i in range(len(masini)):
#     if masini[i] == 'Trabant' or masini[i] == 'Lăstun':
#         masini_vechi.append(masini[i])
#         masini[i] == 'tesla'
# print(f'Modele vechi: {masini_vechi}')
# print(f'Modele noi: {masini}')





# 6. Având dict:
pret_masini = { 'Dacia': 6800,
                'Lăstun': 500,
                'Opel': 1100,
                'Audi': 19000,
                'BMW': 23000}
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.
buget = 15000

# for key, value in pret_masini.items():
#     if value <= buget:
#         print(f'Pentru un buget de sub 15000 euro puteți alege mașină {key}')







# 7. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
# contor = 0

# for i in range(len(numere)):
#     if numere[i]==3:
#         contor += 1
#         print(f'Cifra 3 apare  de {contor} ori')





# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

# suma_i = 0
#
# for x in numere:
#     if x!=0:
#         suma_i = suma_i + x
# print("Suma numerelor =", suma_i)





# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).



# print(f'Valoarea maximă este {heapq.nlargest (1, numere)}')

#
# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

def convert(numere):
    return [-i for i in numere]
print(convert(numere))