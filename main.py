"""
Contact Management System using Binary Search Tree
Author: Emmanuel Nkrumah-Sarpong 
Date: 08-01-2024

This program implements a phone contact management system using a Binary Search Tree
for efficient contact storage and retrieval. Features include:
- Adding and deleting contacts
"""

class Contact:
    """Represents a contact with name, phone number, and additional details."""
    def __init__(self, name, phone, email="", category="general"):
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category
    
    def __str__(self):
        """String representation of the contact."""
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nCategory: {self.category}\n"

class ContactNode:
    """Node in the Binary Search Tree, storing a contact."""
    def __init__(self, contact):
        self.contact = contact
        self.left = None
        self.right = None

class ContactManager:
    """Binary Search Tree implementation for managing contacts."""
    def __init__(self):
        self.root = None
        self.count = 0
    
    def add_contact(self, contact):
        """Add a new contact to the tree."""
        if not self.root:
            self.root = ContactNode(contact)
        else:
            self._add_recursive(self.root, contact)
        self.count += 1
        
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
    
def main():
    """Main function to run the contact management system."""
    manager = ContactManager()
    
    # Add some sample contacts
    sample_contacts = [
        Contact("John Smith", "123-456-7890", "john@email.com", "family"),
        Contact("Alice Johnson", "234-567-8901", "alice@email.com", "work"),
        Contact("Bob Wilson", "345-678-9012", "bob@email.com", "friends"),
        Contact("Carol Brown", "456-789-0123", "carol@email.com", "work"),
        Contact("David Lee", "567-890-1234", "david@email.com", "family")
    ]
    
    for contact in sample_contacts:
        manager.add_contact(contact)
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email (optional): ")
            category = input("Enter category (family/friends/work/general): ")
            if not category:
                category = "general"
            manager.add_contact(Contact(name, phone, email, category))
            print("Contact added successfully!")
        

if __name__ == "__main__":
    main()
