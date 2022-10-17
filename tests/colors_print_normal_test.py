# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Testing colors module function for using default colors print outputs."""


from __future__ import annotations

from mdsanima_dev import colors
from mdsanima_dev.colors import print_normal_mode


LOVE_PYTHON = "I love Python"
NO_EXIST = "no_exsit_color_name"
INFO_KEY_ERROR = colors.INFO_KEY_ERROR
DEFAULT_NORMAL = colors.DEFAULT_NAMES_NORMAL
INFO_ERROR = INFO_KEY_ERROR + " " + str(DEFAULT_NORMAL.keys()) + "\nNone\n"


def test_print_return():
    ret = print_normal_mode()
    assert ret == None


def test_print_default(capsys):
    print_normal_mode()
    out, _ = capsys.readouterr()
    assert out == "\x1b[38;5;255mmdsanima\x1b[0m\n"


def test_print_fg_number(capsys):
    print_normal_mode(LOVE_PYTHON, 208)
    out, _ = capsys.readouterr()
    assert out == "\x1b[38;5;208mI love Python\x1b[0m\n"


def test_print_fg_name_fuchsia(capsys):
    print_normal_mode(LOVE_PYTHON, "fuchsia")
    out, _ = capsys.readouterr()
    assert out == "\x1b[38;5;177mI love Python\x1b[0m\n"


def test_print_fg_name_no_exist(capsys):
    print_normal_mode(LOVE_PYTHON, NO_EXIST)
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR


def test_print_fg_number_bg_number(capsys):
    print_normal_mode(LOVE_PYTHON, 196, 33)
    out, _ = capsys.readouterr()
    assert out == "\x1b[38;5;196m\x1b[48;5;33mI love Python\x1b[0m\n"


def test_print_fg_number_bg_name_sky(capsys):
    print_normal_mode(LOVE_PYTHON, 196, "sky")
    out, _ = capsys.readouterr()
    assert out == "\x1b[38;5;196m\x1b[48;5;39mI love Python\x1b[0m\n"


def test_print_fg_number_bg_name_no_exist(capsys):
    print_normal_mode(LOVE_PYTHON, 202, NO_EXIST)
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR


def test_print_fg_name_teal_bg_number(capsys):
    print_normal_mode(LOVE_PYTHON, "teal", 216)
    out, _ = capsys.readouterr()
    assert out == "\x1b[38;5;43m\x1b[48;5;216mI love Python\x1b[0m\n"


def test_print_fg_name_no_exist_bg_number(capsys):
    print_normal_mode(LOVE_PYTHON, NO_EXIST, 99)
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR


def test_print_fg_name_amber_bg_name_indigo(capsys):
    print_normal_mode(LOVE_PYTHON, "amber", "indigo")
    out, _ = capsys.readouterr()
    assert out == "\x1b[38;5;215m\x1b[48;5;105mI love Python\x1b[0m\n"


def test_print_fg_name_green_bg_name_no_exist(capsys):
    print_normal_mode(LOVE_PYTHON, "green", NO_EXIST)
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR


def test_print_fg_name_no_exist_bg_name_lime(capsys):
    print_normal_mode(LOVE_PYTHON, NO_EXIST, "lime")
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR


def test_print_fg_name_no_exist_bg_name_no_exist(capsys):
    print_normal_mode(LOVE_PYTHON, NO_EXIST, NO_EXIST)
    out, _ = capsys.readouterr()
    assert out == INFO_ERROR
