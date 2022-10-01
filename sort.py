from re import A
from select import select

import time
from turtle import left, right
def SelectionSort(a):
        for i in range(0,len(a)):
                for j in range(i+1,len(a)):
                        if a[i] > a[j]:
                                a[i],a[j] = a[j],a[i]
                
        return a
def BubbleSort(a):
        for i in range(0,len(a)):
                for j in range(i+1,len(a)-1):
                        if a[j] > a[j+1]:
                                a[j],a[j+1] = a[j+1],a[j]

        return a
def Quicksort(a):
        if len(a) < 2:
                return a
        else:
                k = a[0]
                left = [i for i in a[1:] if i <=k]
                right = [i for i in a[1:] if i > k]
                return Quicksort(left) + [k] + Quicksort(right)

def main():
        import random
        arr = []
        for i in range(10):
                x = random.randint(0,100)
                arr.append(x)
        print(arr)
        sap_xep_chon = SelectionSort(arr)
        sap_xep_noi_bot = BubbleSort(arr)
        sap_xep_nhanh = Quicksort(arr)
        print("Dùng sắp xếp chọn ra được: ",sap_xep_chon)
        print("Dùng sắp xếp nổi bọt ra được: ",sap_xep_noi_bot)
        print("Dùng sắp xếp nhanh ra được: ",sap_xep_nhanh)
main()