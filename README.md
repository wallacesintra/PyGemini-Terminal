# PyGemini-Terminal

PyGemini Terminal

A terminal chatbot powered by Google's Gemini API. This chatbot will enable text-based interaction through a user-friendly terminal interface.

## Contributors

* Fredrick Arara <fredrickarara@gmail.com>
* Wallace Wahong'o <otienowallace33@gmail.com>

## Project Features

* **Interactive Terminal Interface**: Provides a user-friendly terminal interface for text-based interaction.

* **Integration with Google's Gemini API**: Leverages the power of Google's Gemini API to generate responses, making the chatbot more intelligent and capable of handling complex queries.

* **Easy Setup**: Designed with a simple setup process, making it easy for users to get started.

* **Open Source**: The project is open-source, allowing developers to contribute and enhance its features.

* **Platform**: Works in Linux.

* **Extensible**: The design allows for easy addition of new features and improvements.

## PyGemini Console Guide

The `console.py` script provides a command-line interface for interacting with the PyGemini application. Here's how to use it:

### Starting the Console

To start the console, navigate to the directory containing `console.py` and run the script with Python:

```bash
python3 console.py
```

### Commands

* **exit**: Exit the console
* **clear**: Clear the console screen
* **history**: View the history of commands. If you provide a title as an argument, you can view the content of that specific history item. Example usage: `history <title>`
* **history_clear**: Clear the history. You can either clear all history or a specific history item by providing a title as an argument. Example usage: `history_clear all` or `history_clear <title>`

### Autocomplete

The console supports autocompletion for the `history` and `history_clear` commands. Just start typing the title of a history item and press `Tab` to autocomplete.
