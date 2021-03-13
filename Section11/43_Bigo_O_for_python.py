def method1():
    l_1 = []
    for n in range(100):
        l_1 = l_1 + [n]

    print(l_1)


method1()


def method2():
    l_2 = []
    for n in range(100):
        l_2.append(n)
    print(l_2)


method2()


def method3():
    l_3 = [n for n in range(100)]
    print(l_3)


method3()


def method4():
    l_4 = list(range(100))
    print(l_4)


method4()