# tuple : Immutable sequence data type, order preserve

tup=(2,3,4,5);
print(tup);


# immutable
#tup[1]=5;
# output : error

# duplicate in tuple
tup=(2,3,3,4,5,6);
print(tup);


# count function
print(tup.count(2));
print(tup.count(3));

#index function
print(tup.index(2));

# tuple with different type of values
tuples=(1,"String",True);
print(tuples);


