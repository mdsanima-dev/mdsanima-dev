#!/usr/bin/python3

# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Functions that may be useful in VFX and Animation Industry."""


import argparse
import sys

from mdsanima_dev import __version__


def get_seconds() -> int:
    """Calculating the number of seconds in an hour.

    :return: Number of seconds in hour and minute.
    :rtype: int
    """
    # setup seconds variables
    sec_in_min = 60
    sec_in_hrs = sec_in_min * sec_in_min

    return sec_in_min, sec_in_hrs


def frames_to_timecode(frames: int, fps: float) -> str:
    """Converting frames number to timecode ``00:00:00:00`` format.

    :param frames: Total frames number.
    :type frames: int
    :param fps: Frames per seconds.
    :type fps: float
    :return: Timecode format.
    :rtype: str

    .. admonition:: USAGE PYTHON
        :class: hint

        *Assigning a function to a variable:*

    .. code:: python

        from mdsanima_dev.utils.converts import frames_to_timecode
        timecode = frames_to_timecode(240, 24)
        print(timecode)

    .. admonition:: USAGE SHELL
        :class: seealso

        *Command line shell console script:*

    .. code:: shell

        mdsanima-converts frames-to-timecode --frames 240 --fps 24
        mdsanima-converts frames-to-timecode --help

    .. admonition:: SEE ALSO
        :class: note

        Shell console script
        `mdsanima-converts <#command-mdsanima-converts>`_ converting
        directly on the command line.
    """
    # assigning a function to a variable setup seconds
    sec_in_min, sec_in_hrs = get_seconds()

    # setup frames
    frames_in_sec = fps
    frames_in_hrs = frames // frames_in_sec
    frame_mod_fps = frames % frames_in_sec

    # calculating timecode
    hrs = int(frames_in_hrs // sec_in_hrs)
    min = int(frames_in_hrs // sec_in_min % sec_in_min)
    sec = int(frames_in_hrs % sec_in_min)
    fra = int(frame_mod_fps)

    # formating timecode
    timecode = str("%02d:%02d:%02d:%02d" % (hrs, min, sec, fra))

    return timecode


def timecode_to_frames(timecode: str, fps: float) -> int:
    """Converting timecode ``00:00:00:00`` format to frames number.

    :param timecode: Timecode format.
    :type timecode: str
    :param fps: Frames per seconds.
    :type fps: float
    :return: Total frames number.
    :rtype: int

    .. admonition:: USAGE PYTHON
        :class: hint

        *Assigning a function to a variable:*

    .. code:: python

        from mdsanima_dev.utils.converts import timecode_to_frames
        frames = timecode_to_frames("00:00:10:00", 24)
        print(frames)

    .. admonition:: USAGE SHELL
        :class: seealso

        *Command line shell console script:*

    .. code:: shell

        mdsanima-converts timecode-to-frames --timecode 00:00:10:00 --fps 24
        mdsanima-converts timecode-to-frames --help

    .. admonition:: SEE ALSO
        :class: note

        Shell console script
        `mdsanima-converts <#command-mdsanima-converts>`_ converting
        directly on the command line.
    """
    # assigning a function to a variable setup seconds
    sec_in_min, sec_in_hrs = get_seconds()

    # extract single values
    tc_hrs = int(timecode.split(":")[0])
    tc_min = int(timecode.split(":")[1])
    tc_sec = int(timecode.split(":")[2])
    tc_fra = int(timecode.split(":")[3])

    # setup and calculating frames
    frames_in_sec = fps
    tc_sec_min = tc_min * sec_in_min
    tc_sec_hrs = tc_hrs * sec_in_hrs
    tc_frames = tc_sec + tc_sec_min + tc_sec_hrs
    frames = round(tc_frames * frames_in_sec + tc_fra)

    return frames


def shell_frames_to_timecode(frames: int, fps: float) -> str:
    """Shell console script converting frames number to timecode
    ``00:00:00:00`` format.

    :param --frames: Total frames number.
    :type --frames: int
    :param --fps: Frames per seconds.
    :type --fps: float
    :return: Timecode format.
    :rtype: str

    .. admonition:: USAGE SHELL
        :class: seealso

        *Command line shell console script:*

    .. code:: shell

        mdsanima-converts frames-to-timecode --frames 240 --fps 24
        mdsanima-converts frames-to-timecode --help

    .. admonition:: USAGE PYTHON
        :class: hint

        *Assigning a function to a variable:*

    .. code:: python

        from mdsanima_dev.utils.converts import frames_to_timecode
        timecode = frames_to_timecode(240, 24)
        print(timecode)


    .. admonition:: SEE ALSO
        :class: note

        Invoke function `frames_to_timecode <#function-frames-to-time-code>`_
        with a given arguments values.
    """
    # run calculation
    timecode = frames_to_timecode(frames, fps)
    print(timecode)


def shell_timecode_to_frames(timecode: str, fps: float) -> str:
    """Shell console script converting timecode ``00:00:00:00`` format to
    frames number.

    :param --timecode: Timecode format.
    :type --timecode: str
    :param --fps: Frames per seconds.
    :type --fps: float
    :return: Total frames number.
    :rtype: str

    .. admonition:: USAGE SHELL
        :class: seealso

        *Command line shell console script:*

    .. code:: shell

        mdsanima-converts timecode-to-frames --time-code 00:00:10:00 --fps 24
        mdsanima-converts timecode-to-frames --help

    .. admonition:: USAGE PYTHON
        :class: hint

        *Assigning a function to a variable:*

    .. code:: python

        from mdsanima_dev.utils.converts import timecode_to_frames
        frames = timecode_to_frames("00:00:10:00", 24)
        print(frames)


    .. admonition:: SEE ALSO
        :class: note

        Invoke function `timecode_to_frames <#function-timecode-to-frames>`_
        with a given arguments values.
    """
    # run calculation
    frames = timecode_to_frames(timecode, fps)
    print(frames)


def _parser_shell_converts_timecode() -> None:
    # setup variables argument parser
    ap_desc = "Converting frames number to timecode and opposite."
    ap_copy = "Copyritht \U000000A9 2022 Marcin Różewski MDSANIMA"
    sp_desc = "Choose converts options which you want to use."
    desc_frame_tc = "Converting frames number to timecode 00:00:00:00 format."
    desc_tc_frame = "Converting timecode 00:00:00:00 format to frames number."
    cmd_frames_tc = "frames-to-timecode"
    cmd_tc_frames = "timecode-to-frames"

    # create the top level argument parser
    ap = argparse.ArgumentParser(
        description=ap_desc,
        epilog=ap_copy,
        formatter_class=argparse.RawTextHelpFormatter,
        prog="mdsanima-converts",
    )
    ap.add_argument(
        "-v", "--version", action="version", version="%(prog)s v" + __version__
    )
    sp = ap.add_subparsers(description=sp_desc, metavar="converts")

    # create the parser for the frames_to_timecode command
    ap_frames_tc = sp.add_parser(
        cmd_frames_tc,
        description=desc_frame_tc,
        help="converting frames to timecode",
        epilog=ap_copy,
    )
    ap_frames_tc.add_argument(
        "-n",
        "--frames",
        required=True,
        type=int,
        help="total frames number",
    )
    ap_frames_tc.add_argument(
        "-f", "--fps", required=True, type=float, help="frames per seconds"
    )

    # create the parser for the timecode_to_frames command
    ap_tc_frames = sp.add_parser(
        cmd_tc_frames,
        description=desc_tc_frame,
        help="converting timecode to frames",
        epilog=ap_copy,
    )
    ap_tc_frames.add_argument(
        "-c",
        "--timecode",
        required=True,
        type=str,
        help="timecode format",
    )
    ap_tc_frames.add_argument(
        "-f", "--fps", required=True, type=float, help="frames per seconds"
    )

    # parse the arguments
    args = ap.parse_args()

    try:
        if len(args.__dict__) == 0:
            ap.print_usage()
            ap_frames_tc.print_usage()
            ap_tc_frames.print_usage()
        if sys.argv[1] == cmd_frames_tc:
            shell_frames_to_timecode(args.frames, args.fps)
        if sys.argv[1] == cmd_tc_frames:
            shell_timecode_to_frames(args.timecode, args.fps)
    except IndexError:
        pass


def main():
    _parser_shell_converts_timecode()


if __name__ == "__main__":
    raise SystemExit(main())
