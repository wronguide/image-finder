import os
import clip
import torch
from PIL import Image
from pathlib import Path ##что это
import os
import platform
import subprocess

def open_image(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", path])
    else:  # Linux и прочие
        subprocess.run(["xdg-open", path])


def get_device():
    return "cuda" if torch.cuda.is_available() else "cpu" ##что это


def ensure_model_loaded(model_name="ViT-B/32", cache_dir="./model_cache", device="cpu"):
    os.makedirs(cache_dir, exist_ok=True)
    model, preprocess = clip.load(model_name, device=device, download_root=cache_dir)
    return model, preprocess


def get_image_paths(folder_path):
    path = Path(folder_path)
    if not path.exists() or not path.is_dir():
        raise FileNotFoundError("Папка не найдена или путь неверен.")
    return [str(p) for p in path.iterdir() if p.suffix.lower() in [".jpg", ".jpeg", ".png"]]


def encode_text(model, query, device):
    tokens = clip.tokenize([query]).to(device)
    return model.encode_text(tokens)


def encode_image(model, image_path, preprocess, device):
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    with torch.no_grad():
        return model.encode_image(image)


def find_similar_images(model, preprocess, image_paths, text_features, device):
    results = []
    for image_path in image_paths:
        try:
            image_features = encode_image(model, image_path, preprocess, device)
            similarity = torch.cosine_similarity(image_features, text_features)
            results.append((image_path, similarity.item()))
        except Exception as e:
            print(f"⚠️ Проблема с файлом {image_path}: {e}")
    return sorted(results, key=lambda x: x[1], reverse=True)

def main():
    device = get_device()
    model, preprocess = ensure_model_loaded(device=device)

    while True:
        folder_path = input("📁 Введи путь к папке с картинками: ").strip().replace("\\", "/")
        search_query = input("🔎 Введи промпт: ").strip()

        if not search_query:
            print("❌ Ошибка: Введен пустой промпт.")
            continue  # вернуться к вводу

        try:
            image_paths = get_image_paths(folder_path)
            if not image_paths:
                print("❌ В папке нет подходящих изображений.")
                continue
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            continue

        try:
            text_features = encode_text(model, search_query, device)
        except Exception as e:
            print(f"❌ Ошибка при обработке текста: {e}")
            continue

        results = find_similar_images(model, preprocess, image_paths, text_features, device)

        if results:
            print("\n🎯 Топ-5 похожих картинок:")
            for i, (path, score) in enumerate(results[:5], 1):
                print(f"{i}. {score:.3f} — {path}")

            choice = input("\n🖼 Введи номер картинки, чтобы открыть, или Enter чтобы пропустить: ").strip()
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(results[:5]):
                    open_image(results[idx][0])
                else:
                    print("❌ Неверный номер.")
        else:
            print("😕 Ничего похожего не найдено.")

        # Тут вопрос — повторить или выйти?
        choice = input("\n🔄 Ввести новый запрос? (д/н): ").strip().lower()
        if choice != 'д' and choice != 'y' and choice != 'yes':
            print("👋 Пока!")
            break


if __name__ == "__main__":
    main()
