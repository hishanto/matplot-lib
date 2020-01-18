import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [7, 4, 6]
x1= [1, 2, 3]
y2= [7, 6, 4]
plt.plot(x,y, label='Frist line')
plt.plot(x1,y2, label='Second line')

plt.xlabel('x asis ')
plt.ylabel('y asis ')
plt.title('matplot graph')

plt.legend()
plt.show()


