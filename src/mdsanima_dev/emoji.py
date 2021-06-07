"""
# Emoji Module

Request data of Emoji from unicode.org and store json dict all data.
"""

import json
import requests
import pathlib
from datetime import datetime
from colors import get_complex_color

HERE = pathlib.Path(__file__).parent

emoji_lis_url = 'http://www.unicode.org/emoji/charts/full-emoji-list.html'
emoji_mod_url = 'http://www.unicode.org/emoji/charts/full-emoji-modifiers.html'


def emoji_get_url_data(emoji_url):
    """
    This function request emoji data url and waiting raise for status if
    status ok returning data text for further processing.

    Args:
        emoji_url (str): Link to emoticons.
    Returns:
        str: Html code as string text.
    Usage:
        Assigning function calling to a variable.
    .. code::
        eud = emoji_get_url_data(emoji_lis_url)
    """
    url = str(emoji_url)
    res = requests.get(url)
    res.raise_for_status()
    emoji_url_data = res.text

    return emoji_url_data


def emoji_clean_url_data(
        bhead:bool=False,
        mhead:bool=False,
        ucode:bool=False,
        emoji:bool=False,
        ename:bool=False,
        emoji_url:str=emoji_lis_url
    ) -> dict:
    """
    This funciton is used to clean up previously requested data and store this
    data in dictionary `.json` file in `json` folder. Default this function
    save a `emoji-list` data. You can use parameter to debug what data is
    saved. Defaults for the end this function printing only stats in colors.
    Also debug mode show cool colors from extracting url.

    Args:
        bhead (bool, optional): Debug mode show big head. Defaults to False.
        mhead (bool, optional): Debug mode show medium head. Defaults to False.
        ucode (bool, optional): Debug mode show unicode. Defaults to False.
        emoji (bool, optional): Debug mode show emoji. Defaults to False.
        ename (bool, optional): Debug mode show emoji name. Defaults to False.
        emoji_url (str, optional): Link to extract. Defaults to emoji_lis_url.
    Returns:
        dict: Save dictionary in to `.json` file.
    Usage:
        Calling function and specific parameter to extract two url.
    .. code::
        emoji_clean_url_data(emoji_url=emoji_lis_url)
        emoji_clean_url_data(emoji_url=emoji_mod_url)
        emoji_clean_url_data(bhead=True)
    """
    mds = get_complex_color

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

