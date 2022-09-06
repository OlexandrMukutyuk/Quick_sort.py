import random
from datetime import datetime


def gen_array(arr, len):
    arr.clear()
    for i in range(len):
        arr.append(random.randint(0, 100000))


def quick_sort(ar):
    arr = ar.copy()
    if len(arr) <= 1:
        return arr
    number = int((len(arr) - 1) / 2)
    first = []
    last = []
    for item in range(len(arr)):
        if item != number:
            if arr[item] <= arr[number]:
                first.append(arr[item])
            else:
                last.append(arr[item])
    return quick_sort(first) + [arr[number]] + quick_sort(last)


def choise_sort(ar):
    arr = ar.copy()
    for item in range(len(arr)):
        tmp = item
        for i in range(item,len(arr)):
            if arr[tmp] > arr[i]:
                tmp = i
        tmp2 = arr[tmp]
        arr[tmp] = arr[item]
        arr[item] = tmp2
    return arr


def auto_test():
    a = []
    gen_array(a,5000)
    print("5000 elements")
    start_time = datetime.now()
    choise_sort(a)
    print(f"to choise sort \t{datetime.now() - start_time}")
    start_time = datetime.now()
    quick_sort(a)
    print(f"to quick sort \t{datetime.now() - start_time}")

    gen_array(a, 10000)
    print("10000 elements")
    start_time = datetime.now()
    choise_sort(a)
    print(f"to choise sort \t{datetime.now() - start_time}")
    start_time = datetime.now()
    quick_sort(a)
    print(f"to quick sort \t{datetime.now() - start_time}")
    gen_array(a, 15000)
    print("15000 elements")
    start_time = datetime.now()
    choise_sort(a)
    print(f"to choise sort \t{datetime.now() - start_time}")
    start_time = datetime.now()
    quick_sort(a)
    print(f"to quick sort \t{datetime.now() - start_time}")
    gen_array(a, 20000)
    print("20000 elements")
    start_time = datetime.now()
    choise_sort(a)
    print(f"to choise sort \t{datetime.now() - start_time}")
    start_time = datetime.now()
    quick_sort(a)
    print(f"to quick sort \t{datetime.now() - start_time}")

    gen_array(a, 100000)
    print("100000 elements")
    start_time = datetime.now()
    choise_sort(a)
    print(f"to choise sort \t{datetime.now() - start_time}")
    start_time = datetime.now()
    quick_sort(a)
    print(f"to quick sort \t{datetime.now() - start_time}")


if __name__ == "__main__":
    auto_test()