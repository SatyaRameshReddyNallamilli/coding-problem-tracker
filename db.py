import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="coding_tracker",
        user="postgres",
        password="Ramesh@1128",
        port="5432"
    )

    cur = conn.cursor()
    print("Database Connected Successfully!")

except Exception as e:
    print("Connection Error:", e)


# -----------------------------
# Add Problem
# -----------------------------
def add_problem(title, platform, difficulty, topic, status, notes):

    try:
        query = """
        INSERT INTO problems
        (title, platform, difficulty, topic, status, notes)
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        cur.execute(query, (title, platform, difficulty, topic, status, notes))
        conn.commit()

        print("\nProblem Added Successfully!")

    except Exception as e:
        print("Error:", e)


# -----------------------------
# View Problems
# -----------------------------
def view_problems():

    try:
        cur.execute("SELECT * FROM problems ORDER BY id")

        rows = cur.fetchall()

        if not rows:
            print("\nNo Problems Found.")
            return

        print("\n========== Coding Problems ==========")

        for row in rows:

            print("----------------------------------------")
            print(f"ID         : {row[0]}")
            print(f"Title      : {row[1]}")
            print(f"Platform   : {row[2]}")
            print(f"Difficulty : {row[3]}")
            print(f"Topic      : {row[4]}")
            print(f"Status     : {row[5]}")
            print(f"Notes      : {row[6]}")
            print("----------------------------------------")

    except Exception as e:
        print("Error:", e)


# -----------------------------
# Search Problem
# -----------------------------
def search_problem(title):

    try:

        query = "SELECT * FROM problems WHERE title ILIKE %s"

        cur.execute(query, ('%' + title + '%',))

        rows = cur.fetchall()

        if not rows:
            print("\nProblem Not Found.")
            return

        print("\n========== Search Result ==========")

        for row in rows:

            print("----------------------------------------")
            print(f"ID         : {row[0]}")
            print(f"Title      : {row[1]}")
            print(f"Platform   : {row[2]}")
            print(f"Difficulty : {row[3]}")
            print(f"Topic      : {row[4]}")
            print(f"Status     : {row[5]}")
            print(f"Notes      : {row[6]}")
            print("----------------------------------------")

    except Exception as e:
        print("Error:", e)


# -----------------------------
# Update Status
# -----------------------------
def update_status(pid, status):

    try:

        query = "UPDATE problems SET status=%s WHERE id=%s"

        cur.execute(query, (status, pid))
        conn.commit()

        if cur.rowcount == 0:
            print("\nProblem ID Not Found.")
        else:
            print("\nStatus Updated Successfully!")

    except Exception as e:
        print("Error:", e)


# -----------------------------
# Delete Problem
# -----------------------------
def delete_problem(pid):

    try:

        query = "DELETE FROM problems WHERE id=%s"

        cur.execute(query, (pid,))
        conn.commit()

        if cur.rowcount == 0:
            print("\nProblem ID Not Found.")
        else:
            print("\nProblem Deleted Successfully!")

    except Exception as e:
        print("Error:", e)


# -----------------------------
# Close Connection
# -----------------------------
def close_connection():

    try:
        cur.close()
        conn.close()
        print("\nDatabase Connection Closed.")

    except:
        pass