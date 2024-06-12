#!/usr/bin/python3

"""
Class MyGeminiApi is responsible for the gemini api
"""

import google.generativeai as genai

from writePrompt import write_file
from util import Util

genai.configure(api_key= "your_gemini_api_key")

util = Util()

class MyGeminiApi():
    """
    Class MyGeminiApi is responsible for the gemini api
    """

    def __init__(self):
        self.generativeModel = genai.GenerativeModel('gemini-pro')

    def generate(self, text):
        response = self.generativeModel.generate_content(text)

        title = self.generativeModel.generate_content(
            "generate a title and the title should not be more than 5 words in text for " + response.text
            )

        promptTitle = util.replace_whitespace_with_underscore(title.text)

        if "**" in promptTitle:
            promptTitle = promptTitle.replace("**", "")

        util.write_file(promptTitle + ".md", response.text)
        
        responseText = response.text

        return responseText
