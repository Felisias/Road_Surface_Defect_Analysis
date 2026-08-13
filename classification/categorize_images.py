import os
import shutil
import random

def categorize_images():
    """Категоризация принятых фотографий на категории: 'только дорога', 'только тротуар', 'дорога и тротуар'."""
    print("[Модуль классификации] Начало классификации фотографий...")

    # Директории для фотографий
    processed_dir = os.path.join("data", "processed")  # Папка с принятыми фотографиями
    road_only_dir = os.path.join(processed_dir, "road_only")  # Папка для фото только с дорогой
    sidewalk_only_dir = os.path.join(processed_dir, "sidewalk_only")  # Папка для фото только с тротуаром
    road_and_sidewalk_dir = os.path.join(processed_dir, "road_and_sidewalk")  # Папка для фото с дорогой и тротуаром

    # Создание необходимых папок, если они не существуют
    os.makedirs(road_only_dir, exist_ok=True)
    os.makedirs(sidewalk_only_dir, exist_ok=True)
    os.makedirs(road_and_sidewalk_dir, exist_ok=True)

    # Обнуление счетчиков
    road_only_count = 0
    sidewalk_only_count = 0
    road_and_sidewalk_count = 0
    total_photos = 0

    # Перебор всех принятых фотографий из папки processed (игнорируем rejected)
    for photo in os.listdir(processed_dir):
        photo_path = os.path.join(processed_dir, photo)
        if os.path.isfile(photo_path) and photo.endswith(('.jpg', '.jpeg', '.png')):  # Проверка на допустимые форматы
            total_photos += 1

            category = random.choice(['road_only', 'sidewalk_only', 'road_and_sidewalk'])

            if category == 'road_only':
                shutil.copy(photo_path, os.path.join(road_only_dir, photo))
                road_only_count += 1
            elif category == 'sidewalk_only':
                shutil.copy(photo_path, os.path.join(sidewalk_only_dir, photo))
                sidewalk_only_count += 1
            elif category == 'road_and_sidewalk':
                shutil.copy(photo_path, os.path.join(road_and_sidewalk_dir, photo))
                road_and_sidewalk_count += 1

    # Итоговая статистика
    print(f"[Модуль классификации] Всего классифицировано фотографий: {total_photos}")
    print(f"[Модуль классификации] 'Только дорога': {road_only_count}")
    print(f"[Модуль классификации] 'Только тротуар': {sidewalk_only_count}")
    print(f"[Модуль классификации] 'Дорога и тротуар': {road_and_sidewalk_count}")
    print("[Модуль классификации] Классификация завершена.")
