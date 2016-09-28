#sleep_in

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

#monkey-trouble

def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile):
    return True
  elif not (a_smile or b_smile):
    return True
  else:
    return False


#sum-double

def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  else:
    return a + b

#diff21

def diff21(n):
  if n > 21:
    return (n - 21)*2
  else:
    return 21 - n

#parrot_trouble

def parrot_trouble(talking, hour):
  for hour in range (0,23):
    if (talking and (hour < 7 or hour > 20)):
      return True
    else:
      return False


#makes10
 def makes10(a, b):
   return (( a == 10 or b == 10 ) or (a + b) == 10)

 #near100

 def near_hundred(n):
   return (( n  >= 90 and n <= 110 ) or ( n >= 190 and n <=210))


#front_back

def front_back(str):
  if len(str) <= 1:
    return str

  mid = str[1:-1]

  return  str[-1] + mid + str[0]


 #front3

 def front3(str):
   if len(str) < 3:
     return str+str+str
   else:
     return str[0:3]+str[0:3]+str[0:3]



