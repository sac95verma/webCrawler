import sys
from utils.utils import is_valid

def validate_input(url, depth):
    if not isinstance(url, str):
        print("Error: Initial URL must be a string")
        sys.exit(1)
    if (not is_valid(url)):
        print("Error: Initial URL must be of URL format e.g. http://example.com")
        sys.exit(1)

    # check for valid integer depth
    try:
        depth = int(depth)
    except ValueError:
        print("Error: Depth must be an integer")
        sys.exit(1)