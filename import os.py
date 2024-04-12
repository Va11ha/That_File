import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
files.sort(key=lambda x: sum(1 for line in open(x, encoding='utf-8')))

output_file = 'output.txt'

with open(output_file, 'w', encoding='utf-8') as f:
    for file_name in files:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.read()
            f.write(f"{file_name}\n")
            f.write(f"{sum(1 for line in file_content.splitlines())}\n")
            f.write(file_content)
            f.write("\n")

print(f"Файл {output_file} успешно создан")
