from numpy import *;

#1. using array function
arr=array([1,2,3,4,5],float);
print(arr);

arr=array([3,4,5,6,7,5],int);
print(arr);

#2 linspace function : taking 3 parameter start,end,parts. diivide krta h ek limit se dusari limit tk parts me

arr=linspace(0,15,4);
print(arr);

#3 arange : take 3 parameters . start,end and step . step mtlb value difference
arr=arange(2,8,2);
print(arr);

#4 logspace : same as linspace but divide according to logs
arr=logspace(0,15,4);
print(arr);

#5 zeros : create the array with inital values zero. by default float type
arr=zeros(5);
print(arr);
arr=zeros(5,int)
print(arr);

#6 ones : create the array with one . 
arr=ones(5);
print(arr)

