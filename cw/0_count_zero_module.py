
def count_elements_mul(A: list, divider: int) -> int:
    """
    Функция считает элементы кратные divider.

    :param A: список целых чисел
    :param divider: целое число, показатель кратности
    :return: количество элементов кратных divider
    """
    k=0
    for i in A:
        if A[i]%divider==0:
            k+=1
    return (k)



    # for elem in A:
    #     # i = 0 1 2 3 4 5 ... n-1
    #     # n = 3  i = 0 1 2
    #     if elem % divider == 0:
    #         k += 1
    # return k

class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def test_count_elements_mul(A, divider, result):
    test_result = count_elements_mul(A, divider)
    check = test_result == result
    if len(A) > 10:
        A = A[:5] + ["..."] + A[-5:]
    print("A =", A)
    print(f"divider = {divider}; result = {result}; test_result = {test_result}")
    print(f"{bcolors.OK}Test passed{bcolors.ENDC}" if check else f"{bcolors.FAIL}Test failed{bcolors.ENDC}")


def test():
    A = [1, 2, 3, 4, 5]
    divider = 3
    result = 1
    test_count_elements_mul(A, divider, result)

    A = [3, 3, 3, 3, 3, 3]
    divider = 3
    result = 6
    test_count_elements_mul(A, divider, result)

    A = list(range(0, 10000))
    divider = 33
    result = 304
    test_count_elements_mul(A, divider, result)


if __name__ == "__main__":
    test()
