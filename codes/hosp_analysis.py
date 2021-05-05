import pandas as pd

def get_stats(df, top_count=10):
    total_count = df.shape[0]
    unique_patient = len(df['pacient'].unique())
    unique_pzs = len(df['pzs'].unique())
    hlavna_diagnoza = len(df['hlavna_diagnoza'].unique())
    unique_drg = len(df['drg'].unique())
    pocet_dni = df['pocet_dni'].mean()

    print('|Názov|Hodnota|')
    print('|-|-|')
    print('| {} | {} |'.format('Počet záznamov', total_count))
    print('| {} | {} |'.format('Počet pacientov', unique_patient))
    print('| {} | {} |'.format('Počet PZS', unique_pzs))
    print('| {} | {} |'.format('Počet unikátnych DRG', unique_drg))
    print('| {} | {} |'.format('Počet hlavných diagnóz', hlavna_diagnoza))
    print('| {} | {} |'.format('Priemerný počet dní hospitalizácie', pocet_dni))



folder_name = './data/final_data'

# Nacitanie Ciselnikov
ciselnik_odbornost_lekar = pd.read_csv('{}/ciselniky/odbornost_lekara.csv'.format(folder_name))
ciselnik_poistenec = pd.read_csv('{}/ciselniky/poistenci_ciselnik.csv'.format(folder_name))
ciselnik_diagnoza = pd.read_csv('{}/ciselniky/diagnozy_ciselnik.csv'.format(folder_name))
ciselnik_vykon = pd.read_csv('{}/ciselniky/katalog_vykonov.csv'.format(folder_name))


HOSP = pd.read_csv('{}/HOSP.csv'.format(folder_name))
get_stats(HOSP)

pass