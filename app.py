member_data = [
    {
        "Name": "Asep Risdiana",
        "Age": 26,
        "Address": "Bandung",
        "Email": "asep@test.com"
    },
    {
        "Name": "Ghazali",
        "Age": 27,
        "Address": "Jakarta",
        "Email": "ghazali@test.com"
    }
]

while True:
    print("""
=====Menu=====
1. List Member
2. Add Member
3. Find Member
4. Delete Member
0. Out
    """)

    menu = input("Please choose menu [0 -4]: ")
    if menu == "1":
        print("=====List Member=====")
        for i in member_data:
            for key, val in i.items():
               print(f"{key}: {val}")
            print("===============")
    elif menu == "2":
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
        else:
            continue
    elif menu == "3":
        print("=====Find Member=====")
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
            print("Member data not found")
    elif menu == "4":
        print("=====Delete Member=====")
        email_member = input("Please input email :")

        index = -1
        for i in range(len(member_data)):
            if member_data[i]["Email"] == email_member:
                index = i
                break
        if index != -1:
            del member_data[index]
        else:
            print("Member data not found")
    elif menu == "0":
        konfirmasi = input("Are you sure to quit? [y/n]")
        if konfirmasi.lower() == "y":
            break
        else:
            continue
    else:
        print("Select menu between 0 - 4")
        continue
