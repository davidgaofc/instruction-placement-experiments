You can implement the 'add_contact' method in the 'ContactBook' class like this:

```python
def add_contact(self, name, phone, email):
    if name in self.contacts:
        self.contacts[name] = (phone, email)
        return f"{name}'s info updated"
    else:
        self.contacts[name] = (phone, email)
        return f"{name} added to contacts"
```

This method checks if the given name already exists in the contacts dictionary. If it does, it updates the existing phone and email details with the new values. If not, it adds a new contact with the given name, phone, and email details to the contacts dictionary. The method then returns a message indicating whether the contact was updated or added.

 tokens:156