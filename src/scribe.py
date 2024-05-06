import json
import os
import csv
import datetime
from datetime import date
import tkinter as tk
from tkinter import filedialog


class Journal:
    last_id = 0

    def __init__(self, memo, tags=None):
        """
        Initialises a new journal entry with memo, tags, creation date, and an automatically assigned ID.
        :param memo: The content of the journal entry.
        :type memo: str
        :param tags: Optional tags for the journal entry. Default is an empty list.
        :type tags: list, optional
        """
        self.memo = memo
        self.tags = tags if tags is not None else []  # Use empty list as default tags
        self.creation_date = datetime.datetime.now().date()  # Use current date and time
        Journal.last_id += 1
        self.id = Journal.last_id

    def match(self, filter):
        """
        Checks if the journal matches the filter text.
        Return True if it matches exactly, False if it does not match.
        Filter is case-sensitive.

        :param filter: The text to search for in the journal's memo and tags.
        :type filter: str

        :return: True if the journal matches the filter, False otherwise.
        :rtype: bool
        """
        if filter in self.memo:
            return True
        for tag in self.tags:
            if filter in tag:
                return True
        return False


class JournalBook:
    """Represent a collection of journals"""

    def __init__(self, storage_file="journal_entries.json"):
        """
        Initialise journalbook with an empty list.

        This method initialises a new instance of JournalBook, which is a collection of Journal entries.
        It creates an empty list to store the journals.

        :return: None
        :rtype: None
        """
        self.storage_file = storage_file
        self.load_entries()

    def load_entries(self):
        """Load journal entries from a JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as file:
                try:
                    data = json.load(file)
                    self.journals = [
                        self.create_journal_from_dict(entry) for entry in data
                    ]
                except json.JSONDecodeError:
                    print(
                        "Error: Unable to load JSON data. The file may be empty or contain invalid JSON."
                    )
                    self.journals = []
        else:
            self.journals = []

    def create_journal_from_dict(self, data):
        """
        Create a Journal object from a dictionary.

        Args:
        data (dict): A dictionary containing journal data.

        Returns:
        Journal: A Journal object created from the dictionary data.
        """
        memo = data.get("memo", "")
        tags = data.get("tags", [])
        creation_date = datetime.datetime.strptime(
            data.get("creation_date", ""), "%Y-%m-%d"
        ).date()
        journal_id = data.get("id", 0)
        return Journal(memo, tags)

    def save_entries(self):
        """Save journal entries to a JSON file."""
        with open(self.storage_file, "w") as file:
            # Serialize each journal entry individually
            serialized_entries = []
            for journal in self.journals:
                serialized_entry = {
                    "memo": journal.memo,
                    "tags": journal.tags,
                    "creation_date": journal.creation_date.isoformat(),
                    "id": journal.id,
                }
                serialized_entries.append(serialized_entry)

            # Write the serialized entries to the JSON file
            json.dump(serialized_entries, file, indent=4)

    def new_journal(self, memo, tags=""):
        """
        Creates a new journal entry in the journalbook.

        :param memo: The content of the journal entry.
        :type memo: str
        :param tags: Optional tags for the journal entry. Default is an empty string.
        :type tags: str, optional

        :return: None
        :rtype: None
        """
        self.journals.append(Journal(memo, tags))
        self.save_entries()

    def search_journal(self, filter):
        """
        Searches all journal entries that match the filter.

        :param filter: The text to search for in the journal's memo and tags.
        :type filter: str

        :return: A list of Journal objects that match the filter.
        :rtype: list
        """
        return [journal for journal in self.journals if journal.match(filter)]

    def search_by_date(self, start_date, end_date):
        """
        Search journal entries by date range.

        Args:
        start_date (datetime.date): Start date of the date range.
        end_date (datetime.date): End date of the date range.

        Returns:
        list: A list of Journal objects that fall within the specified date range.
        """
        return [
            journal
            for journal in self.journals
            if start_date <= journal.creation_date <= end_date
        ]

    def search_by_tags(self, tags):
        """
        Search journal entries by tags.

        Args:
        tags (list): A list of tags to search for.

        Returns:
        list: A list of Journal objects that match the specified tags.
        """
        return [
            journal
            for journal in self.journals
            if any(tag in journal.tags for tag in tags)
        ]

    def get_journal_by_id(self, journal_id):
        """
        Retrieve a journal entry by its ID.

        Args:
        journal_id (int): The ID of the journal entry to retrieve.

        Returns:
        Journal or None: The Journal object with the specified ID, or None if not found.
        """
        for journal in self.journals:
            if journal.id == journal_id:
                return journal
        return None

    def update_journal(self, journal_id, new_memo, new_tags):
        """
        Update a journal entry with new content and tags.

        Args:
        journal_id (int): The ID of the journal entry to update.
        new_memo (str): The updated content of the journal entry.
        new_tags (list): The updated tags of the journal entry.

        Returns:
        bool: True if the update was successful, False otherwise.
        """
        for journal in self.journals:
            if journal.id == journal_id:
                journal.memo = new_memo
                journal.tags = new_tags
                self.save_entries()  # Save changes to the json file
                return True
        return False

    def delete_journal(self, journal_id):
        """
        Deletes a journal entry from the journalbook.

        :param journal_id: The id of the journal entry to delete.
        :type journal_id: int

        :return: None
        :rtype: None
        """
        for journal in self.journals:
            if journal.id == journal_id:  # Access 'id' attribute directly
                self.journals.remove(journal)
                self.save_entries()
                return True
        return False

    def export_entries(self, filename, file_format="json", directory=None):
        """
        Export journal entries to a file in the specified format.

        :param filename: The name of the file to export the entries to.
        :type filename: str
        :param file_format: The format of the file to export to ('json', 'csv', 'txt'). Default is 'json'.
        :type file_format: str
        :param directory: Optional. The directory where the file should be saved. If not specified, a file dialog will be shown to select the directory.
        :type directory: str

        :return: None
        :rtype: None
        """
        if not directory:
            root = tk.Tk()
            root.withdraw()  # Hide the main window
            directory = filedialog.askdirectory(title="Select Directory")
            if not directory:
                print("No directory selected. Export operation cancelled.")
                return

        if file_format == "json":
            with open(os.path.join(directory, filename), "w") as file:
                json.dump(
                    self.journals, file, default=self.json_serialization, indent=4
                )
        elif file_format == "csv":
            with open(os.path.join(directory, filename), "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Memo", "Tags", "Creation Date"])
                for journal in self.journals:
                    writer.writerow(
                        [journal.memo, ", ".join(journal.tags), journal.creation_date]
                    )
        elif file_format == "txt":
            with open(os.path.join(directory, filename), "w") as file:
                for journal in self.journals:
                    file.write(f"Memo: {journal.memo}\n")
                    if journal.tags:
                        file.write(f"Tags: {', '.join(journal.tags)}\n")
                    file.write(f"Creation Date: {journal.creation_date}\n\n")
        else:
            raise ValueError(
                "Unsupported file format. Supported formats are 'json', 'csv', and 'txt'."
            )

        print(f"File exported successfully to: {os.path.join(directory, filename)}")

    def json_serialization(self, obj):
        """Custom JSON serialization function"""
        if isinstance(obj, date):
            return obj.isoformat()  # Serialize datetime.date objects to ISO format
        elif hasattr(obj, "__dict__"):  # Check if the object has a __dict__ attribute
            return (
                obj.__dict__
            )  # Serialize custom objects using their __dict__ attribute
        else:
            raise TypeError(
                "Object of type {} is not JSON serializable".format(type(obj).__name__)
            )
