import sys

def count_arguments():
    num_arguments = len(sys.argv) - 1  # Subtracting 1 to exclude the program name itself
    print(f"Number of command-line arguments: {num_arguments}")

if __name__ == "__main__":
    count_arguments()
