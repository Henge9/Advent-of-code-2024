def main():

   
  with open('2/input', 'r') as input:
    
  #269 is right for task one
  #337 is right for task two
    safe_count_task_one = 0 
 
    for line in input:
      row_as_list = list(map(int, line.split()))
      if safe_counter(row_as_list):
         safe_count_task_one += 1
  
  with open('2/input', 'r') as input:
    safe_count_task_two = 0 
    for line in input:
      row_as_list = list(map(int, line.split()))
      length = len(row_as_list) 
      print(length)
    
      for i in range(0, length):
        print(f"i = {i}")
        print(f"row_as_list: {row_as_list}")
        holy_list = row_as_list.copy()
        del holy_list[i]
        print(f"holy list {holy_list}")
     
        if safe_counter(holy_list):
          safe_count_task_two += 1
          break
    
    
    
    
    print(f"Safe count task one: {safe_count_task_one}")  
       
    print(f"Safe count task two: {safe_count_task_two}")  

def remove_one_element(list, i):
  return list, #[list.]
 

def safe_counter(row_as_list):
  last_value = len(row_as_list)-1
 
        
  diff_safe = True
  diff_increasing = 0
  diff_decreasing = 0
  for i in range(0,last_value):
      diff  = row_as_list[i] - row_as_list[i + 1]

      #print(0 <= (abs(diff)) < 3)
      if abs(diff) < 1:
        print(f"UNSAFE DIFF LOW: {abs(diff)}")
        diff_safe = False
      elif abs(diff) >3:
        print(f"UNSAFE DIFF HIGH: {abs(diff)}")
        diff_safe = False
      else:
        print(f"SAFE DIFF: {abs(diff)}")


      if diff > 0:
        diff_increasing += 1
      elif diff < 0:
        diff_decreasing += 1
     # print(f" asdf {row_as_list[i]}  {row_as_list[i + 1]}  {diff} {abs(diff)}")
  print(f"Increase: {diff_increasing} || Decrease: {diff_decreasing} || {diff_safe}")
  if ((diff_decreasing > 0 and diff_increasing > 0) == False) and (diff_safe == True):

      print("SAFE COUNT")
      return True
  else:
      print("UNSAFE COUNT")
      return False


  
main()