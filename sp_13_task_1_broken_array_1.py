def is_sorted(nums):
    if len(nums) > 1:
        return nums[0] < nums[-1]
    return True

def find_head(nums):
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return 1
        else:
            return 0
    mid = len(nums) // 2
    if nums[mid-1] < nums[mid] < nums[mid+1]:
        if is_sorted(nums[0:mid]):
            return find_head(nums[mid:len(nums)]) + mid
        else:
            return find_head(nums[0:mid]) 
    if nums[mid-1] > nums[mid]:
        return mid
    if nums[mid] > nums[mid+1]:
        return mid + 1

def broken_search(nums, target) -> int:
    array = nums
    index = 0
    while len(array) > 1:
        mid = find_head(array) if not is_sorted(array) else len(array) // 2
        mid = mid if len(array) >=2 else 0
        if array[mid] == target:
            index = index + mid
            break
        if array[0] <= target <= array[mid-1]:
            array = array[0:mid]
        else:
            array = array[mid+1:len(array)]
            index = index + mid + 1
    if len(array) == 1 and array[0] != target:
        return -1
    return index

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12, 15]
    assert broken_search(arr, 5) == 6
    # print(broken_search(arr, 101))


# if __name__ == '__main__':
#     test()