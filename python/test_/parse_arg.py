#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="args a", required=True,
                        choices=['1', '2', '4'])
    args = parser.parse_args()
    print args.a

if __name__ == '__main__':
    main()
