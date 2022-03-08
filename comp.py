
s1=input("enter first string")
s2=input("enter second string")
n=int(input("enter length of charactors for compare"))

def compare(s1,s2,n):
    if len(s1)>=n and len(s2)>=n:
        if (s1[0:n]==s2[0:n]):
            return True
        else:
            return False
    return "Given length is not suitable for operation"

print(compare(s1,s2,n))