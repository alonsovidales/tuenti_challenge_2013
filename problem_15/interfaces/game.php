<?php

interface gameInterface {
	/**
	 * Game is the gateway between the page controller and the board itself.  It simplifies
	 * the interaction between the page controller and the board.  It builds the pieces and
	 * tells the board where to put them.  It determines who goes first and ensures players
	 * take turns.  This class's job is to hide the implementation details of the objects it
	 * contains.
	 *
	 * @difficulty 4/5
	 */

	/**
	 * Builds the object and start a new game by calling $this->newGame()
	 */
	public function __construct();

	/**
	 * Resets the board.
	 * @return string First player X or O
	 */
	public function newGame();

	/**
	 * Determines which player is up next.
	 * @return mixed X, O, or false if game is over.
	 */
	public function whoseTurnIsIt();

	/**
	 * Attempts to set the next piece at the given coordinates.  The appropriate piece (X or O)
	 * is kept track of internally.
	 *
	 * This method checks whether or not the coordinates are integers.  If not, throw an exception.
	 * Boundary checking is handled by a lower layer and exceptions are caught by a higher
	 * layer.
	 *
	 * 0,0 is the top left corner of the board.
	 *
	 * @param int $x
	 * @param int $y
	 */
	public function placeNextPiece($x, $y);

	/**
	 * Returns a simple indication of what piece is at a given coordinate.
	 *
	 * This method checks whether or not the coordinates are integers.  If not, throw an exception.
	 * Boundary checking is handled by a lower layer and exceptions are caught by a higher
	 * layer.
	 *
	 * 0,0 is the top left corner of the board.
	 *
	 * @param int $x
	 * @param int $y
	 * @return mixed X, O, or false
	 */
	public function readLocation($x, $y);

	/**
	 * Indicates who won the game or returns false if game is not over.
	 * @return mixed X, O, or false
	 */
	public function getWinner();

	/**
	 * Returns a grid array indicating true for each piece that is part of the winning line.
	 * The game class is responsible for determining the location of the winning pieces and
	 * the actual winning pattern with boardInterface::getWinningLine().  Game class translates
	 * the board class abbreviations into a more useful form. If there is no current winner, it
	 * will return a grid of all falses.
	 *
	 * @see boardInterface::getWinningLine() for winning line format.
	 *
	 * For example:
	 * Winning line "|2" might be a board like this:
	 * X| |O
	 * -----
	 *  |X|O
	 * -----
	 * X|O|O
	 *
	 * and would return
	 *	$coords[0] = array(FALSE, FALSE, TRUE);
	 *	$coords[1] = array(FALSE, FALSE, TRUE);
	 *	$coords[2] = array(FALSE, FALSE, TRUE);
	 *
	 * @return array
	 */
	public function getWinningCoordinates();

}
