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
    head = find_head(array) if not is_sorted(array) else None
    if head:
        array = nums[0:head] if nums[0] < target < nums[head] else nums[head:len(nums)]
        
    if array[-1] < target:
        return -1    
    while len(array) > 1:
        mid = len(array) // 2 if len(nums) >= 2 else 0
        if array[mid] == target:
            index = index + mid
            break
        if array[mid] < target:
            array = array[mid+1:len(array)]
            index = index + mid
        else:
            array = array[0:mid]
    if len(array) == 1 and array[0] != target:
        return -1
    if index >= len(nums)-1:
        return len(nums) - index - 1
    else:
        return index


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12, 15]
    # assert broken_search(arr, 5) == 6
    print(broken_search(arr, 21))


if __name__ == '__main__':
    test()