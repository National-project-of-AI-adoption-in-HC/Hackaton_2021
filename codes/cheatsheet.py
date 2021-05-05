import pandas as pd

folder_name = './data/final_data'

# Nacitanie Ciselnikov
ciselnik_odbornost_lekar = pd.read_csv('{}/ciselniky/odbornost_lekara.csv'.format(folder_name))
ciselnik_odbornost_ambulancia = pd.read_csv('{}/ciselniky/odbornost_ambulancia.csv'.format(folder_name))
ciselnik_sdl_lieky = pd.read_csv('{}/ciselniky/sdl_lieky_ciselnik.csv'.format(folder_name))
ciselnik_lieky = pd.read_csv('{}/ciselniky/vybrane_lieky_ciselnik.csv'.format(folder_name))
ciselnik_poistenec = pd.read_csv('{}/ciselniky/poistenci_ciselnik.csv'.format(folder_name))
ciselnik_diagnoza = pd.read_csv('{}/ciselniky/diagnozy_ciselnik.csv'.format(folder_name))
ciselnik_vykon = pd.read_csv('{}/ciselniky/katalog_vykonov.csv'.format(folder_name))

# Nacitanie dat do Pandas DataFrame
VLD = pd.read_csv('{}/VLD.csv'.format(folder_name))
VLDD = pd.read_csv('{}/VLDD.csv'.format(folder_name))
GYN = pd.read_csv('{}/GYN.csv'.format(folder_name))
SAS = pd.read_csv('{}/SAS.csv'.format(folder_name))

HOSP = pd.read_csv('{}/HOSP.csv'.format(folder_name))
LIEKY = pd.read_csv('{}/LIEKY.csv'.format(folder_name))
SVLZ = pd.read_csv('{}/SVLZ.csv'.format(folder_name))

# Pre spojenie vsetkych DataFrame, ktore obsahuju vykony
VYKONY = pd.concat([VLD, VLDD, GYN, SAS])

# Join ciselnikov a dat
VLDD_pacient = VLDD.merge(ciselnik_poistenec, left_on='pacient', right_on='id')
VLDD_pacient_left_join = VLDD.merge(ciselnik_poistenec, left_on='pacient', right_on='id', how='left')

# GROUP BY values in dataframe,
# i.e. celkovy pocet dni v nemocnici na pacienta
HOSP.groupby('pacient')['pocet_dni'].sum()
# i.e. priemerny pocet dni, kolko boli pacienti hospitalizovany pre PZS
HOSP.groupby('pzs')['pocet_dni'].mean()

pass
