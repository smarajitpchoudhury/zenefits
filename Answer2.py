# cook your dish here
#The function dict takes in the list of all characters (A) and the word in the form of a string(word)
 fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def match(A,char):
    A.sort()
    for i in range(len(A)):
        if A[i]==char:
            return i
def new_A(A,char):
    B = []
    for i in A:
        if i!=char:
            B.append(i)
    return B
def dict(A,word):
    A.sort()
    weight = 0
    n = len(word)
    for i in range(len(word)):
        
        weight = weight + match(A,word[i])*fact(n-1-i)
        A = new_A(A,word[i])

    return weight+1
print (dict(['c','r','a'],'car'))
