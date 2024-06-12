import pandas as pd
from personel import Personel 
from doktor import Doktor 
from hemsire import Hemsire 
from hasta import Hasta

try: 

    personel1 = Personel(1, "Veli", "Kaya", "İstatistik", 2000)
    personel2 = Personel(2, "Sükrü", "Varol", "İnsan Kaynakları", 1800)

    doktor1 = Doktor(3, "Mehmet", "Koksal", "Noroloji", 9000, "Norolog", 7, "Can")
    doktor2 = Doktor(4, "Leyla", "Ozdemir", "Kardiyoloji", 10000, "Kardiyolog", 6, "MedicalPark")
    doktor3 = Doktor(5, "Ahmet", "Yilmaz", "Dermatoloji", 8000, "Dermatolog", 4, "Acibadem")

    hemsire1 = Hemsire(6, "Aylin", "Akcay", "Ameliyathane", 3000, 12, "Ameliyathane", "Can")
    hemsire2 = Hemsire(7, "Fadime", "Dag", "Yogun Bakim", 5000, 9, "Yogun Bakim", "MedicalPark")
    hemsire3 = Hemsire(8, "Kemal", "Dere", "Cocuk Sagligi", 6000, 10, "Cocuk Sagligi", "Acibadem")

    hasta1 = Hasta(9, "Selim", "Kalin", "1984-02-12", "Akciger Kanseri", "Kemoterapi", doktor1, hemsire1)
    hasta2 = Hasta(10, "Kerim", "Ormanci", "1991-08-27", "Grip", "İlac Tedavisi", doktor2, hemsire2)
    hasta3 = Hasta(11, "Zeliha", "Tarakci", "2001-11-05", "Kirik", "Fizik Tedavi", doktor3, hemsire3)

    # DataFrame oluşturma
    ph_data = {
        "Personel No": [personel1.get_personel_no(), personel2.get_personel_no(), doktor1.get_personel_no(), doktor2.get_personel_no(), doktor3.get_personel_no(), hemsire1.get_personel_no(), hemsire2.get_personel_no(), hemsire3.get_personel_no(), None, None, None],
        "Ad": [personel1.get_ad(), personel2.get_ad(), doktor1.get_ad(), doktor2.get_ad(), doktor3.get_ad(), hemsire1.get_ad(), hemsire2.get_ad(), hemsire3.get_ad(), hasta1.get_ad(), hasta2.get_ad(), hasta3.get_ad()],
        "Soyad": [personel1.get_soyad(), personel2.get_soyad(), doktor1.get_soyad(), doktor2.get_soyad(), doktor3.get_soyad(), hemsire1.get_soyad(), hemsire3.get_soyad(), hemsire3.get_soyad(), hasta1.get_soyad(), hasta2.get_soyad(), hasta3.get_soyad()],
        "Departman": [personel1.get_departman(), personel1.get_departman(), doktor1.get_departman(), doktor2.get_departman(), doktor3.get_departman(), None, None, None, None, None, None],
        "Maaş": [personel1.get_maas(), personel2.get_maas(), doktor1.get_maas(), doktor2.get_maas(), doktor3.get_maas(), hemsire1.get_maas(), hemsire2.get_maas(), hemsire3.get_maas(), None, None, None],
        "Uzmanlık": [None, None, doktor1.get_uzmanlik(), doktor2.get_uzmanlik(),doktor3.get_uzmanlik(), None, None, None, None, None, None],
        "Deneyim Yılı": [None, None, doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(), None, None, None, None, None, None],
        "Hastane": [None, None, doktor1.get_hastane(), doktor2.get_hastane(), doktor3.get_hastane(), hemsire1.get_hastane(), hemsire2.get_hastane(), hemsire3.get_hastane(), None, None, None],
        "Sertifika": [None, None, None, None, None, hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika(), None, None, None],
        "Hasta No": [None, None, None, None, None, None, None, None, hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()],
        "Doğum Tarihi": [None, None, None, None, None, None, None, None, hasta1.get_dogum_tarihi(), hasta2.get_dogum_tarihi(), hasta3.get_dogum_tarihi()],
        "Hastalık": [None, None, None, None, None, None, None, None, hasta1.get_hastalik(), hasta2.get_hastalik(), hasta3.get_hastalik()],
        "Tedavi": [None, None, None, None, None, None, None, None, hasta1.get_tedavi(), hasta2.get_tedavi(), hasta3.get_tedavi()]
    }
    df = pd.DataFrame(ph_data)
    
    df.fillna(0, inplace=True)  # Boş değişken değerleri için 0 atanır
    print("\nHastane DataFrame: \n", df)

    dr_uzmanlik = df[df["Uzmanlık"].notna()].groupby("Uzmanlık").size()
    # doktorları uzmanlık alanlarına göre gruplama ve sayılarını bulma
    print("\nUzmanlık Alanlarına Göre Doktor Sayıları:\n", dr_uzmanlik)

    deneyimli_dr = df[(df["Deneyim Yılı"] > 5)].shape[0]
    # doktorlardan 5 yıldan fazla deneyimli olanları verir   
    print(f"\n5 Yıldan Fazla Deneyime Sahip Doktor Sayısı: {deneyimli_dr}")

    hasta_siralanmis = df[df["Hasta No"] != 0].sort_values(by="Ad")
    # datada hasta no sütununda değeri sıfır olmayan (yani hasta verisi olan) satırları seçer.
    print("\nAlfabetik Olarak Sıralanmış Hasta Bilgileri:\n", hasta_siralanmis)

    maasi_7000_ustunde = df[df["Maaş"] > 7000]
    #Datada maaşı 7000'in üzerindeki personelleri seçer
    print("\nMaaşı 7000'in Üzerindeki Personeller:\n", maasi_7000_ustunde)

    dt_1990_dansonra = df[pd.to_datetime(df["Doğum Tarihi"], errors='coerce') >= '1990-01-01']
    # DataFrame'de doğum tarihi 1990 yılından sonra olanları seçer
    print("\n1990 Sonrası Doğan Hastalar:\n", dt_1990_dansonra)

    new_dataf = df[["Ad", "Soyad", "Departman", "Maaş", "Uzmanlık", "Deneyim Yılı", "Hastalık", "Tedavi"]]
    print("\nYeni DataFrame:\n", new_dataf)

except Exception as e:
    print(f"Hata: {e}")

