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

    def find_contact(self, name):
        """Search for a contact by exact name match."""
        return self._find_recursive(self.root, name.lower())

    def delete_contact(self, name):
        """Delete a contact from the tree."""
        self.root = self._delete_recursive(self.root, name.lower())
    
    
