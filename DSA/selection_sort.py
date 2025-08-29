'''
The algorithm divides the list into two parts:
• A sorted portion (initially empty, grows from left to right)
• An unsorted portion (initially the entire list, shrinks from left to right)

## How It Works

1. Find the minimum: Look through the entire unsorted portion to find the smallest element
2. Swap: Exchange this smallest element with the first element of the unsorted portion
3. Expand sorted region: The sorted portion now includes one more element
4. Repeat: Continue this process with the remaining unsorted elements
'''


def selection_sort(arr: list) -> list:
    start_pos = 0
    while start_pos < len(arr):
        current_min = start_pos
        for i in range(start_pos, len(arr)):
            if arr[i] < arr[current_min]:
                current_min = i
        if start_pos != current_min:
            arr[start_pos], arr[current_min] = arr[current_min], arr[start_pos]
        start_pos += 1
    return arr


if __name__ == '__main__':
    arr = [10, 50, 30, 60, 20, 90, 80]
    print(f"sorted array is: {selection_sort(arr)}")
    arr = [1, 5, 3, 1, 6, 3, 7]
    print(f"sorted array is: {selection_sort(arr)}")
