
import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="coding_tracker",
        user="postgres",
        password="Ramesh@1128",
        port="5432"
    )

    cursor = connection.cursor()

    print("✅ Database Connected Successfully!")

except Exception as e:
    print("❌ Error:", e)
    
def add_problem(title, platform, difficulty, topic, status, notes):

    query = """
    INSERT INTO problems
    (title, platform, difficulty, topic, status, notes)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        title,
        platform,
        difficulty,
        topic,
        status,
        notes
    )

    cursor.execute(query, values)

    connection.commit()

    print("Problem Added Successfully!")

'''add_problem(
    "Two Sum",
    "LeetCode",
    "Easy",
    "Arrays",
    "Solved",
    "Used HashMap"
)'''

def view_problems():

    cursor.execute("SELECT * FROM problems")

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No Problems Found")

    else:

        print("\n------ Coding Problems ------")

        for row in rows:
            print(row)


def search_problem(title):

    query = """
    SELECT * FROM problems
    WHERE title = %s
    """

    cursor.execute(query, (title,))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Problem Not Found")
    else:
        print("\nProblem Found:\n")

        for row in rows:
            print(row)

#search_problem("Two Sum")

def update_status(problem_id, new_status):

    query = """
    UPDATE problems
    SET status = %s
    WHERE id = %s
    """

    cursor.execute(query, (new_status, problem_id))

    connection.commit()

    print("Status Updated Successfully!")

#update_status(1, "Revision")
view_problems()

def delete_problem(problem_id):

    query = """
    DELETE FROM problems
    WHERE id = %s
    """

    cursor.execute(query, (problem_id,))

    connection.commit()

    print("Problem Deleted Successfully!")

#delete_problem(1)
