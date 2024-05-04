import sys
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
            "1" : self.show_journals,
            "2" : self.add_journal,
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
              What would you like to do today?
              1. Show a list of all journal entries
              2. Add a journal entry
              3. Search journals
              4. Delete a journal entry
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
        self.journalbook.new_journal(memo)
        print("Your entry has been added")

    def search_journals(self):
        """
        Search for a specific journal in the journalbook using the match filter.

        Args:
        None

        Returns:
        None: This function does not return any value. It prints the matching journal entries.

        Raises:
        ValueError: If no matching journals are found.
        """
        filter = input("Search for:  ")
        journals = self.journalbook.search_journal(filter)
        self.show_journals(journals)

    def delete_journal(self):
        """
        Delete a specific journal entry from the JournalBook.

        Args:
        None

        Returns:
        bool: Returns True if the journal entry is successfully deleted, False otherwise.

        Raises:
        ValueError: If the journal entry with the specified ID is not found.

        This method prompts the user to enter the ID of the journal entry to delete. If the user confirms the deletion, it attempts to delete the journal entry with the specified ID from the JournalBook. If the deletion is successful, it prints a message indicating that the journal entry has been deleted. If the deletion is not successful, it prints a message indicating that the journal entry could not be found. If the user cancels the deletion, it prints a message indicating that the deletion has been cancelled.
        """
        id_to_delete = int(input("Enter the ID of the journal entry to delete: "))
        if self.confirm_delete():
            deleted = self.journalbook.delete_journal(id_to_delete)
            if deleted:
                print(f"The journal entry with ID {id_to_delete} has been deleted.")
            else:
                print(f"The journal entry with ID {id_to_delete} could not be found.")
        else:
            print("Deletion cancelled.")

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
