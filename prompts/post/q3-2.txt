class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        pass

    def list_contacts(self):
        return "\n".join(f"{n}: {p}, {e}" for n, (p, e) in sorted(self.contacts.items()))

    def search_contact(self, name):
        return f"{name}: {self.contacts[name][0]}, {self.contacts[name][1]}" if name in self.contacts else "Not found"

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return f"{name} deleted"
        return "Contact not found"

    def update_contact_phone(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = (new_phone, self.contacts[name][1])
            return f"{name}'s phone updated"
        return "Contact not found"

    def update_contact_email(self, name, new_email):
        if name in self.contacts:
            self.contacts[name] = (self.contacts[name][0], new_email)
            return f"{name}'s email updated"
        return "Contact not found"

    def get_contact_details(self, name):
        if name in self.contacts:
            phone, email = self.contacts[name]
            return f"Phone: {phone}, Email: {email}"
        return "Contact not found"

    def get_all_phones(self):
        return {n: p for n, (p, e) in self.contacts.items()}

    def get_all_emails(self):
        return {n: e for n, (p, e) in self.contacts.items()}

Implement the 'add_contact' function in the 'ContactBook' class to manage contacts. The function should check if a name exists in the database and update that contact's phone and email if so. If the name isn't found, it must create and store a new contact entry.
