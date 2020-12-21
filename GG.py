from Tkinter import *
import random
root=Tk()
label1=Label(root,text="GUESSING GAME")
no_of_chances=10
points,i=10,1
rand_num=random.randrange(1,101,1)
def restart():
       global no_of_chances
       global points
       global rand_num
       global tf
       global msg
       no_of_chances=10
       points=10
       rand_num=random.randrange(1,101,1)
       tf=Entry(root,text="")
       gs_btn=Button(root,text="Guess",command=lambda : guess(1,int(tf.get())))
       msg=Label(root,text="")
       restrt_btn=Button(root,text="Restart",command=restart)
       exit_btn=Button(root,text="Exit",command=root.quit)
       
       tf.grid(row=1,column=0)
       gs_btn.grid(row=1,column=1)
       msg.grid(row=2,column=0,columnspan=2)
       restrt_btn.grid(row=3,column=0)
       exit_btn.grid(row=3,column=1)
       
def guess(i,n):
       global no_of_chances
       global points
       global rand_num
       global tf
       global msg
       tf=Entry(root,text="Guess a number")
       gs_btn=Button(root,text="Guess",command=lambda : guess(i+1,int(tf.get())))
       restrt_btn=Button(root,text="Restart",command=restart)
       exit_btn=Button(root,text="Exit",command=root.quit)
       if(rand_num==n):
              msg=Label(root,text="Correct, You got "+str(points)+" points!")
       elif(n<rand_num):
              msg=Label(root,text="Your number is less than actual number")
              points-=1
       else:
              msg=Label(root,text="Your number is greater than actual number")
              points-=1
       
       if(points==0):
              msg=Label(root,text="You lost! The Number is "+str(rand_num))
       if(i==no_of_chances):
              gs_btn=Button(root,text="Guess",state=DISABLED)
       tf.delete(0,END)
       tf.grid(row=1,column=0)
       gs_btn.grid(row=1,column=1)
       msg.grid(row=2,column=0,columnspan=2)
       restrt_btn.grid(row=3,column=0)
       exit_btn.grid(row=3,column=1)

tf=Entry(root,text="Guess a number")
gs_btn=Button(root,text="Guess",command=lambda : guess(1,int(tf.get())))
msg=Label(root,text="")
restrt_btn=Button(root,text="Restart",command=restart)
exit_btn=Button(root,text="Exit",command=root.quit)

label1.grid(row=0,column=0,columnspan=2)
label1.config(font=("Courier", 44))
tf.grid(row=1,column=0)
gs_btn.grid(row=1,column=1)
msg.grid(row=2,column=0,columnspan=2)
restrt_btn.grid(row=3,column=0)
exit_btn.grid(row=3,column=1)
root.mainloop()
