# 🖼️ Image Finder with CLIP

Консольный Python-скрипт, который находит картинки по описанию с помощью нейросети CLIP от OpenAI.

## 🚀 Возможности

- Находит картинки в папке по текстовому описанию на **английском языке**.
- Использует модель `ViT-B/32` для сопоставления текста и изображения.
- Удобный CLI-ввод для поиска.

## Как запустить

### Вариант 1: Готовый EXE (рекомендуется)

1. Скачай последнюю версию EXE [по ссылке.](https://github.com/wronguide/image-finder/releases/latest/download/image-finder.exe
)
2. Запусти файл `image-finder.exe`.
3. Следуй подсказкам в консоли.

### Вариант 2: Из исходников (требуется Python и зависимости)

#### 📋 Требования

- Python 3.10 или выше должен быть установлен и доступен из командной строки (добавлен в PATH).
- PyTorch и остальные зависимости устанавливаются из `requirements.txt`.

#### 📦 Установка

1. Клонируй репозиторий:

```bash
git clone https://github.com/wronguide/image-finder
cd image-finder
```

2. Установи зависимости:

```bash
pip install -r requirements.txt
```
Важно: Убедись, что Python 3.10+ и PyTorch установлены корректно!

#### 🧠 Используемые технологии

- [CLIP](https://github.com/openai/CLIP) — модель для поиска по изображению и тексту  
- [PyTorch](https://pytorch.org/) — фреймворк для нейросетей  
- [NumPy](https://numpy.org/) — работа с массивами  
- [Pillow (PIL)](https://python-pillow.org/) — работа с изображениями  
- [tqdm](https://github.com/tqdm/tqdm) — прогрессбар в консоли


#### Как использовать
1. Запусти скрипт: `python main.py`
2. Следуй подсказкам в консоли.
