from random import randint
from time import time

mylist = []
for i in range(1000):
    mylist.append(randint(1, 1000))

def selsort(alist):
    for i in range(0, len(alist)-1):
        min_pos = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min_pos]:
                min_pos = j
        alist[i], alist[min_pos] = alist[min_pos], alist[i]  
    return alist  

def efficient_bubsort(alist):
    for i in range(len(alist)-1, 0, -1):
        swapped = False
        for j in range(0, i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                swapped = True
        if swapped == False:
            return alist
    return alist

def bubsort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(0, i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

def insort(alist):
    for i in range(1, len(alist)):
        value = alist[i]
        position = i

        while position > 0 and alist[position-1]>value:
            alist[position] = alist[position-1]
            position -= 1

        alist[position] = value
    return alist

def mergesort(alist):
    
    if len(alist) > 1:
        mid = len(alist) // 2
        LH = alist[:mid]
        RH = alist[mid:]

        mergesort(LH)
        mergesort(RH)

        l = 0
        r = 0
        k = 0
        while l < len(LH) and r < len(RH):
            if LH[l] <= RH[r]:
                alist[k] = LH[l]
                k += 1
                l += 1

            else:
                alist[k] = RH[r]
                k += 1
                r += 1

        while l < len(LH):
            alist[k] = LH[l]
            l += 1
            k += 1
        
        while r < len(RH):
            alist[k] = RH[r]
            r += 1
            k += 1

    

def main(trials):
    mylist
    print('Starting time trials... Please Wait.')
    
    total = 0
    for i in range(trials):
        start = time()
        bsorted = bubsort(mylist)
        end = time()
        duration = (end - start) * 1000
        total += duration
    avg_dur = total/trials
    print(f'The average time to complete bubble sort: {avg_dur:.5f} milliseconds.')
    

    total = 0
    for i in range(trials):
        start = time()
        bsorted = efficient_bubsort(mylist)
        end = time()
        duration = (end - start) * 1000
        total += duration
    avg_dur = total/trials
    print(f'The average time to complete efficient bubble sort: {avg_dur:.10f} milliseconds.')

    total = 0
    for i in range(trials):
        start = time()
        bsorted = insort(mylist)
        end = time()
        duration = (end - start) * 1000
        total += duration
    avg_dur = total/trials
    print(f'The average time to complete insertion sort: {avg_dur:.10f} milliseconds.')

    total = 0
    for i in range(trials):
        start = time()
        bsorted = selsort(mylist)
        end = time()
        duration = (end - start) * 1000
        total += duration
    avg_dur = total/trials
    print(f'The average time to complete selection sort: {avg_dur:.10f} milliseconds.')

    total = 0
    for i in range(trials):
        start = time()
        bsorted = mergesort(mylist)
        end = time()
        duration = (end - start) * 1000
        total += duration
    avg_dur = total/trials
    print(f'The average time to complete merge sort: {avg_dur:.10f} milliseconds.')


if __name__ == "__main__":
    main(int(input('How many trials would you like to run for each sort method? ')))