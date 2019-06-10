#declared a list to represent matrix
matrix= [x for x in range(9)]
print(matrix)
print('player 1 will be zero')
p1=input('Please enter name of player 1')
p2=input('Please enter name of player 2')
name_and_symbol={
	'O':p1,
	'X':p2
}

#method to mark the positon chosed by player
def mark_position(player,pos):
	while True:
		#check if the position is already used or not
		if isinstance(matrix[pos], int):
			matrix[pos]=player
			return False
		else:
			print("please input an position wich is not used!")
			return True
#method to choose who is the winner 
def check_if_winner(lst):
	if lst[0]==lst[1]==lst[2]:
		print('{} is the winner'.format(name_and_symbol[lst[0]]))
		return False
	if lst[0]==lst[3]==lst[6]:
		print('{} is the winner'.format(name_and_symbol[lst[0]]))
		return False
	if lst[0]==lst[4]==lst[8]:
		print('{} is the winner'.format(name_and_symbol[lst[0]]))
		return False
	if lst[6]==lst[7]==lst[8]:
		print('{} is the winner'.format(name_and_symbol[lst[8]]))
		return False
	if lst[2]==lst[5]==lst[8]:
		print('{} is the winner'.format(name_and_symbol[lst[8]]))
		return False
	if lst[2]==lst[4]==lst[6]:
		print('{} is the winner'.format(name_and_symbol[lst[4]]))
		return False
	if lst[3]==lst[4]==lst[5]:
		print('{} is the winner'.format(name_and_symbol[lst[4]]))
		return False
	if lst[1]==lst[4]==lst[7]:
		print('{} is the winner'.format(name_and_symbol[lst[4]]))
		return False
	return True
print('_____________')
print('|_0_|_1_|_2_|')
print('|_3_|_4_|_5_|')
print('|_6_|_7_|_8_|')
chosed= True
for x in range(9):
	print(x,'iteration')
	print('_____________')
	print('|_{}_|_{}_|_{}_|'.format(matrix[0],matrix[1],matrix[2]))
	print('|_{}_|_{}_|_{}_|'.format(matrix[3],matrix[4],matrix[5]))
	print('|_{}_|_{}_|_{}_|'.format(matrix[6],matrix[7],matrix[8]))
	while chosed:
		print('the square are denoted by numbers')
		pos=int(input("player 1 please choose a square"))
		chosed= mark_position('O',pos)
	chosed= True
	if not check_if_winner(matrix):
		break
	while chosed:
		print('the square are denoted by numbers')
		pos=int(input("player 2 please choose a square"))
		chosed= mark_position('X',pos)
	chosed= True	
	if not check_if_winner(matrix):
		break
