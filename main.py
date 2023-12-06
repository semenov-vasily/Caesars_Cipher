# Функция шифрующая текст в соответствии с алгоритмом Цезаря
def caesar(direction, language, step, text):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for i in range(len(text)):
        if language == 'ru':   # Параметры русского алфавита
            sumbols = 32
            lower_alphabet = rus_lower_alphabet
            upper_alphabet = rus_upper_alphabet
        if language == 'en':   # Параметры английского алфавита
            sumbols = 26
            lower_alphabet = eng_lower_alphabet
            upper_alphabet = eng_upper_alphabet
        if text[i].isalpha():   # Является ли символ буквой
            if text[i] == text[i].lower():
                ind = lower_alphabet.index(text[i])   # Индекс строчной буквы в алфавите
            if text[i] == text[i].upper():
                ind = upper_alphabet.index(text[i])   # Индекс заглавной буквы в алфавите
            if direction == '+':
                index = (ind + step) % sumbols    # Индекс буквы при шифровании с шагом step
            if direction == '-':
                index = (ind - step) % sumbols    # Индекс буквы при дешифровании с шагом step
            if text[i] == text[i].lower():
                print(lower_alphabet[index], end='')   # Вывод строчной буквы в итоговый текст
            if text[i] == text[i].upper():
                print(upper_alphabet[index], end='')   # Вывод заглавной буквы в итоговый текст
        else:
            print(text[i], end='')   # Вывод не буквенных символов в итоговый текст


if __name__ == '__main__':
    # Ввод основных параметров
    direction = input('Введите направление шифрования +/-: ')
    language = input('Какой язык ru/en: ')
    step = int(input('Какой шаг: '))
    text = input('Текст: ')

    # Вызов функции
    caesar(direction, language, step, text)
