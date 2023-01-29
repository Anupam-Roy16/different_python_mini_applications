class bisectionhint:
    help_statement="divide half, cost: up to half"
    def __init__(self,game):
        self.game=game
    def apply(self):
        values=[i for i in range(1,self.game.num_range[1]) if i not in self.game.guesses]
        h_idx=len(values)//2
        h=values[h_idx]
        if self.game.answer<h:
            s="<"
            guesses=values[h_idx:]
        else:
            s=">="
            guesses=values[:h_idx-1]
        hint=f"correct ans {s} {h}"

        cost=self.game.apply_guesses(guesses)
        return hint,cost




class warmcoldhint:
    cost=20
    help_statement=f" warm if last guess is +- 15% of answer otherwise cold, cost:{cost}"
    def __init__(self,game):
        self.game=game
    def apply(self):
        if not  self.game.prev_guess:
            msg="you must at least one guess before this hin"
            return msg,None
        if self.game.answer*.15>= self.game.prev_guess<= self.game.answer *.85\
                :
            temp = "warm"
        else:
            temp = "cold"
        msg=f"last guess {self.game.prev_guess} was {temp}"
        self.game.apply_cost(self.cost)
        return msg,self.cost
