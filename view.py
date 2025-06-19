import sqlite3

DB_PATH = 'instance/messages.db'  # Adjust if your DB path is different

def view_all_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables found:", tables)

    for table_name in tables:
        table_name = table_name[0]
        print(f"\n--- Data from table: {table_name} ---")
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    conn.close()

def delete_message_by_id(message_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM message WHERE id = ?", (message_id,))
    conn.commit()
    print(f"✅ Deleted message with ID {message_id}")
    conn.close()

def delete_user_by_username(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Delete user's messages first (optional but recommended)
    cursor.execute("DELETE FROM message WHERE sender = ? OR receiver = ?", (username, username))

    # Delete the user
    cursor.execute("DELETE FROM user WHERE username = ?", (username,))
    conn.commit()
    print(f"✅ Deleted user '{username}' and their messages")
    conn.close()

# ===== Example Usage =====
# View all data
view_all_data()

# Uncomment to test deletion:
# delete_message_by_id(16)
# delete_user_by_username('virat')
