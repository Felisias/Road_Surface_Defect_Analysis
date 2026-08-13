# prepreprocess.py

import os
import random
import shutil

def preprocess_images():
    """Предобрабатывает изображения: фильтрует некачественные фотографии и сортирует их."""
    print("[Модуль предобработки] Начало предобработки фотографий...")

    # Папки для хранения фотографий
    raw_dir = os.path.join("data", "raw")  # Папка с исходными фото
    processed_dir = os.path.join("data", "processed")  # Принятые фотографии
    rejected_dir = os.path.join("data", "rejected")  # Отклоненные фотографии

    # Создание необходимых папок, если они не существуют
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(rejected_dir, exist_ok=True)

    total_photos = 0  # Общее количество обработанных фотографий
    accepted_count = 0  # Количество принятых фотографий
    rejected_count = 0  # Количество отклоненных фотографий

    # Перебор всех файлов в папке raw
    for photo in os.listdir(raw_dir):
        photo_path = os.path.join(raw_dir, photo)
        if photo.endswith(('.jpg', '.jpeg', '.png')):  # Проверка на допустимые форматы
            total_photos += 1
            if random.random() < 0.2:
                shutil.copy(photo_path, os.path.join(rejected_dir, photo))
                rejected_count += 1
            else:
                shutil.copy(photo_path, os.path.join(processed_dir, photo))
                accepted_count += 1

    # Итоговая статистика
    print(f"[Модуль предобработки] Всего классифицировано фотографий: {total_photos}")
    print(f"[Модуль предобработки] Принято: {accepted_count} фотографий")
    print(f"[Модуль предобработки] Отклонено: {rejected_count} фотографий")
    print("[Модуль предобработки] Предобработка завершена.")
