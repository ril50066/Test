# coding: utf-8
import random;

mylist = [0 , "hello world" , 123 , "測試"];

print("tset:" + str(mylist))
print( "test:" + str(len(mylist)))

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

"""
from tkinter import *
 
root = Tk()
some = Label(root, text="Tk's job!!", width="30", height="5")
some.pack()
root.mainloop()
"""
