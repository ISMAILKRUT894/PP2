from datetime import date
d = date(2026, 2, 1)
formatted = d.strftime("%y-%b-%A")
print(formatted)
print(d)