def find_duplicate(nums):
    if type(nums) != list or len(nums) <= 1:
        return False

    actual = nums[-1]
    if type(actual) != int or actual < 0:
        return False

    prox = nums[actual - 1]
    while actual != prox:
        if type(actual) != int or actual < 0:
            return False
        prox, nums[actual - 1], actual = (
            nums[nums[actual - 1] - 1],
            actual,
            prox,
        )

    return actual


if __name__ == "__main__":
    print(find_duplicate([1, 3, 4, 2, 2]), "2")
    print(find_duplicate([3, 1, 3, 4, 2]), "3")
    print(find_duplicate([1, 1]), "1")
    print(find_duplicate([1, 1, 2]), "1")
    print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]), "7")
