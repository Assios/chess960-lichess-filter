import chess
import chess.pgn
import urllib2
from os import listdir
from os.path import isfile, join

def get_start_position(fen):
    return fen.split('/')[0].upper()

file = "lichess_all_960.pgn"

pgn_out = open("lichess_960_6.pgn", "a")

print("Checking " + file)
pgn_in = open("games/" + file)

game = chess.pgn.read_game(pgn_in)
exporter = chess.pgn.FileExporter(handle=pgn_out, headers=True, variations=True, comments=True)

processed_games = 0

while game:
    processed_games += 1
    if get_start_position(game.headers["FEN"]) == "BRKQNBRN":
        pgn_out = game.accept(exporter)

    if (processed_games % 10000 == 0):
        print(processed_games)

    game = chess.pgn.read_game(pgn_in)
