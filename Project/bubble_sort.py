def bubble_sort(arr):
    """Basic Bubble Sort: return sorted list in ascending order."""
    data = arr.copy()
    n = len(data)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


if __name__ == "__main__":
    sample = [5, 1, 4, 2, 8]
    print("Input :", sample)
    print("Output:", bubble_sort(sample))
