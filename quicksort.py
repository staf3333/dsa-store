nums = [1, 4, 2, 30, 11, 5]


def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    # print("i before loop: ", i)

    for j in range(low, high):
        if arr[j] < pivot:
            # print(
            #     "i after finding elem less than pivot but before incrementing and swapping: ", i)
            i += 1

            # print("i after incrementing: ", i)
            # print("arr[i] before swap: ", arr[i],
            #       " arr[j] before swap: ", arr[j])
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quicksort(arr, low, high):
    if low < high:
        # find partition index using helper function
        pi = partition(arr, low, high)

        # recursively call quick sort on partitioned arr
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


quicksort(nums, 0, len(nums) - 1)
print(nums)
