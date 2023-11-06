def test_add_contact():
    book = ContactBook()

    # Test Case 1: Add a new contact
    book.add_contact("John Doe", "123-456-7890", "john.doe@example.com")
    assert book.list_contacts() == "John Doe: 123-456-7890, john.doe@example.com", "Test Case 1 failed"

    # Test Case 2: Add another new contact
    book.add_contact("Jane Smith", "234-567-8901", "jane.smith@example.com")
    assert "Jane Smith: 234-567-8901, jane.smith@example.com" in book.list_contacts(), "Test Case 2 failed"

    # Test Case 3: Update an existing contact's phone
    book.add_contact("John Doe", "987-654-3210", "john.doe@example.com")
    assert "John Doe: 987-654-3210, john.doe@example.com" in book.list_contacts(), "Test Case 3 failed"

    # Test Case 4: Update an existing contact's email
    book.add_contact("Jane Smith", "234-567-8901", "jane.smith@newdomain.com")
    assert "Jane Smith: 234-567-8901, jane.smith@newdomain.com" in book.list_contacts(), "Test Case 4 failed"

    # Test Case 5: Add new contact with different name but existing phone and email
    book.add_contact("Jim Bean", "987-654-3210", "john.doe@example.com")
    assert "Jim Bean: 987-654-3210, john.doe@example.com" in book.list_contacts(), "Test Case 5 failed"

    # Test Case 6: Update existing contact with new phone and email
    book.add_contact("John Doe", "111-222-3333", "johnny.d@example.com")
    assert "John Doe: 111-222-3333, johnny.d@example.com" in book.list_contacts(), "Test Case 6 failed"

    # Test Case 7: Add a new contact with all new details
    book.add_contact("Alice Wonderland", "333-444-5555", "alice.w@example.com")
    assert "Alice Wonderland: 333-444-5555, alice.w@example.com" in book.list_contacts(), "Test Case 7 failed"

    # Test Case 8: Attempt to add existing contact with same details
    book.add_contact("Alice Wonderland", "333-444-5555", "alice.w@example.com")
    assert book.list_contacts().count("Alice Wonderland: 333-444-5555, alice.w@example.com") == 1, "Test Case 8 failed"

    # Test Case 9: Add new contact with a name that would sort before the existing
    book.add_contact("Aaron Aardvark", "999-888-7777", "aaron.a@example.com")
    assert "Aaron Aardvark: 999-888-7777, aaron.a@example.com" in book.list_contacts(), "Test Case 9 failed"

    # Test Case 10: Update the newly added contact with different phone and email
    book.add_contact("Aaron Aardvark", "888-777-6666", "aaron.new@aardvark.com")
    assert "Aaron Aardvark: 888-777-6666, aaron.new@aardvark.com" in book.list_contacts(), "Test Case 10 failed"

    print("All test cases passed!")


# Run the test
test_add_contact()