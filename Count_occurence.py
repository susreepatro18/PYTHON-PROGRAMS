def count_occurrences(nums, target):
    def find_start(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def find_end(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    start = find_start(nums, target)
    end = find_end(nums, target)

    if start <= end:
        return end - start + 1
    else:
        return 0

nums = [6, 7, 7, 8, 8, 1, 4, 9, 9, 12]
target = int(input("Enter a num: "))
print(count_occurrences(nums, target))