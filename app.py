import function

member_data = []

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
        function.list_member(member_data)
    elif menu == "2":
       function.add_member(member_data)
    elif menu == "3":
        function.find_member(member_data)
    elif menu == "4":
        function.delete_member(member_data)
    elif menu == "0":
        confirm = input("Are you sure to quit? [y/n]")
        if confirm.lower() == "y":
            break
        else:
            continue
    else:
        print("Select menu between 0 - 4")
        continue
