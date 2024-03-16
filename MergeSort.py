def merge_sort(data):
    """Sorts a list of data in ascending order using the merge sort algorithm.

    Args:
        data: The list of data to be sorted.

    Returns:
        A new list containing the sorted data.

    Raises:
        TypeError: If the data contains elements that are not comparable.
    """

    if len(data) <= 1:
        return data  # Base case: Already sorted (single element or empty list)

    mid = len(data) // 2
    left_half = merge_sort(data[:mid])  # Recursively sort the left half
    right_half = merge_sort(data[mid:])  # Recursively sort the right half

    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    """Merges two sorted lists into a single sorted list.

    Args:
        left: The first sorted list.
        right: The second sorted list.

    Returns:
        A new list containing the elements of both lists in sorted order.

    Raises:
        TypeError: If the elements in the lists are not comparable.
    """

    i, j, result = 0, 0, []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements from whichever list has them
    result.extend(left[i:])
    result.extend(right[j:])

    return result

if __name__ == "__main__":
    data = [8, 3, 1, 4, 2, 7, 6, 5]
    sorted_data = merge_sort(data)
    print(sorted_data)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
