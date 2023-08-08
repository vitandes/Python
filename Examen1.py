
def find(numbers):
    if len(numbers) == 0:
       return "[]"
    
    if len(numbers) == 1:
       if numbers[0].lstrip("-").isdecimal():
        return int(numbers[0])
       else:
        a = []
        return a
        
    max = find(numbers[1:])

    if (not isinstance(max,list)) :
        if(numbers[0].lstrip("-").isdecimal()):
            num = int(numbers[0])
            if(num>max):
                return num
            else:
                return max
        else:
            return max
    else:
       if(numbers[0].lstrip("-").isnumeric()):
          num = int(numbers[0])
          return num
       else:
          return a

a = find(["al", "-55", "ññ"])
print(a)