import random
from Number_Guessing_Game.hints import *

class NumberGuessingGame:
    def __init__(self,num_range=(0,100)):
        self.num_range=num_range
        self.points=100
        self.max_points=100
        self.guesses=set()
        self.prev_guess=None
        self.answer=random.randint(*self.num_range)
        self.hints={'bisection':bisectionhint,'warmcold':warmcoldhint}
    def run(self):
        while True:
            user_input=input(f"guess a number between {self.num_range[0]} and {self.num_range[1]} , or type h to see hint:  ")
            if user_input=='h':
                self.get_user_hint()
                continue
            try:
                guess=int(user_input)
                if guess<self.num_range[0] or guess>self.num_range[1]:
                    raise exception
            except:
                print("err,input not valid")
                continue

            correct,cost=self.apply_guess(guess)

            if correct:
                print(f"congrates {self.points}")
                return
            else:
                print(f"sorry point {self.points}")


    def apply_guess(self,guess,prev_gues=True):
        if guess==self.answer:
            correct=True
        else:
            correct=False

        if prev_gues:
            self.prev_guess=guess

        if not guess in self.guesses:
            self.guesses.add(guess)
            cost=self.num_range[1]/self.max_points
            self.apply_cost(cost)
        else:
            cost=0

        return correct,(int)(cost)

    def apply_guesses(self,guesses):
        for guess in guesses:
            self.apply_guess(guess,False)

    def apply_cost(self,cost):
        self.points-=cost
        return self.points


    def get_user_hint(self):
        while True:
            name=input(f"choose hint {[i for i in self.hints.keys()]} or type help")
            if name=='help':
                self.get_hints_help()
            elif name=='q':
                return
            else:
                hint_class=self.hints[name]
                hint=hint_class(self)
                msg,cost=hint.apply()
                print(f"hint: {msg} | cost: {cost} | current score: {self.points}")
                return

    def get_hints_help(self):
        for name,cls in self.hints.items():
            print(f"hint name: {name}")
            print("hint help statement: ", cls.help_statement)
            print()
        return

