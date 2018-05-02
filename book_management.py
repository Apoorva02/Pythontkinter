from tkinter import*
import os

w=Tk("myproject")
heading =Label(w,text="BOOK MANAGEMENT SYSTEM",bg='white',fg='blue',font='Times 16 bold italic')
l1=Label(w,text="BOOK ID",font=("Arial",10),fg="blue")
l2=Label(w,text="BOOK NAME",font=("Arial",10),fg="blue")
l3=Label(w,text="AUTHOR NAME",font=("Arial",10),fg="blue")
l4=Label(w,text="PUBLISHER",font=("Arial",10),fg="blue")
l5=Label(w,text="YEAR OF PUBLICATION",font=("Arial",10),fg="blue")
l6=Label(w,text="PRICE",font=("Arial",10),fg="blue")

count=0

s1=StringVar()
bookid=Entry(w,textvariable=s1,width=35,bd=3)
s2=StringVar()
book=Entry(w,textvariable=s2,width=35,bd=3)
s3=StringVar()
author=Entry(w,textvariable=s3,width=35,bd=3)
s4=StringVar()
publisher=Entry(w,textvariable=s4,width=35,bd=3)
s5=StringVar()
year=Entry(w,textvariable=s5,width=35,bd=3)
s6=StringVar()
price=Entry(w,textvariable=s6,width=35,bd=3)

def addrecord():
    f=open("pythondatabase.txt",'a+')
    
    a=bookid.get()
    b=book.get()
    c=author.get()
    d=publisher.get()
    e=year.get()
    g=price.get()
    f.writelines(a+","+b+","+c+","+d+","+e+","+g+","+"\n")
    #f.write(a.encode('utf-16'))
    #f.write(b.encode('utf-16'))
    #f.write(c.encode('utf-16'))
    #f.write(d.encode('utf-16'))
    #f.write(e.encode('utf-16'))
    #f.write(g.encode('utf-16'))
    f.close()
    
    
def nextrec():
    f=open("pythondatabase.txt",'r')
    global count
    i=0
    while(i<=count):
        l=f.readline()
        i=i+1
        l=l.split(',')
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
    s6.set(l[5])
    
    f.close()
    count=count+1
    
def prevrec():
    f=open("pythondatabase.txt",'r')
    global count
    i=count
    while(i>0):
        l=f.readline()
        i=i-1
        l=l.split(',')
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
    s6.set(l[5])
    f.close()
    count=count-1
def firstrec():
    f=open("pythondatabase.txt",'r')
    global count
    i=count
    l=f.readline()
    i=i-i
    l=l.split(',')
    
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
    s6.set(l[5])
   
    f.close()
    count=count-count

def deleterecord():
    with open("pythondatabase.txt",'r') as f:
         d=f.readlines()
    
    new = []
    for line in d:
         data = line.strip().split()
         if len(data)!=0 and data[2] != bookid.get(): new.append(line)
    with open("pythondatabase.txt",'w') as fp:
       for line in new:   
             fp.write(line)

def last():
    f=open("pythondatabase.txt",'r')       
    a=sum(1 for i in open("pythondatabase.txt"))-1
    print("last record is:",a+1)
   
    l=f.readlines()[a]
    d=l.split()
    s1.set(d[0])
    s2.set(d[1])
    s3.set(d[2])
    s4.set(d[3])
    s5.set(d[4])
    s6.set(d[5])
    
    f.close()

def search():
    f=open("pythondatabase.txt",'r')
    bookid=s1.get()
    print(bookid)
    f=open("pythondatabase.txt",'r')       
    l=f.readlines()
    for i in l:
        d=i.split()
        print(d)
        if(d[2]==bookid):
            
            s1.set(d[0])
            s2.set(d[1])
            s3.set(d[2])
            s4.set(d[3])
            s5.set(d[4])
            s6.set(d[5])
    f.close()

def update():
    x1=bookid.get()
    x2=book.get()
    x3=author.get()
    x4=publisher.get()
    x5=year.get()
    x6=price.get()
    with open("pythondatabase.txt",'r') as f:
              d=f.readlines()
              
    new=[]
    for line in d:
              data=line.strip().split()
              if len(data)!=0 and data[2]!=c3: new.append(line)
              else:
                  new.append(str(x1)+' '+str(x2)+' '+str(x3)+' '+str(x4)+' '+str(x5)+''+str(x6)+"\n")
    with open("pythondatabase.txt",'w') as fp:
              for line in new:
                  fp.write(line)
            
   
    
    
b1=Button(w,text="First record",command=firstrec)
b2=Button(w,text="Previous",command=prevrec)
b3=Button(w,text="Next",command=nextrec)
b4=Button(w,text="Last record",command=last)
b5=Button(w,text="ADD",command=addrecord)
b6=Button(w,text="DELETE",command=deleterecord)
b7=Button(w,text="UPDATE", command=update)
b8=Button(w,text="SEARCH",command=search)

heading.grid(row=1,column=2)
l1.grid(row=4,column=1)
l2.grid(row=5,column=1)
l3.grid(row=6,column=1)
l4.grid(row=7,column=1)
l5.grid(row=8,column=1)
l6.grid(row=9,column=1)



bookid.grid(row=4,column=2)
book.grid(row=5,column=2)
author.grid(row=6,column=2)
publisher.grid(row=7,column=2)
year.grid(row=8,column=2)
price.grid(row=9,column=2)


b1.grid(row=11,column=1,columnspan=2,padx=5,pady=5)
b2.grid(row=11,column=2,columnspan=2,padx=5,pady=5)
b3.grid(row=11,column=3)
b4.grid(row=11,column=4)
b5.grid(row=12,column=1,columnspan=2)
b6.grid(row=12,column=2,columnspan=2)
b7.grid(row=12,column=3,padx=5,pady=5)
b8.grid(row=12,column=4,padx=5,pady=5)


w.mainloop()
