import tkinter as tk
from tkinter import messagebox
from db import connect_to_db, insert_skill, view_skills, update_skill, delete_skill
    
def view_skills_window(conn, root):
    skills = view_skills(conn)
    view_window = tk.Toplevel(root)
    view_window.title("View Skills")
    view_window.geometry("700x700")

    for i, skill in enumerate(skills):
        tk.Label(view_window, text=skill).grid(row=i, column=0)

    tk.Button(view_window, text="Close", command=view_window.destroy).grid(row=len(view_skills(conn))+2, column=0, columnspan=13, pady=10)

def add_skill_window(conn, root):
    def submit():
        skill_name = entry_skill_name.get()
        icon = entry_icon.get()
        years_of_experience = entry_years_of_experience.get()
        experience_type = entry_experience_type.get()
        description = entry_description.get()
        insert_skill(conn, skill_name, icon, years_of_experience, experience_type, description)
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add Skill")
    add_window.geometry("400x400")

    tk.Label(add_window, text="Skill Name:").pack(pady=5)
    entry_skill_name = tk.Entry(add_window)
    entry_skill_name.pack(pady=5)

    tk.Label(add_window, text="Icon:").pack(pady=5)
    entry_icon = tk.Entry(add_window)
    entry_icon.pack(pady=5)

    tk.Label(add_window, text="Years of Experience:").pack(pady=5)
    entry_years_of_experience = tk.Entry(add_window)
    entry_years_of_experience.pack(pady=5)

    tk.Label(add_window, text="Experience Type:").pack(pady=5)
    entry_experience_type = tk.Entry(add_window)
    entry_experience_type.pack(pady=5)

    tk.Label(add_window, text="Description:").pack(pady=5)
    entry_description = tk.Entry(add_window)
    entry_description.pack(pady=5)

    tk.Button(add_window, text="Submit", command=submit).pack(pady=10)
    tk.Button(add_window, text="Cancel", command=add_window.destroy).pack(pady=10)


def update_skill_window(conn, root):
    def update(skill_id, entry_skill_name, entry_icon, entry_years_of_experience, entry_experience_type, entry_description):
            skill_name = entry_skill_name.get()
            icon = entry_icon.get()
            years_of_experience = entry_years_of_experience.get()
            experience_type = entry_experience_type.get()
            description = entry_description.get()

            update_skill(conn, skill_id, skill_name, icon, years_of_experience, experience_type, description)

    def getSkills():
        skills = view_skills(conn)
        for i, skill in enumerate(skills):
            skill_id, skill_name, icon, years_of_experience, experience_type, description = skill

            tk.Label(update_window, text="Skill ID:").grid(row=i+1, column=0, padx=5, pady=5)
            tk.Label(update_window, text=skill_id).grid(row=i+1, column=1, padx=5, pady=5)

            tk.Label(update_window, text="Skill Name:").grid(row=i+1, column=2, padx=5, pady=5)
            entry_skill_name = tk.Entry(update_window)
            entry_skill_name.insert(0, skill_name)
            entry_skill_name.grid(row=i+1, column=3, padx=5, pady=5)

            tk.Label(update_window, text="Icon:").grid(row=i+1, column=4, padx=5, pady=5)
            entry_icon = tk.Entry(update_window)
            entry_icon.insert(0, icon)
            entry_icon.grid(row=i+1, column=5, padx=5, pady=5)

            tk.Label(update_window, text="Years of Experience:").grid(row=i+1, column=6, padx=5, pady=5)
            entry_years_of_experience = tk.Entry(update_window)
            entry_years_of_experience.insert(0, years_of_experience)
            entry_years_of_experience.grid(row=i+1, column=7, padx=5, pady=5)

            tk.Label(update_window, text="Experience Type:").grid(row=i+1, column=8, padx=5, pady=5)
            entry_experience_type = tk.Entry(update_window)
            entry_experience_type.insert(0, experience_type)
            entry_experience_type.grid(row=i+1, column=9, padx=5, pady=5)

            tk.Label(update_window, text="Description:").grid(row=i+1, column=10, padx=5, pady=5)
            entry_description = tk.Entry(update_window)
            entry_description.insert(0, description)
            entry_description.grid(row=i+1, column=11, padx=5, pady=5)

            tk.Button(update_window, text="Update", command=lambda sid=skill_id, esn=entry_skill_name, ei=entry_icon, eyoe=entry_years_of_experience, eet=entry_experience_type, ed=entry_description: update(sid, esn, ei, eyoe, eet, ed)).grid(row=i+1, column=12, padx=5, pady=5)
            # tk.Label(update_window, text="Description:").pack(pady=5)
            # entry_description = tk.Entry(update_window)
            # entry_description.pack(pady=5)

    update_window = tk.Toplevel(root)
    update_window.title("Update Skill")
    update_window.geometry("1500x400")

    tk.Label(update_window, text="Skillset Management System").grid(row=0, column=0, columnspan=2, pady=10)

    getSkills()
    tk.Button(update_window, text="Done", command=update_window.destroy).grid(row=len(view_skills(conn))+2, column=0, columnspan=13, pady=10)

def delete_skill_window(conn, root):
    def delete():
        skill_id = entry_description.get()
        delete_skill(conn, skill_id)
        messagebox.showinfo("Success", "Skill deleted successfully!")
        delete_window.destroy()
    
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Skill")
    delete_window.geometry("400x400")

    tk.Label(delete_window, text="Skill ID:").pack(pady=5)
    entry_description = tk.Entry(delete_window)
    entry_description.pack(pady=5)

    tk.Button(delete_window, text="Delete", command=delete).pack(pady=10)
    tk.Button(delete_window, text="Cancel", command=delete_window.destroy).pack(pady=10)

