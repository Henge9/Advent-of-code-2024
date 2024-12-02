with open('2/input', 'r') as input:
    #356 är fel
    safe_count = 0 
    for line in input:
        row_as_list = list(map(int, line.split()))
        last_value = len(row_as_list)-1
        
        
        diff_safe = True
        diff_increasing = 0
        diff_decreasing = 0
        for i in range(0,last_value):
            diff  = row_as_list[i] - row_as_list[i + 1]
            diff_safe = True
            #print(0 <= (abs(diff)) < 3)
            if abs(diff) < 1 or abs(diff) >3:
               # print(f"UNSAFE DIFF: {abs(diff)}")
                diff_safe = False
           # else:
             #   print(f"SAFE DIFF: {abs(diff)}")
            if diff > 0:
              diff_increasing += 1
            elif diff < 0:
              diff_decreasing += 1
           # print(f" asdf {row_as_list[i]}  {row_as_list[i + 1]}  {diff} {abs(diff)}")
        print(f"Increase: {diff_increasing} || Decrease: {diff_decreasing} || {diff_safe}")
        if ((diff_decreasing > 0 and diff_increasing > 0) == False) and (diff_safe == True):
            safe_count += 1
         #   print("SAFE COUNT")
        else:
            print("UNSAFE COUNT")

        #print(f"{row_as_list}  {row_as_list[last_value]}")
    print(f"Safe reports: {safe_count}")
    