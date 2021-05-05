import pandas as pd


def get_stats_performance(df, top_count=5):
    total_count = df.shape[0]
    unique_patient = len(df['pacient'].unique())
    unique_pzs = len(df['pzs'].unique())
    unique_lekar = len(df['lekar'].unique())
    unique_visit = len(df['navsteva'].unique())
    top_diagnosis = df['diagnoza'].value_counts()[:top_count]
    top_performance = df['vykon'].value_counts()[:top_count]

    return total_count, unique_patient, unique_pzs, unique_lekar, unique_visit, top_diagnosis, top_performance


folder_name = './data/final_data'

# Nacitanie Ciselnikov
ciselnik_odbornost_lekar = pd.read_csv('{}/ciselniky/odbornost_lekara.csv'.format(folder_name))
ciselnik_poistenec = pd.read_csv('{}/ciselniky/poistenci_ciselnik.csv'.format(folder_name))
ciselnik_diagnoza = pd.read_csv('{}/ciselniky/diagnozy_ciselnik.csv'.format(folder_name))
ciselnik_vykon = pd.read_csv('{}/ciselniky/katalog_vykonov.csv'.format(folder_name))

# Nacitanie zaznamov o liekoch
VLD = pd.read_csv('{}/VLD.csv'.format(folder_name))
VLDD = pd.read_csv('{}/VLDD.csv'.format(folder_name))
GYN = pd.read_csv('{}/GYN.csv'.format(folder_name))
SAS = pd.read_csv('{}/SAS.csv'.format(folder_name))

vld_total_count, vld_unique_patient, vld_unique_pzs, vld_unique_lekar, vld_unique_visit, vld_top_diagnosis, vld_top_performance = get_stats_performance(VLD)
vldd_total_count, vldd_unique_patient, vldd_unique_pzs, vldd_unique_lekar, vldd_unique_visit, vldd_top_diagnosis, vldd_top_performance = get_stats_performance(VLDD)
gyn_total_count, gyn_unique_patient, gyn_unique_pzs, gyn_unique_lekar, gyn_unique_visit, gyn_top_diagnosis, gyn_top_performance = get_stats_performance(GYN)
sas_total_count, sas_unique_patient, sas_unique_pzs, sas_unique_lekar, sas_unique_visit, sas_top_diagnosis, sas_top_performance = get_stats_performance(SAS)

print('| Tabuľka | Počet záznamov | Počet pacientov | Počet PZS | Počet lekárov | Počet návštev |')
print('|-|-|-|-|-|-|')
print('|{}|{}|{}|{}|{}|{}|'.format('VLD', vld_total_count, vld_unique_patient, vld_unique_pzs, vld_unique_lekar, vld_unique_visit))
print('|{}|{}|{}|{}|{}|{}|'.format('VLDD', vldd_total_count, vldd_unique_patient, vldd_unique_pzs, vldd_unique_lekar, vldd_unique_visit))
print('|{}|{}|{}|{}|{}|{}|'.format('GYN', gyn_total_count, gyn_unique_patient, gyn_unique_pzs, gyn_unique_lekar, gyn_unique_visit))
print('|{}|{}|{}|{}|{}|{}|'.format('SAS', sas_total_count, sas_unique_patient, sas_unique_pzs, sas_unique_lekar, sas_unique_visit))

print()

print('|  | VLD |  | VLDD |  | GYN |  | SAS |  |')
print('|-|-:|-:|-:|-:|-:|-:|-:|-:|')
print('||Diagnóza|Počet|Diagnóza|Počet|Diagnóza|Počet|Diagnóza|Počet')
for i, ((vld_key, vld_value), (vldd_key, vldd_value), (gyn_key, gyn_value), (sas_key, sas_value)) in enumerate(zip(vld_top_diagnosis.items(), vldd_top_diagnosis.items(),
                                                                                                    gyn_top_diagnosis.items(), sas_top_diagnosis.items())):
    print('| {} | {} | {} | {} | {} | {} | {} | {} | {} |'.format(i+1, vld_key, vld_value, vldd_key, vldd_value, gyn_key, gyn_value, sas_key, sas_value))

print()

print('|  | VLD |  | VLDD |  | GYN |  | SAS |  |')
print('|-|-:|-:|-:|-:|-:|-:|-:|-:|')
print('||Výkon|Počet|Výkon|Počet|Výkon|Počet|Výkon|Počet')
for i, ((vld_key, vld_value), (vldd_key, vldd_value), (gyn_key, gyn_value), (sas_key, sas_value)) in enumerate(zip(vld_top_performance.items(), vldd_top_performance.items(),
                                                                                                    gyn_top_performance.items(), sas_top_performance.items())):
    print('| {} | {} | {} | {} | {} | {} | {} | {} | {} |'.format(i+1, vld_key, vld_value, vldd_key, vldd_value, gyn_key, gyn_value, sas_key, sas_value))

pass
