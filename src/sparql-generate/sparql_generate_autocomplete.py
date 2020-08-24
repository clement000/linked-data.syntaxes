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

class sparql_generate_autocomplete(TextCommand):
    def run(self, edit, symbol_file_path=None, just_import=False):
        self.edit = edit
        self.word = self.get_current_word()
        self.get_prefix_from_prefixCC()
        


    
    def get_prefix_from_prefixCC(self):
        try:
          with urllib.request.urlopen("http://prefix.cc/"+self.word+".file.json") as url:
            data = json.loads(url.read().decode())
            self.data=data
            for key, value in data.items():
                self.key=key
                self.value=value
            self.insert_prefix_statement_from_prefixCC()          
           # print(self.word,data)
        except urllib.error.URLError as e:
          self.alert("No prefix is added (please insert it manually)")  
        #  print(e.reason)

    #get current word at the cursor and convert it to String      
    def get_current_word(self) -> str:
        view = self.view
        return view.substr(view.word(view.sel()[0]))

    def alert(self, message) -> None:
        self.view.show_popup('{}'.format(message),
                             HIDE_ON_MOUSE_MOVE_AWAY)

    def insert_prefix_statement_from_prefixCC(self):
        if self.is_already_added():
            return
        prefix_statment = self.generate_prefix_statement(just_import=True)
        self.insert_on_page(prefix_statment)

    #generate the prefix statment    
    def generate_prefix_statement(self, module_name='', just_import=False) -> str:
        return 'prefix {}\n'.format(self.key+": <"+self.value+">")
        


    def is_already_added(self) -> bool:
        singleline_match = \
            not self.view.find(r'prefix.*\b{}\b'.format(self.word), 0).empty()

        multiline_matches = self.view.find_all(r'\bprefix\b\s*\((\w+)?,?')
        multiline_match = False
        for start_region in multiline_matches:
            end_region = self.view.find(r'\)\s*$', start_region.end())
            prefix_statement_region = \
                Region(start_region.begin(), end_region.end())
            prefix_statement = self.view.substr(prefix_statement_region)
            found = re.search(r"\b{}\b".format(self.word), prefix_statement)
            if found:
                multiline_match = True
                break
        is_already_added = singleline_match or multiline_match
        if is_already_added:
            self.alert('❌ Prefix already exist')

        return is_already_added    

    def insert_on_page(self, text, point=0):
        self.view.insert(self.edit, point, text)
        self.alert('✔ Prefix '+ self.key +' added successfully') 