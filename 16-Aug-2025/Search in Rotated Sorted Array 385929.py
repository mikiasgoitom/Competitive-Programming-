# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, arr: List[int], target: int) -> int:
        '''while low <= high:
            mid = (low + high) // 2
            print("as",low, mid, high)
            if target == arr[mid]:
                return mid

            if arr[low] > arr[high]:
                if arr[low] > arr[mid]:
                    if target < arr[mid]:
                        print("asdfa1")
                        low = mid + 1
                    elif target > arr[mid]:
                        print("asdfa2")
                        high = mid - 1
                elif arr[low] < arr[mid]:
                    if target < arr[mid]:
                        print("asdfa3")
                        high = mid - 1
                    elif target > arr[mid]:
                        print("asdfa4")
                        low = mid + 1
                elif arr[mid] == arr[low]:
                    print("asdfa5")
                    low = mid + 1
                else:
                    print("asdfa6")
                    high = mid - 1
            else:
                if arr[mid] > target:
                    print("asdfa7")
                    high = mid - 1
                else:
                    print("asdfa8")
                    low = mid + 1
            print("sa",low, mid, high)
        '''
        bdr = 0
        if arr[0] > arr[-1]:
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if mid + 1 < len(arr) and mid - 1 > -1:
                    if arr[mid - 1] > arr[mid] < arr[mid + 1]:
                        bdr = mid
                    elif arr[mid - 1] > arr[mid + 1]:
                        bdr = mid + 1
                if arr[mid] < arr[0]:
                    high = mid -1
                else:
                    low = mid + 1
                # print(mid)
            if bdr == 0:
                bdr = 1
        
        # print("jk",bdr)
        if bdr > 0:
            if arr[0] <= target <= arr[bdr - 1]:
                low, high = 0, bdr - 1
                while low <= high:
                    mid = (low + high) // 2
                    if target == arr[mid]:
                        return mid
                    if target < arr[mid]:
                        high = mid -1
                    else:
                        low = mid + 1
            elif arr[bdr] <= target <= arr[-1]:
                low, high = bdr, len(arr) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if target == arr[mid]:
                        return mid
                    if target < arr[mid]:
                        high = mid -1
                    else:
                        low = mid + 1
        else:
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if target == arr[mid]:
                    return mid
                if target < arr[mid]:
                    high = mid -1
                else:
                    low = mid + 1
        return -1