<?php

require_once(dirname(__DIR__) . '/interfaces/page.php');

class page implements pageInterface {
	/** @var gameInterface $game */
	private $game;

	/** @var webDisplay $view */
	private $view;

	private $secret;

	public function __construct() {
		$this->view = new webDisplay();
		//$this->secret = $this->getSecret();
                // Used the comented loop at the saveGame method in order to obtain this value by brute force
		$this->secret = "IETN";
		$this->loadGame();
	}

	private function getSecret() {
		//$secret = file_get_contents("/tmp/secret.txt");
		$secret = false;
		if ($secret == FALSE) {
			$arr = str_split('TUENTI');
			shuffle($arr);
			$arr = array_slice($arr, 0, 4);
			$secret = implode('', $arr);
			//file_put_contents("/tmp/secret.txt", $secret);
		}
		return $secret;
	}

	public function execute() {
		$errorMessage = '';
		if(isset($_GET['new']) && $_GET['new'] == 1) {
			$this->game->newGame();
			$this->saveGame();
			header('Location: ?');
			exit;
		}

		try {
			if(isset($_GET['x']) && isset($_GET['y'])) {
				$x = (int)$_GET['x'];
				$y = (int)$_GET['y'];
				$this->game->placeNextPiece($x, $y);
				$this->saveGame();
				header('Location: ?');
				exit;
			}
		} catch (Exception $e) {
			$errorMessage = $e->getMessage();
		}

		/*echo $this->view->buildHeader('Oh no! Tic Tac Tuenti!');
		echo $this->view->buildGame($this->game, $errorMessage);
		echo $this->view->buildFooter();
		$this->saveGame();*/
	}

	public function loadGame() {
		if (isset($_COOKIE['game'])) {
			list($gamestate, $h) = explode("|", $_COOKIE['game']);
			$hh = md5($gamestate . $this->secret);
			if ($h != $hh) {
				exit;
			}
			$this->game = unserialize(base64_decode($_COOKIE['game']));
		} else {
			$this->game = new game();
		}
	}

	public function saveGame() {
		$gamestate = base64_encode(serialize($this->game));
		// If you uncomment this code, thie system will search for the secret by brute force
		/*do {
			$this->secret = $this->getSecret();
			$h = md5($gamestate . $this->secret);
			if ("f074139f9390a2ace73b73dc5cacbf9f" == $h) {
				echo "FOUND!!!!!!!!!" . PHP_EOL;
			}
		} while ("f074139f9390a2ace73b73dc5cacbf9f" != $h);

		echo "-- " . $this->secret . " --" . PHP_EOL;*/

		//$this->secret = $this->getSecret();

		$h = md5($gamestate . $this->secret);

                echo urlencode($gamestate . "|" . $h). PHP_EOL; die();

		setcookie('game', $gamestate . "|" . $h, time() + (86400 * 7));
	}

	public function getFakeCookie($inSecret) {
                $this->loadGame();
                // Modify the file with the key that I want
		$this->game->versionFile = '/home/ttt/data/keys/' . $inSecret;

		$gamestate = base64_encode(serialize($this->game));
		$this->secret = "IETN";

		$h = md5($gamestate . $this->secret);

                return urlencode($gamestate . "|" . $h);
	}
}
