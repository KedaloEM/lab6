intinput=open('input.txt','r')
output=open('output.txt','w')
B=intinput.readlines()
N=int(B[0])
A=list(map(int,B[1].split()))
min=None
for i in range(len(A)):
       for j in range(len(A)):
           if i!=j:
               if (A[i]<0) and (i<j) and (A[i]==-A[j]):
                   if min==None or ((j-i)<min):
                       min=j-i
if min!=None:
    print(min,file=output)
else:
    print(0,file=output)
intinput.close()
output.close()
