# Sorting Visualizer

# Importing the libraries
from tkinter import Tk
from tkinter import Canvas
from tkinter import Button
from tkinter import Label
from random import choice
from tkinter import StringVar

#-------------------------------------------------Programming Logic-------------------------------------------------

# creating a list to make consistent bars have same difference in heights
barLengthList = [2 * height for height in range(1, 175)]

worker = None

# function to visualize bar swap
def swap(bar1, bar2):
    # fetching the x1, x2, y1, y2 coordinates
    bar1_coords = canvas.coords(bar1)
    bar2_coords = canvas.coords(bar2)
    # moving bars
    canvas.move(bar1, (bar2_coords[0] - bar1_coords[0]), 0)
    canvas.move(bar2, (bar1_coords[2] - bar2_coords[2]), 0)

# function to generate bar
def generateShuffledList():
    labelText.set('Select any Sorting')
    global barLengthList
    barHeights = list(barLengthList)                                                # copying values of one list to another
    global lengthList
    global barList
    canvas.delete('all')                                                            # clearing the canvas completely
    barstart = 2                                                                    # setting the x1 point of first bar
    barend = 6                                                                      # setting the x2 point of first bar
    barList = []                                                                    # creating an empty list to store bar data
    lengthList = []                                                                 # creating an empty list to store the length of bars

    # creating rectangular bars (70)
    for bar in range(1, 175):
        randomY = choice(barHeights)
        barHeights.remove(randomY)
        bar = canvas.create_rectangle(barstart, randomY, barend, 400, fill = '#2bae66')   # creating rectangular bar
        centerBar(bar)
        barList.append(bar)
        barstart += 4
        barend += 4

    # adding the length of bars to list
    for bar in barList:
        bar = canvas.coords(bar)                                                    # fetching coordinates of bar
        length = bar[3] - bar[1]
        lengthList.append(length)

# function to align bar center vertically
def centerBar(bar):
    barData = canvas.coords(bar)
    barHeight = barData[3] - barData[1]
    # canvas.winfo_reqheight() returns size of canvas
    canvas.move(bar, 0, -(int(canvas.winfo_reqheight() / 2) - int(barHeight / 2) - 13))

#==========================================================BubbleSort==========================================================

# function to call bubble_sort
def bubbleSort():
    labelText.set('Bubble Sort')
    global worker
    global speed
    global lengthList
    if lengthList == sorted(lengthList):                                    # checking whether the list is sorted or not
        return
    worker = bubbleSortVisualize()                                          # calling bubbleSortVisualize() function
    speed = 1
    animate()                                                               # calling animate() function
    print('Bubble Sort Complete')

# function for bubble_sort visualizing
def bubbleSortVisualize():
    global sorting_comparison
    global lengthList
    global barList
    for index1 in range(len(lengthList) - 1):
        for index2 in range(len(lengthList) - index1 - 1):
            if lengthList[index2] > lengthList[index2 + 1]:
                lengthList[index2], lengthList[index2 + 1] = lengthList[index2 + 1], lengthList[index2]    # swapping length in lengthList
                barList[index2], barList[index2 + 1] = barList[index2 + 1], barList[index2]                # swapping length in barList
                canvas.itemconfig(barList[index2 + 1], fill = 'blue')                   # changing color of moving bar
                swap(barList[index2 + 1], barList[index2])                              # calling swap function to swap bar
                yield         # yield will suspend the function and sends a value to caller and will resume again from where it suspended
                canvas.itemconfig(barList[index2 + 1], fill = '#2bae66')                # setting color of moving bar back to normal

#==========================================================BubbleSort==========================================================

#==========================================================InsertionSort==========================================================

# function to call insertion_sort
def insertionSort():
    labelText.set('Insertion Sort')
    global worker
    global speed
    global lengthList
    if lengthList == sorted(lengthList):                                    # checking whether the list is sorted or not
        return
    worker = insertionSortVisualize()                                       # calling insertionSortVisualize() function
    speed = 1
    animate()                                                               # calling animate() function
    print('Insertion Sort Complete')

# function for insertion_sort visualizing
def insertionSortVisualize():
    global lengthList
    global barList
    for index in range(len(lengthList)):
        key = index
        while key > 0 and lengthList[key - 1] > lengthList[key]:
            lengthList[key], lengthList[key - 1] = lengthList[key - 1], lengthList[key]             # swapping length in lengthList
            barList[key], barList[key - 1] = barList[key - 1], barList[key]                         # swapping length in barList
            canvas.itemconfig(barList[key], fill = 'blue')                                          # changing color of moving bar
            swap(barList[key], barList[key - 1])                                                    # calling swap function to swap bar
            key -= 1
            yield                                                                   # yield to suspend the function execution
            canvas.itemconfig(barList[key + 1], fill = '#2bae66')                   # setting color of moving bar back to normal

#==========================================================InsertionSort==========================================================

#==========================================================SelectionSort==========================================================

# function to call selection_sort
def selectionSort():
    labelText.set('Selection Sort')
    global worker
    global speed
    global lengthList
    if lengthList == sorted(lengthList):                                    # checking whether the list is sorted or not
        return
    worker = selectionSortVisualize()                                       # calling selectionSortVisualize() function
    speed = 25
    animate()                                                               # calling animate() function
    print('Selection Sort Complete')

# function for selection_sort visualizing
def selectionSortVisualize():
    global lengthList
    global barList
    for index1 in range(len(lengthList)):
        min = index1
        for index2 in range(index1 + 1, len(lengthList)):
            if lengthList[index2] < lengthList[min]:
                min = index2
        lengthList[min], lengthList[index1] = lengthList[index1], lengthList[min]                   # swapping length in lengthList
        barList[min], barList[index1] = barList[index1], barList[min]                               # swapping length in barList
        canvas.itemconfig(barList[min], fill = 'red')                                               # changing color of comparison bar
        canvas.itemconfig(barList[index1], fill = 'blue')                                           # changing color of moving bar
        swap(barList[min], barList[index1])                                     # calling swap function to swap bar
        yield                                                                   # yield to suspend the function execution
        canvas.itemconfig(barList[min], fill = '#2bae66')                       # setting color back to normal
        canvas.itemconfig(barList[index1], fill='#2bae66')

#==========================================================SelectionSort==========================================================

#==========================================================QuickSort==========================================================

# function to call quick_sort
def quickSort():
    labelText.set('Quick Sort')
    global worker
    global speed
    global lengthList
    if lengthList == sorted(lengthList):                                    # checking whether the list is sorted or not
        return
    worker = quickSortVisualize(lengthList, 0, len(lengthList) - 1)         # calling quickSortVisualize() function
    speed = 20
    animate()                                                               # calling animate() function
    print('Quick Sort Complete')

# function for quick_sort visualizing
def quickSortVisualize(arr, low, high):
    if low >= high:
        return
    else:
        # code for partition function starts after here but is written in same function
        global barList
        pivotIndex = low
        pivotValue = arr[high]                                              # setting last value as pivot
        for index in range(low, high + 1):
            if arr[index] < pivotValue:
                arr[index], arr[pivotIndex] = arr[pivotIndex], arr[index]                   # swapping length from lengthList
                barList[index], barList[pivotIndex] = barList[pivotIndex], barList[index]   # swapping length from barList
                canvas.itemconfig(barList[index], fill='blue')                              # changing color of moving bar
                canvas.itemconfig(barList[pivotIndex], fill='red')                          # changing color of pivot
                swap(barList[index], barList[pivotIndex])                               # calling swap function to move bar
                yield                           # yield to suspend function
                canvas.itemconfig(barList[index], fill='#2bae66')                       # setting colors back to normal
                canvas.itemconfig(barList[pivotIndex], fill='#2bae66')
                pivotIndex += 1
        pi = pivotIndex
        arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]                         # swapping length from lengthList
        barList[pivotIndex], barList[index] = barList[index], barList[pivotIndex]       # swapping length from barList
        canvas.itemconfig(barList[index], fill='blue')                                  # changing color of moving bar
        canvas.itemconfig(barList[pivotIndex], fill='red')                              # changing color of pivot
        swap(barList[pivotIndex], barList[index])                                       # calling swap function to move bar
        yield                                                               # yield to suspend function
        canvas.itemconfig(barList[index], fill='#2bae66')                   # setting colors back to normal
        canvas.itemconfig(barList[pivotIndex], fill='#2bae66')
        yield from quickSortVisualize(arr, low, pi - 1)                         # recursion on left part of list
        yield from quickSortVisualize(arr, pi + 1, high)                        # recursion on right part of list

#==========================================================QuickSort==========================================================

#==========================================================MergeSort==========================================================

# TODO: Updations to visualize the bars movement or sorting visualization

# function to call merge_sort
def mergeSort():
    labelText.set('Merge Sort')
    global worker
    global speed
    global lengthList
    if lengthList == sorted(lengthList):                                            # checking whether the list is sorted or not
        return
    worker = mergeSortVisualize(lengthList, 0, len(lengthList) - 1)                 # calling mergeSortVisualize() function
    speed = 5
    animate()                                                                       # calling animate() function
    print('Merge Sort Complete')

# function for merge_sort visualizing
def mergeSortVisualize(arr, low, high):
    global barList
    global barLengthList
    if (low < high):
        mid = low + (high - low) // 2
        mergeSortVisualize(arr, low, mid)
        mergeSortVisualize(arr, mid + 1, high)
        # code for merge function starts after here but is written in same function
        right_index = mid + 1
        if (arr[mid] <= arr[right_index]):
            return
        while (low <= mid and right_index <= high):
            if (arr[low] <= arr[right_index]):
                low += 1
            else:
                value = arr[right_index]
                barValue = barList[right_index]
                index = right_index
                counter = 0
                while (index != low):
                    arr[index] = arr[index - 1]
                    barList[index] = barList[index - 1]
                    canvas.move(barList[index - 1], 4, 0)
                    counter += 1
                    index -= 1
                arr[low] = value
                barList[low] = barValue
                canvas.move(barValue, -(4*counter), 0)
                low += 1
                mid += 1
                right_index += 1

#==========================================================MergeSort==========================================================

#==========================================================HeapSort==========================================================

# function to call heap_sort
def heapSort():
    labelText.set('Heap Sort')
    global worker
    global speed
    global lengthList
    if lengthList == sorted(lengthList):                                        # checking whether the list is sorted or not
        return
    worker = heapSortVisualize(lengthList, len(lengthList))                     # calling heapSortVisualize() function
    speed = 1
    animate()                                                                   # calling animate() function
    print('Heap Sort Complete')

# function for heap_sort visualizing
def heapSortVisualize(arr, length):
    global barList
    for index in range(length):

        # if child is bigger than parent
        if arr[index] > arr[int((index - 1) / 2)]:
            index2 = index

            # swap child and parent until
            # parent is smaller
            while arr[index2] > arr[int((index2 - 1) / 2)]:
                arr[index2], arr[int((index2 - 1) / 2)] = arr[int((index2 - 1) / 2)], arr[index2]           # swapping lengths
                barList[index2], barList[int((index2 - 1) / 2)] = barList[int((index2 - 1) / 2)], barList[index2]
                swap(barList[index2], barList[int((index2 - 1) / 2)])           # calling swap function to swap bars
                canvas.itemconfig(barList[index2], fill = 'red')                # changing color
                canvas.itemconfig(barList[index2 - 1], fill = 'blue')
                yield                                                       # yield to suspend the function execution
                canvas.itemconfig(barList[index2], fill = '#2bae66')            # setting colors back to normal
                canvas.itemconfig(barList[index2 - 1], fill = '#2bae66')
                index2 = int((index2 - 1) / 2)

    for index in range(length - 1, 0, -1):
        # swap value of first indexed
        # with last indexed
        arr[0], arr[index] = arr[index], arr[0]
        barList[0], barList[index] = barList[index], barList[0]
        swap(barList[0], barList[index])
        canvas.itemconfig(barList[0], fill='red')
        canvas.itemconfig(barList[index], fill='blue')
        yield
        canvas.itemconfig(barList[0], fill='#2bae66')
        canvas.itemconfig(barList[index], fill='#2bae66')

        # maintaining heap property
        # after each swapping
        index2, temp_index = 0, 0

        while True:
            temp_index = 2 * index2 + 1

            # if left child is smaller than
            # right child point index variable
            # to right child
            if (temp_index < (index - 1) and
                    arr[temp_index] < arr[temp_index + 1]):
                temp_index += 1

            # if parent is smaller than child
            # then swapping parent with child
            # having higher value
            if temp_index < index and arr[index2] < arr[temp_index]:
                arr[index2], arr[temp_index] = arr[temp_index], arr[index2]
                barList[index2], barList[temp_index] = barList[temp_index], barList[index2]
                swap(barList[index2], barList[temp_index])
                canvas.itemconfig(barList[index2], fill='red')
                canvas.itemconfig(barList[temp_index], fill='yellow')
                canvas.itemconfig(barList[index], fill='blue')
                yield
                canvas.itemconfig(barList[index2], fill='#2bae66')
                canvas.itemconfig(barList[temp_index], fill='#2bae66')
                canvas.itemconfig(barList[index], fill='#2bae66')

            index2 = temp_index
            if temp_index >= index:
                break

#==========================================================HeapSort==========================================================

#==========================================================radixSort==========================================================

# TODO: Write the Radix Sort after solving Merge Sort since it follows the similar approach as Merge Sort
# function to call cocktail_sort
def radixSort():
    labelText.set('Radix Sort')
    global worker
    global speed
    global lengthList
    if lengthList == sorted(lengthList):                            # checking whehter list is sorted or not
        return
    worker = radixSortVisualize(lengthList)                         # calling radixSortVisualize() function
    speed = 1
    animate()                                                       # calling animate() function
    print('Radix Sort Complete')

# function for cocktail_sort visualizing
def radixSortVisualize(arr):
    pass

#==========================================================RadixSort==========================================================

#==========================================================CocktailSort==========================================================

# function to call cocktail_sort
def cocktailSort():
    labelText.set('Cocktail Sort')
    global worker
    global speed
    global lengthList
    if lengthList == sorted(lengthList):                            # checking whehter list is sorted or not
        return
    worker = cocktailSortVisualize(lengthList)                      # calling cocktailSortVisualize() function
    speed = 1
    animate()                                                       # calling animate() function
    print('Cocktail Sort Complete')

# function for cocktail_sort visualizing
def cocktailSortVisualize(arr):
    global barList
    length = len(arr)
    swapped = True
    low = 0
    high = length - 1
    while (swapped == True):

        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False

        # loop from left to right same as the bubble
        # sort
        for index in range(low, high):
            if (arr[index] > arr[index + 1]):
                arr[index], arr[index + 1] = arr[index + 1], arr[index]                 # swapping lengths
                barList[index], barList[index + 1] = barList[index + 1], barList[index]
                swap(barList[index], barList[index + 1])                                # swapping bars
                canvas.itemconfig(barList[index], fill='blue')                          # changing color
                yield                       # yield to suspend the execution of function
                canvas.itemconfig(barList[index], fill='#2bae66')                       # restoring normal colors
                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        high = high - 1

        # from right to left, doing the same
        # comparison as in the previous stage
        for index in range(high - 1, low - 1, -1):
            if (arr[index] > arr[index + 1]):
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                barList[index], barList[index + 1] = barList[index + 1], barList[index]
                swap(barList[index], barList[index + 1])
                canvas.itemconfig(barList[index + 1], fill='blue')
                yield
                canvas.itemconfig(barList[index + 1], fill='#2bae66')
                swapped = True

        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        low = low + 1

#==========================================================CocktailSort==========================================================

#==========================================================GnomeSort==========================================================

# function to call gnome_sort
def gnomeSort():
    labelText.set('Gnome Sort')
    global worker
    global speed
    global lengthList
    if lengthList == sorted(lengthList):                                    # checking whehter list is sorted or not
        return
    worker = gnomeSortVisualize(lengthList)                                 # calling gnomeSortVisualize() function
    speed = 1
    animate()                                                               # calling animate() function
    print('Gnome Sort Complete')

# function for gnome_sort visualizing
def gnomeSortVisualize(arr):
    global barList
    length = len(arr)
    index = 0
    while index < length:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]                 # swapping length
            barList[index], barList[index - 1] = barList[index - 1], barList[index]
            canvas.itemconfig(barList[index], fill = 'blue')                    # changing color
            swap(barList[index], barList[index - 1])                        # swapping bar
            yield                                               # yield to suspend
            canvas.itemconfig(barList[index], fill='#2bae66')               # restoring color
            index = index - 1

#==========================================================GnomeSort==========================================================

#==========================================================Animation==========================================================

# function to animate
def animate():
    global speed
    global worker
    if worker is not None:
        try:
            next(worker)                                    # calling the next iterator
            canvas.after(speed, animate)                    # visualize the movement of bar with time delay
        except StopIteration:
            worker = None
        finally:
            canvas.after_cancel(animate)                    # cancels the callback

#-------------------------------------------------Programming Logic-------------------------------------------------


#-------------------------------------------------GUI Logic-------------------------------------------------

# Setting up the GUI Window
# Opening the GUI Window
root = Tk()
root.geometry('700x550')                                                        # setting the default size of GUI Window
root.minsize(700, 550)                                                          # setting the min size of GUI Window
root.maxsize(700, 550)                                                          # setting the max size of GUI Window
root.title('Sorting Visualizer by Yashasvi Bhatt')                              # Giving the title to GUI Window
root.wm_iconbitmap('images/sorting_icon.ico')                                   # Giving the icon to GUI Window

# creating a canvas inside the GUI Window
canvas = Canvas(width = 700, height = 410, bg = '#fcf6f5')
canvas.grid(row = 0, column = 0, columnspan = 7)

# creating the driver buttons
generate_shuffled_list = Button(text = 'Shuffle', font = 'lucida 10 bold', command = generateShuffledList, width = 13)
bubble_sort_button = Button(text = 'Bubble Sort', font = 'lucida 10 bold', command = bubbleSort, width = 13)
insertion_sort_button = Button(text = 'Insertion Sort', font = 'lucida 10 bold', command = insertionSort, width = 13)
selection_sort_button = Button(text = 'Selection Sort', font = 'lucida 10 bold', command = selectionSort, width = 13)
quick_sort_button = Button(text = 'Quick Sort', font = 'lucida 10 bold', command = quickSort, width = 13)
cocktail_sort_button = Button(text = 'Cocktail Sort', font = 'lucida 10 bold', command = cocktailSort, width = 13)
heap_sort_button = Button(text = 'Heap Sort', font = 'lucida 10 bold', command = heapSort, width = 13)
gnome_sort_button = Button(text = 'Gnome Sort', font = 'lucida 10 bold', command = gnomeSort, width = 13)
merge_sort_button = Button(text = 'Merge Sort', font = 'lucida 10 bold', command = mergeSort, width = 13)
radix_sort_button = Button(text = 'Radix Sort', font = 'lucida 10 bold', command = radixSort, width = 13)

generate_shuffled_list.grid(row = 2, column = 0)
bubble_sort_button.grid(row = 2, column = 1)
insertion_sort_button.grid(row = 3, column = 0)
selection_sort_button.grid(row = 3, column = 1)
quick_sort_button.grid(row = 4, column = 0)
cocktail_sort_button.grid(row = 4, column = 1)
heap_sort_button.grid(row = 5, column = 0)
gnome_sort_button.grid(row = 5, column = 1)
merge_sort_button.grid(row = 6, column = 0)
radix_sort_button.grid(row = 6, column = 1)


Label(text = '').grid(row = 1, column = 0)

labelText = StringVar()
labelText.set('Select any Sorting')
informer_label = Label(textvariable = labelText, font = 'lucida 15 bold', relief = 'sunken', width = 15)
informer_label.grid(row = 2, column = 4)

generateShuffledList()


# holding the window open
root.mainloop()

print('Thank You')

#-------------------------------------------------GUI Logic-------------------------------------------------