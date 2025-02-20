notes = [0] * 10
note = input()

while note != 'End':
    note = note.split("-")
    priority = int(note[0])
    current_note = note[1]

    index = priority - 1
    notes.pop(index)
    notes.insert(index, current_note)
    note = input()

notes = [str(s) for s in notes if s != 0]
print(notes)
