# 🐦 TweetZone

TweetZone, Django kullanılarak geliştirilmiş basit bir Twitter klonudur. Kullanıcılar tweet atabilir, tweetleri listeleyebilir ve gerçek zamanlı bir sosyal medya deneyimine benzer bir yapı ile etkileşimde bulunabilir.

## 🚀 Proje Özellikleri

- Kullanıcı kayıt & giriş sistemi
- Tweet oluşturma, listeleme
- Kullanıcı tweet yönetme
- Django ORM ile veritabanı yönetimi
- Bootstrap ile sade ve responsive frontend
- Admin paneli ile içerik yönetimi
- Moderatör sistemi


## 🛠️ Kullanılan Teknolojiler

| Teknoloji       | Açıklama                         |
|-----------------|----------------------------------|
| Django          | Python web framework             |
| SQLite          | Varsayılan veritabanı            |
| HTML / CSS      | Sayfa tasarımı                   |
| Bootstrap       | Responsive tasarım için          |
| JavaScript      | Etkileşimli frontend öğeleri     |
| Django ORM      | Veritabanı işlemleri             |

## 📁 Proje Yapısı
```bash
TweetZone/
├── tweetzone/ # Django projesi ayarları
├── tweet/ # Tweet uygulaması
│ ├── models.py # Veritabanı modelleri
│ ├── views.py # Görünümler
│ ├── urls.py # URL yönlendirmeleri
│ ├── templates/ # HTML şablonlar
├── static/ # CSS / JS dosyaları
├── db.sqlite3 # Veritabanı dosyası
└── manage.py
```

## ⚙️ Kurulum

Projeyi yerel ortamda çalıştırmak için aşağıdaki adımları takip edin:

```bash
# 1. Reposu klonla
git clone https://github.com/kullaniciadi/tweetzone.git
cd tweetzone

# 2. Sanal ortam oluştur
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# 3. Gerekli paketleri yükle
pip install -r requirements.txt

# 4. Veritabanını migrasyon et
python manage.py migrate

# 5. Sunucuyu başlat
python manage.py runserver
