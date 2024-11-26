import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "SkillsetDB"
DB_USER = "postgres"
DB_PASSWORD = "your_password"

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

def main():
    conn = connect_to_db()
    if conn:
        # Example data to insert
        skill_name = "Python"
        icon = "python-icon.png"
        years_of_experience = 5
        experience_type = "Programming"
        description = "A versatile programming language."

        insert_skill(conn, skill_name, icon, years_of_experience, experience_type, description)

        # Close the connection
        conn.close()

if __name__ == "__main__":
    main()
