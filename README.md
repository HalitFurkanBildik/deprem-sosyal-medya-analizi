# Sosyal Medya Kriz Analizi

## Proje Başlığı

**Deprem Krizi Sırasında Sosyal Medyada Sahte Haber Yayılımı ve Bot Benzeri Hesap Analizi**

## Proje Açıklaması

Bu proje, deprem gibi kriz anlarında sosyal medyada yayılan haberlerin nasıl dağıldığını incelemek amacıyla hazırlanmıştır. Projede sahte haberlerin yayılımı, bot benzeri hesap davranışları, hashtag kullanımı ve kullanıcılar arasındaki haber yayılım ağı analiz edilmiştir.


## Veri Seti Hakkında Önemli Not

Bu projede kullanılan veri seti **eğitim amacıyla simüle edilmiştir**. Veri seti gerçek X/Twitter, Reddit veya forum kullanıcılarından toplanmamıştır.

Veri setinin amacı şu veri bilimi adımlarını gösterebilmektir:

- CSV veri seti okuma,
- veri inceleme ve temel analiz yapma,
- grafik oluşturma,
- basit kurallarla bot benzeri hesap davranışı tespit etme,
- sahte haber ve gerçek haberleri karşılaştırma,
- sosyal medya yayılım ağı oluşturma.

Veri seti simüle edildiği için elde edilen sonuçlar gerçek dünya genellemesi olarak yorumlanmamalıdır. Sonuçlar, örnek bir veri bilimi uygulaması olarak değerlendirilmelidir.

## Araştırma Soruları

Bu projede aşağıdaki sorulara cevap aranmıştır:

1. Veri setinde sahte haber ve gerçek haber dağılımı nasıldır?
2. Sahte haberler gerçek haberlere göre daha fazla beğeni veya yeniden paylaşım almakta mıdır?
3. Kriz anında en çok hangi hashtagler kullanılmaktadır?
4. Basit davranış kuralları kullanılarak bot benzeri hesaplar tespit edilebilir mi?
5. Haber yayılım ağında hangi kullanıcılar daha merkezi konumdadır?

## Veri Seti Sütunları

CSV veri seti `data/` klasörünün içinde yer almaktadır.

| Sütun | Açıklama |
|---|---|
| `post_id` | Her paylaşımın benzersiz numarası |
| `user_id` | Paylaşımı yapan kullanıcı |
| `post_text` | Paylaşım metni |
| `created_at` | Paylaşım zamanı |
| `like_count` | Beğeni sayısı |
| `repost_count` | Yeniden paylaşım sayısı |
| `hashtag` | Paylaşımda kullanılan hashtag |
| `followers_count` | Kullanıcının takipçi sayısı |
| `following_count` | Kullanıcının takip ettiği kişi sayısı |
| `account_age_days` | Hesabın gün cinsinden yaşı |
| `source_user` | Yayılımın başladığı kullanıcı |
| `target_user` | İçeriği yayan kullanıcı |
| `is_fake_news` | Sahte haber etiketi, 1 = sahte, 0 = gerçek |
| `bot_score` | Kural tabanlı bot benzeri davranış puanı |
| `bot_suspect` | Bot benzeri hesap etiketi, 1 = şüpheli, 0 = normal |

## Kullanılan Yöntemler

### 1. Keşifsel Veri Analizi

Veri seti temel istatistikler ve grafikler kullanılarak incelenmiştir.

### 2. Sahte Haber Analizi

Sahte haber ve gerçek haber paylaşımları şu ölçütlerle karşılaştırılmıştır:

- paylaşım sayısı,
- ortalama beğeni sayısı,
- ortalama yeniden paylaşım sayısı.

### 3. Bot Benzeri Hesap Tespiti

Basit bir kural tabanlı bot skoru oluşturulmuştur. Bir hesap/paylaşım aşağıdaki özellikleri taşıyorsa bot skoruna puan eklenmiştir:

- hesabın çok yeni olması,
- takipçi sayısının düşük olması,
- takip edilen kişi sayısının yüksek olması,
- yeniden paylaşım sayısının yüksek olması,
- beğeni sayısı düşükken yeniden paylaşım sayısının yüksek olması.

Bot skoru 3 veya üzeri olan hesaplar **bot benzeri hesap** olarak etiketlenmiştir.

### 4. Hashtag Analizi

Kriz anında en sık kullanılan hashtagler görselleştirilmiştir.

### 5. Ağ Analizi

`source_user` ve `target_user` sütunları kullanılarak yönlü bir ağ grafiği oluşturulmuştur.

- Düğümler kullanıcıları temsil eder.
- Bağlantılar haber yayılım ilişkisini temsil eder.
- Degree centrality yöntemiyle merkezi kullanıcılar belirlenmiştir.

## Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Matplotlib
- NetworkX
- Jupyter Notebook

## Proje Klasör Yapısı

```text
sosyal-medya-kriz-analizi/
│
├── data/
│   └── crisis_social_media_data.csv
│
├── notebooks/
│   └── social_media_crisis_analysis.ipynb
│
├── src/
│   └── analysis.py
│
├── visuals/
│   ├── fake_news_distribution.png
│   ├── interaction_comparison.png
│   ├── bot_distribution.png
│   ├── hashtag_analysis.png
│   └── network_graph.png
│
├── report/
│   ├── sosyal_medya_kriz_analizi_raporu.docx
│   ├── sosyal_medya_kriz_analizi_raporu.pdf
│   └── proje_raporu_taslak.md
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Proje Nasıl Çalıştırılır?

### 1. Projeyi bilgisayara indirme

```bash
git clone https://github.com/kullanici-adi/sosyal-medya-kriz-analizi.git
cd sosyal-medya-kriz-analizi
```

### 2. Gerekli kütüphaneleri kurma

```bash
pip install -r requirements.txt
```

### 3. Jupyter Notebook dosyasını açma

```bash
jupyter notebook notebooks/social_media_crisis_analysis.ipynb
```

Notebook açıldıktan sonra hücreler yukarıdan aşağıya çalıştırılmalıdır.

Alternatif olarak Python dosyası doğrudan çalıştırılabilir:

```bash
python src/analysis.py
```

## Projenin Ana Çıktıları

Bu proje aşağıdaki çıktıları üretmektedir:

- sahte haber ve gerçek haber dağılım grafiği,
- ortalama etkileşim karşılaştırma grafiği,
- bot benzeri hesap dağılım grafiği,
- en sık kullanılan hashtag grafiği,
- sosyal medya haber yayılım ağı grafiği,
- ağdaki merkezi kullanıcılar,
- akademik proje raporu.

## Sonuç

Bu proje, kriz anlarında sosyal medya içeriklerinin temel veri bilimi yöntemleriyle analiz edilebileceğini göstermektedir. Simüle edilmiş veri seti kullanılmış olsa da proje; sahte haber yayılımı, bot benzeri hesap davranışı ve kullanıcılar arası ağ ilişkilerinin nasıl incelenebileceğini örneklemektedir.

## Sınırlılıklar

- Veri seti simüle edilmiştir ve gerçek sosyal medya kullanıcılarını içermez.
- Bot tespiti kural tabanlıdır; gelişmiş makine öğrenmesi modeli kullanılmamıştır.
- Sahte haber etiketleri eğitim amacıyla önceden belirlenmiştir.
- Sonuçlar gerçek dünya genellemesi değil, örnek analiz çıktısıdır.

## Hazırlayan

Veri Bilimi ve Analitiği dersi final projesi için hazırlanmıştır.
