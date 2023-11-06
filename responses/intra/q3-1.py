class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        # Check if name already exists in contacts dictionary
        if name in self.contacts:
            # If name exists, update the phone and email
            self.contacts[name] = (phone, email)
        else:
            # If name does not exist, add the new contact
            self.contacts[name] = (phone, email)

    def list_contacts(self):
        # Sort the contacts dictionary by name and format the contact details
        return "\n".join(f"{n}: {p}, {e}" for n, (p, e) in sorted(self.contacts.items()))

    def search_contact(self, name):
        # Check if name exists in contacts dictionary
        if name in self.contacts:
            # If name exists, return the contact details
            return f"{name}: {self.contacts[name][0]}, {self.contacts[name][1]}"
        else:
            # If name does not exist, return "Not found"
            return "Not found"

    def delete_contact(self, name):
        # Check if name exists in contacts dictionary
        if name in self.contacts:
            # If name exists, delete the contact and return success message
            del self.contacts[name]
            return f"{name} deleted"
        else:
            # If name does not exist, return "Contact not found"
            return "Contact not found"

    def update_contact_phone(self, name, new_phone):
        # Check if name exists in contacts dictionary
        if name in self.contacts:
            # If name exists, update the phone number and return success message
            self.contacts[name] = (new_phone, self.contacts[name][1])
            return f"{name}'s phone updated"
        else:
            # If name does not exist, return "Contact not found"
            return "Contact not found"

    def update_contact_email(self, name, new_email):
        # Check if name exists in contacts dictionary
        if name in self.contacts:
            # If name exists, update the email and return success message
            self.contacts[name] = (self.contacts[name][0], new_email)
            return f"{name}'s email updated"
        else:
            # If name does not exist, return "Contact not found"
            return "Contact not found"

    def get_contact_details(self, name):
        # Check if name exists in contacts dictionary
        if name in self.contacts:
            # If name exists, return the contact details
            phone, email = self.contacts[name]
            return f"Phone: {phone}, Email: {email}"
        else:
            # If name does not exist, return "Contact not found"
            return "Contact not found"

    def get_all_phones(self):
        # Return a dictionary of all contact names and their corresponding phone numbers
        return {n: p for n, (p, e) in self.contacts.items()}

    def get_all_emails(self):
        # Return a dictionary of all contact names and their corresponding emails
        return {n: e for n, (p, e) in self.contacts.items()}

 tokens:655