import pandas as pd


def get_stats(df, top_count=10):
    total_count = df.shape[0]
    unique_patient = len(df['pacient'].unique())
    unique_lekaren = len(df['pzs_lekaren'].unique())
    unique_ambulancia = len(df['pzs_ambulancia'].unique())
    unique_lekar = len(df['lekar'].unique())
    unique_lekar_odosielatel = len(df['lekar_odosielatel'].unique())
    unique_pzs_odosielatel = len(df['pzs_odosielatel'].unique())
    pocet_baleni = df['pocet_baleni'].mean()

    print('|Názov|Hodnota|')
    print('|-|-|')
    print('| {} | {} |'.format('Počet záznamov', total_count))
    print('| {} | {} |'.format('Počet pacientov', unique_patient))
    print('| {} | {} |'.format('Počet lekární', unique_lekaren))
    print('| {} | {} |'.format('Počet ambulancií', unique_ambulancia))
    print('| {} | {} |'.format('Počet lekárov', unique_lekar))
    print('| {} | {} |'.format('Počet lekárov odosielateľov', unique_lekar_odosielatel))
    print('| {} | {} |'.format('Počet PZS odosielateľov', unique_pzs_odosielatel))
    print('| {} | {} |'.format('Priemerný počet balení', pocet_baleni))


folder_name = './data/final_data'

# Nacitanie Ciselnikov
ciselnik_sdl_lieky = pd.read_csv('{}/ciselniky/sdl_lieky_ciselnik.csv'.format(folder_name))
ciselnik_lieky = pd.read_csv('{}/ciselniky/vybrane_lieky_ciselnik.csv'.format(folder_name))
ciselnik_poistenec = pd.read_csv('{}/ciselniky/poistenci_ciselnik.csv'.format(folder_name))
ciselnik_diagnoza = pd.read_csv('{}/ciselniky/diagnozy_ciselnik.csv'.format(folder_name))

# Nacitanie zaznamov o liekoch
LIEKY = pd.read_csv('{}/LIEKY.csv'.format(folder_name))
get_stats(LIEKY)

pass
