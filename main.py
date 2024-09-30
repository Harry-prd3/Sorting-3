import random
def comb_sort(array):
    writes = 0
    compare = 0
    
    gap = len(array)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        for i in range(len(array) - gap):
            compare += 1
            if array[i] > array[i + gap]:
                writes +=1
                array[i], array[i + gap] = array[i + gap], array[i]
                sorted = False
                print(array)
            i += 1
    print(f"number of comparisons: {compare}")
    print(f"number of writes(swaps): {writes}")
    return array

def create_list(array):
    answer = input("Would you like a randomly generated list or would you like to create your own 5? (enter: own/random) ")
    if answer == "own":
        array = []
        for i in range(5):
            num = int(input("Enter the digit: "))
            array.append(num)
        print("Your list is: ", array)
        return array
    elif answer == "random":
        array = []
        for i in range(5):
            array.append(random.randint(0, 50))
        print("Your list is: ", array)
    else:
        print("That's not a valid option. Must be 'own' or 'random'. Please run it again and enter a valid option.")
                
    writes = 0
    compare = 0

    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            compare += 1
            if array[j] < array[min_index]:
                min_index = j
        writes += 1
        array[i], array[min_index] = array[min_index], array[i]
    
    print(f"number of comparisons: {compare}")
    print(f"number of writes(swaps): {writes}")

    if array:
        sorted_array = create_list(array)
        print("Sorted list is:", sorted_array)
    return array
    

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
            if array[i] < item:
                pos += 1
        temp = array[pos]
        array[pos] = item
        item = temp
        writes += 1
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
                if array[i] < item:
                    pos += 1
            temp = array[pos]
            array[pos] = item
            item = temp
            writes += 1
            print(array)

            #if there are element with the same value move the current one to the end of those elements and place it. print
            while item == array[pos]:
                pos += 1
                array[pos], item = item, array[pos]
                writes += 1
                print(array)
    
    print(f"number of comparisons: {compare}")
    print(f"number of writes(swaps): {writes}")
    return(array)
        
        

def bubble_sort(array):
    writes = 0
    compare = 0
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            compare += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                writes += 1
                print(array)
    print(f"number of comparisons: {compare}")
    print(f"number of writes(swaps): {writes}")
    return array


def start():
    print("Choose a sorting algorithm:")
    print("1. Comb Sort")
    print("2. Bubble Sort")
    print("3. Selection Sort")
    print("4. Cycle Sort")
    choice = int(input("Enter your choice (1/2/3/4): "))
    

    if choice == 1:
    
        question = input("Do you want to add your own numbers or random number? (own/random)")
        if question == 'own':
            numbers = input("Enter a list of numbers separated by spaces: ")
            array = [int(num) for num in numbers.split()]
        elif question == 'random':
            length = int(input("how long would you like the array?: "))
            array = random.sample(range(1,100),length)
            print(array)
        else:
            print("invalid input")
        sorted_array = comb_sort(array)
    elif choice == 2:
        
        question = input("Do you want to add your own numbers or random number? (own/random)")
        if question == 'own':
            numbers = input("Enter a list of numbers separated by spaces: ")
            array = [int(num) for num in numbers.split()]
        elif question == 'random':
            length = int(input("how long would you like the array?: "))
            array = random.sample(range(1,100),length)
            print(array)
        else:
            print("invalid input")
        sorted_array = bubble_sort(array)
    elif choice == 3:
        sorted_array = create_list()
    elif choice == 4:
        
        question = input("Do you want to add your own numbers or random number? (own/random)")
        if question == 'own':
            numbers = input("Enter a list of numbers separated by spaces: ")
            array = [int(num) for num in numbers.split()]
            
        elif question == 'random':
            length = int(input("how long would you like the array?: "))
            array = random.sample(range(1,100),length)
            print(array)
        else:
            print("invalid input")
        sorted_array = cycle_sort(array)
    else:
        print("Invalid choice.")
        return

start()