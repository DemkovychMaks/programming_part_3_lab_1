from algo.quick_sort import Quicksort

if __name__ == '__main__':
    arr = [1, 2, 56, 45, -9, 78, 11]
    manager = Quicksort()
    manager.quicksort(arr, "asc")
    print(arr)


