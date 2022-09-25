# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Module ``colors`` is for print complex color in the console output with your
own texts. Also, this module is for showing example colors that's you might be
used in your project.
"""

import os


def _set_color_number() -> str:
    """Define color console variables number with ``x1b`` syntax.

    .. warning:: Do not use this function in your code, it is needed to perform
        other functions.

    :return: Color console literal variable.
    :rtype: str

    :usage:

        Assigning a function to a variable:

        .. code:: python

            sx, xm, ex = _set_color_number()
            start_c, middle_c, end_c = _set_color_number()
    """
    sx = "\x1b[38;5;"
    xm = "m"
    ex = "\x1b[0m"

    return sx, xm, ex


def use_color_number(text: str = "mdsanima", color: int = 255) -> str:
    """This function is almost the same as
    `print_color_number <#function-print-color-number>`_ function.

    The difference is that the return is a sequence of unicode characters
    and to get the output in the terminal in a color you need to use the
    print function.

    :param text: The text you want to use for color output in the console,
        defaults to ``mdsanima``.
    :type text: str, optional
    :param color: The color number you want to use for color output in the
        console, defaults to ``255``.
    :type color: int, optional
    :return: Text string output with ``x1b`` systax.
    :rtype: str

    :usage:

        Assigning a function by calling to variable or assigning a function to
        variable just add after import ``color = use_color_number`` and in the
        next line type ``mdsanima_a = color("I love Python", 86)`` in your
        code or use this:

        .. code:: python

            from mdsanima_dev.colors import use_color_number
            mdsanima_a = use_color_number("I love Python", 86)
            mdsanima_b = use_color_number("mdsanima", 186)
            print(mdsanima_a, mdsanima_b)

        Also you can use
        `machine <../tools/#function-machine>`_ function:

        .. code:: python

            from mdsanima_dev.colors import use_color_number
            from mdsanima_dev.utils.tools import machine
            color = use_color_number
            mdsanima_a = color("I love Python", 86)
            mdsanima_b = color("mdsanima", 186)
            machine(mdsanima_a + " " + mdsanima_b, 0.01)
    """
    sx, xm, ex = _set_color_number()

    return sx + str(color) + xm + text + ex


def print_color_number(text: str = "mds", color: int = 255, end=None) -> str:
    """This feature allows you to print colored text to the output of the
    console. Now the function works the same like print function.

    :param text: The text you want to use for color output in the console,
        defaults to ``mds``.
    :type text: str, optional
    :param color: The color number you want to use for color output in the
        console, defaults to ``255``.
    :type color: int, optional
    :param end: End of line print, defaults to ``None``.
    :type end: str, optional
    :return: Printing colored string text output in the console.
    :rtype: str

    :usage:

        Assigning a function to a variable ``mds`` then function calling
        returning printing colored text on the same line:

        .. code:: python

            from mdsanima_dev.colors import print_color_number
            mds = print_color_number
            mds(color=44)
            mds("mdsa", 160, " ")
            mds("mds", 88, " ")
            mds(text="mds", color=99, end=" ")
            mds("mds", 86)
            mds(end="mdsanima-dev", color=85, text="mds")
    """
    sx, xm, ex = _set_color_number()

    return print(sx + str(color) + xm + text + ex, end=end)


def show_color_number(number: bool = True) -> str:
    """Function prints all available colors with number or string text example.

    :param number: Show color number, defaults to ``True``.
    :type number: bool, optional
    :return: Print all colors number or string example in the console output.
    :rtype: str

    :usage:

        Function calling:

        .. code:: python

            from mdsanima_dev.colors import show_color_number
            show_color_number(True)
            show_color_number(False)
    """
    sx, xm, ex = _set_color_number()

    # Get terminal size columns for center info print.
    terminal = os.get_terminal_size()

    # Calculation terminal size based on 21 count string from info.
    calculate_start = terminal.columns / 2 - 11
    calculate_end = terminal.columns / 2 - 10

    # Setup colors for info print.
    colors = [196, 208, 70, 44, 39]

    # Setup colors info variables.
    cts = sx + str(colors[4]) + xm + ("=" * int(calculate_start)) + ex
    cna = sx + str(colors[0]) + xm + "[" + ex
    csh = sx + str(colors[1]) + xm + " SHOW COLOR " + ex
    cdo = sx + str(colors[2]) + xm + " DONE COLOR " + ex
    cmd = sx + str(colors[3]) + xm + "STRING " + ex
    cnu = sx + str(colors[3]) + xm + "NUMBER " + ex
    cnc = sx + str(colors[0]) + xm + "]" + ex
    cte = sx + str(colors[4]) + xm + ("=" * int(calculate_end)) + ex

    # Print info options colors.
    if number == False:
        show = "mdsanima".ljust(9)
        print(cts + cna + csh + cmd + cnc + cte)
        done = "\n" + cts + cna + cdo + cmd + cnc + cte
    else:
        print(cts + cna + csh + cnu + cnc + cte)
        done = "\n" + cts + cna + cdo + cnu + cnc + cte

    # Print all colors numbers colors.
    for i in range(256):
        if number == True:
            show = "--> " + str(i).ljust(5)
        color = sx + str(i) + xm + show + ex
        print(color, sep=" ", end="", flush=True)

    return print(done)
