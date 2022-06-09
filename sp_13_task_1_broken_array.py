def broken_search(nums, target) -> int:
    print(nums)
    if not nums:
        return -1
    left = 0
    mid = len(nums) // 2
    print(mid)
    right = len(nums)
    if nums[mid] == target:
        return mid
    if nums[left] < nums[mid] < target:
        return broken_search(nums[mid+1:right],target)
    elif nums[left] > nums[mid] > target:       
        return broken_search(nums[mid+1:right],target)
    elif nums[left] < nums[mid] > target:
        return broken_search(nums[left:mid],target)
    elif nums[left] > nums[mid] < target:
        return broken_search(nums[mid+1:right],target)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    # assert broken_search(arr, 5) == 6
    index = broken_search(arr, 5)
    print(index)

if __name__ == '__main__':
    test()