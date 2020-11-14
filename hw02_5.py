my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
rankings = int(input("Введите оценку или '777' для завершения формирования рейтинга "))
while rankings != 777:
    for el in range(len(my_list)):
        if my_list[el] == rankings:
            my_list.insert(el + 1, rankings)
            break
        elif my_list[0] < rankings:
            my_list.insert(0, rankings)
        elif my_list[-1] > rankings:
            my_list.append(rankings)
        elif my_list[el] > rankings and my_list[el + 1] < rankings:
            my_list.insert(el + 1, rankings)
    print(f"текущий список - {my_list}")
    rankings = int(input("Введите оценку или '777' для завершения формирования рейтинга "))