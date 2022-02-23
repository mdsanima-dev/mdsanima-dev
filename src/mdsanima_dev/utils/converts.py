#!/usr/bin/python3

# Copyritht © 2022 Marcin Różewski MDSANIMA


"""
Functions that may be useful in VFX and Animation Industry.
"""


import argparse
from mdsanima_dev import __version__ as ver


def _seconds():
    # setup seconds variables
    sec_in_min = 60
    sec_in_hrs = sec_in_min * sec_in_min

    return sec_in_min, sec_in_hrs


def frames_to_time_code(frames: int, fps: float) -> str:
    """
    Converting frames to time code ``00:00:00:00`` format.

    :param frames: total frames number
    :type frames: int
    :param fps: frames per seconds
    :type fps: float
    :return: time code format
    :rtype: str

    .. admonition:: USAGE PYTHON
        :class: hint

        *Assigning a function to a variable:*

    .. code:: python

        from mdsanima_dev.utils.converts import frames_to_time_code
        time_code = frames_to_time_code(240, 24)
        print(time_code)

    .. admonition:: USAGE SHELL
        :class: seealso

        *Command line shell console script:*

    .. code:: shell

        mdsanima-dev-frames-to-time-code --frames 240 --fps 24
        mdsanima-dev-frames-to-time-code --help

    .. admonition:: SEE ALSO
        :class: note

        Shell console script
        `mdsanima-dev-frames-to-time-code <shell_converts.html#command-mdsanima-dev-frames-to-time-code>`_
        converting directly on the command line.
    """
    # assigning a function to a variable setup seconds
    sec_in_min, sec_in_hrs = _seconds()

    # setup frames
    frames_in_sec = fps
    frames_in_hrs = frames // frames_in_sec
    frame_mod_fps = frames % frames_in_sec

    # calculating time code
    hrs = int(frames_in_hrs // sec_in_hrs)
    min = int(frames_in_hrs // sec_in_min % sec_in_min)
    sec = int(frames_in_hrs % sec_in_min)
    fra = int(frame_mod_fps)

    # formating time code
    time_code = str("%02d:%02d:%02d:%02d" % (hrs, min, sec, fra))

    return time_code


def time_code_to_frames(time_code: str, fps: float) -> int:
    """
    Converting time code ``00:00:00:00`` format to frames.

    :param time_code: time code format
    :type time_code: str
    :param fps: frames per seconds
    :type fps: float
    :return: total frames number
    :rtype: int

    .. admonition:: USAGE PYTHON
        :class: hint

        *Assigning a function to a variable:*

    .. code:: python

        from mdsanima_dev.utils.converts import time_code_to_frames
        frames = time_code_to_frames("00:00:10:00", 24)
        print(frames)

    .. admonition:: USAGE SHELL
        :class: seealso

        *Command line shell console script:*

    .. code:: shell

        mdsanima-dev-time-code-to-frames --time-code 00:00:10:00 --fps 24
        mdsanima-dev-time-code-to-frames --help

    .. admonition:: SEE ALSO
        :class: note

        Shell console script
        `mdsanima-dev-time-code-to-frames <shell_converts.html#command-mdsanima-dev-time-code-to-frames>`_
        converting directly on the command line.
    """
    # assigning a function to a variable setup seconds
    sec_in_min, sec_in_hrs = _seconds()

    # extract single values
    tc_hrs = int(time_code.split(":")[0])
    tc_min = int(time_code.split(":")[1])
    tc_sec = int(time_code.split(":")[2])
    tc_fra = int(time_code.split(":")[3])

    # setup and calculating frames
    frames_in_sec = fps
    tc_sec_min = tc_min * sec_in_min
    tc_sec_hrs = tc_hrs * sec_in_hrs
    tc_frames = tc_sec + tc_sec_min + tc_sec_hrs
    frames = round(tc_frames * frames_in_sec + tc_fra)

    return frames


def shell_frames_to_time_code() -> None:
    """
    Shell console script converting frames to time code ``00:00:00:00`` format.

    :param --frames: total frames number
    :type --frames: int
    :param --fps: frames per seconds
    :type --fps: float
    :return: time code format
    :rtype: None

    .. admonition:: USAGE SHELL
        :class: seealso

        *Command line shell console script:*

    .. code:: shell

        mdsanima-dev-frames-to-time-code --frames 240 --fps 24
        mdsanima-dev-frames-to-time-code --help

    .. admonition:: USAGE PYTHON
        :class: hint

        *Assigning a function to a variable:*

    .. code:: python

        from mdsanima_dev.utils.converts import frames_to_time_code
        time_code = frames_to_time_code(240, 24)
        print(time_code)


    .. admonition:: SEE ALSO
        :class: note

        Invoke function
        `frames_to_time_code <module_converts.html#function-frames-to-time-code>`_
        with a given arguments values.
    """
    # setup variables
    a_des = "Converting frames to time code 00:00:00:00 format."
    a_epi = "Copyritht \U000000A9 2022 Marcin Różewski MDSANIMA"
    h_frm = "total frames number"
    h_fps = "frames per seconds"

    # create the top level argument parser
    ap = argparse.ArgumentParser(description=a_des, epilog=a_epi)

    # add the arguments to the parser
    ap.add_argument("-v", "--version", action="version", version=ver)
    ap.add_argument("--frames", required=True, type=int, help=h_frm)
    ap.add_argument("--fps", required=True, type=float, help=h_fps)

    # calculating time code
    args = ap.parse_args()
    time_code = frames_to_time_code(args.frames, args.fps)
    print(time_code)


def shell_time_code_to_frames() -> None:
    """
    Shell console script converting time code ``00:00:00:00`` format to frames.

    :param --time-code: time code format
    :type --time-code: str
    :param --fps: frames per seconds
    :type --fps: float
    :return: total frames number
    :rtype: None

    .. admonition:: USAGE SHELL
        :class: seealso

        *Command line shell console script:*

    .. code:: shell

        mdsanima-dev-time-code-to-frames --time-code 00:00:10:00 --fps 24
        mdsanima-dev-time-code-to-frames --help

    .. admonition:: USAGE PYTHON
        :class: hint

        *Assigning a function to a variable:*

    .. code:: python

        from mdsanima_dev.utils.converts import time_code_to_frames
        frames = time_code_to_frames("00:00:10:00", 24)
        print(frames)


    .. admonition:: SEE ALSO
        :class: note

        Invoke function
        `time_code_to_frames <module_converts.html#function-time-code-to-frames>`_
        with a given arguments values.
    """
    # setup variables
    a_des = "Converting time code 00:00:00:00 format to frames."
    a_epi = "Copyritht \U000000A9 2022 Marcin Różewski MDSANIMA"
    h_frm = "time code format"
    h_fps = "frames per seconds"

    # create the top level argument parser
    ap = argparse.ArgumentParser(description=a_des, epilog=a_epi)

    # add the arguments to the parser
    ap.add_argument("-v", "--version", action="version", version=ver)
    ap.add_argument("--time-code", required=True, type=str, help=h_frm)
    ap.add_argument("--fps", required=True, type=float, help=h_fps)

    # calculating frames
    args = ap.parse_args()
    frames = time_code_to_frames(args.timecode, args.fps)
    print(frames)
