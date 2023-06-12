# Pirma užduotis - OOP #1:
# Susikurti klasę “BankoSąskaita”, kuri saugotų sąskaitos numerį ir balansą. Klasė turi
# turėti metodus pinigų pridėjimui prie balanso, pinigu išėmimui bei balanso grąžinimui.
#
# Susikurti “BankoSąskaita” klasės objektą ir išbandyti visus metodus bent po vieną kartą.
#
#
# # Create a bank account object
# account = BankAccount("1234567890")
#
# # Deposit funds
# print(account.deposit(1000))
#
# # Withdraw funds
# print(account.withdraw(500))
#
# # Check account balance
# balance = account.get_balance()
# print("Account Balance:", balance)

class BankoSaskaita():
    def __init__(self, saskaita):
        if saskaita >= 0:
            self.saskaita = saskaita
        else :
            print("Jūsų sąskaitoje turi būti pinigų :(. Negalime sukurti tokios sąskaitos")

    def ideti_pinigus(self, idedama_suma):
        try:
            if idedama_suma > 0 :
                self.saskaita = self.saskaita + round(idedama_suma, 2)
                return f"Jūs į savo sąskaitą įdėjote {round(idedama_suma, 2)}. Jūsų pinigų likutis yra {round(self.saskaita, 2)}"
            else :
                print("Kažkas negerai. Įveskite validžią sumą")
        except :
            return "Nėra tokios banko sąskaitos"
    def isimti_pinigus(self, isimama_suma):
        try:
            if isimama_suma > 0 and isimama_suma <= self.saskaita:
                self.saskaita = self.saskaita - round(isimama_suma, 2)
                return f"Jūs išsiėmėte {round(isimama_suma, 2)}. Jūsų pinigų likutis yra {round(self.saskaita, 2)}"
            else :
                print("Kažkas negerai. Įveskite validžią sumą, kurią norite išsiimti.")
        except:
            return "Nėra tokios banko sąskaitos"
    def balansas(self):
        try :
            return f"Jūsų sąskaitos balansas yra {round(self.saskaita, 2)}"
        except :
            return "Nėra tokios banko sąskaitos"

saskaita_8789 = BankoSaskaita(2000)
print(saskaita_8789.ideti_pinigus(500))
print(saskaita_8789.balansas())
print(saskaita_8789.isimti_pinigus(-8900))

saskaita_4456 = BankoSaskaita(555.4)
print(saskaita_4456.ideti_pinigus(44.78))
print(saskaita_4456.isimti_pinigus(5.4487))
print(saskaita_4456.balansas())

saskaita_0758 = BankoSaskaita(-4)
print(saskaita_0758.balansas())
print(saskaita_0758.ideti_pinigus(12))
print(saskaita_0758.isimti_pinigus(78.99))

saskaita_1120 = BankoSaskaita(800.78)
print(saskaita_1120.ideti_pinigus(0.17))
print(saskaita_1120.isimti_pinigus(900))
print(saskaita_1120.balansas())

