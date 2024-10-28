# module_3_hard.ru

def calculate_structure_sum(data_structure):
    all_sum = 0
    if isinstance(data_structure, list) or isinstance(data_structure, tuple) or isinstance(data_structure, set):
        for i in data_structure:
            all_sum += calculate_structure_sum(i)
            # обработка для словарей
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            all_sum += calculate_structure_sum(key)
            all_sum += calculate_structure_sum(value)
    elif isinstance(data_structure, (int, float)):
        all_sum += data_structure
    elif isinstance(data_structure, str):
        all_sum += len(data_structure)
    return all_sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
