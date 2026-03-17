from password_generator import generate_password, check_strength


def interactive_mode():
    print("\n" + "="*50)
    print("🔐  PASSWORD GENERATOR & STRENGTH CHECKER")
    print("="*50)

    while True:
        print("\nWhat do you want to do?")
        print("  1. Generate a password")
        print("  2. Check password strength")
        print("  3. Exit")

        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == "1":
            try:
                length = int(input("Password length (default 12): ") or "12")
                use_upper = input("Include uppercase? (y/n, default y): ").strip().lower() != "n"
                use_digits = input("Include numbers? (y/n, default y): ").strip().lower() != "n"
                use_symbols = input("Include symbols? (y/n, default y): ").strip().lower() != "n"
                count = int(input("How many passwords? (default 1): ") or "1")

                print()
                for i in range(count):
                    pwd = generate_password(length, use_upper, use_digits, use_symbols)
                    strength, score, _ = check_strength(pwd)
                    print(f"  🔑 {pwd}  →  {strength} ({score}/6)")

            except ValueError as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            pwd = input("Enter password to check: ")
            strength, score, feedback = check_strength(pwd)
            print(f"\n  💪 Strength: {strength} ({score}/6)")
            if feedback:
                print("  Tips:")
                for tip in feedback:
                    print(f"    {tip}")
            else:
                print("  ✅ Excellent password!")

        elif choice == "3":
            print("\n👋 Goodbye!\n")
            break

        else:
            print("❌ Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    interactive_mode()
