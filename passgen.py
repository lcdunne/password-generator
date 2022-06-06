import random
import argparse

CH = 'abcdefghijklmnopqrstuvwxyz1234567890!"£$%^&*()-=[];#:@~,./<>?|'
DEFAULT_LEN = 16
DEFAULT_N = 1

def gen_pass(fromstr, k=DEFAULT_LEN):
    if k > len(fromstr):
        return ''.join(random.choices(fromstr, k=k))
    return ''.join(random.sample(fromstr, k=k))

def make_passwords(passlen=DEFAULT_LEN, passcount=DEFAULT_N):
    for i in range(passcount):
        print(f"generated {i+1} :\t{gen_pass(fromstr=CH, k=passlen)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-len", "--length", type=int, default=DEFAULT_LEN,
        help="length of password to create")
    parser.add_argument(
        "-n", "--number", type=int, default=DEFAULT_N,
        help="number of passwords to create")

    args = parser.parse_args()

    make_passwords(args.length, args.number)
