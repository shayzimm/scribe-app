# Scribe Application Help Documentation

## Introduction

Welcome to the Scribe application help documentation. Scribe is a command-line journaling application designed to help you organise your thoughts and daily activities. This document provides instructions on how to install and use the Scribe application effectively.

## Installation

To use Scribe, follow these installation steps:

### Easy Installation

For an easy install, run the following command:

`bash ./src/scribe-script.sh`
-OR-
`source ./src/scribe-script.sh`
-OR-
`. ./src/scribe-script.sh`

This script will check and install all prerequisites and dependencies to ensure that the system can run the program, and will launch the program in your terminal.

### Manual installation

1. Clone the repository from GitHub: `git clone git@github.com:shayzimm/scribe-app.git`
2. Navigate to the project directory: `cd scribe-app`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the main script to start the application: `python3 main.py`

## Dependencies

The Scribe application requires the following dependencies to operate:

- Python 3.10 or greater
- External libraries listed below are specified in the `requirements.txt` file:
  - altgraph==0.17.4
  - packaging==24.0
  - pyinstaller-hooks-contrib==2024.6
  - schedule==1.2.1

## Imported Packages and Modules

- sys
- os
- csv
- datetime
- threading
- json
- time
- tkinter
- queue

## System/Hardware Requirements

Scribe has minimal system requirements and can run on most modern computers with Python installed. However, it is recommended to have:

- Operating System: Windows, macOS, or Linux
- Python 3.10 or greater installed

## Command Line Arguments

The Scribe application supports the following command-line arguments:

- None

## Usage

To use the Scribe application, follow these instructions:

1. Open a terminal or command prompt.
2. Navigate to the directory where the Scribe application is installed.
3. Run the main script to start the application: `python3 main.py`
4. Follow the on-screen instructions to navigate through the application menu and use its features.

## Troubleshooting

If you encounter any issues during installation or usage of the Scribe application, please refer to the following troubleshooting steps:

1. Ensure that all dependencies are installed correctly by re-running the installation steps.
2. Check for any error messages displayed in the terminal or command prompt and troubleshoot accordingly.

## Known Issues

The following are known issues or limitations with the Scribe application:

1. **Export Functionality**: After performing an automated backup, attempting to export journal entries immediately may result in a "RuntimeError: main thread is not in the main loop" error. To resolve this, simply wait a few moments after the backup completes before attempting to export.

2. **Dependency Management**: The application relies on several external libraries, such as `schedule` and `tkinter`, which may require manual installation. Ensure that these dependencies are installed using the provided bash script, the `requirements.txt` file, or through manual installation via pip.

3. **Limited Command-Line Functionality**: Scribe does not support command-line arguments for additional functionality. All interactions and operations are performed within the application's interactive menu system.

4. **File System Interactions**: Certain operations, such as exporting journal entries, rely on system-dependent file dialogues. While efforts have been made to ensure compatibility across different operating systems, users may encounter differences in behaviour based on their system configuration.

## Feedback and Support

If you have any feedback, suggestions, or require further assistance with the Scribe application, please feel free to reach out to me via GitHub or email.
