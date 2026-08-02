# SQL Injection Example

This directory contains examples of SQL injection vulnerability and its mitigation.

## Vulnerable Code

The `vulnerable.py` file demonstrates a SQL injection vulnerability where user input is directly concatenated into a SQL query without proper sanitization.

## Fixed Code

The `fixed.py` file shows the secure implementation of the login function using parameterized queries to prevent SQL injection attacks.

## How to Run

1. Navigate to this directory: `cd skills/sql_injection`
2. Run the vulnerable example: `python vulnerable.py`
3. Run the fixed example: `python fixed.py`
4. Compare the outputs to see how the vulnerability was mitigated

## Expected Output

- The vulnerable example should allow a SQL injection attack, demonstrating the vulnerability.
- The fixed example should prevent the SQL injection attack, showing the secure implementation.