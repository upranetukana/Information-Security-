import hashlib 

a = input("Enter a string:\n") 
result = hashlib.md5() 
print("The byte equivalent of hash is:", end="") 
print(result.digest()) 

import hashlib 
print("The available algorithms are:", end="") 
print(hashlib.algorithms_guaranteed) 
