from tkinter import *
import random
root=Tk()
root.title("Word Sort")
root.geometry("400x400")
label1=Label(root)
def sort_func():
    alpha_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    var_1=random.randint(0, 25)
    var_2=random.randint(0, 25)
    var_3=random.randint(0, 25)
    var_4=random.randint(0, 25)
    var_5=random.randint(0, 26)
     
    
    random_alpha1=alpha_list[var_1]
    random_alpha2=alpha_list[var_2]
    random_alpha3=alpha_list[var_3]
    random_alpha4=alpha_list[var_4]
    random_alpha5=alpha_list[var_5]
    label1["text"]=random_alpha1+random_alpha2+random_alpha3+random_alpha4+random_alpha5
    
btn1 = Button(root)
btn1 = Button(root, text=" Generate random word!  ", command = sort_func)
btn1.place(relx= 0.5, rely = 0.5, anchor= CENTER )

label1.place(relx=0.5, rely = 0.8, anchor= CENTER)

root.mainloop()