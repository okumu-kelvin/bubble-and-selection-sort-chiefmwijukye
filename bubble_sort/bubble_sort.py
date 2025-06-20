def bubble_sort(unsorted_list):  
   
    n = len(unsorted_list)  # Get the number of elements in the list
    
    for i in range(n):  # Loop through the list n times
        
        swapped = False  # Track if any swapping happened in this pass
        
        for j in range(0, n - i - 1):  # Go from start to (n - i - 1) to avoid sorted elements at the end
            
            if unsorted_list[j] > unsorted_list[j + 1]:  # If current item is bigger than next one,.....
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]  # Swap them
                
                swapped = True  # Mark that we did a swap
        
        if not swapped:  # If no swaps happened, the list is already sorted
           
            break  # Exit the loop early for efficiency
   
    return unsorted_list  
