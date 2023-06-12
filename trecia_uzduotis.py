# Trečia užduotis - Logging
#
#
# Sukurti programa, kuri paprašytų įvesti stačiakampio ilgį ir plotį. Sukurti funkcija,
# kuri priimtų ilgį ir plotį, apskaičiuotų plotą bei perimetrą ir juos grąžintų. Gautą rezultatą
# išspausdinti į terminalą. Taip pat, reikia į programą pridėti loggerį ir
# išlogginti rezultatą (plotą ir perimetrą) į failą.



# logging.basicConfig(filename='plotas.log', encoding="UTF-8", filemode= 'w',
# level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("plotas.log", mode = "w"),
        logging.StreamHandler(sys.stdout)
    ]
)



def staciakampio_parametrai(ilgis, plotis):
    plotas = ilgis * plotis
    perimetras = 2*ilgis + 2*plotis
    logging.info(f"Jūsų stačiakampio plotas yra {plotas}, o perimetras - {perimetras}")

ilgis = float(input("Įveskite stačiakampio ilgį: "))
plotis = float(input("Įveskite stačiakampio plotį: "))
staciakampio_parametrai(ilgis, plotis)

