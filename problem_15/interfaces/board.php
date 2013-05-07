<?php

interface boardInterface {
	/**
	 * The game board is responsible for understanding the basic mechanics of the game.
	 * It doesn't care about boundaries, but it can tell you where the pieces are
	 * and who won (if anyone).
	 *
	 * The board is not concerned with basic gameplay, just where the pieces are and whether
	 * there are three in a row in the 3x3 gameplay area.
	 *
	 * This class is built to be safe to serialize and unserialize with __sleep() and __wakeup()
	 * defined if needed.
	 *
	 * @difficulty 5/5
	 */

	/**
	 * Builds a new board.  This method calls $this->resetBoard() to initialize
	 */
	public function __construct();

	/**
	 * Set a piece to a given location.  If the location already has a piece,
	 * return false, otherwise return true.
	 *
	 * This method will verify whether the piece coordinates are available.  If they are,
	 * it tells the piece its coordinates.  The piece itself does error checking and may
	 * thow an exception if the coordinates are out of bounds.  It alsow throws an exception
	 * if the game is over and this method is called.
	 *
	 * @param pieceInterface $piece
	 * @param int horizontal position. valid values 0, 1, 2
	 * @param int vertical position. valid values 0, 1, 2
	 * @return bool success
	 */
	public function setPiece(pieceInterface $piece, $x, $y);

	/**
	 * Read the piece at the given location
	 * @param type $x
	 * @param type $y
	 */
	public function readLocation($x, $y);

	/**
	 * Evaluates the board and determines whether someone has won.
	 *
	 * @return bool Has someone won the game?
	 */
	public function isGameOver();

	/**
	 * If the game has been won, this tells who the winner is.
	 *
	 * @return mixed X, O, or false
	 */
	public function getWinner();

	/**
	 * This class communicates the row that won the game in a very compact manner.  There are
	 * three classes of winning lines:
	 *	| vertical
	 *  - horizontal
	 *  \/ diagonals
	 *
	 * The left and right diagonals are simply the forward or backslash.  There is only one way to
	 * win with a diagonal.
	 *
	 * The horizontal and vertical winning lines each have three possible combinations: 0, 1, or 2
	 * They communicate their respective winning lines as follows:
	 * |0 |1 |2
	 * -0 -1 -2
	 *
	 * EXAMPLE BOARDS & WINNING LINE CODES
	 * O| |X   O| |X   X|X|X    | |X
	 * -----   -----   -----   -----
	 *  |X|     |O|     |O|     |X|
	 * -----   -----   -----   -----
	 * X|O|    X|X|O    |O|    O|O|O
	 *
	 *   /       \       |1      -2
	 *
	 * @return string winning line code
	 */
	public function getWinningLine();

	/**
	 * Clear the game board and start fresh.
	 */
	public function resetBoard();

}
