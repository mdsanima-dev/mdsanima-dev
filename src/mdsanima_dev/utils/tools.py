"""
# Tools Module

There are some useful functions that I usually use for python coding.
"""

import time
import requests
from time import sleep
from mdsanima_dev.colors import get_complex_color


def read_file(file_path: str) -> str:
    """
    Function reads the file and splits it into separate lines.

    Args:
        file_path (str): File path to read and split.
    Returns:
        [list, str, int]: Function returns a list of lines in the string by
                            line and the total number of lines.
    Usage:
    .. code::
        lines, lines_len = read_file(file_path)
    """
    with open(file_path, 'r', encoding='utf-8') as r:
        lines = r.read().splitlines()
    lines_len = len(lines)

    return lines, lines_len


def append_file(file_path: str, data: str) -> str:
    """
    Function save data into file.

    Args:
        file_path (str): File path to save data with append mode.
        data (str): Data to write into file.
    Usage:
    .. code::
        append_file(file_path, data)
    """
    with open(file_path, 'a', encoding='utf-8') as w:
        w.write(str(data) + '\n')


def get_response_json(url: str):
    """
    This function get response json dictionary from url.

    Args:
        url (str): Url address to get response json.
    Returns:
        (json): Dictionary.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def machine(text: str, speed: int = 0.1) -> str:
    """
    This function printing text as a typing on screen at intervals time after
    each letter.

    Args:
        text (string): Text to be entered as an animation.
        speed (int, optional): Time after each print letter. Defaults to 0.1.
    Returns:
        str: Printing text as an animation.
    """
    machine = (str(text) + '\n')
    for chars in machine:
        print(chars, end='', flush=True)
        time.sleep(speed)


class progress:
    """
    Progress bar animation.

    Usage:
        Animation progress bar.
    .. code::
        progress().progress_bar(100, 0.01)

        Animation progress bar with indiwidual percent color.
    .. code::
        progress(percent_color=232).progress_bar(100, 0.01)
    """
    def __init__(self,
            txt_first: str = 'get data', txt_end: str = 'done',
            txt_first_color: int = 112, txt_end_color: int = 192,
            bar_sten_color: int = 203, bar_color: int = 113,
            percent_color: int = 243
        ) -> str:
        """
        Initial function. These values can be set individually to the
        different progress bar.

        Args:
            txt_first (str, optional): First text. Defaults to 'get data'.
            txt_end (str, optional): End text. Defaults to 'done'.
            txt_first_color (int, optional): Color first text. Defaults to 112.
            txt_end_color (int, optional): Color end text. Defaults to 192.
            bar_sten_color (int, optional): Color parenthesis. Defaults to 203.
            bar_color (int, optional): Color bar progress. Defaults to 113.
            percent_color (int, optional): Color percent text. Defaults to 243.
        Returns:
            str: One line progress bar animation.
        """
        self.mds = get_complex_color
        self.txt_first = txt_first
        self.txt_end = txt_end
        self.txt_first_clr = txt_first_color
        self.txt_end_clr = txt_end_color
        self.bar_sten_clr = bar_sten_color
        self.bar_clr = bar_color
        self.percent_clr = percent_color
        self.symbol = '\u25a0'
        bar_st = '\u258c'
        bar_en = '\u2590'

    def progress_conf(self, percent: int, width: int) -> str:
        """
        This function is a configuration of the progress bar. You can use
        this function if you want to make your own loop for.

        Args:
            percent (int): Percent value of the progress bar.
            width (int): Width of the progress bar.
        Returns:
            str: One line progress bar.
        """
        start = width * percent // 100
        end = width - start

        s_start = str(self.symbol * start)
        s_end = str(' ' * end)
        perc = str(percent) + '%'

        self.mds('\r' + self.txt_first.upper(), self.txt_first_clr, ' ')
        self.mds('[', self.bar_sten_clr, '')
        self.mds(s_start, self.bar_clr, '')
        self.mds(s_end, self.bar_clr, '')
        self.mds(']', self.bar_sten_clr, '')
        self.mds(' ' + perc, self.percent_clr, '')

    def progress_bar(self, width: int, speed: int) -> str:
        """
        This function pringint animation of progress bar in one line.

        Args:
            width (int): Width of the progress bar.
            speed (int): Speed of the progress bar left to right.
        Returns:
            str: One line progress bar with color and animation.
        """
        for i in range(101):
            self.progress_conf(i, width)
            sleep(speed)
        self.mds(' ' + self.txt_end.upper(), self.txt_end_clr)
