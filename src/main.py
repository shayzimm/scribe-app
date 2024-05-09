import sys
import os
import datetime
import threading
import time
import schedule

from scribe import JournalBook


class Menu:
    """
    Initialise the Menu class.

    Initialise the JournalBook object and define the choices dictionary.

    Args:
    None

    Returns:
    None
    """

    def __init__(self):
        self.should_exit = False
        self.password_file = "password.txt"
        self.password = self.load_password()
        self.journalbook = JournalBook()
        self.choices = {
            "1": self.add_journal,
            "2": self.show_journals,
            "3": self.search_journals,
            "4": self.delete_journal,
            "5": self.edit_journal,
            "6": self.export_menu,
            "7": self.quit,
        }
        self.scheduler_thread = None

    def load_password(self):
        """
        Load the password from a file if it exists, otherwise prompt the user to set up a password.
        """
        if os.path.exists(self.password_file):
            with open(self.password_file, "r") as file:
                return file.read().strip()
        else:
            return self.setup_password()

    def setup_password(self):
        """
        Prompt the user to set up a password.
        """
        while True:
            password = input("Set up a password: ")
            confirm_password = input("Confirm password: ")
            if password == confirm_password:
                with open(self.password_file, "w") as file:
                    file.write(password)
                return password
            else:
                print("Passwords do not match. Please try again.")

    def authenticate(self):
        """
        Authenticate user by checking password.
        """
        while True:
            entered_password = input("Enter password: ")
            if entered_password == self.password:
                return True
            else:
                print("Incorrect password. Please try again.")
                continue

    def display_menu(self):
        """
        Display Scribe's menu.

        Prints a welcome message and a list of available options for the user.

        Args:
        None

        Returns:
        None
        """
        print(
            """
              Welcome to Scribe - Your Command Line Journal
              Select an option:
              1. Add a new entry
              2. Display all entries
              3. Search
              4. Delete
              5. Edit
              6. Export
              7. Quit program
              """
        )

    def run(self):
        """
        Display menu and respond to user choices.

        This method continuously displays the menu and responds to user input by
        executing the corresponding function.

        Args:
        None

        Returns:
        None
        """
        if not self.authenticate():
            print("Authentication failed. Exiting program.")
            return
        else:
            print("Authentication successful. Welcome to Scribe.")

        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_journals(self, journals=None):
        """
        Display all journal entries in journalbook.

        If no journals are provided, it will use the journals from the journalbook object.

        Args:
        journals (list, optional): A list of Journal objects. Defaults to None.

        Returns:
        None: This function does not return any value. It prints the journal entries.
        """
        if not journals:
            journals = self.journalbook.journals
        for journal in journals:
            tags_str = ", ".join(journal.tags) if journal.tags else None
            if tags_str:
                print(
                    f"{journal.id}. {journal.memo}\n"
                    f"Tags: {tags_str}\n"
                    f"Date created: {journal.creation_date}"
                )
            else:
                print(
                    f"{journal.id}. {journal.memo}\n"
                    f"Date created: {journal.creation_date}"
                )

    def add_journal(self):
        """
        Add a new journal entry to the JournalBook.

        Args:
        None

        Returns:
        None: This function does not return any value. It adds the journal entry to the JournalBook.
        """
        memo = input("Your entry: ")
        tags = input("Add tags separated by a comma, if desired: ").strip().split(",")
        self.journalbook.new_journal(memo, tags)
        print("Your entry has been added")

    def search_journals(self):
        """
        Display sub-options for searching journal entries.

        This method displays sub-options for searching journal entries, including search by keyword,
        search by tags, and search by date.

        Args:
        None

        Returns:
        None: This function does not return any value.
        """
        while True:
            print(
                """
                  Search Options:
                  1. Search by keyword
                  2. Search by tags
                  3. Search by date
                  4. Back to main menu
                  """
            )
            choice = input("Enter an option: ")

            if choice == "1":
                self.search_by_keyword()
            elif choice == "2":
                self.search_by_tags()
            elif choice == "3":
                self.search_by_date()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def search_by_keyword(self):
        """
        Search journal entries by keyword.

        This method prompts the user to enter a keyword and searches for journal entries
        containing that keyword.

        Args:
        None

        Returns:
        None: This function does not return any value. It prints the matching journal entries.
        """
        keyword = input("Enter keyword to search: ")
        journals = self.journalbook.search_journal(keyword)
        self.show_journals(journals)

    def search_by_tags(self):
        """
        Search journal entries by tags.

        This method prompts the user to enter tags and searches for journal entries
        containing any of those tags.

        Args:
        None

        Returns:
        None: This function does not return any value. It prints the matching journal entries.
        """
        tags = input("Enter tags (comma-separated): ").strip().split(",")
        journals = self.journalbook.search_by_tags(tags)
        self.show_journals(journals)

    def search_by_date(self):
        """
        Search journal entries by date range.

        This method prompts the user to enter a start date and end date, and searches for journal entries
        within that date range.

        Args:
        None

        Returns:
        None: This function does not return any value. It prints the matching journal entries.
        """
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        try:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            journals = self.journalbook.search_by_date(start_date, end_date)
            self.show_journals(journals)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def edit_journal(self):
        """
        Edit a specific journal entry.

        This method displays a list of all journal entries and prompts the user to choose which
        entry to edit. It then allows the user to modify the content and tags of the selected entry.

        Args:
        None

        Returns:
        None: This function does not return any value.
        """
        self.show_journals()  # Display list of all journal entries
        journal_id = input("Enter the ID of the journal entry to edit: ")
        try:
            journal_id = int(journal_id)
            journal = self.journalbook.get_journal_by_id(journal_id)
            if journal:
                new_memo = input("Enter the new content for the journal entry: ")
                new_tags = (
                    input(
                        "Enter the new tags for the journal entry (comma-separated): "
                    )
                    .strip()
                    .split(",")
                )
                self.journalbook.update_journal(journal_id, new_memo, new_tags)
                print("Journal entry updated successfully.")
            else:
                print(f"No journal entry found with ID {journal_id}.")
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

    def delete_journal(self):
        """
        Delete a specific journal entry from the JournalBook.

        This method displays a list of all journal entries and prompts the user to choose which
        entry to delete.

        Args:
        None

        Returns:
        None: This function does not return any value.
        """
        self.show_journals()  # Display list of all journal entries
        journal_id = input("Enter the ID of the journal entry to delete: ")
        try:
            journal_id = int(journal_id)
            if self.confirm_delete():
                deleted = self.journalbook.delete_journal(journal_id)
                if deleted:
                    print(f"The journal entry with ID {journal_id} has been deleted.")
                else:
                    print(f"The journal entry with ID {journal_id} could not be found.")
            else:
                print("Deletion cancelled.")
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

    def confirm_delete(self):
        """
        Confirm the deletion of a journal entry.

        This method prompts the user to confirm the deletion of a journal entry. It
        asks the user if they are sure they want to delete the journal entry, and
        returns True if the user confirms the deletion, and False otherwise.

        Args:
        None

        Returns:
        bool: Returns True if the user confirms the deletion, False otherwise.
        """
        choice = input(
            "Are you sure you want to delete this journal entry? (y/n): "
        ).lower()
        return choice == "y"

    def export_menu(self):
        """Display export menu"""
        print(
            """
        Export Options:
        1. Export to JSON
        2. Export to CSV
        3. Export to Text
        """
        )

        choice = input("Enter an option: ")
        if choice == "1":
            self.export_entries("exported_journal.json", "json")
        elif choice == "2":
            self.export_entries("exported_journal.csv", "csv")
        elif choice == "3":
            self.export_entries("exported_journal.txt", "txt")
        else:
            print("Invalid option. Please select a valid export option.")

    def export_entries(self, filename, file_format="json"):
        """
        Export journal entries to a file in the specified format.

        :param filename: The name of the file to export the entries to.
        :type filename: str
        :param file_format: The format of the file to export to ('json', 'csv', 'txt'). Default is 'json'.
        :type file_format: str

        :return: None
        :rtype: None
        """
        self.journalbook.export_entries(filename, file_format)

    def quit(self):
        """
        Terminate the program.

        This method prints a thank you message and exits the program.

        Args:
        None

        Returns:
        None: This function does not return any value. It terminates the program.
        """
        print("Thank you for using Scribe today")
        # Set the flag to exit
        self.should_exit = True
        sys.exit(0)

def schedule_jobs(menu):
    while not menu.should_exit:
        schedule.run_pending()
        time.sleep(1)

def main():
    journalbook = JournalBook()

    # Schedule automated backups
    schedule.every().day.at("12:09").do(journalbook.perform_backup)

    # Initialize the Menu class and create the scheduler thread
    menu = Menu()
    menu.scheduler_thread = threading.Thread(target=schedule_jobs, args=(menu,))
    menu.scheduler_thread.start()

    # Run the application loop
    menu.run()

    # After the loop exits, join the scheduler thread to ensure it terminates
    menu.scheduler_thread.join()

if __name__ == "__main__":
    main()
