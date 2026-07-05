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