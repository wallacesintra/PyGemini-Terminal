#!/usr/bin/python3

import google.generativeai as genai

from writePrompt import write_file
from util import Util

# genai.configure(api_key= "your_gemini_api_key")
genai.configure(api_key= "AIzaSyBPGXS5ps6nYr1Wl4ndP9KImPlPmljPp9Q")


util = Util()



# model = genai.GenerativeModel('gemini-pro')


class MyGeminiApi():
    def __init__(self):
        self.generativeModel = genai.GenerativeModel('gemini-pro')

    def generate(self, text):
        response = self.generativeModel.generate_content(text)

        title = self.generativeModel.generate_content("generate a title and the title should not be more than 5 words in text for " + response.text)

        promptTitle = util.replace_whitespace(title.text)
        
        write_file(promptTitle + ".md", response.text)

        responseText = response.text

        return responseText
    