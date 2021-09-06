#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

def wakuchin(count):
    print("ワク" * count + "チン" * count);

def main():
    parser = argparse.ArgumentParser(description = "Waku Waku Chin Chin")
    parser.add_argument("count",
        type = int,
        default = 2,
        help = "Number of vaccination.")

    args = parser.parse_args()

    if args.count == 0:
        sys.exit("Recommend you to get vaccinated strongly!");

    if args.count < 0:
        sys.exit("You couldn't escape from vaccination.");

    wakuchin(args.count)

if __name__ == "__main__":
    main()