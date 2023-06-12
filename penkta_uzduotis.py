# Penkta užduotis - Pillow
# Sukurti programa, kuri uždėtų nuotraukai kontrastą ir išsaugotų atnaujintą nuotrauką

from PIL import Image, ImageEnhance

def kontrastas(jusu_nuotrauka, jusu_kontrastas):
    foto = Image.open(jusu_nuotrauka)
    prison_ = ImageEnhance.Contrast(foto)
    prison_.enhance(jusu_kontrastas).save("kontrasto_nuotrauka.jpg")

# Mano programa yra funkcija kontrastas. Apačioje ištestuoju programą. Galėčiau funkciją parašyti su input, bet sąlygoje
# nepatikslinta, kokia programa turi būt tai pasirinkau lengvesnį variantą

kontrastas("mike.jpg", 4)
nauja_nuotrauka = Image.open("kontrasto_nuotrauka.jpg")
nauja_nuotrauka.show()