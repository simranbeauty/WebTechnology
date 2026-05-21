<?php
if (isset($_POST['set'])) {
    setcookie("user_theme", $_POST['theme'], time() + (86400 * 30), "/"); // 30 days
    header("Location: cookie.php"); // Refresh to see cookie
    exit();
}

if (isset($_POST['destroy'])) {
    setcookie("user_theme", "", time() - 3600, "/"); // Expire in past
    header("Location: cookie.php");
    exit();
}
?>
<!DOCTYPE html>
<html>
<head><title>Cookie Management</title></head>
<body>
    <h2>PHP Cookie Operations</h2>
    <p><strong>Current Cookie Data (Theme):</strong> 
        <?php echo isset($_COOKIE['user_theme']) ? $_COOKIE['user_theme'] : 'No cookie data found.'; ?>
    </p>

    <form method="POST">
        <select name="theme">
            <option value="light">Light Mode</option>
            <option value="dark">Dark Mode</option>
        </select>
        <button type="submit" name="set">Store Cookie</button>
    </form>
    <br>
    <form method="POST">
        <button type="submit" name="destroy">Destroy Cookie</button>
    </form>
</body>
</html>
