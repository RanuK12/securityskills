#!/usr/bin/env python3
"""
Vulnerable SQL Injection Example

This code demonstrates a SQL injection vulnerability where user input
is directly concatenated into a SQL query without proper sanitization.
"""

import sqlite3

# Create a simple in-memory database for demonstration
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create a users table
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
""")

# Insert some test data
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('user', 'user123')")
conn.commit()

def login(username, password):
    """
    Vulnerable login function that directly concatenates user input into SQL query.
    This allows SQL injection attacks.
    """
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")
    
    cursor.execute(query)
    result = cursor.fetchone()
    
    if result:
        print(f"Login successful! Welcome, {result[1]}")
        return True
    else:
        print("Login failed!")
        return False

if __name__ == "__main__":
    print("=== Vulnerable Login System ===")
    print("Try logging in with admin:admin123")
    
    # Normal login
    print("\n--- Normal Login ---")
    login("admin", "admin123")
    
    # SQL injection attack
    print("\n--- SQL Injection Attack ---")
    # This bypasses the password check by adding OR '1'='1' which is always true
    malicious_input = "' OR '1'='1"
    print(f"Using malicious input: {malicious_input}")
    login(malicious_input, "anything")
    
    conn.close()