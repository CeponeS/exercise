def ex1():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')


def ex2():
    lst1 = [1, 4, 6]
    lst2 = [11, 33, 22]
    print(*[i for _, i in sorted(zip(lst2, lst1))])


def ex3():
    A = ["cool", "lock", "cook"]
    lst = []
    res = []
    for i in A:
        temp = list(map(str, i))
        lst.append(temp)
    for _i in lst[0]:
        if len([_i for string in lst[1:] if _i in string]) == (len(lst) - 1):
            for j in range(1, len(lst)):
                lst[j].pop(lst[j].index(_i))
            res.append(_i)
    print(res)


def ex4():
    sub = {"IV": 2, "IX": 2, "XL": 20, "XC": 20, "CD": 200, "CM": 200}
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    string = 'XXVII'

    number = sum(values[char] for char in string)
    number -= sum(val for key, val in sub.items() if key in string)

    print(number)


for k in range(4):
    print(f'exercise {k+1}')
    eval(f'ex{k+1}()')
