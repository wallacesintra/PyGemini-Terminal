#!/usr/bin/env python3

class Util():
    def __init__(self):
        pass

    def write_file(self, file_name, content):
        import os

        if not os.path.exists('history'):
            os.makedirs('history')
        
        file_name = os.path.join('history', file_name)
        
        with open(file_name, 'w') as file:
            file.write(content)
            file.close()
            return True

    def read_file(self, file_name):
        with open(file_name, 'r') as file:
            content = file.read()
            file.close()
            return content

    
    def get_file_list(self):
        import os

        file_list = os.listdir('history')
        return file_list

    def delete_file(self, file_name):
        import os

        file_name = os.path.join('history', file_name)
        os.remove(file_name)
        return True
    
    def clear_screen(self):
        import os

        os.system('clear')
        return True

    def clear_all_history(self):
        import os

        if(os.path.exists('history')):
            os.system('rm -r history/*')
        return True


    def get_file_path(self, file_name):
        import os

        file_name = os.path.join('history', file_name)
        return file_name
    
    def replace_whitespace_with_underscore(self, text):
        return text.replace(" ", "_")
    
    def replace_underscore_with_whitespace(self, text):
        return text.replace("_", " ")