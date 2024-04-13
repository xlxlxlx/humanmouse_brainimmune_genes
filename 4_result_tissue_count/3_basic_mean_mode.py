import statistics

numbers_B = []
numbers_I = []
numbers_C = []

numbers = numbers_I

# Calculating the maximum, mean, and mode
max_value = max(numbers)
mean_value = statistics.mean(numbers)
mode_value = statistics.mode(numbers)
median_value = statistics.median(numbers)

print(f"Maximum: {max_value}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")