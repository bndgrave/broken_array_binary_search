def is_sorted(nums):
    if len(nums) > 1:
        return nums[0] < nums[-1]
    return True

# def find_head(nums):
#     if len(nums) == 2:
#         if nums[0] > nums[1]:
#             return 1
#         else:
#             return 0
#     mid = len(nums) // 2
#     if nums[mid-1] < nums[mid] < nums[mid+1]:
#         if is_sorted(nums[0:mid]):
#             return find_head(nums[mid:len(nums)]) + mid
#         else:
#             return find_head(nums[0:mid]) 
#     if nums[mid-1] > nums[mid]:
#         return mid
#     if nums[mid] > nums[mid+1]:
#         return mid + 1

def broken_search(nums, target) -> int:
    if len(nums) == 1 and nums[0] != target or len(nums) == 0:
        return -1
    # head = find_head(nums) if not is_sorted(nums) else 0
    # mid = head if head else len(nums) // 2
    mid = len(nums) // 2 if len(nums) >=2 else 0
    if nums[mid] == target:
        return mid
    left, right = nums[0:mid], nums[mid+1:len(nums)]
    flag = None
    if is_sorted(left):
        if left[0] <= target <= left[-1]:
            search_result = broken_search(left, target)
        else:
            flag = 1
            search_result = broken_search(right, target)
    else:
        if right[0] <= target <= right[-1]:
            search_result = broken_search(right, target)
            flag = 1
        else:
            search_result = broken_search(left, target)
    # search_result = (
    #     broken_search(nums[0:mid], target) if nums[0] <= target <= nums[mid-1]
    #     else broken_search(nums[mid+1:len(nums)], target)
    # )   
    if search_result >= 0:
        if flag:
            return search_result + mid + 1
        else:
            return search_result
    else:
        return -1

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12, 15]
    # assert broken_search(arr, 5) == 6
    print(broken_search(arr, 1))


if __name__ == '__main__':
    test()