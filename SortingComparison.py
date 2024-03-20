import time

class SortingAlgorithm:
    def __init__(self, name):
        self.name = name

    def sort(self, data):
        raise NotImplementedError("Subclasses must implement the sort method")

class BubbleSort(SortingAlgorithm):
    def sort(self, data):
        n = len(data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

class MergeSort(SortingAlgorithm):
    def merge(self, left, right):
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        return result + left + right

    def sort(self, data):
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])

        return self.merge(left, right)

def run_comparison(algorithm, data):
    start_time = time.time()
    algorithm.sort(data.copy())  # Avoid modifying original data
    end_time = time.time()

    print(f"{algorithm.name} took {end_time - start_time:.4f} seconds")

# Complex scenario: nested lists with mixed data types
data = [
    [4, "hello", 2.5],
    [3, "world", 1.2],
    [1, "python", 3.14],
]

bubble_sort = BubbleSort("Bubble Sort")
merge_sort = MergeSort("Merge Sort")

print("Original Data:")
print(data)

print("\nSorting with Bubble Sort:")
run_comparison(bubble_sort, data)

print("\nSorting with Merge Sort:")
run_comparison(merge_sort, data)
