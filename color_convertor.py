r = int(input("Введите R (0-255): "))
g = int(input("Введите G (0-255): "))
b = int(input("Введите B (0-255): "))
hex_color = f"#{r:02X}{g:02X}{b:02X}"
print(f"Цвет в формате HEX: {hex_color}")