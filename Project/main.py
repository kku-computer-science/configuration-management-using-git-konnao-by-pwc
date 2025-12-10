from bubble_sort import bubble_sort   # import ฟังก์ชันจากอีกไฟล์

# partition function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

if __name__ == "__main__":
    print("=== Sorting Program (Buble & Quick) ===")
    arr = list(map(int, input("Please enter the number and คั่นด้วย spacebar: ").split()))
    
    print("\nPlease Choose:")
    print("1. Quick Sort enter 1")
    print("2. Bubble Sort enter 2")

    choice = input("1/2: ")
    
    if choice == "1":
        quickSort(arr, 0, len(arr) - 1)
        print("\nผลลัพธ์ (Quick Sort):", arr)
    elif choice == "2":
        result = bubble_sort(arr)
        print("\nผลลัพธ์ (Bubble Sort):", result)
    else:
        print("\nตัวเลือกไม่ถูกต้อง!")

