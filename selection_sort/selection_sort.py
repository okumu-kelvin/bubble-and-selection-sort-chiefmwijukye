def selection_sort(arr):  
    size = len(arr)  # Determine how many items are in the list

    for i in range(size - 1):  # Go through the list one item at a time, except the last (it'll be in place)
        
        min_index = i  # Start by assuming the current position holds the smallest number

        # Scan the unsorted section to the right of the current position
        for j in range(i + 1, size):  
            
            if arr[j] < arr[min_index]:  # If a smaller number is found during the scan
                
                min_index = j  # Remember the position of this new smallest value

        # If a smaller value was found, move it to its correct position by swapping
        if min_index != i:  
            arr[i], arr[min_index] = arr[min_index], arr[i]  # Perform the swap between current and smallest found

    return arr  
