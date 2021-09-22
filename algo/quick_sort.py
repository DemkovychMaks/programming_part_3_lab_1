from timeit import default_timer as timer
from datetime import timedelta


class Quicksort :
    def __init__(self, swap_count = 0, comparison_count = 0):
        self.swap_count = swap_count
        self.comparison_count = comparison_count

    def quicksort (self, arr, order) :
        self.sorting_start = timer()
        self.quicksort_helper(arr, 0, len(arr) - 1, order)
        self.sorting_end = timer()

        print('\nQuick Sort\n')
        print(f'executed in {timedelta(seconds=self.sorting_end - self.sorting_start)}')
        print(f'number of swaps = {self.swap_count} ')
        print(f'number of comparisons = {self.comparison_count} \n')

        return arr

    def quicksort_helper (self, arr, left, right, order) :
        if len(arr) == 1:
            return arr

        if left < right:
            self.comparison_count += 1
            pivot_position = self.partition(arr, left, right, order)

            self.quicksort_helper(arr, left, pivot_position-1, order)
            self.quicksort_helper(arr, pivot_position+1, right, order)

    def partition (self, arr, left, right, order: str) :
        pivot = arr[right]
        border = (left - 1)

        for iterator in range(left, right) :
            self.comparison_count += 1
            if order == "asc":
                if arr[iterator] <= pivot :
                    border +=1
                    self.swap(arr, border, iterator)

            elif order == "desc":
                if arr[iterator] >= pivot :
                    border +=1
                    self.swap(arr, border, iterator)

        self.swap(arr, border+1, right)
        return border+1

    def swap (self, arr, first_element, second_element) :
        self.swap_count +=1
        placeholder = arr[first_element]
        arr[first_element] = arr[second_element]
        arr[second_element] = placeholder