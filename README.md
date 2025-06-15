# 🖼️ Image Finder with CLIP

Консольный Python-скрипт, который находит картинки по описанию с помощью нейросети CLIP от OpenAI.

## 🚀 Возможности

- Находит картинки в папке по текстовому описанию на **английском языке**.
- Использует модель `ViT-B/32` для сопоставления текста и изображения.
- Удобный CLI-ввод для поиска.

## 📋 Требования

- Python 3.10 или выше должен быть установлен и доступен из командной строки (добавлен в PATH).
- PyTorch и остальные зависимости устанавливаются из `requirements.txt`.

## 📦 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/wronguide/image-finder
cd image-finder
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```
Важно: Убедитесь, что Python 3.10+ и PyTorch установлены корректно!

## 🧠 Используемые технологии

- [CLIP](https://github.com/openai/CLIP) — модель для поиска по изображению и тексту  
- [PyTorch](https://pytorch.org/) — фреймворк для нейросетей  
- [NumPy](https://numpy.org/) — работа с массивами  
- [Pillow (PIL)](https://python-pillow.org/) — работа с изображениями  
- [tqdm](https://github.com/tqdm/tqdm) — прогрессбар в консоли


## Как использовать
1. Откройте файл main.py
2. В переменную folder_path поместите путь к папке с картинками
   ```
   folder_path = r"D:\img"
   ```
3. В переменную `search_query` введите промт для поиска картинки
   ```
   search_query = "blue background, paimon, anime art"
   ```
4. Запустите скрипт: `python main.py`
5. Скрипт выведет пути к картинкам. От более похожих до менее.
