# Example test to separate them is 1,2,5
s1 = float(input())
s2 = float(input())
s3 = float(input())
print(s1 + s2 + s3 / 3) #A) 
print((s1 + s2 + s3) / 3) #B) 
print(float(s1 + s2 + s3 / 3)) #C) 
print(float(s1) + float(s2) + float(s3) / 3) #D) 
print(s1*s2*s3 / 3) #E) 
