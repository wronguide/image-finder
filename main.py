import os
import clip
import torch
from PIL import Image

# Загрузка модели
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Папка с картинками
folder_path = r"D:\img"

# Ввод текста
search_query = "blue background, paimon, anime art"

# Преобразуем текст в вектор
text_tokens = clip.tokenize([search_query]).to(device)
text_features = model.encode_text(text_tokens)

# Сканируем картинки
image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
               f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Храним результаты
results = []

for image_path in image_paths:
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    with torch.no_grad():
        image_features = model.encode_image(image)

    similarity = torch.cosine_similarity(image_features, text_features)
    results.append((image_path, similarity.item()))

# Сортируем по совпадению
results.sort(key=lambda x: x[1], reverse=True)

# Показываем топ-5
print("\n🎯 Похожие картинки:")
for path, score in results[:5]:
    print(f"{score:.3f} — {path}")
