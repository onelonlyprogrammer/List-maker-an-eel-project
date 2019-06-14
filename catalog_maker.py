import sys
import pprint
pp = pprint.PrettyPrinter()

#Takes user input and returns items in catalog
def retrive(A_List, request):
    look = None

#Searches for item name in catalog and returns when found
#If not found informs the user
    for look in A_List:
        if request.upper() == look[0].upper():
            return look
    if request != look[0]:
        print("No Item named " + request)
        return ["No Item named " + request]


#Takes arguments for new item and saves them to file
def addToList(A_List, newItem):
    try:
        newItem[1] = int(newItem[1])
        newItem[2] = float(newItem[2])
    except ValueError:
        print ("Invalid input")
        return A_List, "Invalid input"
    except IndexError:
        print ("Error: input name, quantity, and price")
        return A_List, "Error: input name, quantity, and price"

    A_List.append(newItem)
    with open("catalog.txt","w") as file_edit:
        for a in A_List:
            print("writing", a)
            file_edit.write(a[0] + ", " + str(a[1]) + ", " + str(a[2]) + "\n")
    A_List.sort()
    return A_List, None

#Takes user input and searches for item name in catalog
#If item not found informs the user
#When item is found deletes from A_List
def delete(A_List, request):
    trash = [[], []]
    with open("catalog.txt", "w") as file_edit:
        for look in A_List:
            print("working")
            if request.upper() == look[0].upper():
                trash.append(look)
                A_List.remove(look)
                print(look, "sucessfully deleted")
            elif request not in A_List:
                file_edit.write(str(look[0]) + ", " + str(look[1]) + ", " + str(look[2]) + "\n")
    return A_List, trash

#takes user input and searches for item
#When item is found adds price argument to total
def add(A_List, request):
    result = [0.00]

    for r in list(request):
        for look in A_List:
            if r == look[0]:
                request.remove(r)
                result[0] += float(look[2])
                break
            
    if len(request) > 0 :
        print("No item named ", request)
        result.append("could not find " + str(request))

    return result

