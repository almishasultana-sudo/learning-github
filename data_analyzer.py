# Open the dataset file
file = open("numbers.txt", "r")

# Read all lines
numbers = file.readlines()

# Convert text into integers
nums = []
for num in numbers:
    nums.append(int(num.strip()))

# Calculate results
total = sum(nums)
average = total / len(nums)
maximum = max(nums)
minimum = min(nums)

# Display results
print("Total:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)

file.close()
