from pathlib import Path

def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                id, name, age = line.split(',')
                cats_info.append({"id": id, "name": name, "age": int(age)})
        return cats_info
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

cats_info = get_cats_info("cats_file.txt")
print(cats_info)