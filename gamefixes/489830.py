""" Game fix for Skyrim SE
"""
#pylint: disable=C0103

from protonfixes import util
from protonfixes import splash
import subprocess
import os

def main():
    """ Run script extender if it exists.
    """

    # Fixes the startup process.
    if os.path.isfile(os.path.join(os.getcwd(), 'skse64_loader.exe')):
        zenity_bin = splash.sys_zenity_path()
        if not zenity_bin:
            return
        zenity_cmd = ' '.join([zenity_bin, '--question','--text', '"Would you like to run the game with Script Extender?"', '--no-wrap'])
        zenity = subprocess.Popen(zenity_cmd, shell=True)
        zenity.communicate()
        if not zenity.returncode:
            util.replace_command('SkyrimSELauncher.exe', 'skse64_loader.exe')
