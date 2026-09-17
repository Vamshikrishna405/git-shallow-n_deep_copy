import copy as c
print('SHALLOW COPY IN PYTHON')
a=[[1,2],[3,4]]
b=c.copy(a)
print('this is shallow copy',a,id(a),b,id(b))
print('this is shallow copy',a,id(a[0][0]),b,id(b[0][0]))
a[0][0] = 10
print('this is shallow copy',a,id(a[0][0]),b,id(b[0][0]))

print('DEEP COPY IN PYTHON')

x=[[10,20],[30,40]]
y=c.deepcopy(x)
x[0][0]=100
print(x,id(x),y,id(y))
