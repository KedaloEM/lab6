intinput=open('input.txt','r')
output=open('output.txt','w')
A=[]
B=intinput.readlines()
N=int(B[0])
for i in range(1,N-1,1):
    A=A+list(map(int, B[i].split()))
b=0
for elem in A:
    if A.count(elem)==2:
        b=elem
print(b,file=output)
intinput.close()
output.close()
