#!/usr/bin/python

''' @Author: Aravind Madan Mohan'''

"""Product ID number to standard ISBN-10 number converter.

Usage:

$ python main.py

Product ID to be converted: 978140007917
Resulting ISBN-10: 1400079179

"""
import click

from src import converter


INPUT_MESSAGE = "*********************************************** \n Enter the Product ID to be converted to ISBN-10: "
RESULT_MESSAGE = "Resulting ISBN-10: %s"
ERROR_MESSAGE = "An error occurred during ISBN-10 conversion: %s"

import argparse

parser = argparse.ArgumentParser(description='Converts Product ID to ISBN-10.\n No options or arguements. \n Enter the 12 digit Product ID')

args = parser.parse_args()
#print(args.accumulate(args.integers))

def execute_conversion():
    """Get input from STDIN and display the conversion result on STDOUT.

    The input product ID number is converted to a ISBN-10 number. If the
    conversion does not succeed, an error message is presented on STDOUT
    explaining the reason.

    """
    isbn_converter = converter.IsbnConverter()
    product_id = input(INPUT_MESSAGE)
    result_message = ""
    isbn = isbn_converter.convert_from_product_id(product_id)

    result_message = RESULT_MESSAGE % isbn

    print (result_message)

#Main function
if __name__ == '__main__':
    while 1:
        execute_conversion()