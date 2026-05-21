<?php
$filename = "data.txt";
$msg = "";

if (isset($_POST['write'])) {
    $file = fopen($filename, "w") or die("Unable to open file!");
    fwrite($file, $_POST['content'] . "\n");
    fclose($file);
    $msg = "File written successfully.";
}

if (isset($_POST['append'])) {
    $file = fopen($filename, "a") or die("Unable to open file!");
    fwrite($file, $_POST['content'] . "\n");
    fclose($file);
    $msg = "Content appended successfully.";
}

$file_contents = "";
if (file_exists($filename)) {
    $file = fopen($filename, "r");
    if (filesize($filename) > 0) {
        $file_contents = fread($file, filesize($filename));
    }
    fclose($file);
}
?>
<!DOCTYPE html>
<html>
<head><title>File Operations</title></head>
<body>
    <h2>Read, Write, and Append</h2>
    <?php if($msg) echo "<p style='color:green;'>$msg</p>"; ?>
    
    <form method="POST">
        <textarea name="content" rows="4" cols="50" required placeholder="Enter text here..."></textarea><br><br>
        <button type="submit" name="write">Write (Overwrite)</button>
        <button type="submit" name="append">Append</button>
    </form>

    <h3>Current File Contents (Read Operation):</h3>
    <pre style="background:#eee; padding:10px; width:400px;"><?php echo htmlspecialchars($file_contents); ?></pre>
</body>
</html>
