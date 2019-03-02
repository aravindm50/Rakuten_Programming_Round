# -*- coding: utf-8 -*-

''' @Author: Aravind Madan Mohan'''

import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter('always', UserWarning)

class Conv_Exception(Warning):
    """Specialized exception for conversion errors.
    Arguement:
      message (str): Human readable string describing the exception.
    
    Return:
        Warning if invalid product id

    """
    def __init__(self, message):
        self.message = message
        warnings.warn(message) 

    @staticmethod
    def for_invalid_id_length():
        return Conv_Exception("\n ERROR IN DATA LENGTH")

    @staticmethod
    def for_invalid_id_type():
        return Conv_Exception("\n ERROR IN DATA TYPE")
    
    @staticmethod
    def for_both_invalid():
        return Conv_Exception("\n ERROR IN DATA TYPE AND DATA LENGTH")


class IsbnConverter(object):
    """Product ID number to standard ISBN-10 number converter. """

    _LENGTH_PRODUCT_ID = 12
    _LENGTH_ISBN_10 = 10

    def convert_from_product_id(self, product_id):
        """Convert product ID to ISBN-10 number.

        The conversion follows the rules::
          1) The first 3 digits of the product ID are removed; Prefix digits
          2) Remaining digits are ISBN-10 number without error control;
          3) Error control is computed and appended to final number.

          Reference: Given Document

        Arguement:
          product_id (str)

        Return:
          str: ISBN-10 number from given product ID.

        Warning:
          In case of errors during conversion logic as invalid product ID.

        """
        if product_id == 'exit':
            sys.exit()



        else:
            x = self.__validate_length_id(product_id)
            y = self.__validate_int_id(product_id)

            if x == 1 and y == 1:
                partial_isbn = product_id[3:]
                error_control = self.__compute_error_control(partial_isbn)
                return partial_isbn + error_control

            elif x==0 and y==0:
                Conv_Exception.for_both_invalid()

            elif y == 0:
                Conv_Exception.for_invalid_id_type()

            elif x==0:
                Conv_Exception.for_invalid_id_length()


    def __compute_error_control(self, partial_isbn):
        """Compute error control for ISBN-10 numbers.

        The error control digit is computed considering the weighted sum of the
        9 digits of the actual ISBN number and searching for the 10th digit
        satisfying::

            (weighted_sum + control) = 0 mod 11

        Remainder of division by 11 could be any number from 0 to 10. If it works 
        out that the value of the final digit must be 10, the letter 'x' is used 
        instead to complete the ISBN.

        Reference: Given Document

        Arguement:
          partial_isbn (str): ISBN-10 with missing error control digit.

        Return:
          str: control error digit for the provided partial ISBN number.

        """
        weighted_sum = 0
        for i, digit in enumerate(partial_isbn):
            # weighted sum of digits
            weighted_sum += (self._LENGTH_ISBN_10 - i) * int(digit)

        weighted_sum_mod_11 = (weighted_sum % 11)

        if weighted_sum_mod_11 == 0:
            # Remainder is zero so control should be zero
            control = str(weighted_sum_mod_11)
        else:
            # replace by 'x' when 10 is required as digit
            c_digit = 11 - weighted_sum_mod_11
            control = str(c_digit) if c_digit < self._LENGTH_ISBN_10 else "x" # if remainder is not 10 or 0 replace with number

        return control


    """Check the validity of product ID."""

    # Validate length
    def __validate_length_id(self, product_id): 
        """
        Arguement:
          product_id (str)

        Return:
          1 or 0 based on length of ID is 10 or not

        """
        if len(product_id) != self._LENGTH_PRODUCT_ID:
            return 0
        else:
            return 1
        
    #Validate Numeric
    def __validate_int_id(self, product_id):   
        """
        Arguement:
          product_id (str)

        Return:
            1 or 0 based on validity of the product ID is numeric or not

        """
        if product_id.isdigit():
            return 1
        else:
            return 0
            