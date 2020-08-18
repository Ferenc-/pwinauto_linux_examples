#!/usr/bin/env python3
from pywinauto.linux.keyboard import send_keys
from pywinauto.linux.application import Application

QUICK_OPEN = True
TEST_FILE_PATH = '/tmp/test.txt'

with open(TEST_FILE_PATH,'w') as test_file:
   test_file.write('This is the beginning of a beautiful friendship!') 


app = Application().start("gedit")

app.gedit['Untitled Document 1 - gedit'].wait('ready')

if QUICK_OPEN:
    # This only works if you have the focus
    app.gedit['Untitled Document 1 - gedit'].set_focus()
    # Send Ctrl + O to open the FileChooser directl 
    send_keys('^o')
else:
    # Open the file chooser by clicking the button
    app.gedit.Open.click()
    app.gedit['Other Documents...'].click()

# FileChooser opened up
FileChooser = app.gedit.children()[1]
app.gedit['Untitled Document 1 - gedit'].wait('ready')

# Send the ctr+L to switch to editable text
send_keys('^l')
# A better solution would be something like:
# FileChooser.type_keys('^l')
# But this is unimplemented
# Alternatively if you send '/' then it starts by filling in the '/'

SplitPane = FileChooser.children()[1].children()[0].children()[0].children()[0]
Panel = SplitPane.children()[1]
EditWrapper = Panel.children()[0].children()[0].children()[0].children()[0].children()[0]
EditWrapper.set_edit_text(TEST_FILE_PATH)

#print(FileChooser.children())

FileChooserTopButtonRow = FileChooser.children()[0].children()
OpenButton = FileChooserTopButtonRow[1]
OpenButton.click()
