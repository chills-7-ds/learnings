import argparse

parser = argparse.ArgumentParser(description="Greet the user by name.")
parser.add_argument("--name", type=str, default="stranger", help="The name of the user.")
parser.add_argument("--age", type=int, default=None, help="The age of the user.")
parser.add_argument("--shout", action="store_true", help="Shout the greeting in uppercase.")
args = parser.parse_args()

# Handle age display
age_display = args.age if args.age is not None else "unknown age"

# Print normal greeting
print(f"Hello, {args.name}! You are {age_display} years old.")

# Print shout version if flag used
if args.shout:
    print(f"HELLO, {args.name.upper()}! YOU ARE {str(age_display).upper()} YEARS OLD.")

