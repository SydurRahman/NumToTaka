class fseven:
    word=""
    flag=1
    blag=1
    tlag=1
    def __init__(self,p):
        self.num=p
    def single(self,x):
        self.flag=1
        this={"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","0":""}
        w=this[x]
        if(x==0):
            self.flag=0
        return w
    def couple(self,a,b):
        self.blag=1
        that={"1":"Eleven","2":"Twelve","3":"Thirteen","4":"Fourteen","5":"Fifteen","6":"Sixteen","7":"Seventeen","8":"Eighteen","9":"Ninteen","0":"Ten"}
        those={"2":"Twenty","3":"Thirty","4":"Forty","5":"Fifty","6":"Sixty","7":"Seventy","8":"Eighty","9":"Ninty","0":""}
        if a=='1':
            w=that[b]
        elif a!='1':
            m=those[a]
            if a=='0':
                self.blag=0
            n=self.single(b)
            w=m+" "+n
            if (self.blag==0 and self.flag==0):
                self.tlag=0
            else:
                self.tlag=1
        return w
    def amount(self,x):
        these={1:"",2:" Hundred ",9:" Hundred ",4:" Thousand ",11:" Thousand ",3:" Thousand ",10:" Thousand ",6:" Lakh ",13:" Lakh ",5:" Lakh ",12:" Lakh ",8:" Crore ",14:" Crore ",7:" Crore "}
        rd=these[x]
        return rd
user=input("Enter the Amount: ")
userNum=user[::-1]
userNum=userNum+" "
obj=fseven(userNum)
obj.word=""
length=len(userNum)
j=length-2
while(j>=0):
    if(length==2):
        obj.word=obj.word+" "+obj.single(userNum[j])
        break
    if(j==1 or j==4 or j==6 or j==8 or j==11 or j==13):
        obj.word=obj.word+" "+obj.couple(userNum[j],userNum[j-1])
        if(obj.tlag==0):
            pass
        elif(obj.tlag==1):
           obj.word=obj.word+" "+ obj.amount(j)
    elif(j==2 or j==9):
        obj.word=obj.word+" "+obj.single(userNum[j])
        if(obj.flag==0):
            pass
        elif(obj.flag==1):
            obj.word=obj.word+" "+ obj.amount(j)
    elif((j==3 or j==5 or j==7 or j==10 or j==12 or j==14) and userNum[j+1]==" "):
        obj.word=obj.word+" "+obj.single(userNum[j])
        if(obj.flag==0):
            pass
        elif(obj.flag==1):
            obj.word=obj.word+" "+ obj.amount(j)
    j=j-1
obj.word=obj.word+" Taka Only"
print("The Amount is : ")
print(obj.word)
