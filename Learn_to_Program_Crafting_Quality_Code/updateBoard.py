def updateBoard(currentBoard, letter, positionsList):
    """
    :param currentBoard: current board list
    :param letter: letter to add
    :param positionsList: list of positions to add the letter
    :return: a string list of the updated board
    """
    for position in range(len(currentBoard)):
        if position in positionsList:
            currentBoard[position] = letter

    return currentBoard

print(updateBoard(["_", "_", "_"], "A", [1, 2]))
