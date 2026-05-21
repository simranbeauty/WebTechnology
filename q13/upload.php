<?php
if (isset($_POST['upload'])) {
    $target_dir = "uploads/";
    if (!is_dir($target_dir)) {
        mkdir($target_dir, 0777, true);
    }
    
    $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
    
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        $msg = "The file ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " has been uploaded.";
    } else {
        $msg = "Sorry, there was an error uploading your file.";
    }
}
?>
<!DOCTYPE html>
<html>
<head><title>File Upload</title></head>
<body>
    <h2>Upload a File</h2>
    <?php if(isset($msg)) echo "<p>$msg</p>"; ?>
    <form method="POST" enctype="multipart/form-data">
        Select image to upload:
        <input type="file" name="fileToUpload" required><br><br>
        <button type="submit" name="upload">Upload File</button>
    </form>
</body>
</html>
