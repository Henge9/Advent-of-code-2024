# Open the file in read mode
with open('input', 'r') as file:
    # Read each line in the file
    left=[]
    right=[]
    for line in file:
        row_as_list = line.split("   ")
        left.append(int(row_as_list[0].strip()))
        right.append(int(row_as_list[1].strip()))
    left.sort()
    right.sort()
    total_distance = 0 
    for i in range(0, 1000):
        distance = abs(left[i] - right[i])
        total_distance += distance
    print(total_distance)