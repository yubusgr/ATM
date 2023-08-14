import os
import time


bakiye = 5000
usdbakiye = 5000
birimusd = 27
print("YAPI KREDI ATM'YE HOŞ GELDİNİZ...")
time.sleep(2)
def tldendolara(tl,dolar):
    return tl//dolar

def dolardantlye(tl1,tl2):
    return  tl1*tl2

while True:
    print("LÜTFEN YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİN...")
    time.sleep(0.6)
    print("1) Para Cek")
    time.sleep(0.6)
    print("2) Para Yatır")
    time.sleep(0.6)
    print("3) Bakiye Gör")
    time.sleep(0.6)
    print("4) TL den USD ye Çevir")
    time.sleep(0.6)
    print("5) USD den TL ye Cevir")
    time.sleep(0.6)
    print("99) CIKIS")
    secim1 = int(input())
    if(secim1 == 1):
        while True:
            print("Cekmek İstediğiniz Miktarı Girin")
            cekim = int(input())
            if (cekim > bakiye):
                print("Bakiye Yetersiz!")
                time.sleep(2)

            else:
                print("İşlem Gerçekleştiriliyor Lütfen Bekleyin...")
                bakiye -= cekim
                time.sleep(2)
                print("Kalan Bakiyeniz", bakiye)
                time.sleep(1)
                break
    if (secim1 == 2):

        time.sleep(2)
        print("Yatırmak İstediğiniz Tutar:")
        yatir = int(input())
        bakiye += yatir
        time.sleep(0.5)
        print("Lütfen Bekleyin")
        time.sleep(3)
        print("İşlem Başarılı! Yeni Bakiye:",bakiye,"tl")
        time.sleep(2)

    if(secim1 == 3):
        time.sleep(0.6)
        print("Mevcut TL Bakiyeniz:", bakiye,"tl")
        print("Mevcut USD Bakiyeniz:", usdbakiye, "tl")
        time.sleep(2)

    if(secim1 == 4):
        if(bakiye == 0):
            print("Bakiyeniz Yok...")
            time.sleep(2)


        else:
            print("Bakiyeniz USD'ye Dönüştürülüyor. LÜtfen Bekleyiniz...")
            time.sleep(4)
            usdbakiye += tldendolara(bakiye, birimusd)
            bakiye -= bakiye
            print("İşlem Başarılı! \n Yeni Bakiyeniz:", usdbakiye, "dolar")
            time.sleep(2)



    if(secim1 == 5):
        if(usdbakiye == 0):
            print("Bakiyeniz Yoktur...")
            time.sleep(2)

        else:
            print("Lütfen Bekleyin...")
            time.sleep(2)
            bakiye += dolardantlye(usdbakiye,birimusd)
            usdbakiye -= usdbakiye
            print("İşlem Başarılı! \n YENİ BAKİYENİZ:",bakiye,"tl")
            time.sleep(2)


    if(secim1 == 99):
        print("İyi Günler Dileriz")
        time.sleep(2)

        break








