# Set : Immutable, unqiue and not order of insertion . not support the index based access

sets={2,3,4,5}
print(sets);

sets={2,2,3,45};
print(sets);

# with different types
sets={2,'String',True};
print(sets);

#add function in tuple
sets={2,3,4,5,6};
sets.add(7);
print(sets);

#pop function in python :reutrn and remove the random number
sets={2,3,4,5,6,7};
element=sets.pop();
print(element);
print(sets);

#copy function : return shallow copy
set1=sets.copy();
print("Copy of set", set1);

# updates multiple values add
sets.update({11,12,13});
print(sets);


