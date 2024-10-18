def extract_full_names(people):
    return [person['first'] + " " + person['last'] for person in people]

    # full_name = []
    # for person in people:
    #     new_person = person['first'] + " " + person['last']
    #     full_name.append(new_person)
    # return full_name


    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names."""

names = [
    {'first': 'Ada', 'last': 'Lovelace'},
    {'first': 'Grace', 'last': 'Hopper'},
    ]

print(extract_full_names(names))
        # ['Ada Lovelace', 'Grace Hopper']
 