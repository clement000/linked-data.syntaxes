import sublime
import sublime_plugin

import webbrowser

class SparqlGenerateDocCommand(sublime_plugin.ApplicationCommand):

    def run(self, url):
        webbrowser.open(url)

