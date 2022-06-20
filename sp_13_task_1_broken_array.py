# Номер посылки - 69067766

def broken_search(nums, target) -> int:
    start = 0
    end = len(nums) - 1
    index = -1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            index = mid
            break
        if nums[start] <= nums[mid]:
            if nums[start] <= target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] <= target <= nums[end]:
                start = mid + 1
            else:
                end = mid -1
    return index
