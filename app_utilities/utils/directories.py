""" directories utilities """
import os


def get_filename_ext(filepath):
    """ split file dir, name and ext """
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
