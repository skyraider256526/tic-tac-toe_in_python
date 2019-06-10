mtrix= [x for x in range(9)]
print(mtrix)
def mark_position(player,pos):
	while True:
		if isinstance(mtrix[pos], int):
			mtrix[pos]=player
			return False
		else:
			print("please input an position wich is not used!")
			return True
def check_if_winner(lst):
	if lst[0]==lst[1]==lst[2]:
		print('{} is the winner'.format(lst[0]))
		return False
	if lst[0]==lst[3]==lst[6]:
		print('{} is the winner'.format(lst[0]))
		return False
	if lst[0]==lst[4]==lst[8]:
		print('{} is the winner'.format(lst[0]))
		return False
	if lst[6]==lst[7]==lst[8]:
		print('{} is the winner'.format(lst[6]))
		return False
	if lst[2]==lst[5]==lst[8]:
		print('{} is the winner'.format(lst[2]))
		return False
	if lst[2]==lst[4]==lst[6]:
		print('{} is the winner'.format(lst[2]))
		return False
	if lst[3]==lst[4]==lst[5]:
		print('{} is the winner'.format(lst[3]))
		return False
	if lst[1]==lst[4]==lst[7]:
		print('{} is the winner'.format(lst[1]))
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
		chosed= mark_position('p1',pos)
	chosed= True
	while chosed:
		print('the square are denoted by numbers')
		pos=int(input("player 2 please choose a square"))
		chosed= mark_position('p2',pos)
	chosed= True
	if not check_if_winner(mtrix):
		break
