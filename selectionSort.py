class Solution(object):
    def selection_sort(arr):
        n = len(arr)
        for i in range(n-1):
            #assume the current position holds the minimun element
            min_idx = i
            #iterate through the unsorted portion
            for j in range(i+1,n):
                if arr[j] < arr[min_idx]:
                    min_idx=j

            arr[i],arr[min_idx] = arr[min_idx],arr[i]

    def print_array(arr):
        for val in arr:
            print(val,end= " ")
        print()

arr = [64, 25, 12, 22, 11]
    
print("Original array: ", end="")
Solution.print_array(arr)
     
Solution.selection_sort(arr)
    
print("Sorted array: ", end="")
Solution.print_array(arr)