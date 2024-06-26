# Baykar Backend Mühendis Ön Değerlendirme Projesi

## Projeyi çalıştırma

- Proje hazırda kurulu bulunan bir **PostgreSQL** yazılımına ihtiyaç duymaktadır. Postgre içinde `baykar_db` adında bir
  database tanımlı olmalıdır. İçinin boş olması önemli değildir.
    - **PostgreSQL** için default konfigürasyonları kullandım. Bu konfigürasyonlar `settings.py` dosyasında da
      görülebileceği gibi şu şekildedir:
        -     DATABASES = {
                    'default': {
                      'ENGINE': 'django.db.backends.postgresql',
                      'NAME': 'baykar_db',
                      'USER': 'postgres',
                      'PASSWORD': '2222',
                      'HOST': 'localhost',
                      'PORT': '5432',
                    }
                  }

## Çalıştırılması Gereken Kurulum Komutları

- Python kütüphanelerini kurmalıyız.

      $ pip install -r requirements.txt

- Modellerimizi database'e taşımak için aşağıdaki komutu çalıştırmalıyz.

      $ python manage.py migrate 

## Kullanılan Teknolojiler

    - Django
    - Python
    - PostgreSQL
    - Tailwind CSS
    - DataTable
    - REST Framework

## Ekran Akışı

### 1. Giriş Ekranı

![login page](screenshots/login_page_ss.png)

- Zaten hali hazırda hesabı olanlar için sisteme giriş yapabilecekleri sayfa.

### 2. Kayıt Ekranı

![signup page](screenshots/signup_page_ss.png)

- Hesabınızın olmaması durumunda buradan kayıt oluşuturabilirsiniz.

### 3. Ana Sayfa

![home page](screenshots/home_page_ss.png)

- Ana sayfamızda en popüler ürünlerimizi sergilediğimiz kartlardan olşuan animasyonlu bir alanımız vardır.
- Sağ yukarıda bulunan 'RENT NOW' butonu bizi ihların listelendiği mağaza sayfasına götürür.
- Yukarıdaki navigasyon çubuğunda ise sol taraftaki Baykar resmine basarak bu ana sayfaya dönmek mümkündür.
  Sağdaki butonlarda ise sırasıyla 'Sepet' ve 'Kullanıcı Paneli' dir. Kullanıcı panelinden çıkış yapmak ve
  daha önceki satın alımları görebileceğiniz sayfaya yönlendiren buntonlar bulunur.

### 4. Mağaza Sayfası

![store page](screenshots/store_page_ss.png)

- Satılması mümkün olunan cihazların verileri database'den çekilip gereki assatler web server'da store ediliyor.
- Bu veriler ile oluşturulan kartların üzerine tıklanarak sepete eklemek mümkün.
- İstenilen cihazları aldıktan sonra sepete yönelilir.

### 5. Sepet Sayfası

![cart page](screenshots/cart_page_ss.png)

- Alınan ürünler database'de kişiye özel olarak muhafaza edilir ve siz elinizle atmadıkça sepetinizden ürünler düşmez.
- Bu ekranda bulunan '-' ve '+' butonlarını kullanarak sepetinizdeki ürünlerin miktarını değiştirebilirsiniz.
- Ürünlerin birim fiyatını, miktarını, kalem başına toplam ücreti aynı satırda görebilirsiniz.
- Aşağıda ise teslimat ücreti ve ara toplam bulunur.
- Onların altında ise 'Son Toplam' yer alır.
- En altta kalan butonumuz satın alma işlemini bitirmek için basılır.
- Sistem septtekileri hesabınza satın alnımış olarak kayıt düşürüp sepetinizi boşaltır.

### 6. Log Sayfası

![log page](screenshots/rental_log_page_ss.png)

- Bu sayfada satın alma işlemlerinin geçmişini görüyoruz.
- Sağ üstteki filtreyi kullanarak kolonlar arasında filtreleme yapılır.
- Satır sonundaki silme butonuna basarak, o satırı satın alım geçmişinden silmek mümkündür.
- Sağ ikinci buton ise 'Edit' ya da düzenleme butonuna basarak gerekli satırı düzenlemek için dialog ekranı açılır.
  Şu anlık bu dialog ekranı tam çalışmıyor. Zamanın yetersiziliği yüzünden hatayı çözecek vakit bulamadım.
  ![img.png](screenshots/rental_log_page_dialog_ss.png)
- Sol üstteki Baykar resimini tıklayarak ana sayfaya geri dönülür.


