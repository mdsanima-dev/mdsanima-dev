"""
There are some useful functions that I usually use for python programing.
"""

import time
import requests
from time import sleep
from mdsanima_dev.colors import get_complex_color


def read_file(file_path: str) -> str:
    """
    Function reads the file and splits it into separate lines.

    :param file_path: file path to read and split
    :type file_path: str
    :return: list of lines in the string by line and the total number of lines
    :rtype: str
    :usage:

        assigning function calling to a variable

        .. code:: python

            lines, lines_len = read_file(file_path)
    """
    with open(file_path, 'r', encoding='utf-8') as r:
        lines = r.read().splitlines()
    lines_len = len(lines)

    return lines, lines_len


def append_file(file_path: str, data: str) -> str:
    """
    Function save data into file.

    :param file_path: file path to save data with append mode
    :type file_path: str
    :param data: data to write into file one line
    :type data: str
    :usage:

        function calling

        .. code:: python

            append_file(file_path, data)
    """
    with open(file_path, 'a', encoding='utf-8') as w:
        w.write(str(data) + '\n')


def get_response_json(url: str):
    """
    Function get response json dictionary from url.

    :param url: url address to get response json
    :type url: str
    :return: dictionary data
    :rtype: json
    :usage:

        function calling

        .. code:: python

            get_response_json(url)
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def machine(text: str, speed: int = 0.1) -> str:
    """
    Function printing text as a typing on screen at intervals time after
    each letter.

    :param text: text to be entered as an animation
    :type text: str
    :param speed: time after each print letter, defaults to 0.1
    :type speed: int, optional
    :return: printing text in the console as an animation
    :rtype: str
    :usage:

        function calling

        .. code:: python

            machine('I love Python')
    """
    machine = (str(text) + '\n')
    for chars in machine:
        print(chars, end='', flush=True)
        time.sleep(speed)


class progress:
    """
    Progress bar animation.

    :usage:

        animation progress bar

        .. code:: python

            progress().progress_bar(100, 0.01)

        animation progress bar with indiwidual percent color

        .. code:: python

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

        :param txt_first: first text, defaults to 'get data'
        :type txt_first: str, optional
        :param txt_end: end text, defaults to 'done'
        :type txt_end: str, optional
        :param txt_first_color: color first text, defaults to 112
        :type txt_first_color: int, optional
        :param txt_end_color: color end text, defaults to 192
        :type txt_end_color: int, optional
        :param bar_sten_color: color parenthesis, defaults to 203
        :type bar_sten_color: int, optional
        :param bar_color: color bar progress, defaults to 113
        :type bar_color: int, optional
        :param percent_color: color percent text, defaults to 243
        :type percent_color: int, optional
        :return: one line progress bar animation
        :rtype: str
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

        :param percent: percent value of the progress bar
        :type percent: int
        :param width: width of the progress bar
        :type width: int
        :return: one line progress bar
        :rtype: str
        """
        start = width * percent // 100
        end = width - start

        s_start = str(self.symbol * start)
        s_end = str(' ' * end)
        perc = str(percent) + '%'

        self.mds('\r' + self.txt_first.upper(), self.txt_first_clr, ' ')
        self.mds(perc.rjust(4), self.percent_clr, '')
        self.mds('[', self.bar_sten_clr, '')
        self.mds(s_start, self.bar_clr, '')
        self.mds(s_end, self.bar_clr, '')
        self.mds(']', self.bar_sten_clr, '')

    def progress_bar(self, width: int, speed: int) -> str:
        """
        This function pringint animation of progress bar in one line.

        :param width: width of the progress bar
        :type width: int
        :param speed: speed of the progress bar left to right
        :type speed: int
        :return: one line progress bar with color and animation
        :rtype: str
        """
        for i in range(101):
            self.progress_conf(i, width)
            sleep(speed)
        #self.mds(' ' + self.txt_end.upper(), self.txt_end_clr)
