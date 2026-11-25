'''a='Happy Birthday'
print(a[-4:-7:-1])'''


'''# with arg with return// whenever it is return ,we should callbthe function
def convert(s,out):
     out=''
     for i in s:
        if'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
     return out
print(convert(input('enter a string:'),''))'''


'''# with arg without return
def convert (s,out):
    out=''
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
print(convert(input('enter a string:'),''))'''

'''#without arg without return
def convert():
    s=input('enter:')
    out=''
    for i in s:
        if'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
convert()

#without arg with return
def covert():
    s=input('enter:')
    out=''
    for i in s:
        if'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert())'''
    
'''class college:
    cname="gcem"
    cloc='hoodi'
s1=college()
print(s1.cname,s1.cloc)
print(college.cname)
college.cloc='KRPurm'
print(college.cloc)
print(s1.cloc)

print('changing loc wtrsp obj')
s1.cloc='hoodi'
print(s1.cloc)
print(college.cloc)'''

'''class college:
    cname='gcem'
    cloc="hoodi"
s1=college()
s1.sname='deeksha'
s1.phno='099782786'

s2=college()
s2.sname='dhghg'
s2.phno='688397380'

print(s1.cloc)
s1.cloc='KR PURM'
print('After changing')
print(s1.cloc)
print(s2.cloc)
print(college.cloc)'''

'''class college:
    cname='gcem'
    cloc='hoodi'
    @classmethod
    def dis(cls):
      print(cls.cname,cls.cloc)
    def __init__(self,name,phno,usn):
        self.name=name
        self.phno=phno
        self.usn=usn
    def display(self):
      print(self.name,self.phno,self.usn)
    def change_name(self,new):
        self.name=new
    
s1=college('deeksha',998839728,'ad145gd')
s2=college('babu',987936768,'ffd445hgf')
s1.display()
s2.display()
s1.change_name("deekshi")
s1.display()'''








        

        


