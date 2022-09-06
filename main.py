import random
from datetime import datetime


def gen_array(arr, len):
    arr.clear()
    for i in range(len):
        arr.append(random.randint(0,100000000))
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    number = int((len(arr)-1)/2)
    first = []
    last = []
    for item in range(len(arr)):
        if item != number:
            if arr[item] <= arr[number]:
                first.append(arr[item])
            else:
                last.append(arr[item])
    return quick_sort(first) + [arr[number]] + quick_sort(last)

def auto_test(N):
    sr_znach = 0.
    arr = []
    for i in range(N):
        gen_array(arr, 50000)
        start_time = datetime.now()
        arr = quick_sort(arr)
        tmp = datetime.now() - start_time
        #print(tmp)
        sr_znach += float(tmp.total_seconds())

    return(sr_znach / N)

if __name__ == '__main__':
    for i in range(2):
        tmp1 = auto_test(5)
        tmp2 = auto_test(5)
        tmp3 = auto_test(5)
        print("5 - ",float('{:.6f}'.format(((tmp1 + tmp2 + tmp3) / 3))))
        tmp1 = auto_test(10)
        tmp2 = auto_test(10)
        tmp3 = auto_test(10)
        print("10 - ",float('{:.6f}'.format(((tmp1 + tmp2 + tmp3) / 3))))
        tmp1 = auto_test(15)
        tmp2 = auto_test(15)
        tmp3 = auto_test(15)
        print("15 - ",float('{:.6f}'.format(((tmp1 + tmp2 + tmp3) / 3))))
        tmp1 = auto_test(20)
        tmp2 = auto_test(20)
        tmp3 = auto_test(20)
        print("20 - ",float('{:.6f}'.format(((tmp1 + tmp2 + tmp3) / 3))))
        print('-----')