#!/usr/bin/env python3

class Util():

    """
    Class Util is responsible for utility functions
    """
    def __init__(self):
        pass

    def write_file(self, file_name, content):
        """
        Write content to a file
        """
        import os

        if not os.path.exists('history'):
            os.makedirs('history')
        
        file_name = os.path.join('history', file_name)
        
        with open(file_name, 'w') as file:
            file.write(content)
            file.close()
            return True

    def read_file(self, file_name):
        """
        Read content from a file
        """
        with open(file_name, 'r') as file:
            content = file.read()
            file.close()
            return content

    
    def get_file_list(self):
        """
        Get list of files in the history directory
        """
        import os

        file_list = os.listdir('history')
        return file_list

    def delete_file(self, file_name):
        """
        Delete a file
        """
        import os

        file_name = os.path.join('history', file_name)
        os.remove(file_name)
        return True
    
    def clear_screen(self):
        """
        Clear the screen
        """
        import os

        os.system('clear')
        return True

    def clear_all_history(self):
        """
        Clear all history
        """
        import os

        if(os.path.exists('history')):
            os.system('rm -r history/*')
        return True


    def get_file_path(self, file_name):
        """
        Get the file path
        """
        import os

        file_name = os.path.join('history', file_name)
        return file_name
    
    def replace_whitespace_with_underscore(self, text):
        """
        Replace whitespace with underscore
        """
        return text.replace(" ", "_")
    
    def replace_underscore_with_whitespace(self, text):
        """
        Replace underscore with whitespace
        """
        return text.replace("_", " ")