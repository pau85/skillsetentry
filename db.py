import psycopg2
from psycopg2 import sql
from tkinter import messagebox

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "skillsetdb"
DB_USER = "postgres"
DB_PASSWORD = "M@rgi31985"

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Connected to the database successfully!")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def insert_skill(conn, skill_name, icon, years_of_experience, experience_type, description):
    try:
        cursor = conn.cursor()
        insert_query = sql.SQL("""
            INSERT INTO skill (skillName, icon, yearsOfExperience, experienceType, description)
            VALUES (%s, %s, %s, %s, %s)
        """)
        cursor.execute(insert_query, (skill_name, icon, years_of_experience, experience_type, description))
        conn.commit()
        print("Skill inserted successfully!")
    except Exception as e:
        print(f"Error inserting skill: {e}")
        conn.rollback()

def update_skill(conn, skill_id, skill_name, icon, years_of_experience, experience_type, description):
    try:
        cursor = conn.cursor()
        print("in update_skill function - are we getting here?")

        update_query = sql.SQL("""
            UPDATE skill
            SET icon = %s, yearsOfExperience = %s, experienceType = %s, description = %s
            WHERE skillId = %s
        """)

        print("in update_skill function - how about here are we getting here?")
        cursor.execute(update_query, (icon, years_of_experience, experience_type, description, skill_id))
        conn.commit()
        print("Skill updated successfully!")
        messagebox.showinfo("Success", "Skill updated successfully!")

    except Exception as e:
        print(f"Error updating skill: {e}")
        conn.rollback()

def delete_skill(conn, skill_id):
    try:
        cursor = conn.cursor()
        delete_query = sql.SQL("""
            DELETE FROM skill
            WHERE skillId = %s
        """)
        cursor.execute(delete_query, (skill_id,))
        conn.commit()
        print("Skill deleted successfully!")
    except Exception as e:
        print(f"Error deleting skill: {e}")
        conn.rollback()

def view_skills(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM skill")
        skills = cursor.fetchall()
        return skills
    except Exception as e:
        print(f"Error viewing skills: {e}")
        messagebox.showinfo("Error", "Error fetching skills: {e}")
        return []
