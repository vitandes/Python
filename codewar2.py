def rps(p1, p2):
    if p1 == p2:
        return "Draw"
    elif (p1 == "scissor" and p2 == "paper") or (p1 == "rock" and p2 == "scissor") or (p1 == "paper" and p2 == "rock"):
        return "Player 1 won"
    else:
        return "Player 2 won"

     
a =  rps("paper","scissor")
print(a)    
    





