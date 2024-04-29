def Rats(r,unit,arr,n):
    if n == 0:
        return -1
    
    total_required_food = r * unit
    actual_food = 0
    
    for i in range(0,n-1):
      actual_food += arr[i]
      if actual_food >= total_required_food:
          break
          
    if total_required_food > actual_food:
        return 0
    
    return i + 1 
        

if __name__ == "__main__":
    arr = [1,0,0,0,0,0,0,0]
    n = len(arr)
    r =7
    unit = 2

    print(Rats(r,unit,arr,n))
