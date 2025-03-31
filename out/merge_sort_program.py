# Merge Sort in Python

## Introduction

Merge sort is a divide-and-conquer algorithm that divides an array into halves, sorts each half, and then merges them back together. This example demonstrates how to implement merge sort in Python.

## Code Implementation
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Two iterators for traversing the two halves
        i = j = k = 0

        # Copy data to temp arrays left_half and right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
```

## Example Usage

```python
if __name__ == '__main__':
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print('Given array:', test_array)
    merge_sort(test_array)
    print('Sorted array:', test_array)
```

## Output

```plaintext
Given array: [64, 34, 25, 12, 22, 11, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]
```

## Conclusion

This implementation of merge sort demonstrates how to effectively use recursion and merging to sort an array. The code is straightforward and can be adapted for various sorting needs.