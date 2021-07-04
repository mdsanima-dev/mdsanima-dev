"""
Request data of Emoji from https://unicode.org and store json dict all data.

.. important::

    This module only get data from this two links.

    - `Full Emoji List <https://unicode.org/emoji/charts/full-emoji-list.html>`_
    - `Full Emoji Modifiers <https://unicode.org/emoji/charts/full-emoji-modifiers.html>`_
"""

import json
import requests
import pathlib
from datetime import datetime
from mdsanima_dev import colors
from mdsanima_dev.utils.table import table
from mdsanima_dev.utils.table import table_elem

HERE = pathlib.Path(__file__).parent

emoji_lis_url = 'http://www.unicode.org/emoji/charts/full-emoji-list.html'
emoji_mod_url = 'http://www.unicode.org/emoji/charts/full-emoji-modifiers.html'


def emoji_get_url_data(emoji_url: str) -> str:
    """
    This function request emoji data url and waiting raise for status.
    If status ok returning data text for further processing.

    :param emoji_url: link to emoticons
    :type emoji_url: str
    :return: html code as string text
    :rtype: str
    :usage: assigning function calling to a variable

        .. code:: python

            emoji_url_data = emoji_get_url_data(emoji_lis_url)

    .. note::
        This function only I used for request data in function
        `emoji_clean_url_data <#function-emoji-clean-url-data>`_
    """
    url = str(emoji_url)
    res = requests.get(url)
    res.raise_for_status()
    emoji_url_data = res.text

    return emoji_url_data


def emoji_clean_url_data(
        bhead: bool = False, mhead: bool = False, ucode: bool = False,
        emoji: bool = False, ename: bool = False,
        emoji_url: str = emoji_lis_url
    ) -> dict:
    """
    This funciton is used to clean up previously requested data and store in
    dictionary ``.json`` file and saved in to json folder. These folder also
    included in python package. Default save a first link ``emoji_lis_url``,
    the second link is the ``emoji_mod_url`` which are included in this module
    as a variable. If you need to download new data, you can use just these
    two variables only.

    .. admonition:: See also
        :class: seealso

        This two link on `important <#module-mdsanima_dev.emoji>`_ in the
        beginning on this document.

    You can use parameter to debug what data is saved. By defaults for the end
    this function printing only stats in colors. If you want to see use debug
    parameters. Debug mode show cool colors from extracting url.

    :param bhead: debug mode show big head, defaults to ``False``
    :type bhead: bool, optional
    :param mhead: debug mode show medium head, defaults to ``False``
    :type mhead: bool, optional
    :param ucode: debug mode show unicode, defaults to ``False``
    :type ucode: bool, optional
    :param emoji: debug mode show emoji, defaults to ``False``
    :type emoji: bool, optional
    :param ename: debug mode show emoji name, defaults to ``False``
    :type ename: bool, optional
    :param emoji_url: link to extract data, defaults to ``emoji_lis_url``
    :type emoji_url: str, optional
    :return: save dictionary data in to ``.json`` file
    :rtype: dict
    :usage:

        function call extract and save defaults data debug mode

        .. code:: python

            emoji_clean_url_data(bhead=True)

        function call extract and save second link debug mode

        .. code:: python

            emoji_clean_url_data(emoji_url=emoji_mod_url, mhead=True)
    """
    mds = colors.get_complex_color

    # Assigning function calling to a variable.
    eud = emoji_get_url_data(emoji_url)
    lines = eud.splitlines()
    lines_len = len(lines)

    # Initial default variables.
    cnt_bighead = 0
    cnt_mediumhead = 0
    cnt_emoji = 0
    emoji_version = ''

    n_line = '\n'
    l_line = ' '

    # Checking whether to show debug mode.
    bhead_end = n_line if bhead else l_line
    mhead_end = n_line if mhead else l_line
    ucode_end = n_line if ucode else l_line
    emoji_end = n_line if emoji else l_line
    ename_end = n_line if ename else l_line

    # Initial two empty dictionary emo is for all data, emodt is for stats.
    emo = {}
    emodt = {}

    # Cleaning and extracting all requested data.
    for i in range(15, lines_len):
        line = lines[i]
        line_split = line.rsplit("'")

        # Search version.
        if line.find("h1>") >= 1:
            emo_version = line.replace("<h1>", "")\
                .replace("</h1>", "").split(", ")
            emoji_version = emo_version[1]
            emoji_list_dt = emo_version[0]

        # Search big head.
        if line.find("'bighead'") >= 1:
            cnt_bighead += 1
            emo_bighead = line_split[7]\
                .replace("-", " ").replace("&amp;_", "")

            # Printing debug mode in colors.
            mds('\rBIG HEAD'.ljust(13), 34, '-> ')
            mds(emo_bighead.ljust(94), 88, str(bhead_end))

            # Add to dictionary.
            emo[emo_bighead] = {}

        # Search medium head.
        if line.find("'mediumhead'") >= 1:
            cnt_mediumhead += 1
            emo_mediumhead = line_split[7]\
                .replace("-", " ").replace("&amp;_", "")\
                .replace(" ", "_")

            # Printing debug mode in colors.
            mds('\r  MEDIUM'.ljust(13), 24, '-> ')
            mds(emo_mediumhead.ljust(94), 36, str(mhead_end))

            # Add to dictionary.
            emo[emo_bighead][emo_mediumhead] = {}

        # Search unicode value.
        if line.find("'code'") >= 1:
            emo_code_list = []
            emo_code = line_split[6]\
                .replace(">", "").replace("</a</td", "")

            # Add new string to unicode.
            for co_de in emo_code.split(' '):
                ucode_ck = 'U000' if len(co_de)==7 else 'U0000'
                emo_code_list.append(co_de.replace("U+", ucode_ck))
            emo_code = str(emo_code_list).replace(",", "")\
                .replace("[", "").replace("]", "")\
                .replace("'", "")

            # Printing debug mode in colors.
            mds('\r    CODE'.ljust(13), 100, '=> ')
            mds(emo_code.ljust(94), 239, str(ucode_end))

        # Search emoji icons.
        if line.find("'chars'") >= 1:
            cnt_emoji += 1
            emo_emoji = line_split[2]\
                .replace(">", '').replace("</td", '')

            # Printing debug mode in colors and printing emoji.
            mds('\r      EMOJI'.ljust(13), 149, '=> ')
            print(emo_emoji.ljust(94), end=emoji_end)

        # Search emoji name.
        if line.find("class='name'") >= 1:
            emo_name = line_split[2]\
                .replace(">", '').replace("</td", '')\
                .replace("-", ' ').replace(":", "")\
                .replace(",", '').replace(".", '')\
                .replace("(", '').replace(")", '')\
                .replace("’", '').replace("“", '')\
                .replace("”", '').replace("&amp;", '')\
                .replace("   ", ' ').replace("  ", ' ')\
                .replace("!", '').replace(" ", "_").lower()
            if emo_name.lower() == str(" colspan="):
                part = line_split[14]\
                    .replace(">", '').replace("</td", '')\
                    .partition(' ')
                emo_name = part[2]\
                    .replace(":", "").replace(" ", '_')

            # Printing debug mode in colors.
            mds('\r      NAME'.ljust(13), 148, '=> ')
            mds(emo_name.ljust(94), 244, str(ename_end))

            # Add to dictionary.
            emo[emo_bighead][emo_mediumhead][emo_name] = {
                'number': cnt_emoji, 'code': emo_code, 'emoji': emo_emoji
                }

    # Printing end statistic in color.
    mds('\r' + '-' * 30, 228)
    mds('\r' + 'FOUND BIG HEAD'.ljust(20), 34, ' -> ')
    mds(str(cnt_bighead).ljust(94), 32)
    mds('FOUND MEDIUM HEAD'.ljust(20), 31, ' -> ')
    mds(str(cnt_mediumhead).ljust(10), 29)
    mds('FOUND EMOJI'.ljust(20), 149, ' -> ')
    mds(str(cnt_emoji).ljust(10), 197)
    mds('EMOJI VERSION'.ljust(20), 106, ' -> ')
    mds(str(emoji_version).ljust(10), 112)
    mds(str(emoji_list_dt)[:20].ljust(20).upper(), 117, ' -> ')
    mds('DONE'.ljust(18), 107)
    mds('-' * 30, 228)

    # Data and time when json file is generated.
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Add to dictionary.
    emodt['emoji_data'] = {
        'emoji_version': emoji_version,
        'emoji_src': emoji_list_dt,
        'emoji_url': emoji_lis_url,
        'json_generated_dt': now
        }

    emodt['emoji_stats'] = {
        'big_head': cnt_bighead,
        'medium_head': cnt_mediumhead,
        'emoji': cnt_emoji
    }

    # Joining two dictionary.
    emo_dic = {'emo': emo, 'src': emodt}

    # Initial variable and checking what kind of url is generated.
    em_li = 'json/emoji-list.json'
    em_mo = 'json/emoji-modifiers.json'
    wri_emo = em_li if emoji_url==emoji_lis_url else em_mo

    # Saving the extracting data from requested url.
    with open(HERE / wri_emo, 'w', encoding='utf-8') as w:
        json.dump(emo_dic, w, ensure_ascii=False)


def emoji_load_json_data() -> dict:
    """
    This function loading the json data generated on previous function
    `emoji_clean_url_data <#function-emoji-clean-url-data>`_.

    :return: dictionary json all emoji with joining two json ``emoji_list``
        and ``emoji_modifiers``
    :rtype: dict
    :usage: assigning function calling to a variable

        .. code:: python

            emo = emoji_load_json_data()
    """
    with open(HERE / 'json/emoji-list.json', 'r', encoding='utf-8') as dt:
        emo_lis = json.load(dt)
    with open(HERE / 'json/emoji-modifiers.json', 'r', encoding='utf-8') as dt:
        emo_mod = json.load(dt)

    # Joining two json dictionary.
    emo = {'emoji_list': emo_lis, 'emoji_modifiers': emo_mod}

    return emo


class emoji:
    """
    This class has methods for printing various emoji functions.

    .. warning::
        Class `show <#class-show>`_ print all emoji with calling methods inside
        this class. Recommended only used ``class show(emoji)`` to print emoji
        big head, medium head, or just only one emoji.
    """
    def __init__(self) -> str:
        self.mds = colors.get_complex_color

    def emo_stats(self) -> str:
        """
        This method printing the statistic of emoji in the table with colored
        table and colored text.
        """
        # Get all value of emoji in json files.
        e_stats = self.emo[self.emo_list]['src']['emoji_stats']
        e_data = self.emo[self.emo_list]['src']['emoji_data']
        e_heder = str(self.emo_list).replace("_", ' ').upper().ljust(21)

        # Initial table color variable.
        t_col = 82

        # Make table.
        self.head(e_heder.ljust(46), 32, False, True, t_col)
        self.cont('BIG HEAD'.ljust(13), str(e_stats['big_head'])\
            .ljust(29), 149, 107, True, True, t_col)
        self.cont('MEDIUM HEAD'.ljust(13), str(e_stats['medium_head'])\
            .ljust(29), 215, 179, True, True, t_col)
        self.cont('EMOJI COUNTS'.ljust(13), str(e_stats['emoji'])\
            .ljust(29), 203, 167, True, True, t_col)
        self.cont('VERSION'.ljust(13), str(e_data['emoji_version'])[1:]\
            .ljust(29), 161, 125, True, True, t_col)
        self.cont('LIST'.ljust(13), str(e_data['emoji_src'])\
            .ljust(29), 111, 104, True, True, t_col)
        self.cont('JSON DATA GEN'.ljust(13), str(e_data['json_generated_dt'])\
            .ljust(29), 111, 104, True, False, t_col)

    def emo_big_head(self) -> str:
        """
        This method printing all big head text value of emoji in the table with
        colored table and colored text.
        """
        # Get all value of emoji in json files.
        e_head = self.emo[self.emo_list]['emo']
        e_heder = str('BIG HEAD').upper().ljust(21)

        # Initial table color variable.
        t_col = 106

        # Make table.
        self.head(e_heder.ljust(30), 64, False, True, t_col)
        for key_bh in e_head:
            self.cont(str(key_bh).ljust(23),
                str(len(e_head[key_bh]))\
                .ljust(3), 149, 215, True, True, t_col)
        self.tab(t_col).bot(32)

    def emo_medium_head(self) -> str:
        """
        This method printing all medium head text value of emoji in the table
        with colored table and colored text.
        """
        # Get all value of emoji in json files.
        e_head = self.emo[self.emo_list]['emo']
        e_heder = str('MEDIUM HEAD').upper().ljust(21)

        # Initial table color variable.
        t_col = 106

        # Make table.
        self.head(e_heder.ljust(30), 64, False, False, t_col)
        for key_bh in e_head:
            self.tab(t_col).top(32)
            self.cont(str(key_bh).ljust(23),
                str(len(e_head[key_bh]))\
                .ljust(3), 149, 215, True, True, t_col)
            for key_mh in e_head[key_bh]:
                self.cont(str(key_mh).ljust(23),
                    str(len(e_head[key_bh][key_mh]))\
                    .ljust(3), 215, 167, True, True, t_col)
            self.tab(t_col).bot(32)

    def emo_all(self, number: bool = False, names: bool = False) -> str:
        """
        This method prints all available emojis, sorted by heads. You can use
        arguments to print number of emoji and names of emoji.

        :param number: print emoji numbers, defaults to ``False``
        :type number: bool, optional
        :param names: print emoji names, defaults to ``False``
        :type names: bool, optional
        :return: prints all available emojis
        :rtype: str
        """
        # Get all value of emoji in json files.
        e_head = self.emo[self.emo_list]['emo']
        e_heder = str('EMOJI').upper().ljust(21)

        # Initial table color variable.
        t_col = 197

        # Make table.
        self.head(e_heder.ljust(30), 86, False, False, t_col)
        for key_bh in e_head:
            for key_mh in e_head[key_bh]:
                self.tab(t_col).top(32)
                self.cont(str(key_mh).ljust(23),
                     str(len(e_head[key_bh][key_mh]))\
                     .ljust(3), 215, 167, True, True, t_col)
                self.tab(t_col).bot(32)
                for name in e_head[key_bh][key_mh]:
                    emo_num = str(e_head[key_bh][key_mh][name]['number'])
                    emo_emo = str(e_head[key_bh][key_mh][name]['emoji'])
                    check = (self.mds('[', 197, ''),\
                        self.mds(emo_num, 62, ' -> '),\
                        self.mds(emo_emo, end=''),\
                        self.mds(']', 197, '')) if number else print(emo_emo,\
                        end='')
                    check_name = (print(' => ', end=''),\
                        self.mds(str(name), 243, '\n')) if names else ''
                print('\n')

    def emo_head(self, bhead: str, mhead: str,
            number: bool = False, names: bool = False
        ) -> str:
        """
        This method printing all emoji in to a given group.

        :param bhead: name of big head emoji
        :type bhead: str
        :param mhead: name of medium head emoji
        :type mhead: str
        :param number: print emoji numbers, defaults to ``False``
        :type number: bool, optional
        :param names: print emoji names, defaults to ``False``
        :type names: bool, optional
        :return: printing all emoji in to a given group
        :rtype: str
        """
        # Get all value of emoji in json files.
        e_head = self.emo[self.emo_list]['emo']

        # Initial table color variable.
        t_col = 34
        length = len(mhead) + 11

        # Make table.
        self.tab(t_col).top(length)
        self.tab(t_col).con(length, 'EMOJI', mhead, 86, 197)
        self.tab(t_col).bot(length)
        name = e_head[bhead][mhead]
        for emo in name:
            # print(emo)
            emo_num = str(name[emo]['number'])
            emo_emo = str(name[emo]['emoji'])
            check = (self.mds('[', 197, ''),\
                self.mds(emo_num, 62, ' -> '),\
                self.mds(emo_emo, end=''),\
                self.mds(']', 197, '')) if number else print(emo_emo, end='')
            check_name = (print(' => ', end=''),\
                self.mds(str(emo), 243, '\n')) if names else ''
        # chk = '' if names else '\r'
        chk = 1 if names else print('\r')

    def emoji(self, number: int, end: str = '') -> str:
        """
        Printing only one emoji.

        :param number: emoji number to printing
        :type number: int
        :param end: ends of print, defaults to empty string, that's set a print
            two or more emoji in the same line.
        :type end: str, optional
        :return: print one emoji
        :rtype: str
        """
        # Get all value of emoji in json files.
        e_head = self.emo[self.emo_list]['emo']

        # Searching of specific number of emoji and break.
        for key_bh in e_head:
            for key_mh in e_head[key_bh]:
                for key_name in e_head[key_bh][key_mh]:
                    for val in e_head[key_bh][key_mh][key_name].values():
                        if val == number:
                            print(e_head[key_bh][key_mh][key_name]['emoji'],\
                                end=end)
                            break


class show(emoji):
    """
    This class show all emoji or just only one. See documentation for more
    information and screenshot.

    :param emoji: master class of emoji
    :type emoji: class
    :usage:

        assigning function calling to a variable

        .. code:: python

            show = show('emoji_list')
            show.emo_stats()
            show.emo_big_head()
            show.emo_medium_head()
            show.emo_all(True, False)
            show.emo_head('objects', 'music', True, True)
            show.emoji(986)

        or just calling method with arguments in to class

        .. code:: python

            show('emoji_modifiers').emo_head('people_body', 'hands')
    """
    def __init__(self, emo_list: str) -> emoji:
        """
        Initial function to show emoji on various method.

        :param emo_list: use only `emoji_list` and `emoji_modifiers`
        :type emo_list: str
        :return: printing value of specific emoji method
        :rtype: emoji
        """
        self.emo = emoji_load_json_data()
        self.mds = colors.get_complex_color
        self.head = table().headers
        self.cont = table().content
        self.emo_list = emo_list
        self.tab = table_elem
