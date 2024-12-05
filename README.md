# Hayvan Simülasyonu

Bu proje, 500x500 bir alan içerisinde çeşitli hayvanların ve bir avcının rastgele hareket ettiği bir simülasyonu içerir. 
Simülasyonda hayvanlar birbirini avlayabilir, üreyebilir ve avcı hayvanları avlayabilir. 
1000 birim hareket sonunda her türden hayvanın sayısı hesaplanır ve sonuçlar ekrana yazdırılır.

## Özellikler

- **Hayvan Türleri ve Başlangıç Sayıları:**
  - Koyun: 30 (15 erkek, 15 dişi)
  - İnek: 10 (5 erkek, 5 dişi)
  - Tavuk: 10
  - Kurt: 10 (5 erkek, 5 dişi)
  - Horoz: 10
  - Aslan: 8 (4 erkek, 4 dişi)
  - Avcı: 1

- **Hareket ve Avlanma Kuralları:**
  - Koyun: 2 birim rastgele hareket eder.
  - İnek: 2 birim rastgele hareket eder.
  - Tavuk: 1 birim rastgele hareket eder.
  - Kurt: 3 birim rastgele hareket eder ve 4 birim yakınındaki koyun, tavuk, horozları avlar.
  - Aslan: 4 birim rastgele hareket eder ve 5 birim yakınındaki koyun ve inekleri avlar.
  - Avcı: 1 birim rastgele hareket eder ve 8 birim yakınındaki herhangi bir hayvanı avlar.

- **Üreme Kuralları:**
  - Aynı türden bir erkek ve bir dişi hayvan birbirine 3 birim yakınlaşırsa, aynı türden rastgele bir cinsiyette yeni bir hayvan oluşur.

## Simülasyon Süreci

1. Hayvanlar ve avcı, rastgele şekilde belirli birim hareket eder.
2. Hareketler sonucunda avlanma ve üreme kuralları uygulanır.
3. Bu işlem 1000 birim boyunca tekrarlanır.
4. Simülasyon sonunda her türden hayvanın sayısı hesaplanır ve raporlanır.

## Gereksinimler

- Python 3.x
- NumPy (Rastgele hareketler için)
- Matplotlib (Simülasyonu görselleştirmek isterseniz)

## Kullanım

1. Bu repository'yi klonlayın:
   ```bash
   git clone https://github.com/AdnanKahveci/zoo
