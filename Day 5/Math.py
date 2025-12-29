import math 

#sqrt: square of given number 
x=math.sqrt(5);
print("Square of 25 is ",x);

# pow : power of given number
y=math.pow(4,7);
print("Power of 4 ,7",y);

#floor : less roundoff
x=math.sqrt(3.5);
x=math.floor(x);
print(x);

# ceil : rounded top most 
x=math.sqrt(4.5);
x=math.ceil(x);
print(x);

# comb : return the k items from n item without the limitation
x=math.comb(8,4);
print("Combination of k item from n items",x);

#factorial : give the factorial of two number 
x=math.factorial(5);
print("Factorial of given number is ",x);

# lcm : give the lcm of numbers
#x=math.lcm(2,4);
#print("LCM of 2 and 4 is",x);

# perm: return k item from n items withourt limitation ad with order
x=math.perm(8,4)
print("perm of k items from n items ", x);

# gcd : return gcd of numbers
x=math.gcd(2,4);
print("GCD of two numbers is ",x);

# radian : convert degress into radian
x=math.radians(10);
print("Radian is",x);

# degress : convert the radian into degress
print("degress is ",math.degrees(x));
