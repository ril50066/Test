# coding: utf-8
import random;

mylist = [0 , "hello world" , 123 , "����"];

if  "test" in mylist:
    print("Yes");
else:
    print("No");
    
#print();
print("TEST");

i = 10;

while i > 0:
    print(i);
    i -= 1;
    
print("END");


print(random.randint(1, 10));

testStr = [0 , 1 , 2 , 3 , 4];
random.shuffle(testStr);
print(testStr);
