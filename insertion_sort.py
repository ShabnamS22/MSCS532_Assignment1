def insertion_sort_desc(arr):
    """
    Sorts an array in monotonically decreasng order using the insertion sort algorithm
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

            arr[j + 1] = key

    if __name__ == "__main__":
        data = [31, 41, 59, 26, 41, 58]
        print("Original array:", data)

        insertion_sort_desc(data)

        print("Sorted array (descending):", data)