class Cont:
    iban = 'Default'
    titular_cont = 'Default'
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} Soldul tau este: {self.sold}')

    def debitare_cont(self, suma):
        sold = self.sold - suma
        return print(f'Soldult tau dupa debitarea sumei {suma} este {sold}')

    def creditare_cont(self, suma):
        sold = self.sold + suma
        return print(f'Soldul tau dupa creditarea sumei de {suma} este de {sold}')


cont1 = Cont(iban='ROBTLR1324700035', titular_cont='Bogdan Mihalcea', sold=300)
cont1.debitare_cont(suma=50)
cont1.creditare_cont(suma=1000)






# self.numar = numar
         self.data = datetime.now()
        # self.nume_produs = produs
        # self.cantitate = cantitate
        # self.pret_bucata = pret_bucata
        # total = self.cantitate * self.pret_bucata
        # print(f'Factura seria {self.serie} numar {self.numar}')
        # print(f'Data: {self.data}')
        # t = Table().with_columns(
        #     'Produs', make_array(self.nume_produs),
        #     'Cantitate', make_array(self.cantitate),
        #     'Pret bucata', make_array(self.pret_bucata),
        #     'Total', make_array(self.cantitate * self.pret_bucata)
        # )
        # return t
        # table = [[instanta_factura.nume_produs, ]]