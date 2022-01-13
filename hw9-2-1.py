# Author: IBN (AMDG) 1/12/2022

from types import LambdaType


last_initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]
rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

for row in rows:
        for i, v in enumerate(row):
            row[i] = "{0} {1}.".format(v, last_initials[0])
            del last_initials[0]
print(rows)
