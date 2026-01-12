from numpy import *

arr=array([1,2,3,4,5]);

# adding the element with number
arr=arr+5;
print(arr);

# adding two arr
arr1=array([1,2,3,4,5]);
arr2=array([6,7,8,9,10]);
arr3=arr1+arr2;
print(arr3);

#trignometry of element 
arr=sin(arr);
print(arr);

# sum of element 
print(sum(arr1));

#maximum of array
print(max(arr1));

# sort of Array
arr1=sort(arr1);
print(arr1);

#concatenate 
arr3=concatenate((arr1,arr2));
print(arr3);

#aliasing : when two or more array use the same memory address
arr4=array([22,33,44,55]);
arr5=arr4;
print(id(arr4));
print(id(arr5));
arr4[3]=66;
print(arr4);
print(arr5);

#Copy : two types of Array 1. Shallow 2. Deep

# Shallow Copy : Array Share the different memory but the values are dependent to each other
arr6=arr5.view();
arr5[0]=11;
print(arr5);
print(arr6);

# deep copy : Indepent array 
arr4=array([1,2,3,4,5]);
arr5=arr4.copy();
arr4[0]=2;
print(arr4);
print(arr5);

