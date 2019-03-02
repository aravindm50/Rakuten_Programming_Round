Rakuten Programming Round

main.py is the Main function.

"src" folder is the folder containing additional resources.

The International Standard Book Number (ISBN) uniquely identifies a published book with a ten digit
number. For example, the book Coding and Information Theory by Richard Hamming, which was used
as reference for this discussion, is uniquely coded as:

ISBN 0-13-139139-9


The familiar ISBN holds a secret. In common with many similar numbers used in credit cards, price tags, inventory control and membership
numbers, the ISBN is specially constructed to incorporate error detection. A study of the method used
reveals many fundamental features of a robust error detection scheme (i.e. one which reliably detects
errors).


Error control codes are often designed for known applications where certain types of errors are expected to
occur. In this case, the most common errors expected would be those which humans would typically make
when writing or typing a book order. These errors would normally be either "write a single digit
incorrectly", or "switch two adjacent digits". Of course, the ability to detect errors also allows identification
of invalid numbers which might be encountered (for example, if someone were to forge a credit card
number). Forgery is not expected to be a real concern for book numbers, but error detection is very
important.


The final digit in the ISBN provides the desired error detection capability. It is added once the book number
is issued, and, once complete, the entire ten digit ISBN can be checked for errors whenever it is transcribed or
transmitted.
