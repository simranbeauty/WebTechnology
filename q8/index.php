<?php
session_start();
if (!isset($_SESSION['auth_user'])) {
    header("Location: login.php");
    exit();
}
?>
<!DOCTYPE html>
<html>
<head><title>Dashboard</title></head>
<body>
    <h2>Welcome to Dashboard</h2>
    <p>Hello, <?php echo $_SESSION['auth_user']; ?>!</p>
    <a href="logout.php">Logout</a>
</body>
</html>
