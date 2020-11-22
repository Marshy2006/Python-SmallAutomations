from fileinput import FileInput

stringtochange = ""
changedstring = ""
filetochange = "/path/to/file"

with FileInput(filetochange, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(stringtochange, changedstring), end='')
