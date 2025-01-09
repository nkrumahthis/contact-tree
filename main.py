"""
Contact Management System using Binary Search Tree
Author: Emmanuel Nkrumah-Sarpong
Date: 08-01-2024

This program implements a phone contact management system using a Binary Search Tree
for efficient contact storage and retrieval. Features include:
- Adding and deleting contacts
- Searching contacts by name
- Contact categorization
- Automatic saving/loading of contacts
"""

import json
import os
from datetime import datetime


class Contact:
    """Represents a contact with name, phone number, and additional details."""

    def __init__(self, name, phone, email="", category="general", date_added=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category
        self.date_added = date_added or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Convert contact to dictionary for JSON storage."""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "category": self.category,
            "date_added": self.date_added,
        }

    @classmethod
    def from_dict(cls, data):
        """Create contact from dictionary (from JSON)."""
        return cls(
            name=data["name"],
            phone=data["phone"],
            email=data.get("email", ""),
            category=data.get("category", "general"),
            date_added=data.get("date_added"),
        )

    def __str__(self):
        """String representation of the contact."""
        return (
            f"Name: {self.name}\n"
            f"Phone: {self.phone}\n"
            f"Email: {self.email}\n"
            f"Category: {self.category}\n"
            f"Added: {self.date_added}\n"
        )


class ContactNode:
    """Node in the Binary Search Tree, storing a contact."""

    def __init__(self, contact):
        self.contact = contact
        self.left = None
        self.right = None


class ContactManager:
    """Binary Search Tree implementation for managing contacts."""

    def __init__(self, filename="contacts.json"):
        self.root = None
        self.count = 0
        self.filename = filename
        self.load_contacts()

    def save_contacts(self):
        """Save all contacts to JSON file."""
        contacts = []
        self._collect_contacts(self.root, contacts)

        try:
            with open(self.filename, "w") as f:
                json.dump([contact.to_dict() for contact in contacts], f, indent=2)
            print("\nContacts saved successfully!")
        except Exception as e:
            print(f"\nError saving contacts: {e}")

    def load_contacts(self):
        """Load contacts from JSON file."""
        if not os.path.exists(self.filename):
            print("\nNo existing contacts file. Starting fresh.")
            return

        try:
            with open(self.filename, "r") as f:
                contacts_data = json.load(f)

            self.root = None
            self.count = 0

            for contact_data in contacts_data:
                contact = Contact.from_dict(contact_data)
                self.add_contact(contact, save=False)

            print(f"\nLoaded {self.count} contacts.")
        except Exception as e:
            print(f"\nError leading contacts: {e}")

    def add_contact(self, contact, save=True):
        """Add a new contact to the tree."""
        if not self.root:
            self.root = ContactNode(contact)
        else:
            self._add_recursive(self.root, contact)
        self.count += 1
        if save:
            self.save_contacts()

    def _add_recursive(self, node, contact):
        """Helper method for recursive contact addition."""
        if contact.name.lower() < node.contact.name.lower():
            if node.left is None:
                node.left = ContactNode(contact)
            else:
                self._add_recursive(node.left, contact)
        else:
            if node.right is None:
                node.right = ContactNode(contact)
            else:
                self._add_recursive(node.right, contact)
                
    def find_contact(self, name):
        """Search for a contact by exact name match."""
        return self._find_recursive(self.root, name.lower())
    
    def _find_recursive(self, node, name):
        """Helper method for recursive contact search."""
        if node is None or node.contact.name.lower() == name:
            return node
        
        if name < node.contact.name.lower():
            return self._find_recursive(node.left, name)

        return self._find_recursive(node.right, name)

    def delete_contact(self, name):
        """Delete a contact from the tree."""
        initial_count = self.count
        self.root = self._delete_recursive(self.root, name.lower())
        if self.count < initial_count:
            self.save_contacts()
            return True
        return False

    def _delete_recursive(self, node, name):
        """Helper method for recursive contact deletion."""
        if node is None:
            return None

        if name < node.contact.name.lower():
            node.left = self._delete_recursive(node.left, name)
        elif name > node.contact.name.lower():
            node.right = self._delete_recursive(node.right, name)
        else:
            # Contact found, handle deletion
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node has two children
            min_node = self._find_min(node.right)
            node.contact = min_node.contact
            node.right = self._delete_recursive(
                node.right, min_node.contact.name.lower()
            )
            self.count -= 1

        return node

    def _find_min(self, node):
        """Find contact with minimum (alphabetically first) name."""
        current = node
        while current.left:
            current = current.left
        return current
    
    def _collect_contacts(self, node, contacts):
        """Collect all contacts in-order."""
        if node:
            self._collect_contacts(node.left, contacts)
            contacts.append(node.contact)
            self._collect_contacts(node.right, contacts)

    def _display_recursive(self, node):
        """Helper method for recursive contact display."""
        if node:
            self._display_recursive(node.left)
            print(node.contact)
            self._display_recursive(node.right)

    def display_contacts(self):
        """Display all contacts in alphabetical order."""
        if not self.root:
            print("\nNo contacts found.")
            return

        print("\nAll Contacts (Alphabetical Order):")
        print("-" * 40)
        self._display_recursive(self.root)


def main():
    """Main function to run the contact management system."""
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contacts")
        print("4. Display all Contacts")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            if manager.find_contact(name):
                print("\nA contact with this name already exists!")
                continue
            phone = input("Enter phone number: ")
            email = input("Enter email (optional): ")
            category = input("Enter category (family/friends/work/general): ")
            if not category:
                category = "general"
            manager.add_contact(Contact(name, phone, email, category))
            print("Contact added successfully!")

        elif choice == "2":
            name = input("Enter name to find: ")
            contact_node = manager.find_contact(name)
            if contact_node:
                print("\nContact found:")
                print(contact_node.contact)
            else:
                print("\nContact not found")

        elif choice == "3":
            name = input("Enter name to delete: ")
            if manager.delete_contact(name):
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")

        elif choice == "4":
            manager.display_contacts()

        elif choice == "5":
            print("\nThank you for using the Contact Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
