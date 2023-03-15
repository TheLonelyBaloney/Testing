num = "4x^3+8x"
denum = "x^4+x^3+5x-4"

def turntolist(numordenum):
  numordenum = numordenum.replace("-","+-")
  numordenum = numordenum.split("+")
  result = []
  for i in numordenum:
    toappend = ""
    digit_inserted = False
    for j in i:    
      expo = 0
      if j.isdigit() and digit_inserted == False:
        toappend += j
        digit_insterted = True  
      elif j == "-" :
        toappend+= "-"
      elif j.isalpha() or j == "^":
        alpha_inserted = True
        digit_inserted = True
      elif j.isdigit() and digit_inserted == True:
        expo += int(j)
    while len(result) < expo+1:
      result.append(0)
    if alpha_inserted == True and expo == 0:
      expo = 1
    if toappend == "":
      toappend += "1"
      result[expo] = int(toappend)
    else:
      result[expo] = int(toappend)
  return result
####################
num = turntolist(num)
denum = turntolist(denum)
if len(denum) <= len(num):
  raise Exception("Dont be lazy and do the long fraction")
print(num)
####################
def gcd_list(nums):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums[0]
    else:
        a = nums[0]
        for b in nums[1:]:
            while b != 0:
                a, b = b, a % b
        return a

def factor(thalist):
  factored = []
  while len(thalist) != 0:
##################### factor ou gcd
    if gcd_list(thalist) != 1:
        gcd = gcd_list(thalist)
        factored += str(gcd)
        thalist = [num // gcd for num in thalist]
##################### factor out x
    while thalist[0] == 0:
      thalist = thalist[1:]
      factored += "x"
##################### when 2x+2 or 4x+2 ect.
    if len([num for num in thalist if num != 0]) == 2: #check for non 0 numbers
      lastlist = [num for num in thalist if num != 0] #get an abrievated list of non 0 numbers so that theres is no extra 0s
      biggestexpo = len(thalist) -1 # get the biggest expo (assuming that the other integer is expo 0)
      if float(lastlist[1] / lastlist[0]).is_integer() and lastlist[0] != 1: #check if the smaller is a diviser of the bigger and != 1
        div = lastlist[0] #store the divider
        factored += str(div) #add constant factor
        factored.append(f"{lastlist[1]//div}x^{biggestexpo} + {lastlist[0]//div}") #add divided factor
        return factored
      elif float(lastlist[0] / lastlist[1]).is_integer() and lastlist[1] != 1: #check if bigger is a diviser of the bigger and != 1
        div = lastlist[1] #store the diviser
        if lastlist[0]//div == 1:
          factored.append(f"x^{biggestexpo} + {lastlist[1]//div}")
        else:
          if div != 1:
            factored += str(div)
          factored.append(f"{lastlist[1]//div}x^{biggestexpo} + {lastlist[0]//div}")
        return factored   
      else:
        if lastlist[1] == 1:
          factored.append(f"x^{biggestexpo} + {lastlist[0]}")
        else:
          factored.append(f"{lastlist[1]}x^{biggestexpo} + {lastlist[0]}")
        return factored
#######################
print(factor(num))
