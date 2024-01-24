import sys

def shortest_argument():
    arguments = sys.argv[1:]
    if not arguments:
        print("No arguments provided.")
    else:
        shortest = min(arguments, key=len)
        print(f"The shortest argument is: {shortest}")

if __name__ == "__main__":
    shortest_argument()
