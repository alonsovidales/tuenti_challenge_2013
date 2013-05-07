<?php
    $value = file_get_contents('test');
    echo base64_decode($value);
