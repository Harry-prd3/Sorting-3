import random
def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False

def selection_sort():
    answer = input("Would you like a random generated list or would you like to create your own 5 digit list. (enter: own/random)")
    if answer == "own":
        for i in range(5):
            list = int(input("Enter the digit"))


def cycle_sort(array):    
    writes = 0
    compare = 0

    # loop through the array to find cycles to rotate
    for cycleStart in range(0, len(array) -1):
        item = array[cycleStart]

        #check every element to see if it is lower, not already sorted then write and print
        pos = cycleStart
        for i in range(cycleStart + 1, len(array)):
            compare += 1
            if array[i] > pos:
                pos += 1
        temp = array[pos]
        array[pos] = item
        item = temp
        print(array)

        
        #if if the final position is the same then leave the element
        if pos == cycleStart:
            continue
        
        #if there are element with the same value move the current one to the end of those elements and place it. print
        while item == array[pos]:
            pos += 1
            array[pos], item = item, array[pos]
            writes += 1
            print(array)
        
        while pos != cycleStart:
            
            pos = cycleStart
            #check every element to see if it is lower, not already sorted then write and print
            for i in range(cycleStart + 1, len(array)):
                compare += 1
                if array[i] > pos:
                    pos += 1
            temp = array[pos]
            array[pos] = item
            item = temp
            print(array)

            #if there are element with the same value move the current one to the end of those elements and place it. print
            while item == array[pos]:
                pos += 1
                array[pos], item = item, array[pos]
                writes += 1
                print(array)
    
    n = len(array)

    print("After sort : ")
    for i in range(0, n) : 
        print(array[i], end = ' ')
    
    print("number of comparisons: " + compare)
    print("number of writes(swaps): " + writes)
        
        

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def start():
    print("Choose a sorting algorithm:")
    print("1. Comb Sort")
    print("2. Bubble Sort")
    print("3. Selection Sort")
    print("4. Cycle Sort")
    choice = int(input("Enter your choice (1/2/3/4): "))
    choice2= input("Would you like a random generated list or would you like to create your own 5 digit list. (enter: own/random)")
    if choice2 == 'own':
        arr = []
        for i in range(5):
            pass #copy off of suri
        #numbers = input("Enter a list of numbers separated by spaces: ")
        #numbers = int(numbers)
        #arr = numbers.split()
    elif choice2 == 'random':
        [arr] = random.sample(range(1,100, 5))
    else:
        print("Invalid")

    if choice == 1:
        sorted_arr = comb_sort(arr)
    elif choice == 2:
        sorted_arr = bubble_sort(arr)
    elif choice == 3:
        sorted_arr = selection_sort(arr)
    elif choice == 4:
        sorted_arr = cycle_sort(arr)
    else:
        print("Invalid choice.")
        return

    print("Sorted array:", sorted_arr)



start()