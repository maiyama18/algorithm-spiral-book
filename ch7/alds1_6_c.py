from collections import namedtuple

Card = namedtuple('Card', ('mark', 'num'))

n = input()
org_cards = []
for _ in range(n):
    mark, num = input().split()
    card = Card(mark, int(num))
    org_cards.append(card)


def quick_sort(a)
