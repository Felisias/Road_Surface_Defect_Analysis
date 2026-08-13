import os
import random
import shutil

class AnalyzeSurface:
    def __init__(self, processed_dir, results_dir):
        self.processed_dir = processed_dir
        self.results_dir = results_dir
        self.final_results = []

    def analyze_photos(self):
        """Анализирует фотографии в папке processed."""
        print("[Модуль анализа] Начало анализа фотографий...")

        categories = {
            "road_only": "road",
            "sidewalk_only": "sidewalk",
            "road_and_sidewalk": "both"
        }

        for folder in categories.keys():
            category_dir = os.path.join(self.processed_dir, folder)
            if os.path.exists(category_dir):
                print(f"[Модуль анализа] Анализ категории: {folder}...")
                self.analyze_category(category_dir, folder)
            else:
                print(f"[Модуль анализа] Папка {category_dir} не найдена!")

        self.save_results()
        self.save_human_readable_results()
        print("[Модуль анализа] Анализ завершен.")

    def analyze_category(self, category_dir, category):
        """Анализирует фотографии в каждой категории."""
        for photo in os.listdir(category_dir):
            photo_path = os.path.join(category_dir, photo)
            if photo.endswith(('.jpg', '.jpeg', '.png')):  # Проверка на допустимые форматы
                defects = self.analyze_defects(photo_path, category)
                self.final_results.append(defects)
            else:
                print(f"[Модуль анализа] Пропуск: {photo} (не изображение)")

    def analyze_defects(self, photo_path, category):
        has_defects = random.choice([0, 1])  # 0 - нет, 1 - есть

        has_large_potholes = random.choice([0, 1]) if has_defects else 0
        large_pothole_count = random.randint(1, 3) if has_large_potholes else 0

        has_medium_potholes = random.choice([0, 1]) if has_defects else 0
        medium_pothole_count = random.randint(1, 3) if has_medium_potholes else 0

        has_small_potholes = random.choice([0, 1]) if has_defects else 0
        small_pothole_count = random.randint(1, 5) if has_small_potholes else 0

        # Общий подсчет дефектов: сумма дефектов всех типов
        defect_count = large_pothole_count + medium_pothole_count + small_pothole_count

        # Вычисление коэффициента состояния покрытия
        condition_score = 1 - ((large_pothole_count * 10) + (medium_pothole_count * 7) + (small_pothole_count * 5)) / 100
        condition_score = round(condition_score, 2)  # Округление до двух знаков

        # Создание записи для сохранения
        return {
            "photo": os.path.basename(photo_path),
            "category": category,
            "has_defects": has_defects,
            "defect_count": defect_count,  # Общее количество дефектов
            "has_large_potholes": has_large_potholes,
            "large_pothole_count": large_pothole_count,
            "has_medium_potholes": has_medium_potholes,
            "medium_pothole_count": medium_pothole_count,
            "has_small_potholes": has_small_potholes,
            "small_pothole_count": small_pothole_count,
            "condition_score": condition_score
        }

    def save_results(self):
        """Сохраняет результаты в текстовый файл (machine-readable)."""
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)  # Создать папку, если не существует

        results_path = os.path.join(self.results_dir, "analysis_results.txt")
        with open(results_path, "w") as f:
            for result in self.final_results:
                # Запись результатов в машиночитаемом виде (компактный формат)
                f.write(
                    f"{result['photo']}, {result['category']}, {result['has_defects']}, {result['defect_count']}, "
                    f"{result['has_large_potholes']}, {result['large_pothole_count']}, "
                    f"{result['has_medium_potholes']}, {result['medium_pothole_count']}, "
                    f"{result['has_small_potholes']}, {result['small_pothole_count']}, "
                    f"{result['condition_score']}\n"
                )

        print(f"[Модуль анализа] Результаты сохранены в {results_path}")

    def save_human_readable_results(self):
        """Сохраняет результаты в текстовый файл в удобном для чтения виде."""
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)  # Создать папку, если не существует

        human_results_path = os.path.join(self.results_dir, "human_readable_results.txt")
        with open(human_results_path, "w") as f:
            for result in self.final_results:
                # Запись в удобочитаемом формате
                f.write("Photo: {}\n".format(result['photo']))
                f.write("Category: {}\n".format(result['category']))
                f.write("Has Defects: {}\n".format("Yes" if result['has_defects'] else "No"))
                f.write("Total Defect Count: {}\n".format(result['defect_count']))
                f.write("Large Potholes - Present: {}, Count: {}\n".format(
                    "Yes" if result['has_large_potholes'] else "No", result['large_pothole_count']))
                f.write("Medium Potholes - Present: {}, Count: {}\n".format(
                    "Yes" if result['has_medium_potholes'] else "No", result['medium_pothole_count']))
                f.write("Small Potholes - Present: {}, Count: {}\n".format(
                    "Yes" if result['has_small_potholes'] else "No", result['small_pothole_count']))
                f.write("Condition Score: {}\n".format(result['condition_score']))
                f.write("=========================================\n")  # Разделитель между фото

        print(f"[Модуль анализа] Результаты сохранены в {human_results_path}")


# Функция для вызова анализа
def analyze_surface():
    processed_dir = os.path.join("data", "processed")  # Путь к папке с обработанными фотографиями
    results_dir = os.path.join("data", "results")  # Путь к папке с результатами
    analyzer = AnalyzeSurface(processed_dir, results_dir)
    analyzer.analyze_photos()
