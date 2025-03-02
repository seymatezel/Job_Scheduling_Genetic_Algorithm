# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:59:19 2024

@author: Şeyma_Tezel 
"""
#Rastgele 4 sıralama
from random import shuffle
liste=[[3,4,5],
       [5,7,10],
       [2,3,5],
       [8,10,10],
       [4,9,5],
       [1,3,10],
       [3,8,5],
       [7,9,10],
       [6,11,10],
       [2,4,5],
       [4,5,10]]
sıralamalar = []
maliyetler=[]
for i in range(4):
    is_sirasi=[0,1,2,3,4,5,6,7,8,9,10]
    shuffle(is_sirasi)
    sıralamalar.append(is_sirasi)
for  is_sirasi in sıralamalar:
    zaman=0
    maliyet=0
    for j in is_sirasi:
        zaman+=liste[j][0]
        gecikme=zaman-liste[j][1]
        if gecikme>0:
            maliyet+=gecikme*liste[j][2]
    print( is_sirasi, "   Toplam Maliyet:", maliyet)
    
 
#Aralarından en az maliyeli 2'si     
    maliyetler.append(maliyet)
en_uygun1_maliyet=min(maliyetler) 
en_uygun1_sıralama = maliyetler.index(en_uygun1_maliyet)
print("En İyi çözüm 1: ", sıralamalar[en_uygun1_sıralama], "      Toplam Maliyet:", en_uygun1_maliyet)
maliyetler.remove(en_uygun1_maliyet)
en_uygun2_maliyet=min(maliyetler)
en_uygun2_sıralama = maliyetler.index(en_uygun2_maliyet)
print("En İyi çözüm 2: ", sıralamalar[en_uygun2_sıralama], "      Toplam Maliyet:", en_uygun2_maliyet)


#Tek noktalı Çaprazlama
from random import randint
bölünecek_yer = randint(1, 10)
print ("Tek noktalı çaprazlama için üretilen rassal sayı : " ,bölünecek_yer)
print("En İyi çözüm 1: ", sıralamalar[en_uygun1_sıralama], "      Toplam Maliyet:", en_uygun1_maliyet)
print("En İyi çözüm 2: ", sıralamalar[en_uygun2_sıralama], "      Toplam Maliyet:", en_uygun2_maliyet)
yeni_sıralama1 =sıralamalar[en_uygun1_sıralama][:bölünecek_yer]
for k in sıralamalar[en_uygun2_sıralama]:
    if k not in yeni_sıralama1:
        yeni_sıralama1.append(k)

yeni_sıralama2 =sıralamalar[en_uygun2_sıralama][:bölünecek_yer]
for k in sıralamalar[en_uygun1_sıralama]:
    if k not in yeni_sıralama2:
        yeni_sıralama2.append(k)

zaman=0
maliyet1=0
for x in yeni_sıralama1:
    zaman=zaman+liste[x][0]
    gecikme= zaman-liste[x][1]
    if gecikme>0:
        maliyet1=maliyet1+ gecikme*liste[x][2] 
print("Yeni sıralama1:", yeni_sıralama1, "    Toplam Maliyet:", maliyet1)

zaman=0
maliyet2=0
for x in yeni_sıralama2:
    zaman=zaman+liste[x][0]
    gecikme= zaman-liste[x][1]
    if gecikme>0:
        maliyet2=maliyet2+ gecikme*liste[x][2] 
print("Yeni sıralama2:", yeni_sıralama2, "    Toplam Maliyet:", maliyet2)

#Son dört listeden en az maliyetlisi
sıralamalar2 =[sıralamalar[en_uygun1_sıralama],sıralamalar[en_uygun2_sıralama],yeni_sıralama1, yeni_sıralama2 ]
maliyetler2=[en_uygun1_maliyet,en_uygun2_maliyet, maliyet1, maliyet2]
en_uygun_maliyet=min(maliyetler2)
en_uygun_sıralama=maliyetler2.index(en_uygun_maliyet)
print("En İyi sıralama:" ,sıralamalar2[en_uygun_sıralama],"Toplam Maliyet:",en_uygun_maliyet)


#Mutasyon
rassal_sayı2=randint(0,10)
rassal_sayı3=randint(0,10)
while rassal_sayı2==rassal_sayı3:
    rassal_sayı3=randint(0,10)  
print("Mutasyon için üretilen rassal sayılar:",rassal_sayı2," ve ",rassal_sayı3 )

mutasyonlu_sıralama = sıralamalar2[en_uygun_sıralama].copy()
a=mutasyonlu_sıralama[rassal_sayı2]
mutasyonlu_sıralama[rassal_sayı2]=mutasyonlu_sıralama[rassal_sayı3]
mutasyonlu_sıralama[rassal_sayı3]=a

zaman=0
mutasyonlu_maliyet=0
for y in yeni_sıralama2:
    zaman=zaman+liste[y][0]
    gecikme= zaman-liste[y][1]
    if gecikme>0:
        mutasyonlu_maliyet+= gecikme*liste[x][2] 
print("Mutasyonlu Sıralama:", mutasyonlu_sıralama, "    Toplam Maliyet:", mutasyonlu_maliyet)
print("Mutasyonsuz Sıralama:",sıralamalar2[en_uygun_sıralama],"Toplam Maliyet:",en_uygun_maliyet)
    
sıralamalar3=[mutasyonlu_sıralama,sıralamalar2[en_uygun1_sıralama]]
maliyetler3=[mutasyonlu_maliyet, en_uygun_maliyet]
en_uygun_maliyet2=min(maliyetler3)
en_uygun_sıralama2=maliyetler3.index(en_uygun_maliyet2)
print("En İyi sıralama Son:" ,sıralamalar3[en_uygun_sıralama2],"Toplam Maliyet:",en_uygun_maliyet2)













