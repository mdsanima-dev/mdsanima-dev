# Copyritht © 2022 Marcin Różewski MDSANIMA


"""
Functions that may be useful in VFX and Animation Industry.
"""


def _seconds():
    # setup seconds variables
    sec_in_min = 60
    sec_in_hrs = sec_in_min * sec_in_min

    return sec_in_min, sec_in_hrs


def frames_to_time_code(frames: int, fps: float) -> str:
    """
    Function converts number of frames to time code ``00:00:00:00`` format.

    :param frames: Number of total frames.
    :type frames: int
    :param fps: Frames per seconds.
    :type fps: float
    :return: Time code format.
    :rtype: str

    :usage:

        Assigning function calling to a variable:

        .. code:: python

            from mdsanima_dev.utils.converts import frames_to_time_code
            time_code = frames_to_time_code(240, 24)
            print(time_code)
    """
    # assigning function calling to a variable setup seconds
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
    Function converts time code ``00:00:00:00`` format to frames number.

    :param time_code: Number of total frames.
    :type time_code: str
    :param fps: Frames per seconds.
    :type fps: float
    :return: Frames number.
    :rtype: int

    :usage:

        Assigning function calling to a variable:

        .. code:: python

            from mdsanima_dev.utils.converts import time_code_to_frames
            frames = time_code_to_frames("00:00:10:00", 24)
            print(frames)
    """
    # assigning function calling to a variable setup seconds
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
