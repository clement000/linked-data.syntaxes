'''
Auto-complete for prefixes decleration for sparql-generate.

@author: Omar Qawasmeh

@organization: Mines Saint Etienne, France

Inspired by: sublime-python-import-helper, available at:
https://github.com/predragnikolic/sublime-python-import-helper 

'''
import os
import re
import urllib.request, json
from sublime import HIDE_ON_MOUSE_MOVE_AWAY, Region
from sublime_plugin import TextCommand

class test(TextCommand):
    def run(self, edit, symbol_file_path=None, just_import=False):
        self.alert("hello")       


    def alert(self, message) -> None:
        self.view.show_popup('{}'.format(message),
                             HIDE_ON_MOUSE_MOVE_AWAY)
