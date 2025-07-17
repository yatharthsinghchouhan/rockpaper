# rock paper code


continue_check=True
while continue_check:
	i=1

	while i<=3:
		
		player1=input(" rock,  paper,  scissor:")
		player2=input("rock,  paper, scissor:")

		if player1=="rock" and player2=='paper':
			print("player2 wins")
		elif player1=='rock' and player2=='scissor':
			print("player 1 wins")
		elif player1=='rock' and player2=='rock':
			print("tie")
		elif player1=="paper" and player2=='rock':
			print("player1 wins")
		elif player1=='paper' and player2=='scissor':
			print("player 2 wins")
		elif player1=='paper' and player2=='paper':
			print("tie")
		elif player1=="scissor" and player2=='paper':
			print("player1 wins")
		elif player1=='scissor' and player2=='rock':
			print("player 2 wins")
		elif player1=='scissor' and player2=='scissor':
			print("tie")

		else :
			print("invalid syntax")
		i+=1
	choice=input("press Y to continueor N to stop :")
	if choice=="Y":
		contiune_check=True
		print("lETS play again")
	else:
		continue_check = False
		print(" the game has ended   ")









