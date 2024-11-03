# p1-1.py
import sys
from read import read

if __name__ == "__main__":
    filename = sys.argv[1]
    data = read(filename)

    for lst in data:
        print(lst[:5] if len(lst) >= 5 else lst)
