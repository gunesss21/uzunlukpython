import math

def mesafe(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d

# Örnek kullanım
x1, y1 = 1, 2
x2, y2 = 4, 6
print(f"Mesafe: {mesafe(x1, y1, x2, y2)}")
