import sys

threshold = float(sys.argv[1])
limit = float(sys.argv[2])

if not 0.0 <= threshold <= 1_000_000_000.0 or not 0.0 <= limit <= 1_000_000_000.0:
	print("--- Threshold and Limit value must be between 0.0 and 1,000,000,000.0 ---")
	exit()

output = []
sum = 0.0

input_count = int(input("Enter number of inputs (max. 100) : "))

if input_count > 100:
	print("--- Input count limit exceeded. Setting input count to 100 ---")
	input_count = 100

print("\nInput (Enter "+ str(input_count) +" values - press Enter after every value): ")

for i in range(input_count):

	user_input = float(input())

	if not 0.0 <= user_input <= 10_000_000.0:
		print("--- Exiting Program - Input value is outside of 0.0 to 10,000,000.0 range ---")
		exit()

	if user_input < threshold:
		current = 0
	else:
		current = user_input - threshold

	if sum + current > limit:
		x = float(limit - sum)
		output.append(x)
		sum += x
	else:
		output.append(float(current))
		sum += float(current)

print("\n\nOutput: ")

for i in output:
	print(i)

print(sum)