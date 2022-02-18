# Copyritht © 2022 Marcin Różewski MDSANIMA


"""
Functions that may be useful in VFX and Animation Industry.
"""


def frames_to_time_code(frames: int, fps: float) -> str:
    """
    Function converts number of frames to time code ``00:00:00:00`` formats.

    :param frames: number of total frames
    :type frames: integer
    :param fps: frames per second
    :type fps: integer or float
    :return: time code format
    :rtype: string
    :usage:

        assigning function calling to a variable

        .. code:: python

            from mdsanima_dev.utils.convert import frames_to_time_code
            time_code = frames_to_time_code(240, 24)
            print(time_code)
    """
    # Setup variables.
    sec_in_min = 60
    fra_in_min = sec_in_min * fps
    fra_in_hrs = sec_in_min * fra_in_min

    # Calculating time code.
    hrs = int(frames / fra_in_hrs)
    min = int(frames / fra_in_min) % sec_in_min
    sec = int((frames % fra_in_min) / fps)
    fra = int((frames % fra_in_min) % fps)

    # Formating time code.
    time_code = str("%02d:%02d:%02d:%02d" % (hrs, min, sec, fra))
    return time_code
