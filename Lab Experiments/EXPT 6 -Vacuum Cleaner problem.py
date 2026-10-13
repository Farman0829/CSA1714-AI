
# Vacuum Cleaner Problem

rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

location = 'A'

while 'Dirty' in rooms.values():
    print("Vacuum cleaner is in room", location)

    if rooms[location] == 'Dirty':
        print("Cleaning room", location)
        rooms[location] = 'Clean'

    if location == 'A':
        location = 'B'
    else:
        location = 'A'

print("\nFinal Room Status:")
for room, status in rooms.items():
    print("Room", room, ":", status)

print("All rooms are clean!")
