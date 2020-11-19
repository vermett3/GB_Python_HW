def division(*args):
    try:
        x = int(input("Введите 1е число "))
        y = int(input("Введите 2е число "))
        r = x / y
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"

    return r

print(f'result {division()}')
