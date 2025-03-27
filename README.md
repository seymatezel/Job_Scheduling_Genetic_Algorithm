
# Rastgele 4 Sıralama ve Çaprazlama Algoritması
Bu Python kodu, belirli bir liste üzerinde sıralama, gecikme maliyetleri hesaplama, çaprazlama ve mutasyon işlemleri gerçekleştiren bir algoritma sunmaktadır.
# Amaç
Kodun amacı:
1. Rastgele sıralamalar oluşturmak ve her sıralamanın gecikme maliyetini
hesaplamak.
2. En düşük maliyetli sıralamaları bulmak.
3. Tek noktalı çaprazlama yöntemiyle yeni sıralamalar üretmek.
4. Mutasyon işlemi uygulayarak sıralamaları iyileştirme denemeleri yapmak.
# Kullanılan Python Modülleri
random: Rastgele sıralama, çaprazlama ve mutasyon işlemleri için.
# Algoritma Açıklaması
1. Rastgele Sıralama Oluşturma
Her sıralamanın gecikme maliyetini hesaplar:
shuffle() : Liste elemanlarını rastgele sıralar.
maliyet : Gecikmeye dayalı olarak toplam maliyet hesaplanır.

2. En İyi Çözümlerin Seçimi
En az maliyetli iki sıralama seçilir:
İlk iki en düşük maliyetli sıralama belirlenir.
Bu sıralamalar çaprazlama işlemi için kullanılacaktır.

4. Tek Noktalı Çaprazlama

Çaprazlama işlemiyle yeni sıralamalar üretilir:
Tek noktadan bölme: Sıralamalar bölünüp birleştirilir.
Yeni sıralamaların maliyetleri hesaplanır.

4. Mutasyon İşlemi
Mutasyon işlemi rastgele iki elemanı değiştirir:
random.randint(): Rastgele iki nokta seçilir.
Seçilen elemanlar yer değiştirilir ve maliyet hesaplanır.
# Kodun Çıktıları
· Toplam maliyet: Her sıralama ve işlem sonrası maliyet hesaplanır.
· En iyi sıralama: Tüm işlemler sonrası en düşük maliyetli sıralama raporlanır.
# Fonksiyonlar ve İşlevler
Rastgele sıralama:
shuffle(is_sirasi)
Gecikme maliyeti hesaplama:
gecikme = zaman - liste[j][1]
if gecikme > 0:
    maliyet += gecikme * liste[j][2]
Tek noktalı çaprazlama:
yeni_sıralama1 = sıralamalar[en_uygun1_sıralama][:bölünecek_yer]
Mutasyon işlemi:
a = mutasyonlu_sıralama[rassal_sayı2]
mutasyonlu_sıralama[rassal_sayı2] = mutasyonlu_sıralama[rassal_sayı3]
mutasyonlu_sıralama[rassal_sayı3] = a
# Bu Projenin Kullanım Alanları
Bu algoritma aşağıdaki alanlarda kullanılabilir:
· İş sıralama problemleri.
· Genetik algoritma uygulamaları.
· Yapay zeka ve optimizasyon çalışmaları.



