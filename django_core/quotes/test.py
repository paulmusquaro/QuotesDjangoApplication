from collections import Counter

def sort_and_remove_duplicates(input_list):
    # Используем Counter для подсчета частоты каждого элемента в списке
    counter = Counter(input_list)
    return list(counter)

# Пример использования
my_list = [5, 5, 5, 5, 5, 5, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

print(result := sort_and_remove_duplicates(my_list))
