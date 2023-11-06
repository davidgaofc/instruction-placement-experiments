Here is the updated 'add_contact' method in the 'ContactBook' class:

```python
def add_contact(self, name, phone, email):
    if name in self.contacts:
        self.contacts[name] = (phone, email)
        return f"{name} updated"
    else:
        self.contacts[name] = (phone, email)
        return f"{name} added"
```

This method checks if the given name already exists in the contacts dictionary. If it does, it updates the phone and email for that name. If it doesn't, it adds a new entry with the provided parameters. The method returns a string indicating whether the contact was updated or added.

 tokens:138