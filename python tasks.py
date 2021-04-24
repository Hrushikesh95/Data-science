#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[ ]:





# In[2]:


l2 = [1,2,[3,4,5,6],9]
l2[1][4].insert(4,[7,8])
print(l2)


# In[15]:


l1 = [10, 20, [30, 40, [50, 60], 80], 90, 100]
l1[2].insert(2,70)
print(l1)


# In[4]:


l1 = [10, 20, [30, 40, [50, 60], 80], 90, 100]
l1[2].insert(2,70)
print(l1)


# In[5]:


l2 = [1,2,[3,4,5,6],9]
l2[2].insert(4,[7,8])
print(l2)


# In[9]:


#new task 5
dict1 = { 
   "april_batch":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "python":80,
            "maths":70
         }
      }
   }
}

dict1
type(dict1)


# In[10]:


dict1["april_batch"]["student"]["name"]


# In[11]:


dict1["april_batch"]["student"]["marks"]["python"]


# In[16]:


dict1["april_batch"]["student"]["name"]="Hrushikesh"
dict1


# In[2]:


dict1 = { 
   "april_batch":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "python":80,
            "maths":70
         }
      }
   }
}
dict1


# In[4]:


dict1["april_batch"]["student"]["marks"]["DL"]=80
dict1


# In[7]:


Dict = {1: 'Royal', 'name': 'Challengers', 3: 'Benglore'}

print("Accessing a element using get:")
print(Dict.get(1))
print(Dict.get("name"))
print(Dict.get(3))


# In[2]:


Dict = {'Dict1': {1: 'Benglore'},
        'Dict2': {'Name': 'RCB'}}

print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])


# In[21]:


Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'netzwerk',
        'A' : {1 : 'to', 2 : 'For', 3 : 'rcb'},
        'B' : {1 : 'RCB', 2 : 'Life'}}
print("Initial Dictionary: ")
print(Dict)
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)


# In[27]:


Dict = {1: 'RCB', 'name': 'For', 3: 'Life'}
print(Dict)
pop_ele = Dict.pop(1)
print('\nDictionary after deletion: ' + str(Dict))
print('poped key is: ' + str(pop_ele))


# In[29]:


#lists
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with Numbers: ")
print(List)

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with Mixed Values: ")
print(List)


# In[35]:


List1 = []
print(len(List1))
List2 = [10, 20, 14]
print(len(List2))
print(type(List2))


# In[36]:


List = []
print("Initial blank List: ")
print(List)
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)


# In[2]:


List = [1,2,3,4]
print("Initial List: ")
print(List)
List.insert(3, 12)
List.insert(0, 'Netzwerk')
print("\nList after Insert Operation: ")
print(List)


# In[ ]:


#tuples
t=(0,1,2,3)
t_add=t+(4,5,6)
print(t_add)


# In[ ]:


t=(1,2,3)
t1=list(t)
print(t1)


# In[ ]:


t1.insert(2,5)
print(t1)


# In[6]:


#sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y) 

print(z)


# In[7]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y) 

print(z)


# In[1]:


num1=int(input("Enter your value="))
print ("num1="+num1)
num2=int(input ("\nEnter your value="))
print ("num2="+num2)


# In[ ]:


num1=int(input("Enter your value="))
print (num1)
num2=int(input ("\nEnter your value="))
print (num2)


# In[ ]:


num1=input("Enter your value=")
print ("num1="+num1)
num2=input ("\nEnter your value=")
print ("num2="+num2)


# In[2]:


print("Your first number")
num1=int(input())
print("your second number")
num2=int(input())
print("choose your option : 1.addition,2.subtraction,3.multiplication,4.divsion")
d=int(input())
if d==1:
    c=num1+num2
    print(c)
elif d==2:
    c=num1-num2
    print(c)
elif d==3:
    c=num1*num2
    print(c)
elif d==4:
    c=num1%num2
    print(c)   
else:
    print("out of order")

    
    
    


# In[3]:


print("Your first number")
a=int(input())
print("your second number")
b=int(input())
print("choose your option : 1.addition,2.subtraction,3.multiplication,4.divsion")
d=int(input())
if d==1:
    c=a+b
    print(c)
elif d==2:
    c=a-b
    print(c)
elif d==3:
    c=a*b
    print(c)
elif d==4:
    c=a%b
    print(c)   
else:
    print("out of order")


# In[14]:


#loops
count= 10
while(count > 0):
    print(count)
    count = count -1


# In[16]:


#for loop for tuple
RCB = ("Kohli", "Abd", "Max")
for x in RCB:
    print(x) 


# In[29]:



for x in range(6):
  print(x)
else:
  print("Finally finished!") 


# In[18]:


#for loop for sets
set1 = {"abc", 34, True, 40, "male"} 
for x in set1:
    print(x)


# In[22]:


RCB = {
  "Virat": "Dravid",
  "Abd": "Kumble",
  "Cup": 2021
}
for x in RCB:
    print(x)


# In[23]:


RCB = {
  "Virat": "Dravid",
  "Abd": "Kumble",
  "Cup": 2021
}
for x in RCB:
    print(RCB[x])


# In[26]:


for x,y in RCB.items():
    print(x,y)


# In[25]:


for x in RCB.values():
    print(x)


# In[5]:


from functools import reduce
Num = [5, 8, 10, 20, 50, 100,200]
sum = reduce((lambda x, y: x + y), Num) #previous two elements are added to the next element and this goes on till the end of the list like
print (sum)


# In[14]:


import functools
lis = [ 1 , 3, 5, 6, 2, ]
 # using reduce to compute maximum element from list
print ("The maximum element of the list is : ",end="")
print (reduce(lambda a,b : a if a > b else b,lis))


# In[2]:


l1 = ["eat","sleep","repeat"]
s1 = "Netzwerk"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print (" type:",type(obj1))
print (list(enumerate(l1)))
 
# changing start index to 2 from 0
print (list(enumerate(s1,9)))


# In[38]:


def remove(string):
    return string.replace("       hello     ", "hello")
      
# Driver Program
string =  "       hello      "
print ("original string is"+ string)
print("modified string is "+(remove(string)))


# In[7]:


string = "       Hello       "

while string[0] == " ":
    string = string[1:]
    
while string[-1] == " ":
    string = string[:-1]
    
print(string)


# In[20]:


str2="     Hello     "
char=0
for i in str2:
    char=char+1
print(char)


# In[17]:


str1= "My name is navya"
char=0
for i in str1:
    char=char+1
print(char)    


# In[6]:


def multipliers():
    return[lambda x:i*x for i in range(4)]
[ m(1)for m in multipliers()]


# In[58]:



list=[x for x in range(25) if x%2 == 0]
print (list)


# In[26]:


def firstDigit(n):
    while n >= 10:
        n = n / 10;
    return int(n)

def lastDigit (n):
    return(n % 10)
n=54698;

print (firstDigit (n), end = " ")
print (lastDigit (n))
sum=(firstDigit(n) + lastDigit(n))
print(sum)


# In[59]:


Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10

print("\nReverse of entered number is = %d" %Reverse)


# In[41]:


length = float(input('Please Enter the Length of a Triangle: '))
width = float(input('Please Enter the Width of a Triangle: '))

# calculate the area
area = length * width
perimeter= (length * 2 + width * 2)

print("The Area of a Rectangle using", length, "and", width, " = ", area)
print("The Perimeter of Rectangle using", length, "and", width, " = ", perimeter)

if area > perimeter:
    print(" area is greater then perimeter")
    
elif area == perimeter:
    print("area is equal to perimeter")
    
else: 
    print("perimeter is greater")
   


# In[58]:


def Valid(a, b, c):
  
    # Check condition
    if ((a + b + c == 180) and a != 0 and b != 0 and c != 0):
        return True
    else:
        return False
    
if __name__ == "__main__":
    a = 60
    b = 40
    c = 80
    if (Valid(a, b, c)):
        print("Valid")
    else:
        print("Invalid")


# In[52]:


a = 10
b = 14
c = 12
print(max(a, b, c))


# In[53]:


def maximum(a, b, c):
  
    if (a >= b) and (a >= c):
        largest = a
  
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
          
    return largest
  
a = 10
b = 14
c = 12
print(maximum(a, b, c))


