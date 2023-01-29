nominee1=input("Enter name of nominee1: ")
nominee2=input("Enter name of nominee1: ")
voter_list=[1,2,3,4]
no_of_vote_nomi1=0
no_of_vote_nomi2=0
l=len(voter_list)
while True:
    if voter_list==[]:
        print("voting completed")
        if no_of_vote_nomi1>no_of_vote_nomi2:
            print(nominee1," wins with", (no_of_vote_nomi1*100)/l ,"% vote")
        elif no_of_vote_nomi2>no_of_vote_nomi1:
            print(nominee2, " wins with", (no_of_vote_nomi2 * 100) / l ,"% vote")
        else:
            print("equal vote")
        break
    id=int(input("your voter id: "))
    if id in voter_list:
        print("you are voter\n press 1 for nominee1\n press 2 for nominee2")
        d=int(input("enter your vote: "))
        if d==1:
            print("thanks for voting ",nominee1)
            no_of_vote_nomi1+=1
            voter_list.remove(id)
        elif d==2:
            print("thanks for voting ", nominee1)
            no_of_vote_nomi2 += 1
            voter_list.remove(id)
        else:
            print("wrong press")

    else:
        print("you are not voter")

