tmp_str = """
123
321
1234567
"""

file_obj = open("tmp_open.txt", "w", encoding="utf-8")
file_obj.write(tmp_str)
file_obj.close()

with open("tmp_open_2.txt", "w", encoding="utf-8") as f:
    f.write(tmp_str)

with open("tmp_open_2.txt", "r", encoding="utf-8") as f:
    print(f.read())