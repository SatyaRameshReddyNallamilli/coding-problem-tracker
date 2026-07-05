print("Welcome to Coding Problem Tracker")

from db import *

while True:

    print("\n===== Coding Problem Tracker =====")
    print("1. Add Problem")
    print("2. View Problems")
    print("3. Search Problem")
    print("4. Update Status")
    print("5. Delete Problem")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        title = input("Title: ")
        platform = input("Platform: ")
        difficulty = input("Difficulty: ")
        topic = input("Topic: ")
        status = input("Status: ")
        notes = input("Notes: ")

        add_problem(
            title,
            platform,
            difficulty,
            topic,
            status,
            notes
        )

    elif choice == "2":
        view_problems()

    elif choice == "3":

        title = input("Enter Title: ")

        search_problem(title)

    elif choice == "4":

        pid = int(input("Problem ID: "))
        status = input("New Status: ")

        update_status(pid, status)

    elif choice == "5":

        pid = int(input("Problem ID: "))

        delete_problem(pid)

    elif choice == "6":

        print("Thank you!")
        break

    else:

        print("Invalid Choice")