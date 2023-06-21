import webbrowser
import time

links = []

file_path = './channels.txt'

with open(file_path, 'r') as f:
    for line in f:
        if line != '' and line[0] == 'h':
            print(line)
            webbrowser.open(line)
            time.sleep(8)
