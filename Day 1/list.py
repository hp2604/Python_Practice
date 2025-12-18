#defination : collection of data . Also contain different data mutable:chanageable

nums=[2,4,6,8,10];
print(nums[0]);
print(nums[1]);
print(nums[2]);
print(nums[3]);
print(nums[4]);

print(nums);

# Reverse List 
print(nums[-1]);
print(nums[-2]);
print(nums[-3]);
print(nums[-4]);
print(nums[-5]);


# List with string
names=["Harsh","Surbhi"]
print(names[0]);
print(names[1]);


# : operator in List
print(nums[:3]);


# List with different data
values=["Harsh",2,3.5,True];
print(values);


#mutable
values=["changed"," values"];
print(values);

names[1]="Akshat"
print(names);

#add element  in list in last
nums.append(25);
print(nums);

#add element in start
nums.insert(1,12);
print(nums);

#remove particular element in list
nums.remove(25);
print(nums);

#remove element on index based
nums.pop(2);
print(nums);

#delete mulltiple value
del nums[2:3];
print(nums);

#add multiple element
nums.extend([12,14]);
print(nums);

# addition in list
num1=[1,2,3,4];
num2=[5,6,7,8];
print(num1+num2);

#min function 
print(min(nums));

#max function
print(max(nums));

#clear list
num1.clear();
num2.clear();

