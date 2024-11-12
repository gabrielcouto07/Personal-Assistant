# Personal Assistant in Python

Welcome to your **Personal Assistant**! This Python application integrates voice commands, text commands, and GUI features to interact with the assistant, which can perform various tasks, such as playing music, telling jokes, or providing the current time. The assistant leverages Python libraries like `pyttsx3` for text-to-speech, `speech_recognition` for voice commands, and `tkinter` for a user-friendly interface.

## Features

- **Text-to-Speech (TTS)**: Uses `pyttsx3` to respond with voice output.
- **Speech Recognition**: Listens to your voice commands through `speech_recognition`.
- **Command Execution**: Supports commands like playing music, telling jokes, providing the time, searching online, and opening websites.
- **Graphical Interface**: A simple GUI built with `tkinter` for sending text commands and displaying responses.
- **Scrollable Chat Window**: Shows a log of interactions for easy follow-up.

## Getting Started

### Prerequisites

Make sure to have the following Python packages installed:

```bash
pip install pyttsx3 speechrecognition pywhatkit pyjokes
