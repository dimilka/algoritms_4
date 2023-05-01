def part1():
    n = int(input("Количество экспонатов "))
    print("Для каждого экспоната укажите название, вес и стоимость.")
    d = {}
    for i in range(n):
        name, w, c = input(f"{i + 1}. ").split()
        w, c = int(w), int(c)
        d[name] = (w, c)
    names_dict = dict(sorted(d.items(), key=lambda x: x[1][0], reverse=True))

    times_to_stole = int(input("Количество заходов "))
    max_weight = int(input(f"Вместительность "))
    All_cost, All_names = 0, ''
    for _ in range(times_to_stole):
        cost, names, id = dp(names_dict, max_weight)
        N_cost, N_names = cost[id - 1][-1], names[id - 1][-1]
        All_cost += N_cost
        All_names += N_names
        for val in N_names.split():
            del names_dict[val.strip()]
    if All_cost != 0:
        print(f"Украденная сумма: {All_cost}")
        print(f"Украденные экспонаты: {All_names}")
    else:
        print("Ничего украсть не удалось.")

def dp(names_dict, max_weight):
    area = [names_dict[item][0] for item in names_dict]
    value = [names_dict[item][1] for item in names_dict]
    n = len(value)  # находим размеры таблицы

    # создаём таблицу из нулевых значений
    tabl_of_cost = [[0 for a in range(max_weight + 1)] for i in range(n + 1)]
    tabl_of_names = [['' for a in range(max_weight + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for a in range(max_weight + 1):
            # базовый случай
            if i == 0 or a == 0:
                tabl_of_cost[i][a] = 0
                tabl_of_names[i][a] = ''

            # если площадь предмета меньше площади столбца,
            # максимизируем значение суммарной ценности
            elif area[i - 1] <= a:
                if value[i - 1] + tabl_of_cost[i - 1][a - area[i - 1]] > tabl_of_cost[i - 1][a]:
                    tabl_of_cost[i][a] = value[i - 1] + tabl_of_cost[i - 1][a - area[i - 1]]
                    tabl_of_names[i][a] = list(names_dict.keys())[list(names_dict.values()).index((area[i - 1], value[i - 1]))] +\
                                          ' ' + tabl_of_names[i - 1][a - area[i - 1]]
                else:
                    tabl_of_cost[i][a] = tabl_of_cost[i - 1][a]
                    tabl_of_names[i][a] = tabl_of_names[i - 1][a]

            # если площадь предмета больше площади столбца,
            # забираем значение ячейки из предыдущей строки
            else:
                tabl_of_cost[i][a] = tabl_of_cost[i - 1][a]
                tabl_of_names[i][a] = tabl_of_names[i - 1][a]
    return tabl_of_cost, tabl_of_names, len(tabl_of_cost)


part1()