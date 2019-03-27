# -*- coding: utf-8 -*-
import random
import sys
import time

sys.setrecursionlimit(100000)


def input_random(size):
    sort_list=[]
    for i in range(0, size):
        sort_list.append(random.randint(1, size))
    return sort_list


def input_reverse(size):
    sort_list=[]
    for i in range(size, 0, -1):
        sort_list.append(i)
    return sort_list


def swap(sort_list, i, j):
    tmp = sort_list[i]
    sort_list[i] = sort_list[j]
    sort_list[j] = tmp
    return sort_list


def bubble_sort(sort_list, size):
    for i in range(0, size - 1):
        for j in range(0, size - i - 1):
            if sort_list[j] > sort_list[j + 1]:
                swap(sort_list, j, j + 1)
    return sort_list


def selection_sort(sort_list, size):
    for i in range(0, size - 1):
        min_idx = 1
        for j in range(i + 1, size):
            if (sort_list[j] < sort_list[min_idx]):
                min_idx = j
        swap(sort_list, min_idx, i)
    return sort_list


def insertion_sort(sort_list, size):
    for i in range(1, size):
        key = sort_list[i]
        j = i
        while j > 0 and sort_list[j - 1] > key:
            sort_list[j] = sort_list[j - 1]
            j -= 1
        sort_list[j] = key
    return sort_list


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]

    return result


def merge_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list

    mid = int(len(sort_list) / 2)
    leftList = sort_list[:mid]
    rightList = sort_list[mid:]

    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)


def partition1(sort_list,first, last):
    x = sort_list[last]
    i = first - 1
    for j in range(first, last):
        if sort_list[j] <= x:
            i += 1
            swap(sort_list, i, j)
    swap(sort_list, i + 1, last)
    return i + 1


# pivot 마지막
def quicksort1(sort_list,p, r):
    if p < r:
        q = partition1(sort_list,p, r)
        quicksort1(sort_list,p, q - 1)
        quicksort1(sort_list,q + 1, r)


def partition2(sort_list,first, last):
    mid = int((last + first) / 2)
    dic = {sort_list[first]: first, sort_list[mid]: mid, sort_list[last]: last}
    a = [sort_list[first], sort_list[mid], sort_list[last]]
    a.sort()
    pivot_index = dic[a[1]]
    swap(sort_list, last, pivot_index)
    x = a[1]
    i = first - 1
    for j in range(first, last):
        if sort_list[j] <= x:
            i += 1
            swap(sort_list, i, j)
    swap(sort_list, i + 1, last)
    return i + 1


# pivot 랜덤값
def quicksort2(sort_list, p, r):
    if p < r:
        q = partition2(sort_list,p, r)
        quicksort2(sort_list,p, q - 1)
        quicksort2(sort_list,q + 1, r)


def partition3(sort_list,first, last):
    pivot_index = random.randint(first, last)
    swap(sort_list, last, pivot_index)
    x = sort_list[last]
    i = first - 1
    for j in range(first, last):
        if sort_list[j] <= x:
            i += 1
            swap(sort_list, i, j)
    swap(sort_list, i + 1, last)
    return i + 1


# pivot 마지막
def quicksort3(sort_list,p, r):
    if p < r:
        q = partition3(sort_list,p, r)
        quicksort3(sort_list,p, q - 1)
        quicksort3(sort_list,q + 1, r)


def main():

    unsort_list=[]
    time_list=[]
    ##버블정렬 100000은 20분넘게 걸려 제외했습니다
    print("\t\t\t\tRandom1000\t\t\tReverse1000\t\t\tRandom10000\t\t\tReverse10000\t\t\tRandom100000\t\t\tReverse100000")
    print("Bubble\t\t\t\t\t", end='')
    for i in [1000,10000]:
        unsort_list = input_random(i)
        start_time = time.time()
        bubble_sort(unsort_list, i)
        end_time1 = time.time()-start_time
        time_list.append(end_time1)

        unsort_list = input_reverse(i)
        start_time = time.time()
        bubble_sort(unsort_list, i)
        end_time2 = time.time()-start_time
        time_list.append(end_time2)

    for t in time_list:
        print("%0.3f" % t, end='\t\t\t\t\t\t')
    print("\n")

    # 선택 정렬 100000은 20분넘게 걸려 제외했습니다.
    time_list=[]
    print("Selection\t\t\t\t", end='')
    for i in [1000, 10000]:
        unsort_list = input_random(i)
        start_time = time.time()
        selection_sort(unsort_list, i)
        end_time1 = time.time()-start_time
        time_list.append(end_time1)

        unsort_list = input_reverse(i)
        start_time = time.time()
        selection_sort(unsort_list, i)
        end_time2 = time.time()-start_time
        time_list.append(end_time2)

    for t in time_list:
        print("%0.3f" % t, end='\t\t\t\t\t\t')
    print("\n")


    # 삽입 정렬 100000은 너무 오래걸려 뺐습니다.
    time_list=[]
    print("Insertion\t\t\t\t", end='')
    for i in [1000,10000]:
        unsort_list=input_random(i)
        start_time=time.time()
        insertion_sort(unsort_list,i)
        end_time1=time.time()-start_time
        time_list.append(end_time1)

        unsort_list=input_reverse(i)
        start_time=time.time()
        insertion_sort(unsort_list,i)
        end_time2=time.time()-start_time
        time_list.append(end_time2)

    for t in time_list:
        print("%0.3f" % t, end='\t\t\t\t\t\t')
    print("\n")

    # 합병정렬
    time_list=[]
    print("Merge\t\t\t\t\t", end='')
    for i in [1000,10000,100000]:
        unsort_list=input_random(i)
        start_time=time.time()
        merge_sort(unsort_list)
        end_time1=time.time()-start_time
        time_list.append(end_time1)

        unsort_list=input_reverse(i)
        start_time=time.time()
        merge_sort(unsort_list)
        end_time2=time.time()-start_time
        time_list.append(end_time2)
    for t in time_list:
        print("%0.3f" % t, end='\t\t\t\t\t\t')
    print("\n")

    #퀵소트1 마지막 값 피봇, reverse 10000부터 스택오버플로우 발생
    time_list=[]
    print("Quick1\t\t\t\t\t", end='')
    for i in [1000,10000]:
        unsort_list = input_random(i)
        start_time = time.time()
        quicksort1(unsort_list,0, i-1)
        end_time1 = time.time()-start_time
        time_list.append(end_time1)
        if i == 10000:
            break
        unsort_list=input_reverse(i)
        start_time = time.time()
        quicksort1(unsort_list,0, len(unsort_list) - 1)
        end_time2 = time.time() - start_time
        time_list.append(end_time2)

    for t in time_list:
        print("%0.3f" % t, end='\t\t\t\t\t\t')
    print("\n")


    # 퀵소트2 중간값 피봇
    time_list = []
    print("Quick2\t\t\t\t\t", end='')
    for i in [1000,10000,100000]:
        unsort_list = input_random(i)
        start_time = time.time()
        quicksort2(unsort_list, 0, i - 1)
        end_time1 = time.time() - start_time
        time_list.append(end_time1)

        unsort_list = input_reverse(i)
        start_time = time.time()
        quicksort2(unsort_list, 0, len(unsort_list) - 1)
        end_time2 = time.time() - start_time
        time_list.append(end_time2)

    for t in time_list:
        print("%0.3f" % t, end='\t\t\t\t\t\t')
    print("\n")

    #퀵소트3 랜덤피봇
    time_list = []
    print("Quick3\t\t\t\t\t", end='')
    for i in [1000,10000,100000]:
        unsort_list = input_random(i)
        start_time = time.time()
        quicksort3(unsort_list, 0, i - 1)
        end_time1 = time.time() - start_time
        time_list.append(end_time1)

        unsort_list = input_reverse(i)
        start_time = time.time()
        quicksort3(unsort_list, 0, len(unsort_list) - 1)
        end_time2 = time.time() - start_time
        time_list.append(end_time2)

    for t in time_list:
        print("%0.3f" % t, end='\t\t\t\t\t\t')
    print("\n")


main()
