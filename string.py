def remove(s):
    string = ''
    for ch in s:
        if ch.isall():
            string += ch
    return string
if __name__ == '__main__':
    string = input('Enter a string: ')
    string = remove(string)

    print('After special characters removed: {}'.format(string))
