#!/usr/bin/env python3
"""
Fixed SQL Injection Example

This code demonstrates the secure implementation of the login function
using parameterized queries to prevent SQL injection attacks.
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
    Secure login function that uses parameterized queries to prevent SQL injection.
    User input is properly sanitized by the database driver.
    """
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"Executing query: {query}")
    print(f"With parameters: username={username}, password={password}")
    
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    
    if result:
        print(f"Login successful! Welcome, {result[1]}")
        return True
    else:
        print("Login failed!")
        return False

if __name__ == "__main__":
    print("=== Secure Login System ===")
    print("Try logging in with admin:admin123")
    
    # Normal login
    print("\n--- Normal Login ---")
    login("admin", "admin123")
    
    # SQL injection attempt (will fail)
    print("\n--- SQL Injection Attempt ---")
    # This will be treated as a literal string, not as SQL code
    malicious_input = "' OR '1'='1"
    print(f"Using malicious input: {malicious_input}")
    login(malicious_input, "anything")
    
    conn.close()