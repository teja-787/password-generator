import random
import string
import argparse


def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True, exclude_similar=False):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if exclude_similar:
        for char in "0O1lI":
            characters = characters.replace(char, "")
    if not characters:
        raise ValueError("At least one character type must be selected")
    password = ''.join(random.choices(characters, k=length))
    return password


def check_strength(password):
    """Check the strength of a given password."""

    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Too short — use at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("⚠️  Recommended length is 12+ characters")

    # Character variety checks
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("❌ Add numbers")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("❌ Add special characters (!@#$...)")

    # Strength label
    if score <= 2:
        strength = "🔴 Weak"
    elif score <= 4:
        strength = "🟡 Medium"
    elif score == 5:
        strength = "🟢 Strong"
    else:
        strength = "💪 Very Strong"

    return strength, score, feedback


def main():
    parser = argparse.ArgumentParser(description="Password Generator & Strength Checker")

    subparsers = parser.add_subparsers(dest="command")

    # Generate command
    gen = subparsers.add_parser("generate", help="Generate a password")
    gen.add_argument("--length", type=int, default=12, help="Password length (default: 12)")
    gen.add_argument("--no-upper", action="store_false", dest="upper", help="Exclude uppercase")
    gen.add_argument("--no-digits", action="store_false", dest="digits", help="Exclude digits")
    gen.add_argument("--no-symbols", action="store_false", dest="symbols", help="Exclude symbols")
    gen.add_argument("--count", type=int, default=1, help="Number of passwords to generate")
    gen.add_argument("--exclude-similar", action="store_true", help="Exclude similar characters (0,O,l,1,I)")

    # Check command
    check = subparsers.add_parser("check", help="Check password strength")
    check.add_argument("password", type=str, help="Password to check")

    args = parser.parse_args()

    if args.command == "generate":
        for i in range(args.count):
            password = generate_password(
    length=args.length,
    use_upper=args.upper,
    use_digits=args.digits,
    use_symbols=args.symbols,
    exclude_similar=args.exclude_similar
)
            strength, score, feedback = check_strength(password)
            print(f"\n🔑 Password {i+1}: {password}  |  {strength} ({score}/6)")
        if feedback:
            print("\nTips:")
            for tip in feedback:
                print(f"  {tip}")

    elif args.command == "check":
        strength, score, feedback = check_strength(args.password)
        print(f"\n🔍 Password: {args.password}")
        print(f"💪 Strength: {strength} ({score}/6)")
        if feedback:
            print("\nTips to improve:")
            for tip in feedback:
                print(f"  {tip}")
        else:
            print("\n✅ Your password is excellent!")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()