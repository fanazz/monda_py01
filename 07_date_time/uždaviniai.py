from datetime import datetime

dabar = datetime.now()
formatas = "%M:%S"

laikas = dabar.strftime(formatas)
print(laikas)





from datetime import datetime, timedelta

def dienos_iki_gimtadienio(gimimo_data):
    gimimo_data_formatas = datetime.strptime(gimimo_data, "%Y-%m-%d")
    šiandien = datetime.now()
    gimtadienio_data = gimimo_data_formatas.replace(year=šiandien.year)

    if gimtadienio_data < šiandien:
        gimtadienio_data = gimtadienio_data.replace(year=šiandien.year + 1)

    skirtumas = gimtadienio_data - šiandien
    return skirtumas.days

gimimo_data = "1985-03-22"
print(f"Liko {dienos_iki_gimtadienio(gimimo_data)} dienos (-ų) iki nekenčiamiausios metų dienos ir tikiuosi iki viso šito sušikto spektaklio pabaigos.")



def prideti_48_valandas(data_laikas):
    formatas = "%Y-%m-%d %H:%M"
    data = datetime.strptime(data_laikas, formatas)
    nauja_data= data + timedelta(hours=48)
    naujos_data_laikas = nauja_data.strftime(formatas)
    return naujos_data_laikas

data_laikas = "2024-01-16 09:32"
print(f"Pridėjus 48 valandas: {prideti_48_valandas(data_laikas)}")



def skirtumas_dienomis(timestamp1, timestamp2):
    data_1 = datetime.fromtimestamp(timestamp1)
    data_2 = datetime.fromtimestamp(timestamp2)
    skirtumas = abs(data_2 - data_1)
    return skirtumas.days

timestamp1 = 1000000000
timestamp2 = 1655421111
print(f"Laikotarpių skirtumas dienomis: {skirtumas_dienomis(timestamp1, timestamp2)}")




def savaites_diena(data):
    formatas = "%Y-%m-%d"
    datos_objektas = datetime.strptime(data, formatas)
    dienos = ["Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis", "Šeštadienis", "Sekmadienis"]
    return dienos[datos_objektas.weekday()]

data = "2024-03-22"
print(f"Ši data yra {savaites_diena(data)}")