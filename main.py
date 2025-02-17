#_*_ coding:utf-8 _*_
#@Description
#@Aythor
#@Copyright
#@version
'''
import turtle
pen1 =turtle.Pen()
pen2=turtle.Pen()
pen1.speed(1)
pen1.width(9)
pen1.color("blue")
pen1.circle(99)
pen1.goto(0,99)
pen2.width(9)
pen2.color("green")
pen2.circle(77)
pen2.goto(0,-99)

pen1.left(2)
pen1.fd(3)
'''
'''
i_i,n,mb= 99, "m" ,0
print(i_i,n,mb)
import keyword
# print("abc" in keyword.kwlist)
print(id(n))
n=0
print(id(n))
'''
"""
phone=110
phone=input("请输入")
print("歪",phone,"吗")
"""
"""
phone1 = 0O11   #8
phone2 = 0X11   #16
# phone=eval(input(phone))
print(phone1,phone2)
#del phone1  #删除变量
import time
start = time.time()
print(2**9999)
print(len(str(2**9999)))
print(time.time()-start)
"""

"""
import sys
print(sys.int_info)
print(sys.float_info)
"""
""""
#n=0.12345678901234567890
#print(n)
import decimal
num1=decimal.Decimal('0.12345678901234567890')
print(num1)
print(num1*num1)
"""
"""
num1="0.123456789012345678901234567890"
import decimal
#保留多少位有效数字
#默认最高十七位精度
num=decimal.Decimal(str(num1))
decimal.getcontext().prec=20
#此行代码打印时不能直接打印变量，必须为代数式
print(num*1)
"""
"""
#N = Ng * Fp * Ne * Fl * Fi * Fc * L
Ng = 24183300   #人口总数
count_male,count_female=12323800,11859500
Fp=count_female/Ng
Ne=(count_female-15000*Fp)/count_female
Fl=20/100/2
Fi=367645/Ng
Fc=0.05
L=0.1
N=Ng*Fp*Ne*Fl*Fc*L
"""
"""
#基本运算符
num1=1111
num2=999
print(num1//num2)
print(num1/num2)
print(num1%num2)
print(num1+num2,num1*num2,num1-num2)
print(10%4,10%-4,-10%4,10**4)
"""
"""
#复合运算符 +=,-=,/=,//=,%=,**=
#python中无++，--，加减只表示正负
#两行之间可以用\连接
print(1-1-1-1-1-1-1\
      -1-1-1-1-1
      )
"""
"""
#数字兑换人民币兑换
#输入钱数
money=eval(input("请输入钱数"))
part_int=int(money)
part_float=(money-part_int)*10
hundred_set=part_int//100
part_int-=hundred_set*100
fifty_set=part_int//50
part_int-=fifty_set*50
twenty_set=part_int//20
part_int-=twenty_set*20
ten_set=part_int//10
part_int-=part_int-ten_set*10
five_set=part_int//5
one_set=part_int-five_set*5
five_cent=part_float//5
one_cent=part_float-five_cent*5
print("一百元\t","五十元\t","二十元\t","十元\t","五元\t","一元\t","五角\t","一角\t")
print(hundred_set,"\t\t",fifty_set,"\t\t",twenty_set,"\t\t",ten_set,"\t\t",five_set,"\t\t",one_set,"\t\t",five_cent,"\t\t",one_cent,"\t\t")
"""
"""
#input()默认返回值为字符串
text=input("请输入")
#输入text=1+1+1+1
print(text)    #输出为1+1+1+1
text=eval(text)
print(text)    #输出为4
"""
#print("\"sda\"",'"j"',"\a")
#print("qwertyuiop\b\b\b\b\b")
#print('qwertyuiop\r123')

#for i in range(99):
#    print("*")
#a="{0}{1}{2}"
#print(a.format(1, 2, 3))
"""
str="0"
print("|{:20}|".format(str))  #左对齐并用空格填充
print("|{:>20}|".format(str)) #右对齐……
print("|{:<20}|".format(str)) #左对齐并用空格填充
print("|{:^20}|".format(str)) #居中
print("|{:->20}|".format(str))#左对齐并用空—填充
print("|{:-<20}|".format(str))#右对齐 —
print("|{:-^20}|".format(str))#居中 —
"""

"""
#python的%

向负无穷取，余数绝对为正数
c=a%b
r=a-c*b
10/3=3......1
r=10-3*3=1

-10/3=-4....2
r=-10-3*-4=2

-9/5=-2...1
r=-9--2*5=1
取余数时余数应负则负
-10/3=-3....-1
......
"""
"""
r=eval(input("Please input the radius of the cricle :"))
if r<0:print("Please input the right radius!!!")
else:print("The area of the circle whose radius is {} is{}".format(r,3.14*r**2))
"""
#import time
#now=time.localtime()
#print( now.tm_year,now.tm_mon,now.tm_mday)


""""
#自主投胎系统
print("\t欢迎进入自助投胎系统!!!")
total_money,
print("\t\t1.开始")
print("\t\t2.结束")
choice=eval(input("\t请输入你的选择："))
if choice==1:
    pass
if choice==2:
    pass
    
    
    
"""
"""
a=0
i=eval(input())
if i==1:
    a=1
print(a)
""""""
import sys
key0=eval(input("使用前请先设置密码（仅支持纯数字）："))
print("请输入需要商品:")
goods_1,goods_2,goods_3=input(),input(),input()
print("请输入各商品的价格与个数")
goods_price1=eval(input("商品一：元\b"))
goods_count1=eval(input("个\b"))
goods_price2=eval(input("商品二：元\b"))
goods_count2=eval(input("个\b"))
goods_price3=eval(input("商品三：元\b"))
goods_count3=eval(input("个\b"))
print("商品：{}\t{}\t{}\t".format(goods_1,goods_2,goods_3))
print("价格：{}\t{}\t{}\t".format(goods_price1,goods_price2,goods_price3))
print("个数：{}\t{}\t{}\t".format(goods_count1,goods_count2,goods_count3))
serive=eval(input("是否需要打折？"
             "（1：需要"
             "2：不需要"
             "3：打骨折）"))
if serive==1:
    print("已打10折")
elif serive==2:
    print("土豪请继续。。。。")
elif serive==3:
    print("来人，拖出去打骨折!!!"
          "(卒)")
    sys.exit()
else :
    print("外星友人，货币不通")
    sys.exit()
choice=eval(input("是否确认订单？（1代表确认|2代表否认）"))
if choice==1:
    key=input("请输入支付密码：")
    if key==key:
        print("支付成功")
        sys.exit()
    else:print("输入密码错误，系统退出")
elif choice==2:
    print("不买起开")
else :
    print("看不懂中国话？")"""
#泽勒公式 h=(q+26(m+1)/10+k+k/4+j/4+5j)%7
"""
import sys
print("请输入日期（分别为年份，月份，这个月中的第几天）：")
sum_year,m_month,q_day=eval(input("年份:")),eval(input("月份:")),eval(input("日期:"))
if m_month>12 or m_month<1 or q_day>31 or q_day<1:
    #sum_year != int or m_month != int or q_day != int
    print("输入错误，请重新开始程序")
    sys.exit()
if sum_year%4!=0 and m_month==2:
    if q_day>28 :
        print("输入错误，请重新开始程序")
        sys.exit()
elif sum_year%4==0 and m_month==2:
    if q_day>29 :
        print("输入错误，请重新开始程序")
        sys.exit()
j_century=sum_year//100
k_year=sum_year%100
if m_month==1 or m_month==2: m_month+=12
#i=q_day+26*(m_month+1)/10
h_weekday=(((q_day+26*(m_month+1)//10+k_year+k_year//4+j_century//4+5*j_century)//1)%7+6)%7
#h_weekday=(h_weekday+6)%7
if h_weekday==1:h_weekday='一'
elif h_weekday==2: h_weekday="二"
elif h_weekday==3: h_weekday="三"
elif h_weekday==4:h_weekday="四"
elif h_weekday==5:h_weekday="五"
elif h_weekday==6:h_weekday="六"
elif h_weekday==0:h_weekday="天"
else :print("系统错误")
print("今天是：{}年{}月{}日 星期{}".format(sum_year,m_month,q_day,h_weekday))
"""
"""
import turtle
i=0
pen1=turtle.Pen()
print("please count in the...(r,x,y)")
radius,circle_center_x,circle_center_y=eval(input("r=")),eval(input("x=")),eval(input("y="))
print("please count in the...(x,y)")
hole_x,hole_y=eval(input("x=")),eval(input("y="))
lf=(circle_center_y-hole_y)**2+(circle_center_x-hole_x)**2
if lf<radius**2 :i=0
elif lf==radius**2 :i=2
else :i=1
pen1.penup()
pen1.goto(circle_center_x,circle_center_y)
pen1.down()
pen1.width(2)
pen1.circle(1)
pen1.penup()
pen1.goto(circle_center_x,circle_center_y-radius)
pen1.down()
pen1.circle(radius)
a=["在圆内","在圆外","在圆上"]
pen1.up()
pen1.goto(hole_x,hole_y)
pen1.down()
pen1.circle(1)
pen1.up()
pen1.goto(circle_center_x,circle_center_y-3*radius)
pen1.down()
pen1.write(a[i])
print("{}".format(a[i]))

#i=4 i_s=math.sqrt(math.pow(i))=2
"""
"""
i=eval(input("请输入数字"))
j=len(str(i))
k=0
while j>0:
    j-=1
    k+=i%10
    i=i//10
print("您输入的数字各个位数之和为：",k)
"""
"""
import pygame
pygame.mixer.init()                                   #进行初始化
music_path="venv/music/Avicii - UMF Ultra.mp3"
pygame.mixer.music.load(music_path.encode("UTF-8"))
#pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1,0)
print("回车键停止播放")
input()
pygame.mixer.music.stop()
"""
'''
p=eval(input("请输入总页数："))
if p%2==0:
    print("您输入的是总偶数页：")
    r=p//2
    l=r+1
    print("这是反面")
    while r>0:
        if r%2==0:
            print(l,",",r,",")
        r -= 1
        l += 1
    print("-"*40,"（我是分割线）")
    r = p // 2
    l = r + 1
    print("这是正面")
    while r > 0:
        if r%2==1:
            print(r,",", l,",")
        r -= 1
        l += 1
else :
    print("您输入的是总奇数页：")
    p+=1
    r = p // 2
    l = r + 1
    print("这是反面")
    while r > 0:
        if r % 2 == 0:
            print(l,",", r,",")
        r -= 1
        l += 1
    print("-"*40,"（我是分割线）")
    r = p // 2
    l = r + 1
    print("这是正面")
    while r > 0:
        if r % 2 == 1:
            if l==p:
                print(r)
            else:print(r,",", l,",")
        r -= 1
        l += 1
print("结束")
'''
"""
#拳皇示例跟打（无音乐包，只有逻辑）
#import winsound  某个声音播放
import pygame
import random
name_player1,name_player2=input("请输入玩家一的名称："),input("请输入玩家二的名称：")
attack=random.random()
i=random.random()
j=random.random()
#print(i,"\n",j)

#mu="venv/music/Avicii - UMF Ultra.mp3"
#pygame.mixer.music.load(mu.encode("UTF-8"))  可以用上述方法写


# pygame.mixer.init()
# mu="venv/music/Avicii - UMF Ultra.mp3".encode("utf-8")
# pygame.mixer.music.load(mu)
# # pygame.mixer.music.set_volume(0.1)
# # pygame.mixer.music.play(-1,0)
# # input("回车以停止播放")
# # pygame.mixer.music.stop()
a=["","","",""]
i=0
print("请选择下列英雄：")
while i<4:
    print("\t{}.{}".format(i,a[i]))
    i+=1
choice_player1,choice_player2=0,0
while choice_player1      choice_player2
    choice_player1=eval(input("请输入{}的选择：").format(name_player1))
    choice_player2=eval(input("请输入{}的选择：").format(name_player2))
"""
"""
列表
lst[0,1,2,3,4,5,6,7,8,9]
"""
#for循环中rang()类
#for i in range(10):
#   print(i)    #[0,10)
#range(0,50,5)    [0,5,10......]
#range(50,0,-5)   [50,45,40....]
#range(1,10)      [1,2,3,4.....] [1,10)
#遍历时使用了iter() 迭代函数
"""
#自制迭代器
class M:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >=self.end:
            raise StopIteration
        result=self.start
        self.start+=1
        return result

M_sumnum=M(0,100)
for element in M_sumnum:
    print(element)
"""
"""
#用for写成的死循环，由于返回值一直未None，所以不多占用内存
class Infinite:    #无限迭代
    def __iter__(self):
        return self
    def __next__(self):
        return None
i=0
for obj in Infinite():
    print(i)
    i+=1
"""
"""
# for 累加
#计算1-10累加
k=0
for i in range(11):
   k+=i
   print(k)
"""
'''
#用for用户输入等差数列求和
a=eval(input("请输入开始数:"))
b=eval(input("请输入结束数:"))
c=eval(input("请输入等差数:"))
if a>b: c=-c
sum=b
for i in range(a,b,c) :
    sum+=i
print(sum)
'''
'''
#打印月历
import sys
l=29
p=eval(input("请输入年份："))
if p%4==0:
    l=l+1
q=eval(input("请输入月份："))
if q<1 or q>12:
    print("输入错误")
    sys.exit()
s=eval(input("请输入这个月的第一天是星期几："))
if s<1 or s>7:
    print("输入错误")
    sys.exit()
a=["一","二","三","四","五","六","天"]
print("{}年{}月的月历为：".format(p,q))
for i in range(7):
    print("星期{}".format(a[i]),end="\t")
print("\n",(s-1)*"\t\t",end="")
if q==1 or q==3 or q==5 or q==7 or q==8 or q==10 or q==12:
    for i in range(1,32):
        if (s+i-2)%7==0:
            print("\n")
        print(i,end="\t\t")
elif q==2:
    for i in range(1,l):
        if (s+i-2)%7==0:
            print("\n")
        print(i,end="\t\t")
else :
    for i in range(1,31):
        if (s+i-2)%7==0:
            print("\n")
        print(i,end="\t\t")
'''
'''
#控制台版进度条
print("开始执行".center(100,"*"))
import time
for i in range(100):
    print("\r","█"*(i),end="")
    time.sleep(1)
'''
'''
#list1=[i for i in range(11) if i%2==0]
#list2=[i for i in range(0,11,2)]

#print(list1,"\n",list2)
#print(55 in list1,55 not in list1)
#print(list1+list2)
#print(list1*4)
###***print(list1-list2)    list不支持减法
#取列表切片
#list1=[i for i in range(11)]
#print(list1[3])   #取出单个元素
#print(list1[3:5]) #取出片段
#print(list1[-3])  #python中元素下标可以是负数
#print(list1[-9:-1])   #负数即为长度加上这个负数的下标
###***print(list1[-12]) #可以是负数但是绝对值不能大于长度
#列表求和，最大值，最小值
list1=[i for i in range(11)]
print("sum:",sum(list1))
import random
random.shuffle(list1)  #乱序函数
print("乱序后：",list1)
print("max:",max(list1),"min:",min(list1))
print("平均值",sum(list1)/len(list1))
'''
'''
#列表比较
list1=[1,3,1]
list2=[1,3,1]
list3=[2,2,4]
print(list1>list2,list1>list3,list2>list3)
'''
"""
list1=[]
list1.append(1)
print(list1)
list2=[2]
list1.extend(list2)
print(list2)
print(list1,"    ",list2)
list1.extend(list1)
print(list1.count(1)) #数有几个1
print(list1.index(1)) #
#insert 若超出则插入最后
list1.insert(2,999)
print(list1)
#pop 下标越界会报错 提取
p=list1.pop(2)
print(p,list1)
#remove 删除第一次出现的数
list1.remove(1)
print(list1)
#reverse 反转
list1.reverse()
print(list1)
list1.sort() #排序
print(list1)
#将字符串分成列表
list3="qw,er,t,y,u".split(",")
print(list3)
#录入，一次性接受
ui =input("请输入多个数字并用空格隔开")
list_ui=ui.split(" ")
list_ui2=[eval(x) for x in list_ui]
print(list_ui2)
"""
'''
#洗牌程序
import random
list0=[x for x in range(0,54)]
for i in range(0,54):
    if i==52:
        list0.insert(list0.pop(i),"大王")
        continue
    elif i == 53:
        list0.insert(list0.pop(i), "小王")
        continue
    else :
        if i//4==0:
            list0.insert(list0.pop(i), "A")
        elif i//4==11:
            list0.insert(list0.pop(i), "J")
        elif i//4==12:
            list0.insert(list0.pop(i), "Q")
        elif i//4==13:
            list0.insert(list0.pop(i), "K")
        else:
            list0.insert(list0.pop(i), str(int(i)//4))
    temprorary=str(list0[i])
    if i%4==0:
        #temprorary="{}{}".format("红桃", temprorary)
        #list0.insert(list0.pop(i),temprorary)
        list0[i]="{}{}".format("红桃", temprorary)
    elif i%4==1:
        #list0.insert(list0.pop(i), "{}{}".format("方片",temprorary))
        list0[i] = "{}{}".format("方片", temprorary)
    elif i%4==2:
        #list0.insert(list0.pop(i), "{}{}".format('黑桃',temprorary))
        list0[i] = "{}{}".format("黑桃", temprorary)
    else:
        #list0.insert(list0.pop(i), "{}{}".format("梅花",temprorary))
        list0[i] = "{}{}".format("梅花", temprorary)
random.shuffle(list0)
list1,list2,list3=[],[],[]
for i in range(0,18):
    list1.append(list0[i])
for i in range(18,36):
    list2.append(list0[i])
for i in range(36, 54):
    list3.append(list0[i])
print("\n",len(list1),"\n",len(list2),"\n",len(list3))
print("\n",list1,"\n",list2,"\n",list3)
'''
'''
import xpinyin
h=""
pingyin=xpinyin.Pinyin()
print(pingyin.get_pinyin(h))
'''
'''
#二维列表
list0=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range(len(list0)):
    for j in range(len(list0[i])):
        print(list0[i][j],end=" ")
'''
'''
#五子棋
d=0
# for kl in range(10):
#     d+=1
#     x,y=eval(input("请输入落子位置：(以左上角为原点,x坐标)")),eval(input("请输入落子位置：(以左上角为原点,y坐标)"))
#     if 0<x<18 and 0<y<18:
#         print("您的落子位置为（{}，{}）".format(x,y))
import sys
list0=[]
for i in range(19):
    list0.append([])
    for j in range(19):
        if i==0 and j==0 :
            list0[i].append("┏")
        elif i==0 and j==18:
            list0[i].append("┓")
        elif i==18 and j==0:
            list0[i].append("┗")
        elif i==18 and j==18:
            list0[i].append("┛")
        elif i==0 or i==18 :
            list0[i].append("━")
        elif j==0 or j==18:
            list0[i].append("┃")
        else:
            list0[i].append("╋")
for kl in range(99):
    d += 1
    x, y = eval(input("请输入落子位置：(以左上角为原点,x坐标)")), eval(input("请输入落子位置：(以左上角为原点,y坐标)"))
    if 0 < x < 18 and 0 < y < 18:
        print("您的落子位置为（{}，{}）".format(x, y))
    if d%2==0:
        if list0[x][y] =="╋":
            list0[x][y]="●"
        else :print("落子失败")
    if d%2==1:
        if list0[x][y] =="╋":
            list0[x][y]="○"
        else :print("落子失败")
    for i in range(19):
        for j in range(19):
            print(list0[i][j], end=" ")
        print("")
    for i in range(19):
            for j in range(19):
                if list0[i][j]=="●" or list0[i][j]=="○":
                    if list0[i][j]==list0[i][j+1]==list0[i][j+2]==list0[i][j+3]==list0[i][j+4] or list0[i][j]==list0[i+1][j]==list0[i+2][j]==list0[i+3][j]==list0[i+4][j] or list0[i][j] == list0[i + 1][j + 1] == list0[i + 2][j + 2] == list0[i + 3][j + 3] == list0[i + 4][j + 4] :
                        print("恭喜胜利")
                        if list0[i][j] == list0[i + 1][j + 1] == list0[i + 2][j + 2] == list0[i + 3][j + 3] == list0[i + 4][j + 4]:
                            list0[i][j] =list0[i + 1][j + 1] = list0[i + 2][j + 2] = list0[i + 3][j + 3] = list0[i + 4][j + 4]="╋"
                        elif list0[i][j]==list0[i+1][j]==list0[i+2][j]==list0[i+3][j]==list0[i+4][j]:
                            list0[i][j] =list0[i + 1][j] = list0[i + 2][j] = list0[i + 3][j] = list0[i + 4][j]="╋"
                        elif list0[i][j]==list0[i][j+1]==list0[i][j+2]==list0[i][j+3]==list0[i][j+4] :
                            list0[i][j] = list0[i][j + 1]= list0[i][j + 2] = list0[i][j + 3] = list0[i][j + 4]="╋"
                        con=input("请问是否继续（y/n）")
                        if con=="n":
                            sys.exit()
    # for i in range(19):
    #     for j in range(19):
    #         print(list0[i][j],end=" ")
    #     print("")
    '''
'''
def a(k):
    print("*"*k)
    if k==0:
      print(k)
k=eval(input())
if __name__=="__main__":
    a(k)
'''
'''
list0=[12,3,4,5,7,97]
print(sum(list0,9))
print("round(4.4)(4.5)(5.5)",round(4.4),round(4.5),round(5.5))
#round(x.5)时趋于偶数 取近似值
#sum求和
print("ord  ASCLL码打印(i对应的“",ord("i"))
print("chr  65对应字符",chr(65))
print("bin 二进制转换 3=",bin(3))
print("oct 八进制转换 9=",oct(9))
print("hex 十六进制转换 17=",hex(17))

'''
"""
import math
print(math.ceil(99.8))
print(math.floor(99.8))
print(math.fabs(-998.98))
"""


'''
#计算三角形面积
#计算角度
#A=acos((a*a-b*b-c*c)/(-2*b*c)
#B=acos((b*b-a*a-c*c)/(-2*a*c)
#C=acos((c*c-b*b-a*a)/(-2*b*a)
#海伦公式。。。。。。
import math
x1,y1=1,0
x2,y2=-1,0
x3,y3=0,2
l12=math.sqrt(pow(math.fabs(x1-x2),2)+pow(math.sqrt(y1-y2),2))
l23=math.sqrt(pow(math.fabs(x2-x3),2)+pow(math.sqrt(y1-y2),2))
l13=math.sqrt(pow(math.fabs(x1-x3),2)+pow(math.sqrt(y1-y3),2))
'''
'''
#exec 执行字符串语句
exec("i=0")
print(i)
#执行不会报
#global()访问当前全局变量
#locals（）返回局部变量
'''
'''
def p(o):
    o+=999
    print(o)
    return
#return 终止程序，交还控制权(转换流）
def k(x,y):
    sum=x+y
    y+=7
    sum0=x+y
    return sum,sum0
o=2
k(1,o)
p(o)
print(o,k(1,o))
#参数在经过函数进行过程变化，不进行最终变化
#即形式参数取实际参数的内存地址副本
def text():
    pass
#pass不作任何事情结束函数
'''
"""
#元组（tuple）的创建访问与删除
#1.与列表相似，元组的元素不可改变
#2.元组用小括号
#3.元组不可变，列表可变
tuple1=tuple((1,2,4))
print(type(tuple1),tuple1)
print(tuple1[1])
#下标不可越界
#长度固定，访问速度快
#tuole2=(100)  错误
tuple2=(100,)  #正确
#用推倒式定义
tuple3=(k for k in range(1,10))
#打印时不会打印元素而是打印对象
#因为还没有调用所以未被生成
#更省效率
print(tuple3)
#访问
for i in tuple3:
    print(i)
"""
"""
#返回值单个拆分接受，接受时要与返回个数一致
e=1
def m(e):
    return e,e+1,e+2
a,b,c=m(1)
print(a,b,c)
"""
'''
#位置参数和命名关键字参数
def k(x,y,z):
    for i in range(y):
        print(x*z)
k(y=5,x="gun",z=1) #命名关键字参数 好处：调用可以更改顺序
k("gun",5,1) #位置参数
k("gun",z=1,y=5) #可以混用 但位置必须在命名前面用
'''
"""
import time
#模拟喊话功能
def yell(name,channel,messsage,times,interval):
    for i in range(times):
        sum1=str.format("[{}]{}:{}".format(channel,name,messsage))
        print(sum1)
        time.sleep(interval)
        return sum1
yell("我","世界",".....",10,100)
"""
'''
#可变参数
def get_sum(*nums):
    result=0
    for num in nums:
        result+=num
    return result
print(get_sum(12,234,23456,2345))

'''
'''
#不可变类型 int float string number tuple（元组）
#不可变对象的值不变，引用变了
a=1
print(id(a))
a=2
print(id(a))
a=1
print(id(a))
#第一次和第二次的地址不一样，第一次和第三次的地址一样，说明后方为对象
'''
'''
#可变类型 列表 字典 集合 自定义类型
list1=[1,2,3]
print(id(list1))
list1[0]=99
print(id(list1))
list1[0]=1
print(id(list1))
#三次list1的地址都没有变，但是若打印元素的地址却会变
'''
'''
#默认参数
def o(a,b=9):
    print(a*b)
o("a",99)
o("a")
'''
'''
from mybag import text
#import mybag.text as text
#from mybag import *
if __name__ == '__main__':
    text.repeat()
'''
'''
import printer
printer.printer()
'''
"""
class a:
    def __init__(self,name,sex,job):
#_init_初始化程序
        self.name=name
        self.sex=sex
        self.job=job
    def eat(self):
        pass
    def perfoms(self):
        pass
"""
'''
class weapon:
    def __init__(self,name,intro,power,type):
        self.name=name
        self.intro=intro
        self.power=power
        self.type=type
    def show(self):
        formatter="名称:{}\n说明:{}\n威力:{}\n类型:{}"
        print(formatter.format(self.name,self.intro,self.power*"★",self.type))
if __name__ == '__main__':
    weapon1=weapon(" hh","ga",3,"af")
    weapon1.show()
'''
'''
import turtle
import math
class circle:
    def __init__(self,r,color,fill_color,x,y):
        self.r=r
        self.color=color
        self.fill_color=fill_color
        self.x=x
        self.y=y
    def area(self):
        return math.pi*math.pow(self.r,2)
    def c(self):
        return math.pi*2*self.r
    def show(self):
        formatter="圆心：({},{})\n半径：{}\n周长：{:.2f}\n面积：{:.2f}\n边框颜色：{}\n填充颜色：{}"
        pr=formatter.format(self.x,self.y,self.r,self.c(),self.area(),self.color,self.fill_color)
        return pr
    def show2(self):
        turtle.setup(800,600)
        turtle.title("画圆")
        p=turtle.Pen()
        p.up()
        p.goto(self.x,0.5*self.y)
        p.down()
        p.color(self.color)
        p.fillcolor(self.fill_color)
        p.begin_fill()
        p.circle(self.r)
        p.end_fill()
        p.up()
        p.goto(0,-200)
        p.color("black")
        p.write(self.show())
        turtle.done()
if __name__ == '__main__':
    k=circle(90,"red","black",0,0)
    k.show()
    k.show2()
'''
'''
class role:
    def __init__(self,name,sex,age):
        self.name=name
        self.__sex=sex  #双下划线为私有
        self._age=age   #一个下划线为受保护 可以被普通访问
    def printter(self):
        print(self.name,self.__sex)
if __name__ == '__main__':
    role1=role("k",1,2)
    print(role1.name)     #可访问公有
#    print(role1.__sex)   #不可访问私有
    role.printter(role1)
    print(role1._age)
    #内部访问私有
#其他方式访问私有
    print(role1._role__sex)  #不从内部也可以访问
'''
'''
#玩家类
class Player:
    def __init__(self,id,name):
        self.__id=id
        self.__name=name
        self.cash_lv=0
        self.lv=0
        self.bi=0
        self.cash=0
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def recharge(self):
        money=input("请输入充值金额：")
        money=int(money)
        if money<1:
            print("充值金额不能小于一")
            return
        else:
            self.cash+=money
            self.bi+=money*100
            return
    def get_cash_lv(self):
        l=self.cash
        if l>0:
            self.cash_lv=1
            while l//10>1:
                self.cash_lv+=1
                l=l//10
            print("您现在的充值等级是：",self.cash_lv)
        else: print("当前未充值")
    def __str__(self):
        content="id:{}\t|name:{}\t|"
        return content.format(self.__id,self.__name)
if __name__ == '__main__':
    player1=Player(1,"hh")
    player1.recharge()
    player1.get_cash_lv()
    print(player1)
'''
'''
class actor:
    def __init__(self,name,age=0):
        self.name=name
        self.age=age
    def age_increase(self):
        days=eval(input("请输入度过天数："))
        if days>0:
            self.age=1
            self.age+=days//365
            return
        else:
            print("抱歉，还未出生")
            return
    def __str__(self):
        context="|name:{}\n|age:{}"
        return context.format(self.name,self.age)
    #比较两个对象中的元素 若无此函数则对比内存，一定不相等
    def __eq__(self, other):
        if self.name==other.name:
            return "相等"
        else: return "不相等"'''
#该类已写入text
'''
from mybag.text import actor #从其他包里调出类
from math import pi          #同此
import printer
if __name__ == '__main__':
    a=actor("wo")
    b=actor("ni")
    b.age_increase()
    print("a:",a)
    print("b:",b)
    c=actor("wo")
    print(c==a)
            # #列表操作对象
            # actor_list=[
            #     actor("c"),
            #     actor("d")
            # ]
            # for actor in actor_list:
            #     actor.age_increase()
            #     print(actor)
'''
'''
str1="h123456H"
print(str1.isalnum())
#isalname  判断是否纯数字字母组合

print(str1.isalpha())
#isalpha   判断是很纯字母

print(str1.isdigit())
#判断字符串是纯数字，包含全角数字，（1），```

print(str1.isdecimal())
#纯数字
#推荐使用

print(str1.isnumeric())
#支持中文数字``````

print(str1.isdentifier())
#判断是否是合法的

print(str1.isspace())
print(str1.isupper())
print(str1.islower())
'''
"""
#验证年龄的合法性
age=""
while not age.isdecimal() or 0>int(age) or int(age)>100:
    age=input()
print("f",age)
"""
'''
#判断字符串是否纯中文     unicode  4E00--9FFF 为中文
k=input()
if not len(k):
    print("f")
else:
    for char in k:
        if not"\u4e00"<="\u9fff":
            print("f")
        else:print("s")
'''
'''
#实现用户名登陆
user_list=[]
class user:
    def __init__(self,keyword,password):
        self.keyword=keyword
        self.password=password
    #def __str__(self):
    #    result=
    # #     return
    # def get_keyword(self):
    #   result="{}".format(self.keyword)
    #   return result
    #     #return self.keyword
    # def get_password(self):
    #     result = "{}".format(self.password)
    #     return result

       # return self.password
def vuce():
    k=(input("请输入用户名和密码\n用户名："))
    p=(input("密码："))
    user_list.append(user(k,p))
    o = len(user_list)
    print("你为第{}个用户".format(o))
    k2=user_list[o-1].keyword
    p2=user_list[o-1].password
    print("您的用户名为：{}\n密码为：{}".format(k2,p2))
def dglu():
    k = input("请输入用户名和密码\n用户名：")
    p = input("密码：")
    in_user=user(k,p)
    for i in range(len(user_list)):
        if k==user_list[i].keyword:
            if p==user_list[i].password:
                print("登陆成功")
            else:
                print("密码或用户名错误，请重新登陆")
            return
        else:
            print("该用户还未注册，请重新注册或登陆")
            return
if __name__ == '__main__':
    choice=""
    while choice!="n":
        choice=eval(input("欢迎来到XXX登录系统\n请选择登陆或注册\n1.登陆\n2.注册\n3.退出（输入n）"))
        if choice==1:
            dglu()
            continue
        elif choice==2:
            vuce()
            continue
'''
'''
#判断合法性
valid_symbols = [str(value) for value in range(ord("A"), ord("Z") + 1)]

def validate_login_name(login_name):
    str_len=len(login_name)
    if str_len>25 or str_len==0:
        return False
    invalid_chars=" !@#$%^&*()_+-="
    for char in login_name:
        if char in invalid_chars:
            return False
    return True
def validate_password(password):
    str_len=len(password)
    if str_len<6 or str_len>18:
        return False
if __name__ == '__main__':
    login_name=input()
    print(validate_login_name(login_name))
'''
'''
#运算符重载
class M:
    def __init__(self,data=0):
        self.data=data
    def __add__(self, other):
        return M(self.data-other.data)
    def __str__(self):
        return str(self.data)
    #def __repr__(self):
    #并存默认用str
    #repr 转换为解释器可读
    #str 转换为用户可读
    def
if __name__ == '__main__':
    a=M(12)
    b=M(1)
    print(a+b)
'''
'''
#自定义列表类
class Mylist:
    def __init__(self,data=None):
        self.data=None
        if data is None:
            self.data=[]
        else:
            self.data=data
    def __getitem__(self, index):
        return self.data[index]
    #让自定义列表类可以通过下标访问
    def __setitem__(self, index, value):
        self.data[index]=value
    #让自定义列表可以通过下标赋值
    def __contains__(self, item):
        return self.data.__contains__(item)
    #判断某元素是否在列表中
    #也可以直接用 item in list来判断
    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    my_list=Mylist([1,2,3,4])
    my_list[0]=1234
    print(my_list[0])
'''
'''
#自定义矩阵
class M:
    def __init__(self,data=None):
        self.__data=None
        if data is None:
            self.__data=[]
        else:
            self.__data=data
    def __getitem__(self,index):
        return self.__data[index]
    def __add__(self, other):
        result=[]
        for i in range(len(self.__data)):
            result.append([])
            for j in range(len(self.__data[i])):
                result[i].append(self[i][j]+other[i][j])
        return M(result)
    def __str__(self):
        content="["
        for item in self.__data:
            content+="\n\t["
            for element in item:
                content+=str(element)+", "
            content=content[0:-2]
            content+="],"
        content+="\b\n]"
        return content

import numpy
if __name__ == '__main__':
    # m1=M([[1,2,3],[1,2,3]])
    # m2=M([[1,2,3],[1,2,3]])
    # m3=m1+m2
    # print(m3)
    m1=numpy.mat("1 2 3;1 2 3")
    m2=numpy.mat([[1,2,3],[1,2,3]])
    print(m1+m2)
    m3=numpy.mat(numpy.random.randint(2,10,size=(3,3)))
    print(m3)
'''
'''
import ctypes
class DynamicArray:
    def __init__(self,capacity=16):
        self._length=0
        self._capacity=capacity
        self._elements=None
        self._elements=self.___make_array(self._capacity)
    def ___make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    def __getitem__(self, item):
        if 0<=item<self._length:
            return self._elements[item]
        else:
            raise IndexError("数组下标越界")
    def __setitem__(self, item,value):
        if 0 <= item < self._length:
           self._elements[item]=value
        else:
            raise IndexError("数组下标越界")
    def append(self,element):
        if self._length==self._capacity:
            self._capacity*=2
            self.__resize(self._capacity)
        self._elements[self._length]=element
        self._length+=1
    def get_capacity(self):
        return self._capacity
    def __str__(self):
        content="【"
        for element in range(self._length):
            content+=str(self._elements[element])+", "
        content=content[0:-2]+"】"
        return content
    def __resize(self,new_capacity):
        new_array=self.___make_array(new_capacity)
        for i in range(self._length):
            new_array[i]=self._elements[i]
        del self._elements
        self._elements=new_array
    def __len__(self):
        return self._length
    def find(self,element):
        for i in range(self._length):
            if self._elements[i]==element:
                return i
        return -1
    def remove(self,element):
        remove_index=self.find(element)
        if remove_index==-1:
            print("未找到")
            return
        else:
            for i in range(self._length-remove_index-1):
                self._elements[remove_index+i]=self._elements[remove_index+1+i]
            self._elements[self._length-1]=None
            self._length-=1
            #print("删除后：{}".format(self._elements))
    def insert(self,index,value):
        if index>self._length-1:
            print("下标越界")
            return
        else:
            if self._length == self._capacity:
                self._capacity *= 2
                self.__resize(self._capacity)
            for i in range(self._length-index):
                self._elements[self._length-i]=self._elements[self._length-i-1]
            self._elements[index]=value
            self._length+=1
            # tempy=self._elements[index+1]
            # self._elements[index+1]=self._elements[index]
    def sort(self):
        for i in range(self._length-1):
            j=0
            while self._elements[j+i]>=self._elements[j+i+1] and j+i+1<=self._length-1:
                temple=self._elements[j+i]
                self._elements[j+i]=self._elements[j+i+1]
                self._elements[j+i+1]=temple
                if j+i+1==self._length-1:
                    return
                j+=1
if __name__ == '__main__':
    a=DynamicArray()
    #不可以用来赋初值 a[1]=13
    for i in range(16):
        a.append(i)
    print(a)
    print(len(a))
    print(a.get_capacity())
    # a.remove(9)
    # a.remove(3)
    print(a)
    print(len(a))
    print(a.get_capacity())
    a.insert(3,123)
    print(a)
    print(len(a))
    print(a.get_capacity())
    a.sort()
    print(a)
    print(len(a))
    print(a.get_capacity())
'''
'''
#继承到实现
class Hero:
    def __init__(self,nick_name,level=1,max_life=100,curr_life=100):
        self.__nick_name=nick_name
        self.__level=0
        self.set_level(level)
        self.__max_life=max_life
        self.__curr_life=curr_life
    def __str__(self):
        content="{}\t{}\t{}\t{}".format(self.__nick_name,self.__level,self.__max_life,self.__curr_life)
        return content
    def get_nick_name(self):
        return self.__nick_name
    def move(self):
        print(self.__nick_name+"走")
    def set_level(self,level):
        if level<0 or level>999:
            level=1
        self.__level=level
    def get_level(self):
        return self.__level
class Warrior(Hero):
    def __init__(self,nick_name,level=1,max_life=100,curr_life=100):
        super().__init__(nick_name,level,max_life,curr_life)
        self.__physics_attack=1
    def __str__(self):
        return super().__str__()+"\t"+str(self.__physics_attack)
    def move(self):
        print(self.get_nick_name()+"爬")
if __name__ == '__main__':
    hero1=Hero("测试英雄")
    print(hero1)
    hero1.move()
    warrior1=Warrior("测试战士")
    print(warrior1)
    warrior1.move()
'''
'''
#Object类 所有类到子类
class Hero:
    def __new__(cls, *args, **kwargs):
    #必须有返回值
        print("new")
    def __init__(self):
        print("init")
if __name__ == '__main__':
    hero1=Hero()
    '''
'''
#实现单例模式 通过重写new实现单例

class Singleton:
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls,"_me"):
    #         setattr(cls,"_me",object.__new__(Singleton))
    #         cls._me=super().__new__(Singleton)
    #     return cls._me
    def __init__(self,n):
        self.n=n

     
        setattr(self,"k", 7)  #貌似找到了自动定义变量的方法
        print(self.k)
if __name__ == '__main__':
    a=Singleton(345)
    print(a.k)
'''
'''
#星际争霸 指挥官互动
import time
import random
total_value=0   #总资产

class BattleUnit:
    def __init__(self,name,**kwarges):
        self.name=name
        self.hp=100
        self.attack=0
        self.kwarges=kwarges
        for key,value in kwarges.items():
            setattr(self,key,value)
    def __str__(self):
        content=self.name
        for key,value in self.kwarges.items():
            content+="\t"+str(key)+":"+str(value)
        return content
    def fight(self,battle_unit):
        if not isinstance(battle_unit,BattleUnit):
            print("无法攻击")
            return
        attack=random.randint(1,self.attack)
        battle_unit.hp-=attack
        print(self.name+"攻击"+battle_unit.name+"打掉了{}滴血".format(attack))
        return
#以上为父类
class SCV(BattleUnit):
    #挖矿修理单位
    def __init__(self,name,**kwarges):
        super().__init__(name,**kwarges)
        self.__make_value=10
        self.__hp_increase=2
    def fight(self,battle_unit):
        print("SCV对于攻击一窍不通，只能用拳头捶")
        battle_unit.hp-=1
        print(battle_unit.name+"几乎没有感觉")
    def mining(self):
        global total_value
        print("采矿~~~","(自动采矿10s)","每秒采矿{}金".format(self.__make_value))
        for i in range(1,10):
            total_value+=10
    def repair(self,repair_unit):
        total_time=0
        print(self.name+"正在修理"+repair_unit+"~~~~~~")
        while repair_unit.hp<=100:
            repair_unit.hp+=10
            time.sleep(2)
            total_time+=self.__hp_increase
        if repair_unit.hp>=100:
            repair_unit.hp=100
            print(repair_unit.name+"已修理完成，总耗时："+str(total_time)+'s')
        print("-"*40)
#以上为子类1
class Marine(BattleUnit):
    def __init__(self,name,**kwargs):
        super(Marine, self).__init__(name,**kwargs)

######
if __name__ == '__main__':
    b=SCV("sav1")
    c=SCV("scv2")
    b.mining()
    print(total_value)
    '''
'''
import os
 file_path=r"D:\Apps\python pycharm 编译器\PyCharm Community Edition 2020.2.1\project\project1\TEXT"
file=open( file_path,"r")
print(file.read())
file.close()
file_path= file_path.replace("/",os.sep) #让代码兼容程序  os

with open( file_path,"r") as file:
    #用with打开的文件不需要手动close
    #会自动调用
    print(file.read())
''''''
import os
#中文文件名打开
#file_path="D:\Apps\python pycharm 编译器\PyCharm Community Edition 2020.2.1\project\project1\哈哈"
file_path="哈哈"
#if not os.path.isfile(file_path): #判断是否为文件
if not os.path.exists(file_path): #判断文件是否存在
    print("文件不存在")
else:
    with open(file_path,"r",encoding="utf_8") as file:
        #print(file.read())    #读取后指针不会重置
        #print(file.read(10))  #只读取10个字符
        #print(file.readline()) #读取当前行
        #print(file.readlines()) #读取剩余行，以list形式返回
        #用readline 实现readlines
        # line=file.readline()
        # while line:
        #     print(line,end="")
        #     line=file.readline()
        '''
'''
#text 指针不重置性
file_path="哈哈"
with open(file_path, "r", encoding="utf_8") as file:
    print(file.read(10))
    for text in file.readlines():
        print(text)
#并没有重复打印，而且同一行可以分开，说明字符指针不会重置
'''
'''
#os模块
import os

print("当前操作系统名称：",os.name)
print("环境变量path：",os.getenv("path"))
print("获得当前工作目录：",os.getcwd())
print("当前目录下的所有目录和文件：",os.listdir())
folder_path="c:\\windows"
file_list=os.listdir(folder_path)  #获得某路径下的文件和文件夹
file_count = 0
folder_count = 0
for file_name in file_list:
    #full_name=folder_path+"\\"+file_name   #不兼容方法
    full_path=os.path.join(folder_path,file_name)   #兼容方法
    print(full_path)
    if os.path.isfile(full_path):
        file_count+=1
    else:
        folder_count+=1
print("文件夹数：{}\n文件数：{}".format(folder_count,file_count))
print(file_list)
'''
'''
import os
#创建文件
k="awrewetryjy"
k1=open(k,"w")
# k1_in=input()
# k1.write(k1_in)
k1.close()
# k2=open(k,"r")
# print(k2.readline())
# k2.close()
#文件删除
os.remove(k)
#创建文件夹
if os.path.exists("hdewfr"):
    os.rmdir("hdewfr") #删除文件夹
    print("已删除")
else:
    os.mkdir("hdewfr")  #新建文件夹
    print("已新建")
os.rmdir("hdewfr")  #新建文件夹
print("已删除")
'''
'''
#查找文件的目录
import os
i=open("qet","w")
print(os.path.abspath("qet"))
i.close()
os.remove("qet")

 '''
# #分割字符串：
# rstrip()  #删除字符串末尾的\n
# line="tuyhi opgy 0u90gyhj guyhj"
# item_list=line.split(" ")#(中间填分割字符串的方式)
# item_list=list(filter(None,item_list))  #过滤列表中的东西仅能过滤空

'''
#异常处理
try:
    a,b=input("please put two numbers in it")
    result=a/b
    print(result)
except:  #中间可填异常类型 如 except “error” as “某名称”:~~~~~
    print("123456790")
else:
    print("congradulate")
finally:
    print("finash")
'''
#
        #import  traceback
#traceback.print_exc()   打印出异常栈信息
#traceback.format_exc()   以字符串返回
        #import sys
# exc_type,exc_value,exc_tracebake=sys.exc_info()  #用三个变量来记录sys返回到错误  分别为类型 信息 行数位置返回为元组类型
# curr_traceback=traceback.extract_tb(exc_tracebake)
# for file_name,line_name,func_name,source in curr_traceback:
#     print("第{}行，{}->{} 所在源文件{}".format(line_name,func_name,source,file_name))
#这些应写在except下
'''
#自定义异常
class Hero:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def set_health(self,health):
        if health<0:                                #判断是否异常
            raise myerror1("health can not < 0")    #抛出异常
# 以下为自定义异常名称
class myerror1(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.mag=msg
        #msg为错误提示
#调用：
if __name__ == '__main__':
    # try:
    #     raise myerror1("afgh") #括号内为抛出异常的信息
    # except myerror1 as uyt:
    #     print(uyt)
    try:
        hero1 = Hero("测试", -50)
        hero1.set_health(hero1.health)      #若只传入变量而不调用已写好的判断error的函数 则不会抛出错误
    except myerror1 as k:                    #接收异常，处理异常
        print(k)                             #这样打印出来是白色字
        #raise myerror1("health can not < 0") # 若直接抛出则打印出红色字
    finally:
        print("end")
    print("\“efghthgrhyu\"")    #自定义异常处理后仍可以运行后面的代码，与一般异常一样  若未写except则会执行finally里的代码 而不执行后续代码 
'''
'''
#日志处理
import logging,os
#日志的常见级别：CRITICAL(严重的)》ERROR>WARNING>INFO>DEBUG
logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log.txt",
    filemode="a",
    format="%(asctime)s - %(name)s - %(filename)s [line:%(lineno)d] - %(levelname)s - %(message)s"
)
logging.debug("普通测试信息")
logging.info("普通日志消息")
logging.warning("警告信息")
logging.error("错误信息")
logging.critical("严重错误信息")
'''
'''
#爬虫
#import fake_useragent
#import requests
#import xpath
from lxml import html
import requests
from fake_useragent import UserAgent #此库中可以进行随机请求头访问，防止爬时被某网站禁止
url="https://www.baidu.com/"
#可能会遇到反爬程序，可通过添加浏览器请求头来访问
# headers={"user-agent":""}   #此为字典类型
#使用fake_useragent来代替headers
user_agent=UserAgent()
headers={"user-agent":user_agent.random}
#print("随机浏览器头",user_agent.random)
#print("指定浏览器头",user_agent.firefox)   #firefox可改为其他浏览器名称
response=requests.get(url,headers=headers)
print(response.status_code)  #打印出网址为url的网站 访问状态码
#如果编码不一样还需要进行转码
html_str=response.text
print(html_str)             #打印出网站内容，即源码
#html_str=str(html_str.encode("iso-8859-1"),encoding="utf-8")
#iso-8858-1为基础编码，先将原代码转为基础编码，再用基础编码转为网站编码

# #接下来解析 lxml 中html
etree=html.etree
html_obj=etree.HTML(html_str)
ul_news_top_a=html_obj.xpath("//*[@id='lm-new']/a/span")   #获得需解析的url对象
print(ul_news_top_a[0].text)   #""中间填入xpath码
# for a in ul_news_top_a:
#     print(a.text)
'''


















