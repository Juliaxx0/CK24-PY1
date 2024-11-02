# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, split_ = ','):
    set_str1 = set(str1.split(split_))
    set_str2 = set(str2.split(split_))
    intersection_list = list(set_str1.intersection(set_str2))
    intersection_list.sort()

    return intersection_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
