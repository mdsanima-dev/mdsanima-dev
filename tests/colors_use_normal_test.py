# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Testing colors module function for using default colors."""


from __future__ import annotations

from mdsanima_dev import colors
from mdsanima_dev.colors import use_normal_mode


LOVE_PYTHON = "I love Python"
NO_EXIST = "no_exsit_color_name"
INFO_KEY_ERROR = colors.INFO_KEY_ERROR
DEFAULT_NORMAL = colors.DEFAULT_NAMES_NORMAL
INFO_ERROR = INFO_KEY_ERROR + " " + str(DEFAULT_NORMAL.keys()) + "\n"


def test_use_default():
    ret = use_normal_mode()
    assert ret == "\x1b[38;5;255mmdsanima\x1b[0m"


def test_use_fg_number():
    ret = use_normal_mode(LOVE_PYTHON, 86)
    assert ret == "\x1b[38;5;86mI love Python\x1b[0m"


def test_use_fg_name_red():
    ret = use_normal_mode(LOVE_PYTHON, "red")
    assert ret == "\x1b[38;5;196mI love Python\x1b[0m"


def test_use_fg_name_no_exist(capsys):
    use_normal_mode(LOVE_PYTHON, NO_EXIST)
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR


def test_use_fg_number_bg_number():
    ret = use_normal_mode(LOVE_PYTHON, 45, 196)
    assert ret == "\x1b[38;5;45m\x1b[48;5;196mI love Python\x1b[0m"


def test_use_fg_number_bg_name_organe():
    ret = use_normal_mode(LOVE_PYTHON, 27, "orange")
    assert ret == "\x1b[38;5;27m\x1b[48;5;208mI love Python\x1b[0m"


def test_use_fg_number_bg_name_no_exist(capsys):
    use_normal_mode(LOVE_PYTHON, 199, NO_EXIST)
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR


def test_use_fg_name_rose_bg_number():
    ret = use_normal_mode(LOVE_PYTHON, "rose", 33)
    assert ret == "\x1b[38;5;203m\x1b[48;5;33mI love Python\x1b[0m"


def test_use_fg_name_no_exist_bg_number(capsys):
    use_normal_mode(LOVE_PYTHON, NO_EXIST, 86)
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR


def test_use_fg_name_blue_bg_name_red():
    ret = use_normal_mode(LOVE_PYTHON, "blue", "red")
    assert ret == "\x1b[38;5;27m\x1b[48;5;196mI love Python\x1b[0m"


def test_use_fg_name_cyan_bg_name_no_exist(capsys):
    use_normal_mode(LOVE_PYTHON, "cyan", NO_EXIST)
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR


def test_use_fg_name_no_exist_bg_name_red(capsys):
    use_normal_mode(LOVE_PYTHON, NO_EXIST, "red")
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR


def test_use_fg_name_no_exist_bg_name_no_exist(capsys):
    use_normal_mode(LOVE_PYTHON, NO_EXIST, NO_EXIST)
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR
