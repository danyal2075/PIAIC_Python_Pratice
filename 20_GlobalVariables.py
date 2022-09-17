# if we donot give any variable inside the function it will take global variable ( Outside variable).


name = " sohial ". title()
def change_name():
    #name = " HAMZA ".title()
    print("Inside Loop",name)
change_name()
print(name)