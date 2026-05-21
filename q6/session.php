<?php
session_start();

if (isset($_POST['set'])) {
    $_SESSION['username'] = $_POST['username'];
    $msg = "Session variable 'username' set to " . $_SESSION['username'];
}

if (isset($_POST['destroy'])) {
    session_unset();
    session_destroy();
    $msg = "Session destroyed.";
}
?>
<!DOCTYPE html>
<html>
<head><title>Session Management</title></head>
<body>
    <h2>PHP Session Operations</h2>
    <p><strong>Current Session Data:</strong> 
        <?php echo isset($_SESSION['username']) ? $_SESSION['username'] : 'No session data found.'; ?>
    </p>

    <?php if(isset($msg)) echo "<p style='color:blue;'>$msg</p>"; ?>

    <form method="POST">
        <input type="text" name="username" placeholder="Enter Username" required>
        <button type="submit" name="set">Store Session</button>
    </form>
    <br>
    <form method="POST">
        <button type="submit" name="destroy">Destroy Session</button>
    </form>
</body>
</html>
