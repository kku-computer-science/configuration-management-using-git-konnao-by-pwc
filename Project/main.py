from quick_sort import quickSort
from bubble_sort import bubble_sort   # import ฟังก์ชันจากอีกไฟล์


if __name__ == "__main__":
    while True:
        print("=== Sorting Program (Buble & Quick) ===")
        
        print("\nPlease Choose:")
        print("1. Quick: Sort enter 1")
        print("2. Bubble: Sort enter 2")
        print("3. Exit: enter 3")

        choice = input("1/2/3: ")
        if choice == "3":
            print("Thank You!")
            break

        nums_str = input("ป้อนตัวเลขคั่นด้วย space: ")

        try:
            arr = list(map(int, nums_str.split()))
        except ValueError:
            print("กรุณาป้อนเฉพาะตัวเลขเท่านั้น!\n")
            continue
        
        if choice == "1":
            quickSort(arr, 0, len(arr) - 1)
            print("\nผลลัพธ์ (Quick Sort):", arr)
        elif choice == "2":
            result = bubble_sort(arr)
            print("\nผลลัพธ์ (Bubble Sort):", result)
        else:
            print("\nตัวเลือกไม่ถูกต้อง!")
            continue