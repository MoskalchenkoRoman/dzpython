# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')