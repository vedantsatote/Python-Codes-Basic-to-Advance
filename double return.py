def compare_numbers(a, b):
    if a > b:
        return "a is greater"
    if a < b:
        return "b is greater"
    if a==b:
        return "a and b are equal"

result = compare_numbers(10, 5)
print(result)  # Output: "a is greater"

result = compare_numbers(5, 10)
print(result)  # Output: "b is greater"

result = compare_numbers(5, 5)
print(result)  # Output: "a and b are equal"
