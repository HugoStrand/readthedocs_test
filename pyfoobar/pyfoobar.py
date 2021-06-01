""" pyfoobar: Python Module for testing read the docs 

Author: H. U.R. Strand (2017)
"""

class MyClass():
    """ This is a test class with some doc strings.

    Extended description of the class

    Todo:
        Write more documentation!

    Notes:
        Needs more testing!"""

    def __init__(self, name):
        """ Here we construct the MyClass object

        Parameters
        ----------
        name : (str)
            The name of the MyClass instance.

        """

    def do_stuff_with_args(self, A, B):
        """ This is a method that takes arguments
        
        Longer description of the function...

        Parameters
        ----------
        A : int
            Description of A
        B : float
            Description of B

        Returns
        -------
        int 
            The sum of A and B
        
        """
        print(A + B)

    def math_docstring(self):
        r""" Here we test the sphinx based math features :math:`\alpha+\beta+\gamma`

        .. math ::
           \int_0^\beta d\tau e^{-i\nu_n \tau} G(\tau) = G(i\nu_n)

        Do we have to indent the math along the method? """

    def do_stuff(self):
        """ This is not a default method that actually does something """
        print("Roses are red, violets are blue, these docs are meant entirely for you.")
    
    def no_doc_string(self):
        print("What happens when we do not have a docstring?")

    def _private_method(self):
        """ This is a Python "private" method by one underscore..."""
        return 1337

    def __very_private_method(self):
        """ This is a Python "very private" method by two underscores..."""
        return 1337*2

    def __str__(self):
        """ String representation of Myclass """
        return "Hello MyClass world!"    
    
if __name__ == '__main__':

    mc = MyClass()
    print(mc)
