## Projenin Amacı
Projenin temel amacı otomotiv, gıda gibi fabrikalarda çalışan personellerin özellikle endüstriyel makinelerin bulunduğu alanlarda dikkatsizlik nedeniyle başlarına gelebilecek iş kazalarını en aza indirgeyebilmektir.

Tasarım insanı gerçek zamanlı olarak tespit edip makineyi durdurma esasına dayalı olarak çalışmaktadır. Ayrıca bilgiler MQTT Protokolü kullanılarak aktarılıp kayıt altına alınmaktadır. Diğer projelerden en temel farkımız ise gerçek zamanlı olarak kişi tespiti anında makinenin durdurulabilmesi ve bu teknolojinin fabrikalardaki endüstriyel makinelere uyarlanabilmesidir.

İş kazalarını önlemede İş Sağlığı ve Güvenliğinde IoT Tabanlı Dijital Dönüşüm Yaklaşımı isimli projenin belirlenen 3 ana katman bulunmaktadır. Bunlar Veri Alışveriş Katmanı, Web Arayüz Katmanı ve Veri Analizi Katmanıdır.


## Veri Analiz Katmanı

Bu katman, gerçek zamanlı kişi tespiti için kullanılan görüntü verileri üzerinde işlem yapmaktadır. Projenin bu bölümünde, insan, makine ve hücre duvarı görüntülerini etiketleme ve kontrol süreçlerini sağlama amacıyla kullanılan yöntemler açıklanmaktadır.

Görselleri etiketlemek için Label Studio ortamı kullanılmıştır. Kendi tasarladığımız hücre duvarı görüntüleri, makine görselleri ve Open Images veri setinden alınan insan görselleri üzerinde etiketleme işlemi gerçekleştirilmiştir.

Daha verimli bir çalışma için, eldeki görselleri Roboflow ortamında Augmentation işlemine tabi tuttuk. Augmentation işlemi, algoritmanın çeşitli çevresel faktörlerle optimize edilmiş çalışma durumunu sağlamayı amaçlamaktadır. Işık ayarları, kamera açısı gibi değişkenlerin tespit oranını düşürmeden etkilenmesini önlemek için yapılmıştır.

Toplamda 467 görselden oluşan 3 farklı sınıfımız bulunmaktadır: "Person" (kişi), "Hucreduvari" (hücre duvarı) ve "Makine" (makine). Bu görsellerin 19'u test amacıyla, 41'i eğitim sırasında doğrulama amacıyla ve 407'si eğitim amacıyla kullanılmaktadır.

Augmentation işlemi sonucunda 1221 görsel elde edilmiştir ve bu görseller YOLO algoritmasının versiyon 5 modeli kullanılarak eğitilmiştir.

![Verimlilik Oranı Değer Tabloları](https://github.com/deryapolatt/Real-TimePersonDetection/blob/main/deger_tablosu.PNG)
### Veri İletişimi Katmanı

MQTT (Message Queuing Telemetry Transport) protokolü kullanılmıştır.

## Web Arayüz ve Firebase Katmanı

MQTT tarafından web arayüzüne gönderilmiş olan “İnsan tespit edildi” veya “İnsan tespit edilemedi.” çıktıları kişilerin görüntüleyebilecekleri bir platforma aktarmış olmayı sağlıyor. Web arayüzümüzü tasarlarken Flask frameworku ve Python programlama dili kullanıldı.
