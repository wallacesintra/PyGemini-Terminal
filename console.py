#!/usr/bin/env python3

import cmd
import os

from gemini_api import MyGeminiApi

from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.table import Table
from util import Util

gemini = MyGeminiApi()
console = Console()
text = Text()
util = Util()

table = Table(title="History", show_edge= False)
table.add_column("Title", style="bold yellow")

titles = []

introduction = Text("PyGemini, \nYour terminal Gemini generative model ", style="bold green")

introduction.stylize("bold yellow", 0, 8)

introduction.append("\n\nHow can I assist you today?", style="bold green")

introduction.append("\nType help or ? to list commands", style="bold blue")


class MyPrompt(cmd.Cmd):
    # intro = console.print("Welcome to the gemini console. Type help or ? to list commands.", style="bold blue")
    intro = console.print(introduction)
    prompt = 'PyGemini> '


    def do_exit(self, arg):
        'Exit the console'
        console.print("Goodbye, see you soon ...", style="bold yellow")
        return True

    def do_clear(self, arg):
        'Clear the screen'
        util.clear_screen()
        

    def default(self, arg):
        'prompt'
        console.print(Markdown(gemini.generate(arg)), style="bold green")

    def do_history(self, arg):
        'View history'
        history = os.listdir('history')

        if(len(history) == 0):
            console.print("No history available", style="bold #FFA500")
            return
        
        elif arg == "":
            for file in history:
                title = util.replace_underscore_with_whitespace(file.split(".md")[0])

                if title not in titles:
                    titles.append(title)
                    table.add_row(title)
            
            console.print(table)
            console.print("type 'history <title>' to view content", style="bold blue")
            return

        selected_file = util.replace_whitespace_with_underscore(arg) + ".md"
        os.system('python3 -m rich.markdown history/{}'.format(selected_file))

    def do_history_clear(self, arg):
        """
        type 'history_clear all' to clear all history or history_clear <title> to clear specified title
        """
        
        if arg == "":
            console.print("type 'history_clear all' to clear all history or 'history_clear <title>' to clear specified title", style="bold blue")
        if (arg == "all"):
            if os.path.exists('history'):
                util.clear_all_history()
                console.print("History cleared", style="bold #FFA500")
            else:
                console.print("No history available", style="bold #FFA500")
        elif arg != "":
            selected_file = util.replace_whitespace_with_underscore(arg) + ".md"
            if selected_file in os.listdir('history'):
                os.remove('history/' + selected_file)
                console.print("History cleared", style="bold #FFA500")
            else:
                console.print("No history available", style="bold #FFA500")
        
        
    def complete_history(self, text, line, begidx, endidx):
        if not text:
            completions = titles
        else:
            completions = [f for f in titles if f.startswith(text)]
        return completions

    def complete_history_clear(self, text, line, begidx, endidx):
        if not text:
            completions = titles
        else:
            completions = [f for f in titles if f.startswith(text)]
        return completions

if __name__ == '__main__':
    MyPrompt().cmdloop()
