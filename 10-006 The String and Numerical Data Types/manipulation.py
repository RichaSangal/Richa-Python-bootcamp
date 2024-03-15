import os
os.system('cls' if os.name == 'nt' else 'clear')

# define a vriable for the string and anoter fr length
# use the len function in indexing the position required 

str_manip=input("Enter a sentence: ")
str_manip_len=len(str_manip)
print(str_manip_len)
str_manip_lastletter=str_manip[str_manip_len:str_manip_len-2:-1]
str_manip_last3=str_manip[str_manip_len:str_manip_len-4:-1]
str_manip_replace=str_manip.replace(str_manip_lastletter,"@")
print(str_manip_replace)
print(str_manip_last3)
print(str_manip[0:3]+str_manip[str_manip_len-2:str_manip_len])