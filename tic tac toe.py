board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]
print("Tic Tac Toe Game enter section between(0-8)")
print(board[0], "|", board[1], "|", board[2])
print("----------")
print(board[3], "|", board[4], "|", board[5])
print("----------")
print(board[6], "|", board[7], "|", board[8])

RESULT_1 = 'Player with X win'
RESULT_2 = 'Player with O win'
TIE = "Tie score"

def draw_board_section():

   print(board[0], "|", board[1], "|", board[2])
   print("----------")
   print(board[3], "|", board[4], "|", board[5])
   print("----------")
   print(board[6], "|", board[7], "|", board[8])

while True:
       section = int(input("Player1 choose section : "))
       section2 = int(input("Player2 choose section : "))
       if section == section2:
           print("The section is already taken!")
           continue

       elif 0 not in board: # Check for Tie result
           print(TIE)


       if board[section] != "x" and board[section2] != "o":
           board[section] = "x"
           board[section2] = "o"

       draw_board_section()

	   # Check row 
	   def check_row_O():
		   if board[0] == "o" and board[1] == "o" and board[2] == "o" or \
              board[3] == "o" and board[4] == "o" and board[5] == "o" or \
              board[6] == "o" and board[7] == "o" and board[8] == "o":
               print(RESULT_2)
		
		check_row_O()	
		
		# Check column
		def check_column_O():
            if board[0] == "o" and board[3] == "o" and board[6] == "o" or \
               board[1] == "o" and board[4] == "o" and board[7] == "o" or \
               board[2] == "o" and board[5] == "o" and board[8] == "o":
                print(RESULT_2)
        
		check_column_O()

		# Check diagonal
		def check_diagonal_O():	
            if board[0] == "o" and board[4] == "o" and board[8] == "o" or \
               board[2] == "o" and board[4] == "o" and board[6] == "o":
               print(RESULT_2)
		
		check_diagonal_O()

       # Check row
       def check_row_X():
           if board[0] == "x" and board[1] == "x" and board[2] == "x" or \
              board[3] == "x" and board[4] == "x" and board[5] == "x" or \
              board[6] == "x" and board[7] == "x" and board[8] == "x":
               print(RESULT_1)

       check_row_X()

        # Check column
       def check_column_X():
           if board[0] == "x" and board[3] == "x" and board[6] == "x" or \
              board[1] == "x" and board[4] == "x" and board[7] == "x" or \
              board[2] == "x" and board[5] == "x" and board[8] == "x":
               print(RESULT_1)

       check_column_X()

       # Check diagonal
       def check_diagonal_X():
           if board[0] == "x" and board[4] == "x" and board[8] == "x" or \
              board[2] == "x" and board[4] == "x" and board[6] == "x":
               print(RESULT_1)

       check_diagonal_X()