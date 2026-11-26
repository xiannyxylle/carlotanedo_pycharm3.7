# Assessment 3.7: Sorting Algorithms
# Student: CARLO TAÑEDO
# Sorting Method: Selection Sort

def prepare_name_array(full_name):
    unsorted_arr = []
    # Only allow standard uppercase English letters (excludes spaces and symbols like 'Ñ')
    allowed_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in full_name.upper():
        if char in allowed_letters and char not in unsorted_arr:
            unsorted_arr.append(char)

    return unsorted_arr


def selection_sort(arr):
    # Create a copy so the original unsorted array remains intact
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    print("--- Selection Sort Process ---")
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j

        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
        print(f"Pass {i + 1}: {sorted_arr}")

    return sorted_arr


def main():
    full_name = "CARLO TAÑEDO"

    # Create the two required arrays: unsorted and sorted
    unsorted_array = prepare_name_array(full_name)
    sorted_array = selection_sort(unsorted_array)

    print("\n--- Final Result ---")
    print(f"Full Name:      {full_name}")
    print(f"Unsorted Array: {unsorted_array}")
    print(f"Sorted Array:   {sorted_array}")


if __name__ == "__main__":
    main()