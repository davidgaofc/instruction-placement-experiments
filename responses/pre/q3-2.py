To implement the 'add_contact' function, we need to check if the given name already exists in the dictionary 'self.contacts'. If it does, we update the phone and email for that contact. If it doesn't, we create a new contact entry with the given name, phone, and email.

Here's the updated code:

```python
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            # Contact already exists, update phone and email
            self.contacts[name] = (phone, email)
            return f"{name}'s contact updated"
        else:
            # Contact doesn't exist, create a new entry
            self.contacts[name] = (phone, email)
            return f"{name}'s contact created"

    # Rest of the code is the same as before
    # ...
```

Now the 'add_contact' function will update or create a new contact entry as required.

 tokens:208