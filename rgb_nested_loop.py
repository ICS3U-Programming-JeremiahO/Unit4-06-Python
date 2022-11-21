#!/usr/bin/env python3
# Created By: Jeremiah Omoike
# Date: November 13 2022
# This program shows colour variations up to 255


def main():

    # colour initializations
    red = 0
    green = 0
    blue = 0

    print("These are RGB colour variations up to 256:")
    print("")

    # determines the different colour codes
    # displays results to the console
    for blue in range(0, 257, 1):
        print("RGB ({}, {}, {})".format(red, green, blue))
        if blue == 256:
            print("")
            for green in range(1, 256, 1):
                blue = 0
                print("RGB ({}, {}, {})".format(red, green, blue))
                if green == 256:
                    print("")
                    for red in range(1, 257, 1):
                        green = 0
                        print("RGB ({}, {}, {})".format(red, green, blue))


if __name__ == "__main__":
    main()
