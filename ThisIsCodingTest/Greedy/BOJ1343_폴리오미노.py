board = input()
result = []
i = 0

while i < len(board):
    if board[i:i+4] == 'XXXX':
        result.append('AAAA')
        i+=4
    elif board[i:i+2] == 'XX':
        result.append('BB')
        i+=2
    elif board[i:i+1] == '.':
        result.append('.')
        i+=1
    else:
        break

result = "".join(result)

if len(result) == len(board):
    print(result)
else:
    print(-1)
