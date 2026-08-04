# SQL Injection Example

This directory contains examples of SQL injection vulnerability and its mitigation.

## Vulnerable Code

The `vulnerable.py` file demonstrates a SQL injection vulnerability where user input is directly concatenated into a SQL query without proper sanitization.

## Fixed Code

The `fixed.py` file shows the secure implementation of the login function using parameterized queries to prevent SQL injection attacks.

## Before/After Diff

```diff
- def login(username, password):
-     """
-     Vulnerable login function that directly concatenates user input into SQL query.
-     This allows SQL injection attacks.
-     """
-     query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
-     print(f"Executing query: {query}")
-     
-     cursor.execute(query)
-     result = cursor.fetchone()
+ def login(username, password):
+     """
+     Secure login function that uses parameterized queries to prevent SQL injection.
+     User input is properly sanitized by the database driver.
+     """
+     query = "SELECT * FROM users WHERE username = ? AND password = ?"
+     print(f"Executing query: {query}")
+     print(f"With parameters: username={username}, password={password}")
+     
+     cursor.execute(query, (username, password))
+     result = cursor.fetchone()
```

**Key change**: String interpolation (`f"..."`) → Parameterized query (`?` placeholders with tuple params).

## How to Run

1. Navigate to this directory: `cd skills/sql_injection`
2. Run the vulnerable example: `python vulnerable.py`
3. Run the fixed example: `python fixed.py`
4. Compare the outputs to see how the vulnerability was mitigated

## Expected Output

- The vulnerable example should allow a SQL injection attack, demonstrating the vulnerability.
- The fixed example should prevent the SQL injection attack, showing the secure implementation.

## Installation for AI Agents (Claude Code / Cursor)

This skill is part of the **Anthropic Cybersecurity Skills** library. Install the full library in one command:

```bash
# Option 1: npx (recommended for agentskills.io compatible platforms)
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# Option 2: Git clone
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

Once installed, the skill is available at `skills/sql_injection/` and can be invoked by name: `sql_injection` or `detecting-sql-injection`.