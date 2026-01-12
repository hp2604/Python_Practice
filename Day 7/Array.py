# Array : same type collection but not fixed size. There are different code each type
# Use krne k liye function import krte h array. Is function k do paraneter hote h 1 type and dusara array.
# b : unsigned char #B: signed char size 1 byte.
# h : unsigned short  # H : signed Short size 2 byte
# i : unsigned Integer # I : signed Integer 
# l : unsigned long  #L : Signed Long 
# f: float  #d: double 


# Creation of Array
from array import * ;

arr=array('i', [2,4,1,8]);
print(arr);

# for loop
for i in range(0,len(arr)):
        print(arr[i]);

# User Input Array
userArray=array('i',[]);
n=int(input("Enter the Size of Array"));

for i in range(n) :
    ele=int(input("Enter the next value of Array"));
    userArray.append(ele);

print(userArray);


# Linear Search in Array
no=int(input(" Enter the number "));
count =0;
for i in range(len(userArray)) :
    if(no==i) :
        print("Number present at ",i)
        count +=1;
        break;

if(count==0) :
    print("number is not present");


val=array('i',[2,1,3,4,5,64,4]);

#count : return the occurence of number 
print(val.count(4));

#index : return the index of the element else error if the number is not present 
print(val.index(3))

# insert : put element before the the i insert(i,x)
val.insert(3,6);
print(val)

# pop : remove and return the element at index i
remove=val.pop(4);
print(remove);
print(val)

# remove : remove the first occurnce of no.
val.remove(4);
print(val)

# reverse : reverse the array
val.reverse();
print(val)

# tolist: convert the array in list
ls=val.tolist();
print(ls)
