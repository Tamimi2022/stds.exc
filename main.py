# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Your code here
import sys


def main():
    # TODO: read text from stdin
    text = sys.stdin.read()

    # TODO: Filter character given as an argument from the text

    # TODO: Print the result to stdout

    # TODO: Print the total number of removed characters to stderr
    if len(sys.argv) == 1:
        sys.stderr.write('0') # stdrr
        sys.stdout.write(text) # stdout
    else:
        char = sys.argv[1]
        sys.stdout.write(text.replace(char, ''))
        sys.stderr.write(str(text.count(char)))

if __name__ == "__main__":
    main()