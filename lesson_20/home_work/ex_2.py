# Exercitiul_2
"""
Creați o nouă clasă ListăNumere (NumbersList) care extinde clasa list.
Clasa ListăNumere (NumbersList) ar trebui să permită doar valori numerice (int și float) să fie adăugate în listă.
Acest lucru înseamnă că va trebui să suprascrieți funcțiile __init__, append, extend.
Adăugați metode suplimentare după cum este descris mai jos:
• get_sum() - returnează suma tuturor valorilor
• get_average() - returnează valoarea medie a tuturor numerelor din listă
"""


# Solution
class NumbersList(list):
    def __init__(self, numbers=None):
        super().__init__()
        if numbers is not None:
            for num in numbers:
                self.append(num)

    def append(self, value):
        if isinstance(value, (int, float)):
            super().append(value)
        else:
            raise ValueError("Only numeric values (int and float) can be added to the list.")

    def extend(self, values):
        for value in values:
            self.append(value)

    def get_sum(self):
        return sum(self)

    def get_average(self):
        if len(self) == 0:
            raise ValueError("The list is empty. Cannot calculate the average.")
        return sum(self) / len(self)
