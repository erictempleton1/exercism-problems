"""
def hey(words):
    if words.isupper():
        return 'Woah, chill out!'
    if words.endswith('?'):
        return 'Sure.'
    # checks for spaces and non-text chars
    if words.isspace() or not words:
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
"""
        
        
def hey(statement):
    if not statement or statement.isspace():
        return 'Fine. Be that way!'
    if statement.isupper():
        return 'Woah, chill out!'
    if statement[-1:] == '?':
        return 'Sure.' 
    return 'Whatever.'
