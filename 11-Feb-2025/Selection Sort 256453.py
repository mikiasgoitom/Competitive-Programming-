# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            
            for j in range(i+1, len(arr)):
                if arr[min_idx] >= arr[j]:
                    min_idx = j
                    
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
        return arr