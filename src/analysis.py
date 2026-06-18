import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path

# Ana klasör yolları
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "crisis_social_media_data.csv"
VISUALS_DIR = BASE_DIR / "visuals"
VISUALS_DIR.mkdir(exist_ok=True)

# Veri setini okuma
df = pd.read_csv(DATA_PATH)

print("Veri seti başarıyla yüklendi.")
print("Toplam paylaşım sayısı:", len(df))
print("Benzersiz kullanıcı sayısı:", df["user_id"].nunique())
print("Sahte haber paylaşımı sayısı:", df["is_fake_news"].sum())
print("Bot benzeri paylaşım sayısı:", df["bot_suspect"].sum())

# Sahte haber ve gerçek haber dağılımı
fake_counts = df["is_fake_news"].value_counts().sort_index()
plt.figure(figsize=(6, 4))
plt.bar(["Gerçek Haber", "Sahte Haber"], fake_counts.values)
plt.title("Sahte Haber ve Gerçek Haber Dağılımı")
plt.ylabel("Paylaşım Sayısı")
plt.tight_layout()
plt.savefig(VISUALS_DIR / "sahte_gercek_haber_dagilimi.png")
plt.close()

# Ortalama etkileşim karşılaştırması
interaction = df.groupby("is_fake_news")[["like_count", "repost_count"]].mean()
interaction.index = ["Gerçek Haber", "Sahte Haber"]
interaction.plot(kind="bar", figsize=(7, 4))
plt.title("Ortalama Etkileşim Karşılaştırması")
plt.ylabel("Ortalama Değer")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(VISUALS_DIR / "ortalama_etkilesim_karsilastirmasi.png")
plt.close()

# Bot benzeri hesap dağılımı
bot_counts = df["bot_suspect"].value_counts().sort_index()
plt.figure(figsize=(6, 4))
plt.bar(["Normal", "Bot Benzeri"], bot_counts.values)
plt.title("Bot Benzeri Hesap Dağılımı")
plt.ylabel("Paylaşım Sayısı")
plt.tight_layout()
plt.savefig(VISUALS_DIR / "bot_benzeri_hesap_dagilimi.png")
plt.close()

# Hashtag analizi
hashtag_counts = df["hashtag"].value_counts().head(10)
plt.figure(figsize=(9, 4))
plt.bar(hashtag_counts.index, hashtag_counts.values)
plt.title("En Çok Kullanılan Hashtagler")
plt.ylabel("Frekans")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(VISUALS_DIR / "hashtag_analizi.png")
plt.close()

# Ağ analizi
G = nx.from_pandas_edgelist(
    df,
    source="source_user",
    target="target_user",
    create_using=nx.DiGraph()
)

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=500, font_size=8, arrows=True)
plt.title("Sosyal Medya Haber Yayılım Ağı")
plt.tight_layout()
plt.savefig(VISUALS_DIR / "haber_yayilim_agi.png")
plt.close()

# Merkezi kullanıcıları bulma
degree_centrality = nx.degree_centrality(G)
central_users = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)

print("\nEn merkezi 10 kullanıcı:")
for user, score in central_users[:10]:
    print(user, round(score, 4))

print("\nGrafikler visuals klasörüne kaydedildi.")
