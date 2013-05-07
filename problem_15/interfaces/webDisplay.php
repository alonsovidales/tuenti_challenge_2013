<?php

interface webDisplayInterface {
	/**
	 * This class is the view for our Tic Tac Toe game.  Each method RETURNS the appropriate
	 * HTML block for display on the page.
	 *
	 * The page is proper HTML5, XHTML, or Strict HTML
	 *
	 * @difficulty 3/5
	 */

	/**
	 * Empty constructor
	 */
	public function __construct();

	/**
	 * Sets the page title and builds the page header HTML, including the main body container,
	 * any navigation, and other top-of-page material.
	 *
	 * @param string $title
	 * @return string HTML
	 */
	public function buildHeader($title);

	/**
	 * Builds the board itself.  Using CSS and/or images, displays the current state of the board.
	 * There may be error messages to show depending at the top of the page.  These should be
	 * highlighted appropriately.
	 *
	 * If the game is still ongoing, provide clickable regions in the playable spaces so the current
	 * player can click there and submit their move.  Requested moves are links back to the current
	 * page with the following querystring params: x and y
	 *
	 * If the game is over, highlights the winning pieces and provide a button which will reset
	 * the board for a new game.  This button links back to the same page with the querystring
	 * param ?new=1
	 *
	 * @param gameInterface Game object.
	 * @param string $errorMessage error message the page should display.  Blank for none.
	 *
	 * @return string HTML
	 */
	public function buildGame(gameInterface $game, $errorMessage);

	/**
	 * Generates the page footer.  Closes the main body container and make any elements that should
	 * go at the bottom of each page.
	 *
	 * @return string HTML
	 */
	public function buildFooter();
}
