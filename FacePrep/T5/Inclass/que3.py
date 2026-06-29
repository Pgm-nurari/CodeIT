"""
Emergency Supply Drone: Maximizing Resource Value Delivery    

You are designing a software system for emergency supply drones that deliver aid during natural disasters. Each drone has a limited weight capacity and must be loaded with the most valuable combination of resources (food, medicine, etc.).

Each supply item has:

A weight.
A value (representing usefulness or market price).
The drone can carry fractions of items if needed. Your task is to write a function to determine the maximum total value that can be carried in the drone without exceeding its weight limit.

Given the weights and values of n items and a drone capacity W, return the maximum value that can be carried in the knapsack using fractional parts of items if necessary.



Input Format

First line: two integers n (number of items) and W (capacity of the drone).
Next n lines: each contains two integers value and weight for each item.


Output Format

A single floating-point number representing the maximum value that can be carried, rounded to 2 decimal places.


Example 1

Sample Input 1

3 50

60 10

100 20

120 30



Sample Output 1

240.00



Explanation

Items sorted by value/weight ratio:
(60/10 = 6.0)
(100/20 = 5.0)
(120/30 = 4.0)
Pick item 1 (10 kg, full), item 2 (20 kg, full), and 20 kg of item 3 (2/3 of it = 80 value).
Total value = 60 + 100 + 80 = 240.00
 

Example 2

Sample Input 2

2 10

100 5

60 10



Sample Output 2

130.00



Explanation

Take all of item 1 (5kg = 100).
Remaining capacity = 5kg. Take 5kg of item 2 (half = 30).
Total value = 100 + 30 = 130.00
"""

def fractional_knapsack(n, W, items):
    # Calculate value to weight ratio for each item
    items = [(value, weight, value / weight) for value, weight in items]
    
    # Sort items by value/weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0
    remaining_capacity = W
    
    for value, weight, ratio in items:
        if remaining_capacity <= 0:
            break
        
        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take the fraction of the item that fits
            total_value += ratio * remaining_capacity
            remaining_capacity = 0
    
    return round(total_value, 2)   

def main():
    n, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    
    max_value = fractional_knapsack(n, W, items)
    print(f"{max_value:.2f}")
    
if __name__ == "__main__":
    main()    
