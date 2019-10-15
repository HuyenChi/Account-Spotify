import os
file_object = open('spotify.txt', mode = 'a+')
x = file_object.read()
print(type(x))
lst_x = [i for i in x.split("<tr>")]
#print(lst_x)
lst_x.remove(lst_x[0])
print(lst_x[0])
print(lst_x[1])
a = lst_x[0].strip("<td>Premium-Other</td><td>")
print(a)
a = a.split("</td><td>")
print(a)