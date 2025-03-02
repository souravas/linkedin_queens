import math


def fetch_file_contents():
    with open("input_html.txt", "r") as file:
        return file.readlines()


def parse_html():
    board_color_html = []
    for line in fetch_file_contents():
        if "data-cell-idx" in line:
            board_color_html.append(line)
    return board_color_html


def find_color(line):
    return line.split(',')[0].split('color')[1].strip()


def board_length():
    return int(math.sqrt(len(parse_html())))


def create_board():
    length = board_length()
    board = [[0] * length for _ in range(length)]
    k = 0
    board_colors_html = parse_html()
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = find_color(board_colors_html[k])
            k += 1
    return board


def unique_colors(board):
    colors = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] not in colors:
                colors.append(board[i][j])
    return colors


def is_valid(board, i, j):
    for index in range(len(board[0])):
        if board[i][index].startswith("-"):
            if index != j:
                return False
    for index in range(len(board)):
        if board[index][j].startswith("-"):
            if index != i:
                return False
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj].startswith("-"):
            return False
    return True


def fill_board(board, colors_list_index, colors_list):
    if colors_list_index >= len(colors_list):
        return True
    current_color = colors_list[colors_list_index]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if current_color == board[i][j]:
                board[i][j] = "-" + current_color
                if is_valid(board, i, j):
                    if fill_board(board, colors_list_index + 1, colors_list):
                        return True
                board[i][j] = current_color
    return False


def print_board(board):
    cell_width = 15
    for row in board:
        for cell in row:
            display_text = "♛" if cell.startswith("-") else cell.strip()
            print(display_text.ljust(cell_width), end="  ")
        print()


def main():
    board = create_board()
    colors_list = unique_colors(board)
    fill_board(board, 0, colors_list)
    print_board(board)


main()
