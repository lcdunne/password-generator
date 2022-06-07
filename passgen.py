import random
import argparse

ALL_CHARS = 'abcdefghijklmnopqrstuvwxyz1234567890!£$%^&*()-=[];#:@~,./<>?|'
CHARS = ''.join(set(ALL_CHARS + ALL_CHARS.upper())) # Get uppercases too
DEFAULT_LEN = 16
DEFAULT_N = 1

def gen_pass(k=DEFAULT_LEN, fromchars=CHARS):
    return ''.join(random.choices(fromchars, k=k))

def make_passwords(passn=DEFAULT_N, passlen=DEFAULT_LEN, fromchars=CHARS):
    for i in range(passn):
        print(f"generated {i+1} :\t{gen_pass(k=passlen, fromchars=fromchars)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-n", "--number", type=int, default=DEFAULT_N,
        help="number of passwords to create")
    parser.add_argument(
        "-len", "--length", type=int, default=DEFAULT_LEN,
        help="length of password to create")

    args = parser.parse_args()

    make_passwords(passn=args.number, passlen=args.length)
