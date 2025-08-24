from collections import Counter

def sort_by_frequency(input_list):
    # Use Counter to count the frequency of each element
    element_counts = Counter(input_list)

    # Sort the list based on frequency in increasing order
    sorted_list = sorted(input_list, key=lambda x: (element_counts[x], x))

    return sorted_list

# Example usage:
my_input = [1, 1, 2, 3, 2, 3, 5, 1]
result = sort_by_frequency(my_input)
print(result)
