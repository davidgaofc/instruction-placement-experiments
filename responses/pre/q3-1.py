Here's the code for the add_contact function:

```python
def add_contact(self, name, phone, email):
    if name in self.contacts:
        self.contacts[name] = (phone, email)
        return f"{name} updated"
    else:
        self.contacts[name] = (phone, email)
        return f"{name} added"
```

This function first checks if the name already exists in the contacts dictionary. If it does, it updates the phone and email for that name. If it doesn't, it adds a new entry with the given name, phone, and email. The function then returns a message indicating whether the contact was added or updated.

 tokens:137