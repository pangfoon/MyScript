#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 8
b = 2
print( "Addition:\t" , a , "+" , b , "=" , a + b )
'''
expression
opertor -,*
Operand a,b
'''
print( "Subtraction:\t" , a , "-" , b , "=" , a - b )
print( "Multiplication:\t" , a , "x" , b , "=" , a * b )
print( "Division:\t" , a , "?" , b , "=" , a / b )
print( "Floor Division:\t" , a , "?" , b , "=" , a // b )
print( "Modulus:\t" , a , "%" , b , "=" , a % b )
print( "Exponent:\t " , a , "? = " , a ** b , sep = "" )


# In[2]:


a = 8
b = 4
print( "Assign Values:\t\t" , "a =" , a , "\tb =" , b )
a += b
print( "Add & Assign:\t\t" ,"a =" , a , "(8 += 4)" )
a -= b #a = a-b
print( "Subtract & Assign:\t" , "a =" , a , " (12 - 4)" )
a *= b
print( "Multiply & Assign:\t" , "a =" , a , "(8 ? 4)" )
a /= b
print( "Divide & Assign:\t" , "a =" , a , "(32 ? 4)" )
a %= b
print( "Modulus & Assign:\t" , "a =" , a , "(8 % 4)" )


# In[3]:


nil = 0
num = 0
max = 1
cap = "A"
low = "a"

print( "Equality :\t" , nil , "==" , num , nil == num )
print( "Equality :\t" , cap , "==" , low , cap == low )

print( "Inequality :\t" , nil , "!=" , max , nil != max )

print( "Greater :\t" , nil , ">" , max , nil > max )
print( "Lesser :\t" , nil , "<" , max , nil < max )

print( "More Or Equal :\t" , nil , ">=" , num , nil >= num )
print( "Less or Equal :\t" , max , "<=" , num , max <= num )


# In[4]:


a = True
b = False
print( "AND Logic:" )
print( "a and a =" , a and a )
print( "a and b =" , a and b )
print( "b and b =" , b and b )
print( "\nOR Logic:" )
print( "a or a =" , a or a )
print( "a or b =" , a or b )
print( "b or b =" , b or b )
print( "\nNOT Logic:" )
print( "a =" , a , "\tnot a =" , not a )
print( "b =" , b , "\tnot b =" , not b )


# In[5]:


a = 1
b = 2
print( "\nVariable a Is :" , "One" if ( a == 1 ) else "Not One" )
print( "Variable a Is :" , "Even" if ( a % 2 == 0 ) else "Odd" )
print( "\nVariable b Is :" , "One" if ( b == 1 ) else "Not One" )
print( "Variable b Is :" , "Even" if ( b % 2 == 0 ) else "Odd" )
max = a if ( a > b ) else b
print( "\nGreater Value Is:" , max )


# In[9]:


a= (input("A:"))
b= (input("B:"))
max= a if ( a > b ) else b
print("max:", max)


# In[10]:


a = 2
b = 4
c = 8
print( "\nDefault Order:\t", a, "*", c,"+", b, "=", a * c + b )
print( "Forced Order:\t", a, "* (", c,"+", b, ") =", a * ( c + b ) )
print( "\nDefault Order:\t", c, "//", b, "-", a, "=", c // b - a )
print( "Forced Order:\t", c, "// (", b,"-", a, ") =", c // ( b - a ) )
print( "\nDefault Order:\t", c, "%", a, "+", b, "=", c % a + b )
print( "Forced Order:\t", c, "% (", a, "+", b, ") =", c % ( a + b ) )
print( "\nDefault Order:\t", c, "**", a, "+", b, "=", c ** a + b )
print( "Forced Order:\t", c, "** (", a, "+", b, ") =", c ** ( a + b ) )


# In[11]:


a = input( "Enter A Number: " )
b = input( "Now Enter Another Number: " )
sum = a + b
print( "\nData Type sum :" , sum , type( sum ) )
sum = int( a ) + int( b )
print( "Data Type sum :" , sum , type( sum ) )
sum = float( sum )
print( "Data Type sum :" , sum , type( sum ) )
sum = chr( int( sum ) )
print( "Data Type sum :" , sum , type( sum ) )


# In[12]:


a = 10
b = 5
print( "a =" , a , "\tb = " , b )
# 1010 ^ 0101 = 1111 (decimal 15)
a = a ^ b
# 1111 ^ 0101 = 1010 (decimal 10)
b = a ^ b
# 1111 ^ 1010 = 0101 (decimal 5)
a = a ^ b
print( "a =" , a , "\tb = " , b )


# In[13]:


quarter = [ "January" , "February" , "March" ]
print( "First Month :" , quarter[0] )
print( "Second Month :" , quarter[1] )
print( "Third Month :" , quarter[2] )

coords = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9 ]] 
print( "\nTop Left 0,0 :" , coords[0][0] )
print( "Bottom Right 1,2 :" , coords[1][2] )
print( "\nSecond Month First Letter :" , quarter[1][0] )


# In[14]:


basket = [ "Apple" , "Bun" , "Cola" ]
crate = [ "Egg" , "Fig" , "Grape" ]
print( "Basket List:" , basket )
print( "Basket Elements:" , len( basket ) )
basket.append( "Damson" )
print( "Appended:" , basket )
print( "Last Item Removed:" , basket.pop() )
print( "Basket List" , basket )
basket.extend( crate )
print( "Extended:" , basket )
del basket[1] # del ลบตำแหน่งข้อมุล
print( "Item Removed:" , basket )
del basket[1:3]
print( "Slice Removed:" , basket )


# In[15]:


zoo = ( "Kangaroo" , "Leopard" , "Moose" )# ข้อมูลประเภท Tuple ไม่สามารถเปลี่ยนแปลงได้
print( "Tuple:" , zoo , "\tLength:" , len( zoo ) )
print( type( zoo ) )

bag = { "Red" , "Green" , "Blue" }# ข้อมูลประเภท set เปลี่ยนแปลงได้
bag.add( "Yellow" )
print( "\nSet:" , bag , "\tLength" , len( bag ) )
print( type( bag ) )
print( "\nIs Green In bag Set?:" , "Green" in bag )
print( "Is Orange In bag Set?:" , "Orange" in bag )

box = { "Red" , "Purple" , "Yellow" }
print( "\nSet:" , box , "\t\tLength" , len( box ) )
print( "Common To Both Sets:" , bag.intersection( box ) )


# In[16]:


dict = { "name" : "Bob" , "ref" : "Python" , "sys" : "Win" } #key = name    value = Bob
print( "Dictionary:" , dict )

print( "\nReference:" , dict[ "ref" ] )

print( "\nKeys:" , dict.keys() )

del dict[ "name" ]
dict[ "user" ] = "Tom"
print( "\nDictionary:" , dict )
print( "\nIs There A name Key?:" ,"name" in dict )


# In[21]:


num = int( input( "Please Enter A Number: " ) )
if num > 5 :
	print( " Number Exceeds 5 " )
elif num < 5 :
	print( "Number is Less Than 5" )
else :
	print( "Number Is 5" )

if num > 7 and num < 9 :
	print( "Number is 8" )
if num == 1 or num == 3 :
	print( "Number Is 1 or 3" )


# In[28]:


i = 1
while i < 4 : #ทำซ้ำไปเรื่อย
    print( "\nOuter Loop Iteration:" , i )
    i += 1 # การเปลี่ยนแปลงค่าของการนับ
    j = 1
    while j < 4 :
        print( "\tInner Loop Iteration:" , j )
        j += 1


# In[31]:


chars = [ "A" , "B", "C" ]
fruit = ( "Apple" , "Banana" , "Cherry" )
dict = { "name" : "Mike" , "ref" : "Python" , "sys" : "Win" }

print( "\nElements:\t" , end = " " ) # end =  การเอาข้อมูลมาต่อท้ายกัน จะไม่มีการขึ้บรรทัดใหม่
for item in chars :# item  คือ ข้อมูลที่อยู่ใน chars
	print( item , end = " " )
    
print( "\nEnumerated:\t" , end = " " )
for item in enumerate( chars ) :
	print( item , end = " " )
    
print( "\nZipped:\t" , end = " " )
for item in zip( chars , fruit ) : # in zip คือ การจับคู่ที่มัน index ตรงกัน
	print( item , end = " " )
    
print( "\nPaired:" )
for key , value in dict.items() :# dict.items  การแสดงค่าของ dict 
	print( key , "=" , value )


# In[ ]:




