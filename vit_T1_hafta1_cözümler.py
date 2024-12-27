#Soru 1: Ekrana 1'den 10'a kadar sayıları yazdıran bir Python kodu yazın.
#Sefa Öztürk
for n in range (1,11):
    print(n,end=' ')
    
    
#Soru 2: Kullanıcıdan bir sayı girişi alın ve ekrana bu sayıya kadar çift sayıları yazdıran bir
# Python programı yazın. Bunu önce 'for' ile sonra da 'while' döngüleriyle yapın.
#Fırat-for dongusu ıle
kullanici=int(input("Sayı giriniz:"))
sayilar=range(0,kullanici)
çift_sayi=[]
print('For dongusu ile:')
for i in sayilar:
    if i%2==0:
        çift_sayi.append(i)
print("Çift sayilar.",çift_sayi)
#Sefa-while dongusu ıle
sayi=int(input('Lutfen bir sayi girin:'))
print('While dongusu ile:')
i=2
while i<=sayi:
    print(i,end=' ')
    i += 2

#Soru 3: Kullanıcıdan başlangıç ​​ve bitiş değerini alıp, bu değerler arasındaki tüm sayıları (bitiş değeri dahil) ekrana yazdıran bir Python kodu yazınız.
#Bahattin
baslangic = int(input("Başlangıç değerini girin: ")) 
bitis = int(input("Bitiş değerini girin: "))  

print(f"{baslangic} ile {bitis} arasındaki sayılar (bitiş dahil):")

for i in range(baslangic, bitis + 1):  
    print(i) 
    
    
#Soru 4: Kullanıcıdan bir sayı alın ve bu sayının tek mi yoksa çift mi olduğunu yazdıran bir Python kodu yazın.
# Serap
number = int(input("Lütfen bir sayı giriniz: "))

if number % 2 == 0:
    print(f"{number} çift sayıdır.")
else:
    print(f"{number} tek sayıdır.")


#Soru 5 : Kullanıcıdan pozitif bir tam sayı girişi alın ve faktöriyelini hesaplayan bir Python programı yazın. 
# Faktöriyel, bir sayının kendisi ile 1 arasındaki tüm pozitif tam sayıların çarpımıdır. 
# Örneğin: kullanıcı 5 girdiyse program şu çıktıyı vermeli: Kullanıcıdan bir sayı girin: 5 Faktöriyel: 120
#Fırat
sayı=int(input("Lütfen pozitif bir tam sayı giriniz."))
faktöriyel=1
i=1

if sayı<0:
    print("Negatif sayı.")

elif sayı==0 or sayı==1:
    print("faktöriyel 1")
    
else:
    while i<=sayı:
        faktöriyel*=i
        i+=1
    print(faktöriyel)
    
#Soru 6: Kullanıcıdan bir sayı alan ve bu sayının asal olup olmadığını kontrol eden bir Python kodu yazın.

#Serap
# Kullanıcıdan bir sayı al
sayi = int(input("Bir sayı girin: "))

# Asal sayı kontrolü
if sayi <= 1:
    print(f"{sayi} bir asal sayı değildir.")
else:
    asal_mi = True
    for i in range(2, int(sayi ** 0.5) + 1):  # Sayının kareköküne kadar bölenleri kontrol et
        if sayi % i == 0:
            asal_mi = False
            break
    if asal_mi:
        print(f"{sayi} bir asal sayıdır.")
    else:
        print(f"{sayi} bir asal sayı değildir.")
        
#Soru 7: Fibonacci dizisini hesaplayan ve sonucu belirli bir sınıra kadar sayı içeren bir liste olarak döndüren bir döngü nasıl oluşturulur?
#Fırat
sinir=int(input("Fibonacci sınır sayınızı giriniz:"))

fibonacci_sayi=[0,1]

while fibonacci_sayi[-1] + fibonacci_sayi[-2] <=sinir:
    yeni=fibonacci_sayi[-1] + fibonacci_sayi[-2]
    fibonacci_sayi.append(yeni)
print(fibonacci_sayi)


#Soru 8: Kullanıcıdan bir kelime alan ve bu kelimenin tersini ekrana yazdıran bir Python kodu yazın.
#Bahattin
kelime = input ("Bir kelime girin:")
ters_kelime = kelime [::-1]
print(f"Girdiginiz kelime: tersi'{ters_kelime}'")


#Soru 9: Kullanıcıdan bir kelime girişi alan ve bu kelimenin bir palindrom olup olmadığını (geriye doğru okunduğunda da aynı) kontrol eden 
#bir döngü ve koşullu ifade kombinasyonu nasıl oluşturulur?
#Sefa
#Palindrome (Tersten okununca da ayni olan kelime)
kelime=input('Bir kelime girin:')
kelime=kelime.lower()
reverse=kelime[::-1]
if kelime==reverse:
    print(f'{kelime} bir palindrome kelimedir.')
else:
    print(f'{kelime} bir palindrome kelime degildir.')

    
#Soru 10: Kişinin kilo endeksini hesaplayan ve endeks değerine göre zayıf, kilolu veya fazla kilolu sonucunu döndüren kodu yazın. 
# (Kilo endeksi hesaplaması için internete bakabilirsiniz) 
# Bunun için kullanıcıdan kilo ve boy ölçülerini isteyin. Kilo endeksi 25'in altındaysa zayıf, 25-30 arasıysa normal,
# 30-40'ın üzerindeyse kilolusunuz. 40'ın üzerindeyse kilolusunuz.
#Fırat
ad=input("Lütfen adınızı giriniz:")
kilo=float(input("Lütfen kilonuzu kg cinsinden giriniz:"))
boy=float(input("Lütfen boyunuzu metre cinsinden giriniz:"))

formül=kilo/(boy**2)
print(ad,"Beden kitle endeksiniz:",formül)

if 0<=formül<=25:
    print("Beden kitle endeksinize göre zayıf çıktınız.")
    
elif 25<=formül<=30:
    print("Beden kitle endeksinize göre iyi durumdasınız.")
    
elif 30<=formül<=40:
    print("Beden kitle endeksinize göre kilolu durumdasınız.")
    
else:
    print("Beden kitle endeksinize göre aşırı kilolusunuz.")
    
    

#Soru 11: Kullanıcının girdiği üç sayıdan en büyüğünü bulan bir Python programı nasıl yazılır?
#Bahattin
sayi1 = float (input("Birinci sayiyi girin:"))
sayi2 = float (input("Ikinci sayiyi girin:"))
sayi3 = float (input("Ucuncu sayiyi girin:"))
if sayi1 >= sayi2 and sayi1 >= sayi3:
    print(f"En buyuk sayi: {sayi1}")
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    print(f"En buyuk sayi: {sayi2}")
else: 
    print (f"En buyuk sayi: {sayi3}")
    
#Soru 12: Herhangi bir ders için bir öğrenciden Vize ve Final notlarını alın. Vize sınav notunun %40'ı ile Final notunun %60'ının toplamı yıl sonu
#ortalamasını verecektir. Ortalama 50'nin altındaysa ekranda "FAILED" (BAŞARISIZ) yazısı, 50 veya üzeriyse ekranda "SUCCESSFUL" (BAŞARILI) yazısı 
#görünecektir. Bu yazdırma işlemi 4 derstir ve dersler birbiri ardına yazılacaktır.

ders_sayisi = 4
for i in range(1, ders_sayisi + 1):
    # Kullanıcıdan notları alma
    vize= float(input(f"{i}. ders için Vize notunu girin: "))
    final = float(input(f"{i}. ders için Final notunu girin: "))
    ortalama = (vize * 0.4) + (final * 0.6)
    if ortalama < 50:
        sonuc = "FAILED"
    else:
        sonuc = "SUCCESSFUL"
    print(f"{i}. ders için Yılsonu ortalaması: {ortalama:.2f}")
    print(sonuc)
    
