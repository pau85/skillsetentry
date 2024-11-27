import tkinter as tk
from db import connect_to_db, insert_skill, view_skills, update_skill, delete_skill
from gui import view_skills_window, add_skill_window, update_skill_window, delete_skill_window

# this code, open_interface, is not in use here right now, only for terminal interface
def open_interface(conn):
    while True:
        print("1. Add a skill")
        print("2. View all skills")
        print("3. Update a skill")
        print("4. Delete a skill")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            skill_name = input("Enter the skill name: ")
            icon = input("Enter the icon file name: ")
            years_of_experience = int(input("Enter the years of experience: "))
            experience_type = input("Enter the experience type: ")
            description = input("Enter the description: ")
            insert_skill(conn, skill_name, icon, years_of_experience, experience_type, description)
        elif choice == "2":
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM skill")
            skills = cursor.fetchall()
            for skill in skills:
                print(skill)
        elif choice == "3":
            skill_id = int(input("Enter the skill ID to update: "))
            skill_name = input("Enter the skill name: ")
            icon = input("Enter the icon file name: ")
            years_of_experience = int(input("Enter the years of experience: "))
            experience_type = input("Enter the experience type: ")
            description = input("Enter the description: ")
            update_skill(conn, skill_id, skill_name, icon, years_of_experience, experience_type, description)
        elif choice == "4":
            skill_id = int(input("Enter the skill ID to delete: "))
            delete_skill(conn, skill_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

def main():
    global root
    conn = connect_to_db()
    if conn:
        # Example data to insert
        # skill_name = "TypeScript"
        # icon = "typescript-icon.png"
        # years_of_experience = 5
        # experience_type = "Programming"
        # description = "A versatile programming language."

        # insert_skill(conn, skill_name, icon, years_of_experience, experience_type, description)

# Lets create an interface to insert data
        # print("Enter the skill details:")
        # skill_name = input("Skill Name: ")
        # icon = input("Icon: ")
        # years_of_experience = input("Years of Experience: ")
        # experience_type = input("Experience Type: ")
        # description = input("Description: ")
        # insert_skill(conn, skill_name, icon, years_of_experience, experience_type, description)
        
        # open_interface()

        root = tk.Tk()
        root.title("Main Menu")
        root.geometry("300x300")

        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)
        tk.Label(button_frame, text="Skillset Management System").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Button(button_frame, text="View Skills", command=lambda: view_skills_window(conn, root)).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="Add Skill", command=lambda: add_skill_window(conn, root)).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(button_frame, text="Update Skill", command=lambda: update_skill_window(conn, root)).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="Delete Skill", command=lambda: delete_skill_window(conn, root)).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(button_frame, text="Exit", command=lambda: (conn.close(), root.quit())).grid(row=3, column=0, columnspan=2, pady=20)

        root.mainloop()
        # Close the connection
        conn.close()

if __name__ == "__main__":
    main()
