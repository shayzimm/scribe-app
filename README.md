# Scribe - Your Command Line Journal

Scribe is a command-line journaling application designed to help you keep track of your thoughts, ideas, and daily activities.

## Table of Contents

- [Scribe - Your Command Line Journal](#scribe---your-command-line-journal)
  - [Table of Contents](#table-of-contents)
  - [GitHub Repository](#github-repository)
  - [Project Management](#project-management)
  - [Help Documentation](#help-documentation)
  - [Style Guide](#style-guide)
  - [Scribe Walkthrough](#scribe-walkthrough)
    - [Introduction](#introduction)
    - [Installation](#installation)
      - [Easy Installation](#easy-installation)
      - [Manual installation](#manual-installation)
    - [Getting Started](#getting-started)
    - [Adding Journal Entries](#adding-journal-entries)
    - [Viewing Journal Entries](#viewing-journal-entries)
    - [Searching Journal Entries](#searching-journal-entries)
    - [Editing Journal Entries](#editing-journal-entries)
    - [Performing Backups](#performing-backups)
    - [Exporting Entries](#exporting-entries)
    - [Quitting the Application](#quitting-the-application)
  - [References](#references)

## GitHub Repository

[GitHub](https://github.com/shayzimm/scribe-app.git)

## Project Management

[Implementation Plan](docs/implementationplan.md)

[Kanban Board](https://trello.com/invite/b/lIp5K9vY/ATTIbd8b8e28b173cb2794b75b84fc3bb582D10C6BBF/scribe-app)

## Help Documentation

[Help](docs/help.md)

## Style Guide

[PEP8](https://peps.python.org/pep-0008/#documentation-strings)

## Scribe Walkthrough

### Introduction

Welcome to the walkthrough of the Scribe application. Scribe is a command-line journaling application designed to help you keep track of your thoughts, ideas, and daily activities. Here we'll explore all the features and functionalities of Scribe, including how to add journal entries, search for entries, perform backups, and more.

### Installation

To use Scribe, follow these installation steps:

#### Easy Installation

 Open the Scribe GitHub repository and click the green code button. Select 'Download ZIP' and move the file to a directory which can be navigated to. Run the following command:

`bash ./src/scribe-script.sh`
-OR-
`source ./src/scribe-script.sh`
-OR-
`. ./src/scribe-script.sh`

This script will check and install all prerequisites and dependencies to ensure that the system can run the program, and will launch the program in your terminal.

#### Manual installation

1. Clone the repository from GitHub: `git clone git@github.com:shayzimm/scribe-app.git`
2. Navigate to the project directory: `cd scribe-app`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the main script to start the application: `python3 main.py`

### Getting Started

Upon launching the application, you'll be asked to create a password. Once signed in, you'll be greeted with a menu that lists the available options. You can navigate through the menu using the numeric keys corresponding to each option.

### Adding Journal Entries

Allows users to add new journal entries to the application.

1. When the user selects the "Add a new entry" option from the main menu, they are prompted to enter the content of their journal entry.
2. Optionally, the user can add tags to categorise the entry.
3. The entry is then saved automatically to the journal.

### Viewing Journal Entries

Enables users to view all existing journal entries.

1. Choosing the "Display all entries" option from the main menu triggers the application to display a list of all journal entries along with their creation dates and tags, if any.

### Searching Journal Entries

Allows users to search for specific journal entries based on keywords, tags, or date ranges.

1. Upon selecting the "Search" option from the main menu, users are prompted to choose a search criterion (keyword, tags, or date).
2. Based on the selected criterion, users input the search term or range.
3. The application then displays all matching journal entries.
4. If there are no matching journal entries, all journal entries will be displayed.

### Editing Journal Entries

Allows users to edit the content or tag/s of a specific journal entry.

1. Upon selecting the Edit option from the main menu, the user will be presented with a list of journal entries and their associated IDs to choose from.
2. The user will enter their desired journal entry ID and edit the content and tag/s.

### Performing Backups

Automatically creates backups of journal entries to ensure data safety.

1. Scribe performs automated backups daily, saving a copy of the current journal entries to a separate directory.

### Exporting Entries

Enables users to export journal entries to various file formats.

1. Choosing the "Export" option from the main menu allows users to select the desired export format (JSON, CSV, or plain text).
2. Users specify the directory where they want to save the exported file.
3. The application exports the journal entries to the chosen format and location.

### Quitting the Application

Allows users to exit the application.

1. Selecting the "Quit program" option from the main menu terminates the program and closes the command-line interface.

---

## References

- van Rossum, G., Warsaw, B. and Coghlan, N. (2023). PEP 8 – Style Guide for Python Code | peps.python.org. [online] peps.python.org. Available at: https://peps.python.org/pep-0008/.

- www.gnu.org. (2022). Bash Reference Manual. [online] Available at: https://www.gnu.org/software/bash/manual/bash.html.

- Python Software Foundation (2023). csv — CSV File Reading and Writing — Python 3.8.1 documentation. [online] Python.org. Available at: https://docs.python.org/3/library/csv.html.

- Python Software Foundation (2023). Datetime — Basic Date and Time Types — Python 3.7.2 Documentation. [online] Python.org. Available at: https://docs.python.org/3/library/datetime.html.