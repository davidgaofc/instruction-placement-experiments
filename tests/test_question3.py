from response_form_clean.pre import q3_1 as pre1
from response_form_clean.pre import q3_2 as pre2
from response_form_clean.pre import q3_3 as pre3
from response_form_clean.pre import q3_4 as pre4
from response_form_clean.pre import q3_5 as pre5

from response_form_clean.post import q3_1 as post1
from response_form_clean.post import q3_2 as post2
from response_form_clean.post import q3_3 as post3
from response_form_clean.post import q3_4 as post4
from response_form_clean.post import q3_5 as post5

from response_form_clean.intra import q3_1 as intra1
from response_form_clean.intra import q3_2 as intra2
from response_form_clean.intra import q3_3 as intra3
from response_form_clean.intra import q3_4 as intra4
from response_form_clean.intra import q3_5 as intra5

import json
def test_add_contact(function):
    counter = 0
    book = function.ContactBook()

    # Test Case 1: Add a new contact
    try:
        book.add_contact("John Doe", "123-456-7890", "john.doe@example.com")
        if(book.list_contacts() == "John Doe: 123-456-7890, john.doe@example.com"):
            counter += 1
    except:
        pass

    # Test Case 2: Add another new contact
    try:
        book.add_contact("Jane Smith", "234-567-8901", "jane.smith@example.com")
        if("Jane Smith: 234-567-8901, jane.smith@example.com" in book.list_contacts()):
            counter += 1
    except:
        pass

    # Test Case 3: Update an existing contact's phone
    try:
        book.add_contact("John Doe", "987-654-3210", "john.doe@example.com")
        if("John Doe: 987-654-3210, john.doe@example.com" in book.list_contacts()):
            counter += 1
    except:
        pass


    # Test Case 4: Update an existing contact's email
    try:
        book.add_contact("Jane Smith", "234-567-8901", "jane.smith@newdomain.com")
        if("Jane Smith: 234-567-8901, jane.smith@newdomain.com" in book.list_contacts()):
            counter += 1
    except:
        pass

    # Test Case 5: Add new contact with different name but existing phone and email
    try:
        book.add_contact("Jim Bean", "987-654-3210", "john.doe@example.com")
        if("Jim Bean: 987-654-3210, john.doe@example.com" in book.list_contacts()):
            counter += 1
    except:
        pass

    # Test Case 6: Update existing contact with new phone and email
    try:
        book.add_contact("John Doe", "111-222-3333", "johnny.d@example.com")
        if "John Doe: 111-222-3333, johnny.d@example.com" in book.list_contacts():
            counter += 1
    except:
        pass

    # Test Case 7: Add a new contact with all new details
    try:
        book.add_contact("Alice Wonderland", "333-444-5555", "alice.w@example.com")
        if "Alice Wonderland: 333-444-5555, alice.w@example.com" in book.list_contacts():
            counter += 1
    except:
        pass

    # Test Case 8: Attempt to add existing contact with same details
    try:
        book.add_contact("Alice Wonderland", "333-444-5555", "alice.w@example.com")
        if book.list_contacts().count("Alice Wonderland: 333-444-5555, alice.w@example.com") == 1:
            counter += 1
    except:
        pass

    # Test Case 9: Add new contact with a name that would sort before the existing
    try:
        book.add_contact("Aaron Aardvark", "999-888-7777", "aaron.a@example.com")
        if "Aaron Aardvark: 999-888-7777, aaron.a@example.com" in book.list_contacts():
            counter += 1
    except:
        pass

    # Test Case 10: Update the newly added contact with different phone and email
    try:
        book.add_contact("Aaron Aardvark", "888-777-6666", "aaron.new@aardvark.com")
        if "Aaron Aardvark: 888-777-6666, aaron.new@aardvark.com" in book.list_contacts():
            counter += 1
    except:
        pass

    return counter


# Run the test
test_iterator = {"pre": [pre1, pre2, pre3, pre4,pre5], "post": [post1, post2, post3, post4,post5], "intra": [intra1, intra2, intra3, intra4,intra5]}

results = {}
for key, value in test_iterator.items():
    results[key] = []
    for i in value:
        results[key].append(test_add_contact(i))

print(results)
try:
    with open('results/question3.json', 'w') as json_file:
        json.dump(results, json_file)
except:
    print("failed to write")
