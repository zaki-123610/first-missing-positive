def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target = nums[i] - 1
            nums[i], nums[target] = nums[target], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    examples = [
        ([0, -2, 1, 2], 3),
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([1, 2, 3], 4),
        ([1, 1], 2),
        ([2, 2, 2], 1),
        ([], 1),
        ([-5, -1], 1),
        ([2], 1),
        ([1], 2),
    ]

    for nums, expected in examples:
        result = first_missing_positive(nums.copy())
        assert result == expected, f"{nums}: expected {expected}, got {result}"
        print(f"{nums} -> {result}")

    print("All tests passed.")
