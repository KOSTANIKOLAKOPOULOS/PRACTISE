# ΔΟΜΗ ΑΚΟΛΟΥΘΙΑΣ ΑΣΚΗΣΗ 5.1
name=input("δωσε το ονοματεπωνυμο :")
school=input("δωσε την ταξη που παει το παιδι :")
grade1=int(input("δωσε 1ο βαθμο "))
list=[]
list.append(grade1)
grade2=int(input("δωσε 2ο βαθμο "))
list.append(grade2)
grade3=int(input("δωσε 3ο βαθμο "))
list.append(grade3)
average=sum(list)/3
print("ΟΝΟΜΑ {} ΤΑΞΗ {} ΜΕΣΟΣ ΟΡΟΣ ΒΑΘΜΟΛΟΓΙΑΣ {}".format(name,school,average))
