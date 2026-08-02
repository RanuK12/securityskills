# Security Skills Examples

This directory contains examples of cybersecurity skills with vulnerable and fixed code implementations.

## Structure

Each skill directory contains:

- `SKILL.md`: The original skill description from the Anthropic-Cybersecurity-Skills repository
- `vulnerable.py`: A minimal, intentionally vulnerable code example
- `fixed.py`: The same code example with security fixes applied
- `README.md`: Instructions on how to run the examples and verify the vulnerability

## How to Use

1. Navigate to a skill directory: `cd skills/<skill-name>`
2. Run the vulnerable example: `python vulnerable.py`
3. Run the fixed example: `python fixed.py`
4. Compare the outputs to see how the vulnerability was mitigated

## Example

For SQL injection vulnerability:

```bash
cd skills/sql_injection
python vulnerable.py  # This will demonstrate the vulnerability
python fixed.py        # This will show the secure implementation
```

## Contributing

To add a new vulnerability example:

1. Create a new directory under `skills/`
2. Copy the `SKILL.md` from the corresponding skill in the parent directory
3. Create `vulnerable.py` and `fixed.py` files
4. Create a `README.md` with instructions for testing
5. Test your examples thoroughly before submitting