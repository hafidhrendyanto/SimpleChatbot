<?php
    // echo $_GET['subject'];
    // $s_amount = $_POST['s_amount'];
    // echo $s_amount; 
    // $txt = ' "dimana kantin terdekat labtek 5" ';
    // $command = 'python C:\xampp\htdocs\stima\boyermoore.py'. $txt;
    // 
    // echo $command;
    // echo "------";
    // $s = "apa itu chatbot";
    // python $command = 'python C:\xampp\htdocs\stima\boyermoore.py' . $s;
    // python $output = passthru($command);
    // echo shell_exec($command);
    // $s = exec('python C:\xampp\htdocs\test.py');
    // echo "eh co php";

    if ($_POST['method'] == 'bm'){
		$ques = $_POST['ques'];
		$temp = exec('python boyermoore.py "'.trim($_POST['ques']," "));
		echo $temp;
    }
	// elseif ($_POST['method'] == 'kmp'){
		// $question = $_POST['question'];
		// $temp = exec('python KMP.py "'.trim($_POST['question']," "));
		// echo $temp;
	// }
	// elseif ($_POST['method'] == 'bm'){
		// $question = $_POST['question'];
		// $temp = exec('python Boyer-Moore.py "'.trim($_POST['question']," "));
		// echo $temp;
	// }
?>