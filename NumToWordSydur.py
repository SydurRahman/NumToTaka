class fseven:
    word=""
    flag=1
    blag=1
    tlag=1
    def __init__(self,p):
        self.num=p
    def single(self,x):
        self.flag=1
        if x=='1':
           w="One"
        elif x=='2':
            w="Two"
        elif x=='3':
            w="Three"
        elif x=='4':
            w="Four"
        elif x=='5':
            w="Five"
        elif x=='6':
            w="Six"
        elif x=='7':
            w="Seven"
        elif x=='8':
            w="Eight"
        elif x=='9':
            w="Nine"
        elif x=='0':
            w=""
            self.flag=0
        return w
    def couple(self,a,b):
        self.blag=1
        if a=='1':
            if b=='0':
                w="Ten"
            elif b=='1':
                w="Eleven"
            elif b=='2':
                w="Twelve"
            elif b=='3':
                w="Thirteen"
            elif b=='4':
                w="Fourteen"
            elif b=='5':
                w="Fifteen"
            elif b=='6':
                w="Sixteen"
            elif b=='7':
                self.w="Seventeen"
            elif b=='8':
                w="Eighteen"
            elif b=='9':
                w="Ninteen"
        elif a!='1':
            if a=='0':
                m=""
                self.blag=0
            elif a=='2':
                m="Twenty"
            elif a=='3':
                m="Thirty"
            elif a=='4':
                m="Fourty"
            elif a=='5':
                m="Fifty"
            elif a=='6':
                m="Sixty"
            elif a=='7':
                m="Seventy"
            elif a=='8':
                m="Eighty"
            elif a=='9':
                m="Ninety"
            n=self.single(b)
            w=m+" "+n
            if (self.blag==0 and self.flag==0):
                self.tlag=0
            else:
                self.tlag=1
        return w
    def amount(self,x):
        if(x==1):
             rd=""
        elif(x==2 or x==9):
            rd=" Hundred "
        elif(x==4 or x==11 or x==3 or x==10):
            rd=" Thousand "
        elif(x==6 or x==13 or x==5 or x==12):
            rd=" Lakh "
        elif(x==8 or x==14 or x==7 or x==14):
            rd=" Crore "
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
        obj.word=obj.word+" "+obj.single(userNum[j])+" Taka Only"
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
