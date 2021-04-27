#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :
@Date     :2021/04/27 10:44:51
@Author      :xbMa
'''

import argparse
import sys


def parse_arguments():
    '''
        usage of argparse,  execute in cmd like: python argparse_demo.py -r <par1> -s <par2> <echo>
    
    Return:
    -----------
        args :    Namespace    all parameters input from sys.argv[1:]
    '''
    parser = argparse.ArgumentParser(description="This is a argparse demo")
    parser.add_argument("echo", help="echo the string you enter")
    parser.add_argument("-r", "--par1", help="parameter1")
    parser.add_argument("-s",
                        "--par2",
                        default="value2",
                        help="parameter2,have a default")

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_arguments()
    print(f"location parameter [echo] is : {args.echo}")
    print(f"keyword parameter [par1] is : {args.par1}")
    print(f"keyword parameter [par2] is : {args.par2}")