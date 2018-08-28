#!/usr/bin/python3

with ts3.query.TS3Connection("localhost") as ts3giris:
ts3giris.girelim(
kullanici_adi="serveradmin", # Sunucu Kullanıcı Adı
yatqa_sifresi="FoOBa9" # Sunucu Şifreniz
)

ts3dosya = ts3.filetransfer.TS3FileTransfer(ts3giris)

#Resim Yüklüyoruz
#Klasör Açıyoruz
#Ardından Upload Yapıyoruz

with open("resim.uzantisi", "klasor ismi") as dosya:
ts3dosya.init_upload(input_file=dosya, name="resim.uzantisi", cid=2) # Dosya Adı ve Kullanici İD'si
