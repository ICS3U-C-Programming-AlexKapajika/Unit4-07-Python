#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Nov 11, 2023
# This program prints integers from 1000 to 2000,  outputting five integers per line with each separated by a space.

import time


def main():

    for counter in range(1000,2001):
        if counter == 1000 or counter == 2000:
            print(f"{counter} ",end= "")
        elif counter %5 == 0 :
            print(f" \n {counter} ",end="" )
        else :
            print(f"{counter} ",end= "")


if __name__== "__main__":
    main()