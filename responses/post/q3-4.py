To implement the `add_contact` method in the `ContactBook` class, you can modify the method as follows:

```python
def add_contact(self, name, phone, email):
    if name in self.contacts:
        self.contacts[name] = (phone, email)
        return f"{name} updated"
    else:
        self.contacts[name] = (phone, email)
        return f"{name} added"
```

This method checks if the `name` already exists in the `contacts` dictionary. If it does, it updates the existing phone and email. If it doesn't, it adds a new entry with the provided parameters.

Here's the updated code:

```python
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            self.contacts[name] = (phone, email)
            return f"{name} updated"
        else:
            self.contacts[name] = (phone, email)
            return f"{name} added"
    
    ...
    # other methods
    ...
```

 tokens:228