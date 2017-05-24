from deck import Deck 
from card import Card 
print("Welcome to War, please enter names of player1 and player2 \n")
ctr=0 
Player1= str(raw_input("Player1- "))
Player2= str(raw_input("Player2- "))

Player1w =0
Player2w =0
while (ctr!=52):
	myDeck= Deck()
	myDeck.Shuffle()
	raw_input(Player1 + " Press enter to draw card")
	draw1= myDeck.TakeFromTop()
	draw1.displayCard()
	raw_input(Player2 + " Press enter to draw card")
	draw2= myDeck.TakeFromTop()
	draw2.displayCard()
	if (draw1>draw2):
		Player1w+=1 
		print(Player1 + " wins!")
		ctr=1 
	if (draw2>draw1):
		Player2w+=1
		print(Player2 + " wins!")
		ctr=1
	if (draw1==draw2):
		raw_input("War! Press enter to draw again!")
		War1= mydeck.TakeFromTop()
		War1.displayCard()
		War2= mydeck.TakeFromTop()
		War2.displayCard()
	if Player1w== 52:
		print(Player1 + "Wins the game!")
		ctr=1
	if Player2w== 52:
		print(Player2 + "Wins the game!")
		ctr=1

	
