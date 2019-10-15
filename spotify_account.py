import os
file_object = open('spotify.txt', mode = 'a+')
x = file_object.read()
print(type(x))
lst_x = [i for i in x.split("<tr>")]
#print(lst_x)
lst_x.remove(lst_x[0])
print(lst_x[0])
print(lst_x[1])
			# a = lst_x[0].split("<td>Premium-Other</td><td>")
			# print(a)
			# b = ''.join(a)
			# b = b.split("</td><td>")
			# print(b)
			# print(b[0])
			# b[0]=b[0].split(":")
			# print(b[0])
			# print(b[0][1])
			# c = b[0][1]
			# c = c.split('"')
			# print(c)
			# d = b[2]
			# d = d.split("</td></tr>")
			# print(c[0],b[0][2],b[1],d[0])
			# z = c[0] +':'+ b[0][2]+ '\n' + b[1] +'\n' + 'Day:'+ d[0]
			# print(z)
			# print(type(z))
# print(lst_x[0].strip("<td>Premium-Other</td><td>"))
lst_y = [] # username and passwords
lst_z = [] # all information
for i in lst_x:
	a = i.strip("<td>Premium-Other</td><td>") #<a href="mailto:cari1712@hotmail.com">cari1712@hotmail.com</a>:carinucha</td><td>Cntry: AR</td><td>15.09.2019 16:13:28</td></tr>
	a = a.split("</td><td>") #['<a href="mailto:cari1712@hotmail.com">cari1712@hotmail.com</a>:carinucha', 'Cntry: AR', '15.09.2019 16:13:28</td></tr>']
	b = a[0] #'<a href="mailto:cari1712@hotmail.com">cari1712@hotmail.com</a>:carinucha'
	b = b.split(":") # ['<a href="mailto','cari1712@hotmail.com">cari1712@hotmail.com</a>','carinucha']
	c = b[1].split('"') # b[1] = 'cari1712@hotmail.com">cari1712@hotmail.com</a>' to ['cari1712@hotmail.com','>cari1712@hotmail.com</a>']
	a[2] = a[2].strip("</td></tr>") # '15.09.2019 16:13:28</td></tr>'
	a[2] = a[2].strip("</td></tr></tabl")
	z = c[0]+':'+b[2]
	y = c[0]+':'+b[2] + '||' + a[1] + '||' + a[2]
	lst_y.append(z)
	lst_z.append(y)
print('-----------------------------')
print(lst_y)
file_object.close()
file_new = open('user_pass.txt',mode = 'w+')
for i in lst_y:
	file_new.write(i)
	file_new.write('\n')
file_new.close()
file_info = open('information_spotify.txt',mode = 'w+')
for i in lst_z:
	file_info.write(i)
	file_info.write('\n')
file_info.close()