# Scribe - Your Command Line Journal

Scribe is a command-line journaling application designed to help you keep track of your thoughts, ideas, and daily activities.

## Table of Contents

- [Scribe - Your Command Line Journal](#scribe---your-command-line-journal)
  - [Table of Contents](#table-of-contents)
  - [Project Management](#project-management)
  - [Help Documentation](#help-documentation)
  - [Style Guide](#style-guide)
  - [Scribe Walkthrough](#scribe-walkthrough)
    - [Introduction](#introduction)
    - [Installation](#installation)
    - [Getting Started](#getting-started)
    - [Adding Journal Entries](#adding-journal-entries)
    - [Viewing Journal Entries](#viewing-journal-entries)
    - [Searching Journal Entries](#searching-journal-entries)
    - [Performing Backups](#performing-backups)
    - [Exporting Entries](#exporting-entries)
    - [Quitting the Application](#quitting-the-application)

## Project Management

[Implementation Plan](docs/implementationplan.md)

[Kanban Board](https://trello.com/b/lIp5K9vY)

## Help Documentation

[Help](docs/help.md)

## Style Guide

[PEP8](https://peps.python.org/pep-0008/#documentation-strings)

## Scribe Walkthrough

### Introduction

Welcome to the walkthrough of the Scribe application. Scribe is a command-line journaling application designed to help you keep track of your thoughts, ideas, and daily activities. Here we'll explore all the features and functionalities of Scribe, including how to add journal entries, search for entries, perform backups, and more.

### Installation

To use Scribe, follow these installation steps:

1. Clone the repository from GitHub: `git clone https://github.com/your_username/scribe.git`
2. Navigate to the project directory: `cd scribe`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the main script to start the application: `python main.py`

### Getting Started

Upon launching the application, you'll be greeted with a menu that lists the available options. You can navigate through the menu using the numeric keys corresponding to each option.

### Adding Journal Entries

Allows users to add new journal entries to the application.

1. When the user selects the "Add a new entry" option from the main menu, they are prompted to enter the content of their journal entry.
2. Optionally, the user can add tags to categorize the entry.
3. The entry is then saved automatically to the journal.

### Viewing Journal Entries

Enables users to view all existing journal entries.

1. Choosing the "Display all entries" option from the main menu triggers the application to display a list of all journal entries along with their creation dates.

### Searching Journal Entries

Allows users to search for specific journal entries based on keywords, tags, or date ranges.

1. Upon selecting the "Search" option from the main menu, users are prompted to choose a search criterion (keyword, tags, or date).
2. Based on the selected criterion, users input the search term or range.
3. The application then displays all matching journal entries.

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
