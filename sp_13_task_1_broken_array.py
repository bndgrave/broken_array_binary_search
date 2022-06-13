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
    left, right = nums[0:mid], nums[mid:len(nums)]
    if nums[mid-1] < nums[mid] < nums[mid+1]:
        if is_sorted(left):
            return find_head(right) + mid
        else:
            return find_head(left) 
    if nums[mid-1] > nums[mid]:
        return mid
    if nums[mid] > nums[mid+1]:
        return mid + 1


def broken_search(nums, target) -> int:
    print(nums)
    if len(nums) == 1 and nums[0] != target:
        return -1
    if not is_sorted(nums):
        head = find_head(nums)
        return (
            broken_search(nums[0:head], target) 
            if nums[0] <= target <= nums[head-1]
            else broken_search(nums[head:len(nums)], target) + head
        )   
    mid = len(nums) // 2 if len(nums) >= 2 else 0
    if nums[mid] == target:
        return mid
    if nums[-1] < target:
        return -1
    return (
        broken_search(nums[0:mid], target) if nums[mid] > target
        else broken_search(nums[mid+1:len(nums)], target) + mid + 1
    )

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12, 15]
    # arr = [2, 3, 4, 5, 6, 7, 8, 1, 2]
    arr1 = broken_search(arr, 6)
    # arr = [1, 2]
    # assert broken_search(arr, 5) == 6
    # index = broken_search(arr, 101)
    print(arr1)

if __name__ == '__main__':
    test()