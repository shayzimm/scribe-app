# Scribe Application Help Documentation

## Introduction
Welcome to the Scribe application help documentation. Scribe is a command-line journaling application designed to help you organize your thoughts and daily activities. This document provides instructions on how to install and use the Scribe application effectively.

## Installation
To use Scribe, follow these installation steps:
1. Clone the repository from GitHub: `git clone https://github.com/your_username/scribe.git`
2. Navigate to the project directory: `cd scribe`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the main script to start the application: `python main.py`

## Dependencies
The Scribe application requires the following dependencies to operate:
- Python 3.x
- External libraries specified in the `requirements.txt` file

## System/Hardware Requirements
Scribe has minimal system requirements and can run on most modern computers with Python installed. However, it is recommended to have:
- Operating System: Windows, macOS, or Linux
- Python 3.x installed

## Command Line Arguments
The Scribe application supports the following command-line arguments:
- None

## Usage
To use the Scribe application, follow these instructions:
1. Open a terminal or command prompt.
2. Navigate to the directory where the Scribe application is installed.
3. Run the main script to start the application: `python main.py`
4. Follow the on-screen instructions to navigate through the application menu and use its features.

## Troubleshooting
If you encounter any issues during installation or usage of the Scribe application, please refer to the following troubleshooting steps:
1. Ensure that all dependencies are installed correctly by re-running the installation steps.
2. Check for any error messages displayed in the terminal or command prompt and troubleshoot accordingly.
3. If the issue persists, please refer to the project's GitHub repository for additional support or open a new issue for assistance.

## Known Issues

The following are known issues or limitations with the Scribe application:

1. **Export Functionality**: After performing an automated backup, attempting to export journal entries immediately may result in a "RuntimeError: main thread is not in the main loop" error. To resolve this, simply wait a few moments after the backup completes before attempting to export.

2. **Graphical User Interface**: The application currently lacks a graphical user interface (GUI), operating solely through the command line interface (CLI). While efforts are underway to develop a GUI for enhanced user experience, the current version is CLI-based.

3. **Dependency Management**: The application relies on several external libraries, such as `schedule` and `tkinter`, which may require manual installation. Ensure that these dependencies are installed using the provided `requirements.txt` file or through manual installation via pip.

4. **Limited Command-Line Functionality**: Scribe does not support command-line arguments for additional functionality. All interactions and operations are performed within the application's interactive menu system.

5. **File System Interactions**: Certain operations, such as exporting journal entries, rely on system-dependent file dialogues. While efforts have been made to ensure compatibility across different operating systems, users may encounter differences in behaviour based on their system configuration.

## Feedback and Support
If you have any feedback, suggestions, or require further assistance with the Scribe application, please feel free to reach out to me via GitHub or email.
