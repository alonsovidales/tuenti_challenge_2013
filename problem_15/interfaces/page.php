<?php

interface pageInterface {

	/**
	 * Attempts to load a game.  If none is saved, creates a new one.
	 */
	public function __construct();

	/**
	 * Performs the actual game saving
	 */
	public function saveGame();

	/**
	 * Performs the actual game loading from a prior save
	 */
	public function loadGame();

	/**
	 * The main event.
	 *
	 * If there is a pending move, attempt to play it.  Capture any exceptions and turn them into
	 * error messages passed along to the display object.  Execute the display object's three
	 * primary mehtods and echo their output.
	 *
	 * Bonus points for double checking the webDisplay output and throwing a fatal error if any of
	 * the methods return blank.
	 */
	public function execute();
}
