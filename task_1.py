from pathlib import Path

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                salaries.append(float(line.split(',')[1]))
                
            total_salary = sum(salaries)
            average_salary = total_salary / len(salaries)
            
            return total_salary, average_salary
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
