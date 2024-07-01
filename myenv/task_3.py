import sys
from pathlib import Path
from colorama import init, Fore, Style # type: ignore

# Ініціалізація colorama для підтримки кольорового виведення
init()

def display_directory_structure(dir_path):
    try:
        # Перевірка, чи існує вказана директорія
        dir_path = Path(dir_path)
        if not dir_path.exists() or not dir_path.is_dir():
            raise FileNotFoundError(f"Directory '{dir_path}' does not exist or is not a directory.")

        # Виведення імен піддиректорій (синій колір)
        print(Fore.BLUE + f"Contents of directory: {dir_path}")
        print(Style.RESET_ALL)  # Скидаємо колір

        for item in dir_path.iterdir():
            if item.is_dir():
                print(Fore.BLUE + f"📁 {item.name}")  # Використовуємо синій колір для директорій
            elif item.is_file():
                print(Fore.GREEN + f"📄 {item.name}")  # Використовуємо зелений колір для файлів
            else:
                print(item.name)

        print(Style.RESET_ALL)  # Скидаємо колір в кінці

    except FileNotFoundError as e:
        print(Fore.RED + f"Error: {e}")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
    finally:
        print(Style.RESET_ALL)  # Завжди скидаємо колір в кінці, навіть якщо виникла помилка

# Отримання шляху до директорії з аргументів командного рядка
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        display_directory_structure(directory_path)
