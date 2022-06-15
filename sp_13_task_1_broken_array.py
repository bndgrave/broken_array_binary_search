def is_sorted(nums):
    if len(nums) > 1:
        return nums[0] < nums[-1]
    return True

def broken_search(nums, target) -> int:
    if len(nums) == 1 and nums[0] != target or len(nums) == 0:
        return -1
    mid = len(nums) // 2 if len(nums) >=2 else 0
    if nums[mid] == target:
        return mid
    if is_sorted(nums[0:mid]):
        if nums[0] <= target <= nums[mid-1]:
            search_result = broken_search(nums[0:mid], target)
            return search_result if search_result >= 0 else -1
        else:
            search_result = broken_search(nums[mid+1:len(nums)], target)
            return search_result + mid + 1 if search_result >= 0 else -1
    else:
        if nums[mid+1] <= target <= nums[-1]:
            search_result = broken_search(nums[mid+1:len(nums)], target)
            return search_result + mid + 1 if search_result >= 0 else -1
        else:
            search_result = broken_search(nums[0:mid], target)
            return search_result if search_result >= 0 else -1

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12, 15]
    assert broken_search(arr, 5) == 6
    # print(broken_search(arr, 1))


# if __name__ == '__main__':
#     test()