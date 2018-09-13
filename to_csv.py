import chess
import chess.pgn

white_wins = 0
black_wins = 0
draws = 0

games = open("lichess_960_6.pgn")
outfile = open("out6.csv", "a")

game = chess.pgn.read_game(games)
outfile.write("White;Black;White Rating;Black Rating;Avg Rating;Result;Time Control;Game url\n")

num_games = 0
while game:
    white = game.headers['White']
    black = game.headers['Black']
    result = game.headers['Result']
    site = game.headers['Site']
    tc = game.headers['TimeControl']
    wr = game.headers['WhiteElo']
    br = game.headers['BlackElo']

    try:
    	avg = str((int(wr) + int(br))/2)
    except:
    	avg = '?'

    outfile.write(white + ";" + black + ";" + wr + ";" + br + ";" + avg + ";" + result + ";" + tc + ";" + site + "\n")

    num_games += 1

    if result == "1-0":
    	white_wins += 1
    elif result == "0-1":
    	black_wins += 1
    else:
    	draws += 1

    game = chess.pgn.read_game(games)

print("-- Number of games: %s --" % num_games)
print("-- Number of white wins: %s --", white_wins)
print("-- Number of black wins: %s --", black_wins)
print("-- Number of draws: %s --", draws)
