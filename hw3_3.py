def my_func(x, y, z):
    sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    print(sum(total))

print(my_func(int(input("введите 1е число ")), int(input("введите 2е число ")), int(input("введите 3е число "))))