import catalog_maker as cat
import eel

A_List = []

try:
    with open("catalog.txt", "r") as file:
        for f in file:
            f = list(f.strip().split(", "))
            f[1] = int(f[1])
            f[2] = float(f[2])
            A_List.append(f)

#Opens catalog.txt
#If catalog.txt not found makes new file named catalog.txt
except FileNotFoundError:
    error_Input = input("file not found. make now one? ") 

    if "y" in error_Input.upper():
            file = open("catalog.txt", "w")
            file.close()
            print("new file created")

eel.init("web")

@eel.expose
def get_item(func_request, item_request):
    global A_List
    
    if func_request == 0:
        item = cat.retrive(A_List, item_request)
        return item
    
    elif func_request == 1:
        A_List, ret_String = cat.addToList(A_List, item_request)
        if ret_String != None:
            return ret_String
    
    elif func_request == 2:
        A_List = cat.delete(A_List, item_request)

    elif func_request == 3:
        return A_List
    
eel.start('main.html')