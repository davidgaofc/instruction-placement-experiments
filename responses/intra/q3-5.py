class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            # Update existing contact
            self.contacts[name] = (phone, email)
        else:
            # Add new contact
            self.contacts[name] = (phone, email)

    def list_contacts(self):
        return "\n".join(f"{name}: {self.contacts[name][0]}, {self.contacts[name][1]}" for name in sorted(self.contacts.keys()))

    def search_contact(self, name):
        if name in self.contacts:
            return f"{name}: {self.contacts[name][0]}, {self.contacts[name][1]}"
        else:
            return "Not found"

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return f"{name} deleted"
        else:
            return "Contact not found"

    def update_contact_phone(self, name, new_phone):
        if name in self.contacts:
            phone, email = self.contacts[name]
            self.contacts[name] = (new_phone, email)
            return f"{name}'s phone updated"
        else:
            return "Contact not found"

    def update_contact_email(self, name, new_email):
        if name in self.contacts:
            phone, email = self.contacts[name]
            self.contacts[name] = (phone, new_email)
            return f"{name}'s email updated"
        else:
            return "Contact not found"

    def get_contact_details(self, name):
        if name in self.contacts:
            phone, email = self.contacts[name]
            return f"Phone: {phone}, Email: {email}"
        else:
            return "Contact not found"

    def get_all_phones(self):
        return {name: self.contacts[name][0] for name in self.contacts.keys()}

    def get_all_emails(self):
        return {name: self.contacts[name][1] for name in self.contacts.keys()}

 tokens:414