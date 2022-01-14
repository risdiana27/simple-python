def list_member(member_data):
    print("=====List Member=====")
    if len(member_data) > 0:
        for i in member_data:
            for key, val in i.items():
                print(f"{key}: {val}")
            print("===============")
    else:
        print("Member not found")

def add_member(member_data):
    print("=====Add Member=====")
    name_member = input("Please input name member : ")
    age_member = int(input("Please input age member : "))
    address_member = input("Please input address member : ")
    email_member = input("Please input email member : ")
    confirm = input("Are you sure to add this member? [y/n]")

    if confirm.lower() == "y":
        tmp_data = {
            "Name": name_member,
            "Age": age_member,
            "Address": address_member,
            "Email": email_member
        }

        member_data.append(tmp_data)

def find_member(member_data):
    print("=====Find Member=====")
    if len(member_data) < 1:
        print("Member not found")
        return

    name_member = input("Please input name :")
    index = -1
    for i in range(len(member_data)):
        name = member_data[i]["Name"].lower()
        if name.find(name_member.lower()) != -1:
            index = 0
            print("Name : {0}".format(member_data[i]["Name"]))
            print("Age: {0}".format(member_data[i]["Age"]))
            print("Address : {0}".format(member_data[i]["Address"]))
            print("Email : {0}".format(member_data[i]["Email"]))
            print("===============")

    if index == -1:
        print("Member not found")

def delete_member(member_data):
    print("=====Delete Member=====")
    if len(member_data) < 1:
        print("Member not found")
        return

    email_member = input("Please input email :")
    index = -1
    for i in range(len(member_data)):
        if member_data[i]["Email"] == email_member:
            index = i
            break
    if index != -1:
        del member_data[index]
    else:
        print("Member not found")