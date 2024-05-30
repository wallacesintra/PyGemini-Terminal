#!/usr/bin/env python3

import cmd
import os
# import sys

from testGemini import MyGeminiApi

from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.table import Table
from util import Util

gemini = MyGeminiApi()
console = Console()
text = Text()
util = Util()

table = Table(title="History")
table.add_column("Title", style="bold yellow")

titles = []


class MyPrompt(cmd.Cmd):
    intro = console.print("Welcome to the gemini console. Type help or ? to list commands.", style="bold blue")
    prompt = 'PyGemini> '


    def do_exit(self, arg):
        'Exit the console'
        console.print("Goodbye, see you soon ...", style="bold yellow")
        return True
    
    def do_hello(self, arg):
        'Say hello'
        print('Hello', arg)

    def do_generate(self, arg):
        'Generate content'
        print('Generating content for', arg)
        console.print(Markdown(gemini.generate(arg)), style="bold green")

    def do_clear(self, arg):
        'Clear the screen'
        os.system('clear')
        

    def default(self, arg):
        'Handle input that is not a recognized command'
        console.print(Markdown(gemini.generate(arg)), style="bold green")

    def do_history(self, arg):
        'View history'
        history = os.listdir('history')

        if(len(history) == 0):
            console.print("No history available", style="bold red")
            return
        
        elif arg == "":
            for file in history:
                # console.print(file, style="bold yellow")
                # title = file.split(".")[0]
                title = util.replace_underscore(file.split(".")[0])
                titles.append(title)
                table.add_row(title)
            
            console.print(table)
            console.print("'history <title>' to view content", style="bold blue")
            return

        selected_file = util.replace_whitespace(arg) + ".md"
        os.system('python3 -m rich.markdown history/{}'.format(selected_file))
        
        # console.print(file_content , style="bold green")
    def complete_history(self, text, line, begidx, endidx):
        if not text:
            # completions = os.listdir('history')
            completions = titles
        else:
            # completions = [f for f in os.listdir('history') if f.startswith(text)]
            completions = [f for f in titles if f.startswith(text)]
        return completions


if __name__ == '__main__':
    MyPrompt().cmdloop()
