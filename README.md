# 🔐 Password Generator & Strength Checker

A command-line tool to generate secure passwords and check password strength.

## Features
- 🔑 Generate passwords with custom length and character sets
- 💪 Check strength of any existing password
- 📊 Detailed feedback on how to improve weak passwords

## Usage

### Generate a password
```bash
python password_generator.py generate --length 16
```

### Generate without symbols
```bash
python password_generator.py generate --length 12 --no-symbols
```

### Check your password strength
```bash
python password_generator.py check "MyPassword123!"
```

## Example Output
```
🔑 Generated Password: kR#9mXpL@2nQvY
💪 Strength: 💪 Very Strong (6/6)
```

## Requirements
- Python 3.6+
- No external dependencies