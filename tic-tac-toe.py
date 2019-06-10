#declared a list to represent matrix
matrixtrix= [x for x in range(9)]
print(matrixtrix)
print('player 1 will be zero')
p1=input('Please enter name of player 1')
p2=input('Please enter name of player 2')
name_and_symbol={
	'O':p1,
	'X':p2
}
//method to mark the positon chosed by player
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
		print('{} is the winner'.format(name_and_symbol[0]))
		return False
	if lst[0]==lst[3]==lst[6]:
		print('{} is the winner'.format(name_and_symbol[0]))
		return False
	if lst[0]==lst[4]==lst[8]:
		print('{} is the winner'.format(name_and_symbol[0]))
		return False
	if lst[6]==lst[7]==lst[8]:
		print('{} is the winner'.format(name_and_symbol[6]))
		return False
	if lst[2]==lst[5]==lst[8]:
		print('{} is the winner'.format(name_and_symbol[2]))
		return False
	if lst[2]==lst[4]==lst[6]:
		print('{} is the winner'.format(name_and_symbol[2]))
		return False
	if lst[3]==lst[4]==lst[5]:
		print('{} is the winner'.format(name_and_symbol[4]))
		return False
	if lst[1]==lst[4]==lst[7]:
		print('{} is the winner'.format(name_and_symbol[4]))
		return False
	return True
print('_____________')
print('|_1_|_2_|_3_|')
print('|_4_|_5_|_6_|')
print('|_7_|_8_|_9_|')
chosed= True
for x in range(9):
	print(x,'iteration')
	while chosed:
		print('the square are denoted by numbers')
		pos=int(input("player 1 please choose a square"))
		chosed= mark_position('O',pos)
	chosed= True
	while chosed:
		print('the square are denoted by numbers')
		pos=int(input("player 2 please choose a square"))
		chosed= mark_position('X',pos)
	chosed= True
	print('_____________')
	print('|_{}_|_{}_|_{}_|'.format(matrix))
	print('|_{}_|_{}_|_{}_|'.format(matrix))
	print('|_{}_|_{}_|_{}_|'.format(matrix))	
	if not check_if_winner(matrix):
		break
