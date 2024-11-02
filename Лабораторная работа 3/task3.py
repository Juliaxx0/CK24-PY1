# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()

    letter_list = []
    for letter in range(len(text)):
        if text[letter].isalpha() and text[letter] not in letter_list:
            letter_list.append(text[letter])

    letter_dict = {}
    for letter in letter_list:
        letter_dict[letter] = text.count(letter)

    return letter_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dictionary):
    count_letter = 0
    for count in dictionary.values():
        count_letter += count

    frequency_dict = {}
    for keys, value in dictionary.items():
        frequency_dict[keys] = round(value / count_letter, 2)

    return frequency_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

dict_ = calculate_frequency(count_letters(main_str))

for key, value in dict_.items():
    print(key + ': ' + '%.2f' % value)