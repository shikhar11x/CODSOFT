list=["coding","practice"]
a=input("WHAT YOU WANT TO DO\n"
        "To add -> add\n"
        "To delete -> del\n"
        "To view -> view\n"
        "write here ->>> ")
if a =="add":
    add=input("what task you want to add :")
    list.append(add)
    print(list)
elif a=="del":
    print(list)
    d=input("which task you wanna delete : ")
    list.remove(d)
    print( list,"\ndeleted sucessfully")
elif a=="view":
    print("your task are\n",list)
else:
    print("invalid value")
