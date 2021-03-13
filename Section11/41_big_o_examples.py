# O(1) constant
def func_constant(values):
    print(values[0])


lst = [1, 2, 3, 4]
func_constant(lst)


# O(n) Linear
def func_linear(values):
    for item in values:
        print(item)


func_linear(lst)


# O(n^2) Quadratic
def func_quad(values):
    for item_1 in values:
        for item_2 in values:
            print(item_1, item_2)


func_quad(lst)


def print_once(values):
    for item in values:
        print(item)


# the O(n)
print_once(lst)


def print_2(values):
    for item in values:
        print(item)

    for item in values:
        print(item)


# O(n) + O(n) = O(2n) or O(n)
print_2(lst)


def comp(values):
    print(values[1])  # O(1)
    for item in values[:(len(values) // 2)]:  # O(n/2)
        print(item)

    for x in range(10):  # O(10)
        print("hello world")


# total = O(1 + n/2 + 10) = O (11 + n/2) almost O(n)
print("printing comp:")
comp(lst)


def matcher(values, match):

    for item in values:
        if item == match:
            return True

    return False


# best case O(1), worth case O(n)
print("Matcher: ")
result = matcher(lst, 4)
print(result)


def create_list(n):
    new_list = []
    for num in range(n):
        new_list.append(num)
    return new_list


l_1 = create_list(5)
print(l_1)


def printer(n):
    for x in range(n):  # time complexity O(n)
        print("hello World")  # space complexity O(1)


printer(5)
