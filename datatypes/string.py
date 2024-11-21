x ="hello world"
multi_line_string= """
this is a 
multi line 
string
"""

print(x)
print(multi_line_string)

# accessing string
print(x[0])

# looping through string

for i in  x:
    print(i)
    
    
# string length
print(len(x))  

#check string
txt ="The best things in life are free!"
print("free" in txt)  

if "free" in txt:
    print("Yes")
    
if "data" not in txt:
    print("Very True")    
    
# string slicing
print(txt[10:])  


#modify string
print(txt.upper())

print(txt.lower())  

# to remove white spaces
print(txt.strip())

#replace string
print(txt.replace("free","paid"))

#split string by seperator e,g whitesapce or ,

print(txt.split(" "))

# format string
name="John"
new_txt = f"My name is {name}"
print(new_txt)    


# escape charector
txt = "We are the so-called \"Vikings\" from the north."