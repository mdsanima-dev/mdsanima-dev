"""
# Colors Module

Definitions of complex colors printed in the console output with your own text.
"""

def complex_color():
    """
    Define color console variables.

    Returns:
        literal: Color console variable.
    Usage:
        Assigning function calling to a variable.
    .. code::
        sx, xm, ex = complex_color()
        start_c, middle_c, end_c = complex_color()
    """
    sx = '\x1b[38;5;'
    xm = 'm'
    ex = '\x1b[0m'

    return sx, xm, ex


def show_complex_color(number:bool=False):
    """
    Function prints all available colors with a number.

    Args:
        number (boot): Show color number. Defaults to False.
    Returns:
        print: Show all colors.
    Usage:
        Function calling.
    .. code::
        show_complex_color(True)
    """
    sx, xm, ex = complex_color()

    # Print info options.
    if number == False:
        print('[SHOW COMPLEX COLOR ONLY]\n')
        show = 'mdsanima'.ljust(9)
        done = '\n\n[DONE MDSANIMA]'
    else:
        print('[SHOW COMPLEX COLOR NUMBER]\n')
        done = '\n\n[DONE NUMBER]'

    # Print all colors with numbers.
    for i in range(255):
        if number == True:
            show = '--> ' + str(i+1).ljust(5)
        color = (sx + str(i) + xm + show + ex)
        print(color, sep = ' ', end = '   ', flush = True)

    return print(done)


def get_complex_color(text:str='mdsanima', color:int=255):
    """
    This function allows you to print colored text to the console output.

    Args:
        text (str, optional): The text you want to use for color output
                                in the console. Defaults to 'mdsanima'.
        color (int, optional): The color number you want to use for color
                                output in the console. Defaults to 255.
    Returns:
        str: Colored text output in the console.
    Usage:
        Assigning function to variable.
    .. code::
        mds = get_complex_color

        Printing colored text on the same line by function calling.
    .. code::
        print(
            mds(),
            mds('example text', 77),
            mds(text='more example', color=99),
            mds(color=187) + mds('-dev', 86),
            mds('check it', 196)
        )
    """
    sx, xm, ex = complex_color()

    return (sx + str(color) + xm + text + ex)
