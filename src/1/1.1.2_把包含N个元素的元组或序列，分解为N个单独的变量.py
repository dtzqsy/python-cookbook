# 前提是，待分解的对象必须是可迭代对象

p = (4,5)
x,y = p
print(x)
print(y)


data = ['ACME',50,91.1,(2012,12,21)]
name,shares,price,date =data
print(name)
print(date)


name,shares,price,(year,mon,day) = data   # 重点
print('')
print('日期为：{}年-{}月-{}日'.format(year,mon,day))


s = 'hello'
a,b,c,d,e = s   # 拆分字符串
print(d)

data = ['ACME',50,91.1,(2012,12,21)]
_,shares,price,_ = data  # 用"_"来代表无用的变量名
print(price)
