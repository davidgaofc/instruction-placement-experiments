To implement the 'add_contact' function in the 'ContactBook' class, we need to check if the provided name already exists in the contacts directory. If it exists, we update the existing contact's details. If it does not exist, we create a new profile with the provided information.

Here is the updated code for the 'add_contact' function:

```python
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            # Update existing contact's details
            self.contacts[name] = (phone, email)
            return f"{name}'s details updated"
        else:
            # Create new contact profile
            self.contacts[name] = (phone, email)
            return f"{name} added to contacts"

    # Remaining code...

```

Now, when calling the 'add_contact' function, it will either update an existing contact's details or create a new contact profile.

 tokens:204