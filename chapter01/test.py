# -*- coding:utf-8 -*-

'''
《图解算法》第一章     《grokking algorithms》
binary_search algorithms    二分查找法
'''

def binary_search(testList,item):

    low=0
    high=len(testList)-1

    while low<=high:
        #mid=int((low+high)/2)
        mid=(low+high)//2      # 注意：python 3.x中除法运算有变化
        guess=testList[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':

    myList = [1,3,5,7,9]
    print(binary_search(myList,3))
    # print(binary_search(myList,0))