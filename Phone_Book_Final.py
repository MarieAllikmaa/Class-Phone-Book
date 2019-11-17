phone_book = []

def get_contact(first_name, last_name, phone_book):
    for contact in phone_book:
        if all([contact['first_name'] == first_name,
                contact['last_name'] == last_name]):
            return contact
    return None
def add_contact(first_name, last_name, phone_book):
    if get_contact(first_name, last_name, phone_book):
        print(f'{first_name} {last_name} is already in ur phonebook')
    else:
        phone_number = input(f'please enter {first_name}\'s phone number')
        contact = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'favorite': False,
        }
        phone_book.append(contact)
        print(f'{phone_number} saved for {first_name} {last_name}')

def delete_contact(first_name, last_name, phone_book):
    contact = get_contact(first_name, last_name, phone_book)
    if contact:
        index = phone_book.index(contact)
        phone_book.pop(index)
        print(f'{first_name} {last_name} deleted form phonebook')
    else:
        print(f'{first_name} {last_name} not found in phonebook')

def edit_contact(first_name, last_name, phone_book):
    contact = get_contact(first_name, last_name, phone_book)
    if not contact:
        print(f'{first_name} {last_name} not found in phonebook')
    else:
        field_to_modify = input('modify first name(F), last name(L) or phone(P)? ')
        if field_to_modify == 'F':
            contact['first_name'] = input('input new first name: ')
        elif field_to_modify == 'L':
            contact['last_name'] = input('input new last name: ')
        elif field_to_modify == 'P':
            contact['phone_number'] = input('input new phone number: ')
        else:
            print('Bad choice')
def get_favorites(phone_book):
    favorite_contacts = []
    for contact in phone_book:
        if contact['favorite']:
            favorite_contacts.append(contact)
    return favorite_contacts

def toggle_favorite(first_name, last_name, phone_book):
    contact = get_contact(first_name, last_name, phone_book)
    if not contact:
        print(f'{first_name} {last_name} not found in phonebook')
    else:
        contact['favorite'] = not contact['favorite']
        if contact['favorite']:
            print(f'{first_name} {last_name} is marked as favorite')
        else:
            print(f'{first_name} {last_name} is not favorite anymore')

def pretty_print(phone_book):
    columns = ['First name', 'Last name', 'Phone number', 'Is favorite']
    for column in columns:
        print(f'{column:15} |', end='')
    print()
    for contact in phone_book:
        for k, v in contact.items():
            if isinstance(v, bool):
                value = str(v)
            else:
                value = v
            print(f'{value:15} |', end='')
        print()

while True:
    print(f'Here are your contacts:')
    pretty_print(phone_book)
    user_input = input('Would you like to add(A), delete(D), edit(E) contact, manage favorites(F) or quit(Q)? ')

    if user_input == 'A':
        name = input('Please input contact name: ')
        first_name, last_name = name.split()
        add_contact(first_name, last_name, phone_book)

    elif user_input == 'D':
        name = input('Please input contact name: ')
        first_name, last_name = name.split()
        delete_contact(first_name, last_name, phone_book)

    elif user_input == 'E':
        name = input('Please input contact name: ')
        first_name, last_name = name.split()
        edit_contact(first_name, last_name, phone_book)

    elif user_input == 'F':
        action = input('Do you want to see list of favorite contacts(L) or toggle favorite option(T)? ')
        if action == 'L':
            print(f'Favorite contacts: {get_favorites(phone_book)}')

        elif action == 'T':
            name = input('Please input contact name: ')
            first_name, last_name = name.split()
            toggle_favorite(first_name, last_name, phone_book)

        else:
            print('Wrong selection')
    elif user_input == 'Q':
        break
    else:
        print('Wrong selection')