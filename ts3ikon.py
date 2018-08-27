#!/usr/bin/python3

with ts3.query.TS3Connection("localhost") as ts3conn:
ts3conn.login(
client_login_name="serveradmin", # Sunucu Kullanıcı Adı
client_login_password="FoOBa9" # Sunucu Şifreniz
)

# Yeni Giriş Alıyoruz
# Ts3 Girisi.

ts3ft = ts3.filetransfer.TS3FileTransfer(ts3conn)

#Resim Yüklüyoruz
#Klasör Açıyoruz
#Ardından Upload Yapıyoruz

with open("resim.uzantisi", "klasor ismi") as file:
ts3ft.init_upload(input_file=file, name="resim.uzantisi", cid=2) # Dosya Adı ve Kullanici İD'si
