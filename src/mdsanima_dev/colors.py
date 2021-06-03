"""
# Colors Module

Definitions of the colors printed in to console output.
"""


def show_complex_color():
    """
    This function prints all available colors with a number.

    Returns:
        console_print: Show all colors.
    Usage:
    .. code::
        show_complex_color()
    """
    # Define color console variables.
    sx = '\x1b[38;5;'
    ex = '\x1b[0m'

    # Print all colors with numbers.
    for i in range(255):
        color = (sx + str(i) + 'm' + 'color ' + str(i+1).ljust(3) + ex)
        print(color, sep = ' ', end = '   ', flush = True)

    print('\n\nDONE')

