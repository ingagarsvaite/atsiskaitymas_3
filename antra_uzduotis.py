# Antra užduotis - OOP #2:
#
# Susikurti klasę “Figūra”, kuri saugoja ilgį ir plotį. Klasė turi turėti metodus plotui ir perimetrui
# apskaičiuoti ir grąžinti
#
# Susikurti klasę “Stačiakampis”, kuris paveldi iš “Figūra”. Stačiakampio klasėje turi būti įgyvendinti
# stačiakampio ploto ir perimetro skaičiavimo metodai.
#
# Susikurti klasę “StatusisTrikampis”, kuris paveldi iš “Figūra”. Trikampio klasėje turi būti įgyvendinti
# stačiojo trikampio ploto ir perimetro skaičiavimo metodai.
#
# Susikurti bent po vieną stačiakampį ir trikampį, atspausdinti jų plotus ir perimetrus

import math

class Figura:
    def __init__(self, ilgis, plotis):
        self.ilgis = ilgis
        self.plotis = plotis

    def skaiciuoti_plota(self):
        print(f"Jei jūsų figūra yra stačiakampis, jūsų figūros plotas yra {self.ilgis*self.plotis}")

    def skaiciuoti_perimetra(self):
        print(f"Jei jūsų figūra yra lygiagretainis, jūsų figūros plotas yra {2*self.ilgis+2*self.plotis}")

# Nelabai supratau, kaip įgyvendinti ploto skaičiavimą Staciakampis klasėje. Nutariau sprendimui pasirinkti kitą approach,
# tam, kad geriau prisiminčiau, kaip skirtingai pritaikyti paveldėjimą.
# Buvo mintis Figura klasese skaiciuoti_plota ir skaiciuoti_perimetra
# funkcijose parasyti pass ir paveldimose klasėse sukurti naujas, nutariau
# padaryti kiek kitaip. Attributes ilgis ir plotis neatitinka trikampio charakteristikų.
class Staciakampis(Figura):
    pass

class StatusisTrikampis(Figura):
    def skaiciuoti_plota(self):
        print(f"Stačiojo trikampio plotas yra {self.ilgis*self.plotis*0.5}")
    def skaiciuoti_perimetra(self):
        izambine = math.sqrt(self.ilgis**2 + self.plotis**2)
        print(f"Stačiojo trikampio perimetras yra {self.ilgis + self.plotis + round(izambine, 2)}")


mano_staciakampis = Staciakampis(5, 8)
print(mano_staciakampis.skaiciuoti_plota())
print(mano_staciakampis.skaiciuoti_perimetra())

mano_trikampis = StatusisTrikampis(3, 4)
print(mano_trikampis.skaiciuoti_plota())
print(mano_trikampis.skaiciuoti_perimetra())

tavo_trikampis = StatusisTrikampis(4, 4)
print(tavo_trikampis.skaiciuoti_plota())
print(tavo_trikampis.skaiciuoti_perimetra())

#
# # Testing the classes
# rectangle = Rectangle(5, 10)
# triangle = RightTriangle(3, 4)
#
# print("Rectangle Information:")
# print("Area:", rectangle.calculate_area())
# print("Perimeter:", rectangle.calculate_perimeter())
# print()
#
# print("Right Triangle Information:")
# print("Area:", triangle.calculate_area())
# print("Perimeter:", triangle.calculate_perimeter())


