with open("input.txt", "r") as f:
    banks = f.readlines()
def process_bank(bank):
    largest = 0
    for i in range(0, len(bank)-1):
        curr = bank[i]
        if int(curr) > int(bank[largest]):
            largest = i
    print(bank)
    next_large = largest+1
    for i in range(largest+1, len(bank)):
        curr = bank[i]
        if int(curr) > int(bank[next_large]):
            next_large = i
    return int(bank[largest] + bank[next_large])
total_j = 0
for i, bank in enumerate(banks):
    print(f"Processing bank # {i}")
    output = process_bank(bank.strip())
    print(f"Highest Joltage: {output}")
    total_j += output
print(f"Total Joltage: {total_j}")
