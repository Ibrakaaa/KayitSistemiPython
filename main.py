import re

while True:

    kadi = input("Lütfen Kullanıcı Adınızı Giriniz: ")


    bul = re.search("^[a-z0-9-_]{3,16}$",kadi)


    if bul:
     print("Kullanıcı Adınız "+kadi+" Olarak Oluşturuldu")
     break

    else:
     print("Hatalı Giriş Yaptınız Lütfen Karakterlere ve Uzunluğa Dikkat Ederek Tekrar Giriş Yapınız")

#ŞİFRe

while True:

    sifre = input("\nLütfen Şifrenizi Giriniz: ")
    sifrebul = re.search("^[^"+kadi+"][a-z0-9-_]{8,16}$",sifre)

    if sifrebul:
       print("Şifreniz "+len(sifre)*"*"+ " Olarak Oluşturulmuştur")
       break

    else:
      print("Böyle Şifre Mi Olur Amk")

#telefon

while True:

    tele = input("\nLütfen Cep Telefonunuzu Giriniz: ")
    telebul = re.search("^05[0-9]{9}$",tele)

    if telebul:
     print("Telefon Numaranız"+tele+" Olarak Kaydedilmiştir")
     break

    else:
        print("Lütfen Geçerli Bir Telefon Numarası Giriniz")

# eposta

while True:

    posta = input("Lütfen E-posta Adresinizi Giriniz: ")
    postabul = re.search("^[a-z0-9\._-]+@[a-z0-9\.-_]+\.[a-z]{2,6}$",posta)

    if postabul:
      print("E-posta Adresiniz "+posta+" Olarak Kaydedilmiştir")
      break

    else:
        print("Yanlış Adres Girdiniz")

