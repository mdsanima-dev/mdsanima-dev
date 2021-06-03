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
    Function prints all available colors with a number or only text.

    Args:
        number (boot): Show color number. Defaults to False.
    Returns:
        print: Show all colors.
    Usage:
        Function calling.
    .. code::
        show_complex_color()
        show_complex_color(True)
    """
    sx, xm, ex = complex_color()
    col = [251, 246, 243, 197, 161]
    cna = (sx + str(col[0]-1) + xm + '[' + ex)
    cnb = (sx + str(col[0]-1) + xm + '\n\n[' + ex)
    csh = (sx + str(col[1]-1) + xm + 'SHOW COMPLEX COLOR ' + ex)
    cdo = (sx + str(col[2]-1) + xm + 'DONE COMPLEX COLOR ' + ex)
    cmd = (sx + str(col[3]-1) + xm + 'MDSANIMA' + ex)
    cnu = (sx + str(col[4]-1) + xm + 'NUMBER' + ex)
    cnc = (sx + str(col[0]-1) + xm + ']' + ex)
    cne = (sx + str(col[0]-1) + xm + ']\n' + ex)

    # Print info options.
    if number == False:
        show = 'mdsanima'.ljust(9)
        print(cna + csh + cmd + cne)
        done = (cnb + cdo + cmd + cnc)
    else:
        print(cna + csh + cnu + cne)
        done = (cnb + cdo + cnu + cnc)

    # Print all colors.
    for i in range(255):
        if number == True:
            show = '--> ' + str(i+1).ljust(5)
        color = (sx + str(i) + xm + show + ex)
        print(color, sep = ' ', end = '', flush = True)

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
