L=[]
str="yes"

while str =="yes":
    print("Enter book data:")
    L.append({
        "Name": input("name:"),
        "ISBN": input("ISBN:"),
        "year": input("year:"),
        "Author": input("Author:")
    })

    str=input("do you want to read another book : (yes):")

b1=input("search for book name:")
for x in L:
    if b1 == x ["Name"] :
        print("found it:")
        break
    else:
        print("not found")

