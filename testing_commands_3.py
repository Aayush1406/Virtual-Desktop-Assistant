l1=["aayush","rajesh","bhavsar","hello"]
l2=["hello"]
flag=False
'''for i in range(0,len(l1)):
    print("1 loop",l1[i])
    for j in range(len(l2)):
        print("2 loop",l2[j])
        if l2[j] in l1[i]:
            print("success")
            flag=True
            print(l1[i])
            print(type(l1[i]))
            break
    
#print("not found")
if(flag==True):
    print("success")
else:
    print("not found")'''
for i in l1:
    for j in l2:
        if j in i:
            print("success")