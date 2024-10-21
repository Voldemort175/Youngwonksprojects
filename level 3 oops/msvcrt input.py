import msvcrt

def get_char():
    return msvcrt.getch().decode('utf-8', errors='ignore')

while True:
    print("yes")
    key = get_char()
    print(key)
