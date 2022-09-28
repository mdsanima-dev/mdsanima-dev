# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Module ``colors`` is for printing complex colors in the console output with
your own texts. This module is for showing example colors output in the shell
terminal window. You can use this output on your future projects.

The core functionality is for replace default ``print`` function to allow
printing your string in colors on the terminal window. You can use many default
colors available on ``int`` values.
"""

import os


def _set_colors() -> str:
    """Define color console variables number with ``x1b`` syntax.

    .. warning:: Do not use this function in your code, it is needed to perform
        other functions.

    :return: Color console literal variable. Returns type ``str``.

    :usages:

        Assigning a function to a variable. Sample code in two versions, short
        and long. Only use one version that you like.

        Short code sample:

        .. code:: python

            sx, xm, ex = _set_colors_number()

        Long code sample:

        .. code:: python

            c_start, c_middle, c_end = _set_colors_number()
    """
    sx = "\x1b[38;5;"
    xm = "m"
    ex = "\x1b[0m"

    return sx, xm, ex


def use_colors(text: str = "mdsanima", color: int = 255) -> str:
    """This function is almost the same as
    `print_colors <#function-print-colors>`_ function but it differs in one
    specific detail.

    The difference is that the return is a sequence of unicode characters
    and to get the output in the terminal in a color you need to use the
    print function.

    :param text: The text you want to use for color output.
        Defaults to ``mdsanima``.
    :type text: str, optional
    :param color: The color number you want to use for color output.
        Defaults to ``255``.
    :type color: int, optional
    :return: Text string color output with ``x1b`` systax.
        Returns type ``str``.

    :usages:

        Assigning a function to variable. After imports modules add this code
        ``color_text = use_colors`` then in the next line type this pieces
        ``mdsanima = color_text("I love Python", 39)`` of code. Next you can
        simple type this ``print(mdsanima)`` code for printing color text
        string output in your shell terminal window.

        Assigning a function by calling to variable, use this example code:

        .. code:: python

            from mdsanima_dev.colors import use_colors
            love = use_colors("I love Python", 86)
            devs = use_colors("App Development", 186)
            print(love, devs)

        You can alss use `machine <../tools/#function-machine>`_ function with
        this example code:

        .. code:: python

            from mdsanima_dev.colors import use_colors
            from mdsanima_dev.utils.tools import machine
            love = use_colors("I love Python", 74)
            devs = use_colors("App Development", 104)
            machine(love + " " + devs, 0.01)

    :screenshots:

        Want to see terminal screenshots from the sample code above along with
        cool show output thats we produced.
    """
    sx, xm, ex = _set_colors()

    return sx + str(color) + xm + text + ex


def print_colors(text: str = "mdsanima", color: int = 255, end=None) -> str:
    """This feature allows you to print colored text to the output of the
    console. Now the function works the same like print function.

    :param text: The text you want to use for color output in the console,
        defaults to ``mdsanima``.
    :type text: str, optional
    :param color: The color number you want to use for color output in the
        console, defaults to ``255``.
    :type color: int, optional
    :param end: End of line print, defaults to ``None``.
    :type end: str, optional
    :return: Printing colored string text output in the console.
    :rtype: str

    :usage:

        Assigning a function to a ``mdsanima`` variable. Instead of typing
        ``mdsanima`` you can assign any string in these variable like
        ``my_print`` or something else. Then call this funtion to returning
        printing colored text on the same line or next line.

        You can simple create test function like this sample code:

        .. code:: python

            from mdsanima_dev.colors import print_colors

            mdsanima = print_colors

            def colors_printing_test():
                mdsanima(color=42)
                mdsanima("example", 30, " ")
                mdsanima("colored text", 32, " ")
                mdsanima(text="development", color=38, end=" ")
                mdsanima("in one line", 86)
                mdsanima(color=50, text="your text", end=" ")
                mdsanima("example", color=80, end=" in ")
                mdsanima("colors", color=110, end=" ")
                mdsanima("more devs colors", color=140)
                mdsanima(color=48)

            colors_printing_test()
    """
    sx, xm, ex = _set_colors()

    return print(sx + str(color) + xm + text + ex, end=end)


def show_colors(number: bool = True) -> str:
    """Function prints all available colors with number or string example text.

    :param number: Show color number, defaults to ``True``.
    :type number: bool, optional
    :return: Print all colors number or string example in the console output.
    :rtype: str

    :usage:

        This is a function call. Type this sample code in your console:

        .. code:: python

            from mdsanima_dev.colors import show_colors
            show_colors(True)
            show_colors(False)
    """
    sx, xm, ex = _set_colors()

    # Get terminal size columns for center info print.
    terminal = os.get_terminal_size()

    # Calculation terminal size based on 22 count string from info variables.
    calculate_start = terminal.columns / 2 - 11
    calculate_end = terminal.columns / 2 - 11

    # Setup colors for info print.
    colors = [196, 208, 70, 11, 39]

    # Setup colors info variables.
    cts = sx + str(colors[4]) + xm + ("=" * int(calculate_start)) + ex
    cna = sx + str(colors[0]) + xm + "[" + ex
    csh = sx + str(colors[1]) + xm + " SHOW COLORS " + ex
    cdo = sx + str(colors[2]) + xm + " DONE COLORS " + ex
    cmd = sx + str(colors[3]) + xm + "STRING " + ex
    cnu = sx + str(colors[3]) + xm + "NUMBER " + ex
    cnc = sx + str(colors[0]) + xm + "]" + ex
    cte = sx + str(colors[4]) + xm + ("=" * int(calculate_end)) + ex

    # Print info colors options.
    if number == False:
        show = "mdsanima".ljust(9)
        print(cts + cna + csh + cmd + cnc + cte)
        done = "\n" + cts + cna + cdo + cmd + cnc + cte
    else:
        print(cts + cna + csh + cnu + cnc + cte)
        done = "\n" + cts + cna + cdo + cnu + cnc + cte

    # Print all colors numbers.
    for i in range(256):
        if number == True:
            show = "--> " + str(i).ljust(5)
        color = sx + str(i) + xm + show + ex
        print(color, sep=" ", end="", flush=True)

    return print(done)
