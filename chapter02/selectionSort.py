# coding:utf-8

__author__ = 'Janvn'

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))    #pop根据索引删除元素，并返回删除的元素值
    return newArr


def main():
    testArr = [5,4,6,2,7,10,20,15]
    print(selectionSort(testArr))      #[2, 4, 5, 6, 7, 10, 15, 20]


if __name__ == '__main__':
    main()