import sys
import xbmc
import xbmcgui
import re


def updateEditCursor(action, pos_str, edit_str):
    current_cursor_pos = len(edit_str) if pos_str == '' else int(pos_str)
    if action == "editCursorLeft":
        current_cursor_pos = max(0, current_cursor_pos - 1)
    elif action == "editCursorRight":
        current_cursor_pos = min(len(edit_str), current_cursor_pos + 1)
    elif action == "editCursorReset":
        current_cursor_pos = len(edit_str)

    # edit_str = edit_str.replace(" ", "_")
    xbmc.executebuiltin("Skin.SetString(editCurPos, %d)" % (
        current_cursor_pos,))
    xbmc.executebuiltin("Skin.SetString(editText, %s%s%s)" % (
        edit_str[:current_cursor_pos], "|",
        edit_str[current_cursor_pos:]))


def updateNumpadCursor(action, cursor_index, num_str, key_or_edit_str):
    selected_field = 0 if cursor_index == '' else int(cursor_index)
    # Split up flag which indicate that currently selected field was
    # edited.
    # The first field is always in this state on press of
    # delete key. This rebuild Kodi's behaviour
    edited = (selected_field & 128 == 128)
    if action in ["numpadDel"]:
        edited = edited or (selected_field == 0)

    selected_field = selected_field - (selected_field & 128)

    if num_str == '':
        num_str = "0.0.0.0"

    fields_str = num_str.split(".")
    while len(fields_str) < 4:
        fields_str.append("0")

    fields = [int(x) for x in fields_str]

    # The key button are overloaded with two onclick events.
    # The following code assumes that the string represent the state before
    # both events starts.
    if action == "numpadKey":
        key = int(key_or_edit_str)
        if edited:
            fields[selected_field] = 10*fields[selected_field]+key
        else:
            fields[selected_field] = key

        fields_str[selected_field] = str(fields[selected_field])

        if(10*(fields[selected_field]) > 255
           or fields[selected_field] == 0):
            selected_field = (selected_field + 1) % 4
            edited = False
        else:
            edited = True

    if action == "numpadDel":
        if fields[selected_field] == 0:
            selected_field = max(0, selected_field - 1)
            edited = False
        elif edited:
            fields[selected_field] = int(fields[selected_field]/10)
            fields_str[selected_field] = str(fields[selected_field])
        else:
            selected_field = max(0, selected_field - 1)
            edited = False

    if action == "numpadLeft":
        if selected_field == 0 and fields[selected_field] == 0:
            edited = False
        else:
            selected_field = max(0, selected_field - 1)
            edited = False

    if action == "numpadRight":
        if selected_field == 0 and fields[selected_field] == 0:
            edited = False
        else:
            selected_field = min(3, selected_field + 1)
            edited = False

    if action == "numpadReset":
        selected_field = 0
        edited = False

    if action == "numpadFinish":
        edited = False
        old_edit_text = key_or_edit_str
        old_edit_text = old_edit_text.replace("|", "")

        text = insert_new_ip(old_edit_text, fields_str)
        # old_edit_text = extract_ip(old_edit_text, True)

        # Reset position of virtual keypad. This puts the curor at the end.
        # key_or_edit_str variable contains edit string in this case
        xbmc.executebuiltin("Skin.SetString(editCurPos,)")
        xbmc.executebuiltin("Skin.SetString(editText, %s|)" % (
            text))

    xbmc.executebuiltin("Skin.SetString(numpadCurPos, %d)" % (
        selected_field + 128 if edited else selected_field,))
    fields_str[selected_field] = "[COLOR=blue]" \
        + fields_str[selected_field] + "[/COLOR]"
    xbmc.executebuiltin("Skin.SetString(numpadText, %s.%s.%s.%s)" % (
        fields_str[0],
        fields_str[1],
        fields_str[2],
        fields_str[3]))


def insert_new_ip(text, l_ip):
    # Check if text contain ip
    m = re.search("(\s*[0-9]{1,3}[.]){3}\s*[0-9]{1,3}", text)
    if m is None:
        return "%s%s.%s.%s.%s" % (
            text,
            l_ip[0],
            l_ip[1],
            l_ip[2],
            l_ip[3])

    return "%s%s.%s.%s.%s%s" % (
        text[:m.start()],
        l_ip[0],
        l_ip[1],
        l_ip[2],
        l_ip[3],
        text[m.end():])


"""
# Other approach: Disable animations of edit control.
# Unfortunaty, it never works.
def test():
    wid = xbmcgui.getCurrentWindowId()
    # did = xbmcgui.getCurrentWindowDialogId()

    # win = xbmcgui.Window(did) # freeze
    win = xbmcgui.Window(wid)
    con = win.getControl(312)  # does not exists
    con.setAnimations([])
"""

# Main code

base_url = sys.argv[0]
action = str(sys.argv[1])


# if action in ["editCursorLeft", "editCursorRight", "editCursorReset"]:
if action[:4] == "edit":
    updateEditCursor(action, sys.argv[2], sys.argv[3])

# if action in ["numpadKey", "numpadDel", "numpadReset",
#               "numpadLeft", "numpadRight", "numpadFinish"]:
if action[:6] == "numpad":
    updateNumpadCursor(action, sys.argv[2], sys.argv[3], sys.argv[4])
