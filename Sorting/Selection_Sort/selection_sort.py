# Selection sort: Starting with first element, find the smallest element in list, swap with first

def selection_sort(arr):
    unsorted_items = len(arr)

    for i in range(unsorted_items - 1): # -1 so we don't do an extra comparison

        # Record the current index as the index of the minimum value (to compare against the others)
        min_idx = i

        # Loop through unsorted items to find actual minimum
        for curr_idx in range(i + 1, unsorted_items): # +1 to avoid comparison to self
            if arr[curr_idx] < arr[min_idx]:
                min_idx = curr_idx

        # Swap elements
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()


if __name__ == "__main__":
    array = [64, 25, 12, 22, 11]

    print("Original array: ", end="")
    print_array(array)

    selection_sort(array)

    print("Sorted array: ", end="")
    print_array(array)