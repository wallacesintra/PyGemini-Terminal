#!/usr/bin/env python3
import os

def write_file(file_name, content):

    if not os.path.exists('history'):
        os.makedirs('history')
    
    file_name = os.path.join('history', file_name)
    
    with open(file_name, 'w') as file:
        file.write(content)
        file.close()
        return True
