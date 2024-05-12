# Scribe App Walkthrough

## Introduction
Welcome to the walkthrough of the Scribe application. Scribe is a command-line journaling application designed to help you keep track of your thoughts, ideas, and daily activities. In this document, we'll explore all the features and functionalities of Scribe, including how to add journal entries, search for entries, perform backups, and more.

## Table of Contents
- [Scribe App Walkthrough](#scribe-app-walkthrough)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Getting Started](#getting-started)
  - [Adding Journal Entries](#adding-journal-entries)
    - [Description:](#description)
    - [Logic:](#logic)
  - [Viewing Journal Entries](#viewing-journal-entries)
    - [Description:](#description-1)
    - [Logic:](#logic-1)
  - [Searching Journal Entries](#searching-journal-entries)
    - [Description:](#description-2)
    - [Logic:](#logic-2)
  - [Performing Backups](#performing-backups)
    - [Description:](#description-3)
    - [Logic:](#logic-3)
  - [Exporting Entries](#exporting-entries)
    - [Description:](#description-4)
    - [Logic:](#logic-4)
  - [Quitting the Application](#quitting-the-application)
    - [Description:](#description-5)
    - [Logic:](#logic-5)

## Installation
To use Scribe, follow these installation steps:
1. Clone the repository from GitHub: `git clone https://github.com/your_username/scribe.git`
2. Navigate to the project directory: `cd scribe`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the main script to start the application: `python main.py`

## Getting Started
Upon launching the application, you'll be greeted with a menu that lists the available options. You can navigate through the menu using the numeric keys corresponding to each option.

## Adding Journal Entries
### Description:
Allows users to add new journal entries to the application.

### Logic:
1. When the user selects the "Add a new entry" option from the main menu, they are prompted to enter the content of their journal entry.
2. Optionally, the user can add tags to categorize the entry.
3. The entry is then saved automatically to the journal.

## Viewing Journal Entries
### Description:
Enables users to view all existing journal entries.

### Logic:
1. Choosing the "Display all entries" option from the main menu triggers the application to display a list of all journal entries along with their creation dates.

## Searching Journal Entries
### Description:
Allows users to search for specific journal entries based on keywords, tags, or date ranges.

### Logic:
1. Upon selecting the "Search" option from the main menu, users are prompted to choose a search criterion (keyword, tags, or date).
2. Based on the selected criterion, users input the search term or range.
3. The application then displays all matching journal entries.

## Performing Backups
### Description:
Automatically creates backups of journal entries to ensure data safety.

### Logic:
1. Scribe performs automated backups daily, saving a copy of the current journal entries to a separate directory.

## Exporting Entries
### Description:
Enables users to export journal entries to various file formats.

### Logic:
1. Choosing the "Export" option from the main menu allows users to select the desired export format (JSON, CSV, or plain text).
2. Users specify the directory where they want to save the exported file.
3. The application exports the journal entries to the chosen format and location.

## Quitting the Application
### Description:
Allows users to exit the application.

### Logic:
1. Selecting the "Quit program" option from the main menu terminates the program and closes the command-line interface.

---

