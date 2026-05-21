<?php 
require_once '../db.php';
session_start();
?>
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Login Form</h2>
    <form method="POST">
        <input type="email" name="email" placeholder="Email" required><br><br>
        <input type="password" name="password" placeholder="Password" required><br><br>
        <button type="submit" name="login">Login</button>
    </form>

    <?php
    if (isset($_POST['login'])) {
        $email = $_POST['email'];
        $password = $_POST['password'];

        $stmt = $pdo->prepare("SELECT * FROM registrations WHERE email = ?");
        $stmt->execute([$email]);
        $user = $stmt->fetch();

        if ($user && password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['user_name'] = $user['name'];
            echo "<p style='color:green;'>Login successful! Welcome {$user['name']}.</p>";
        } else {
            echo "<p style='color:red;'>Invalid email or password.</p>";
        }
    }
    ?>
</body>
</html>
