from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Instructions1(Page):
    pass


class Instructions2(Page):
    pass


class Instructions3(Page):
    pass


class Results(Page):
    pass


page_sequence = [Instructions1, Instructions2, Instructions3, Results]
