"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


first = texts[0]
i1 = first[0]
a1 = first[1]
sT1 = first[2]


last = calls[-1]
i2 = last[0]
a2 = last[1]
sT2 = last[2]
l = last[3]

print(
    f"First record of texts, {i1} texts {a1} at time {sT1}")

print(
    f"Last record of calls, {i2} calls {a2} at time {sT2}, lasting {l} seconds")