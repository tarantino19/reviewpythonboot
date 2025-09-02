# try:
#   10 / 2
# except Exception:
#   print("can't divide by zero")
  

try:
  10 / 0
except Exception as e:
  print(e)

# prints "division by zero"

# don't do this
def craft_sword(metal_bar):
    try:
        if metal_bar == "bronze":
            return "bronze sword"
        if metal_bar == "iron":
            return "iron sword"
        if metal_bar == "steel":
            return "steel sword"
        raise Exception("invalid metal bar")
    except Exception as e:
        print(f"An error occurred: {e}")
        

# do this
try:
    craft_sword("gold bar")
except Exception as e:
    print(e)
    
#types of exception
try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)
    
    
    

