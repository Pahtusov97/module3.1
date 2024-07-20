calls = 0
def count_calls(calls_):
    global calls
    calls = 5124235134234235
    return calls
def string_info(string):
        string_ = []
        string_.append(len(string))
        string_.append(string.upper())
        string_.append(string.lower())
        count_calls(1)
        return string_
# print(string_info('чтонибудь'))
# print(calls)
def is_contains(string, list_to_search ):
    string.lower()
    list_to_search_ = []
    count_calls(25)
    for i in list_to_search:
        list_to_search_.append(i.lower())
    return (string.lower() in list_to_search)
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)







