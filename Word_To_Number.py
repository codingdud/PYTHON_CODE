n=int(input("ENTER THE NUMBER = "))
t1=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
t2=['Null','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty']
t3=['Null','Null','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninty','Hundred']
if(n>=0 and n<=10):
    print(t1[n])
if(n>10 and n<=20):
    print(t2[n%10])
if(n>20 and n<100):
    print(t3[n//10],t1[n%10])
if(n==100):
    print("Hundred")
if(n>100 and n<1000):
    p=n//10
    print(t1[n//100],"Hundred",t3[p//10],t1[n%10])
if(n==1000):
    print("Thousand")
if(n>1000 and n<10000):
    p=n//100
    p1=n//10
    print(t1[n//1000],"Thousand",t1[p%10],"And",t3[p1%10],t1[n%10])
if(n==10000):
    print("Ten Thousand")
if(n>10000 and n<100000):
    p1=n%1000
    p2=p1//100
    p3=p1//10
    p=n//1000
    if(p>=0 and p<=10):
        print(t1[p],"Thousand",t1[p2%10],"Hundred And",t3[p3%10],t1[p1%10])
    if(p>10 and p<=20):
        print(t2[p%10],"Thousand",t1[p2%10],"Hundred And",t3[p3%10],t1[p1%10])
    if(p>20 and p<100):
        print(t3[p//10],t1[p%10],"Thousand",t1[p2%10],"Hundred And",t3[p3%10],t1[p1%10])
if(n==100000):
    print("One Lakh")


