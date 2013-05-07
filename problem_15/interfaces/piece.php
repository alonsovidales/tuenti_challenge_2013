<?php

interface pieceInterface {
	/**
	 * The Tic Tac Toe piece is a simple construct with two important duties:
	 *
	 * First, upon creation, it must be told what sort of piece it is.  If there is invalid
	 * input here, it will bubble up an error.
	 *
	 * Second, when the piece is placed on the board, the piece itself must determine whether
	 * the coordinates are within the grid.  When asked, the piece will divulge its location.
	 *
	 * This class is built to be safe to serialize and unserialize with __sleep() and __wakeup()
	 * defined if needed.
	 *
	 * @difficulty 1/5
	 */

	/**
	 * Build a new piece.  The only valid inputs are X and O.
	 * Out of bounds input throws an exception.
	 *
	 * @param type $type X or O
	 */
	public function __construct($type);

	/**
	 * Gets the piece type.  Will either return X or O
	 * @return string type
	 */
	public function getPieceType();

	/**
	 * Sets the coordinate values for the position of the piece.
	 * 0,0 is the top left of the board
	 * Out of bounds input throws an exception.
	 *
	 * This method is only called from within the board object when the piece
	 * is placed on the board.  The board object has already determined that there are no
	 * other pieces at this coordinate.
	 *
	 * @param int $x  Valid values are 0,1, and 2
	 * @param int $y  Valid values are 0,1, and 2
	 */
	public function setLocation($x, $y);

	/**
	 * Returns a coordinate value for the horizontal position of the piece.
	 * 0,0 is the top left of the board
	 *
	 * @return mixed position, values: false, 0, 1 or 2
	 */
	public function getLocationX();

	/**
	 * Returns a coordinate value for the vertical position of the piece.
	 * 0,0 is the top left of the board
	 *
	 * @return mixed position, values: false, 0, 1 or 2
	 */
	public function getLocationY();

	/**
	 * Magic method wrapper for getPieceType();
	 */
	public function __toString();
}
