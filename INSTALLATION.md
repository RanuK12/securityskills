# Installation Guide for Claude Code / Cursor

This library is designed to be easily installed and used with AI coding assistants like Claude Code and Cursor. Here's how to get started:

## Installation Options

### Option 1: Using the agentskills.io CLI (Recommended)

```bash
# Install the skills library using the CLI
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# Or update if already installed
npx skills update mukul975/Anthropic-Cybersecurity-Skills
```

### Option 2: Manual Installation

```bash
# Clone the repository
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills

# Install dependencies
pip install -r requirements.txt  # For Python examples
npm install                      # For Node.js examples (if any)
```

## Running the SQL Injection Example

The SQL injection example demonstrates a common web vulnerability and its secure implementation. This is a great way to see the skills in action.

### Step-by-Step Demonstration

1. **Navigate to the SQL injection example:**
   ```bash
   cd skills/sql_injection
   ```

2. **Run the vulnerable version:**
   ```bash
   python vulnerable.py
   ```
   
   This will show how a SQL injection attack can bypass authentication:
   ```
   === Vulnerable Login System ===
   Try logging in with admin:admin123
   
   --- Normal Login ---
   Executing query: SELECT * FROM users WHERE username = 'admin' AND password = 'admin123'
   Login successful! Welcome, admin
   
   --- SQL Injection Attack ---
   Using malicious input: ' OR '1'='1
   Executing query: SELECT * FROM users WHERE username = '' OR '1'='1' AND password = 'anything'
   Login successful! Welcome, admin
   ```

3. **Run the secure version:**
   ```bash
   python fixed.py
   ```
   
   This will show how parameterized queries prevent the injection:
   ```
   === Secure Login System ===
   Try logging in with admin:admin123
   
   --- Normal Login ---
   Executing query: SELECT * FROM users WHERE username = ? AND password = ?
   With parameters: username=admin, password=admin123
   Login successful! Welcome, admin
   
   --- SQL Injection Attempt ---
   Using malicious input: ' OR '1'='1
   Executing query: SELECT * FROM users WHERE username = ? AND password = ?
   With parameters: username=' OR '1'='1, password=anything
   Login failed!
   ```

### Key Differences

**Vulnerable Version:**
- Uses string interpolation (`f"..."`) to build SQL queries
- User input is directly concatenated into the query string
- Allows attackers to inject malicious SQL code

**Secure Version:**
- Uses parameterized queries with placeholders (`?`)
- User input is properly sanitized by the database driver
- Prevents SQL injection attacks by separating code from data

## Using Skills in AI Assistants

Once installed, the skills are available to your AI coding assistant:

1. **In Claude Code/Cursor**, you can reference skills by name:
   ```
   # Use the sql_injection skill to check for vulnerabilities
   sql_injection
   
   # Or the broader detecting-sql-injection skill
   detecting-sql-injection
   ```

2. **Skills include:**
   - Vulnerable code examples
   - Secure implementations
   - Explanations of the vulnerabilities
   - Before/after code comparisons

## Available Skills

The library contains 817 skills across 29 security domains, including:

- Web vulnerabilities (SQL injection, XSS, CSRF)
- Authentication bypasses
- Privilege escalation
- Malware analysis
- Network security
- Cloud security
- And many more...

Each skill follows the agentskills.io standard and is mapped to six industry frameworks:
- MITRE ATT&CK
- NIST CSF 2.0
- MITRE ATLAS
- MITRE D3FEND
- NIST AI RMF
- MITRE Fight Fraud Framework (F3)

## Next Steps

1. Explore other skills in the `skills/` directory
2. Try examples from different security domains
3. Integrate skills into your security workflows
4. Contribute your own examples (see CONTRIBUTING.md)

## Troubleshooting

- **Python errors**: Make sure you have Python 3.6+ installed
- **Permission issues**: Ensure you have execute permissions on the example files
- **Import errors**: Check that you're in the correct directory when running examples

For more detailed information, see the [README.md](README.md) file.