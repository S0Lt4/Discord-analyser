# Discord-analyser

**Discord-analyser** botu, kamerada gösterilen el hareketlerine göre bu hareketlerin isimlerini tanıyabilen bir bottur. Toplamda 11 farklı sınıfı tanıyabilir. Bu bot, özellikle el hareketleriyle etkileşime girmek isteyen projeler için faydalıdır.

## Sınıflar
Bot, aşağıdaki 11 el hareketi sınıfını tanıyabilir:

1. **Merhaba**
2. **Rock'n Roll**
3. **Kalp**
4. **Tamam**
5. **Yumruk**
6. **Barış**
7. **Başparmak Yukarı**
8. **Çarpan Yumruk**
9. **Utanmak**
10. **Birazcık**
11. **Rahat Ol**

## Kullanılan Kütüphaneler

### **discord.py**:
Discord botları geliştirmek için kullanılan popüler bir Python kütüphanesidir. `discord.ext.commands` modülü, bot komutlarını kolayca tanımlamayı ve yönetmeyi sağlar. Bu bot, kullanıcıların Discord üzerinden komut göndermesini sağlar ve görselleri işlemeye imkan tanır.

### **os**:
Python'un standart kütüphanesidir ve dosya işlemleri için kullanılır. Örneğin, görsel dosyalarını kaydetmek için kullanılır.

### **random**:
Python'un yerleşik `random` modülü, rastgele sayılar üretmek ve rastgele seçimler yapmak için kullanılır. Bu, gelecekte rastgele öğe seçimleri veya diğer rastgele işlemler eklenebileceği anlamına gelir.

### **keras.models (load_model)**:
Keras, TensorFlow'un bir parçası olarak derin öğrenme modellerini yüklemek ve kullanmak için kullanılan bir kütüphanedir. `load_model` fonksiyonu, önceden eğitilmiş bir modelin yüklenmesini sağlar.

### **PIL (Pillow)**:
**PIL (Python Imaging Library)**, resim işleme için kullanılan bir kütüphanedir. Pillow, bu kütüphanenin aktif olarak geliştirilen sürümüdür ve resim dosyaları üzerinde işlemler yapmanızı sağlar. `Image` ve `ImageOps` modülleri, resimleri açmak, boyutlandırmak ve ön işleme yapmak için kullanılır.

### **numpy**:
**NumPy**, bilimsel hesaplamalar için kullanılan bir Python kütüphanesidir. Özellikle sayısal işlemler ve dizi manipülasyonu yapmanıza olanak tanır. Modelin girdi verisini uygun formata dönüştürmek için kullanılır.

## Başlangıç

### Gereksinimler

- Python 3.7 veya daha yeni bir sürüm
- Discord bot token'ı
- Keras model dosyası (`.h5`) ve etiket dosyası (`labels.txt`)

### Kurulum

1. **Gerekli kütüphaneleri yükleyin**:
   ```bash
   pip install discord.py pillow numpy keras
