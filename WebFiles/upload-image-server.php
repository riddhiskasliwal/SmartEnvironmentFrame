<?php
  
    $conn = @mysqli_connect("localhost", "root", "");
	if (!$conn)
		die("Error connecting to database: " . mysqli_error($conn));
	if (!mysqli_select_db($conn, "piframe"))
		die("Error selecting User Information from database: " . mysqli_error($conn));
	 
	if($_SERVER['REQUEST_METHOD'] == 'POST')
	{

		$image = $_POST['image'];
		$data = addslashes($image);

		$sql = "INSERT INTO  images (image)
		VALUES ('{$data}')";

		if ($conn->query($sql) === TRUE) 
	    	echo 'Your image is uploaded';
		else {
		    echo "Error: " . $sql . "<br>" . $conn->error;
		}
		//}
		mysqli_close($conn);
	} else {
		echo "Please Try Again";
	}
 ?>