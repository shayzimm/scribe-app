import sys
import datetime
from scribe import Journal, JournalBook

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
        self.journalbook = JournalBook()
        self.choices = {
            "1" : self.add_journal,
            "2" : self.show_journals,
            "3" : self.search_journals,
            "4" : self.delete_journal,
            "5" : self.quit
        }

    def display_menu(self):
        """
        Display Scribe's menu.

        Prints a welcome message and a list of available options for the user.

        Args:
        None

        Returns:
        None
        """
        print("""
              Welcome to Scribe
              Please select an option:
              1. Add a new journal entry
              2. Display all journals
              3. Search journals
              4. Delete a journal
              5. Quit program
              """)

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
        while True:
            self.display_menu()
            choice = input("Enter an option: " )
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
            print(f"{journal.id}. {journal.memo}")

    def add_journal(self):
        """
        Add a new journal entry to the JournalBook.

        Args:
        None

        Returns:
        None: This function does not return any value. It adds the journal entry to the JournalBook.
        """
        memo = input("Your entry: " )
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
            print("""
                  Search Options:
                  1. Search by keyword
                  2. Search by tags
                  3. Search by date
                  4. Back to main menu
                  """)
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
        choice = input("Are you sure you want to delete this journal entry? (y/n): ").lower()
        return choice == "y"

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
        sys.exit(0)

if __name__ == "__main__":
    """
    This is the main entry point of the program.
    It initialises the Menu class and runs the application.

    Args:
    None

    Returns:
    None: This function does not return any value. It initialises the Menu class and runs the application.
    """
    Menu().run()
