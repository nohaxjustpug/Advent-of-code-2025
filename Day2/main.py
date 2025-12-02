ranges = []

#with open("input.txt", "r") as f:
#    input = f.readline()
#    ranges = input.split(",")

ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(",")

id_total = 0

halfs = []
thirds = []
quarters = []
fifths = []
sixths = []
sevenths = []

splits = [halfs, thirds, quarters, fifths, sixths, sevenths]

def split_string(string, n):
    if len(string) % n != 0:
        return None 
    else:
        part_size = len(string)
        return_list = [string[i:i + part_size] for i in range(0, len(string), part_size)] 
        return return_list

def check_splits(split):
    total = 0
    target = len(split)
    for i in range(1, len(split)):
        if int(split[i]) == int(split[0]):
            total += 1
    if total == target:
        return int(split[0])
    else:
        return None

for r in ranges:
    sr = r.split("-")
    start = int(sr[0])
    end = int(sr[1])
    for i in range(start, end+1):
        i_str = str(i)
        if len(i_str) % 2 == 0:
            for j in range(len(splits)):
                splits[j] = split_string(i_str, j+2)
                if splits[j] != None:
                    if check_splits(splits[j]) != None:
                        id_total += i
                        print(f"New total: {id_total:010d}")
                        continue
