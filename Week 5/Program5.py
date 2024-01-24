import sys

def temperature_stats():
    if len(sys.argv) < 2:
        print("Usage: python script.py <temp1> <temp2> ...")
        sys.exit(1)

    temperatures = list(map(float, sys.argv[1:]))
    print(f"Max temperature: {max(temperatures)}")
    print(f"Min temperature: {min(temperatures)}")
    print(f"Mean temperature: {sum(temperatures) / len(temperatures)}")

if __name__ == "__main__":
    temperature_stats()
