<?php
require_once '../../db.php';

if (isset($_POST['register'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $pass = password_hash($_POST['password'], PASSWORD_DEFAULT);
    $phone = $_POST['phone'];
    $gender = $_POST['gender'];
    $faculty = $_POST['faculty'];

    $stmt = $pdo->prepare("INSERT INTO registrations (name, email, password, phone, gender, faculty) VALUES (?, ?, ?, ?, ?, ?)");
    if ($stmt->execute([$name, $email, $pass, $phone, $gender, $faculty])) {
        header("Location: login.php");
        exit();
    }
}
?>
<!DOCTYPE html>
<html>
<head><title>Register</title></head>
<body>
    <h2>Auth - Register</h2>
    <form method="POST">
        <input type="text" name="name" placeholder="Name" required><br><br>
        <input type="email" name="email" placeholder="Email" required><br><br>
        <input type="password" name="password" placeholder="Password" required><br><br>
        <input type="text" name="phone" placeholder="Phone" required><br><br>
        <input type="radio" name="gender" value="male" checked> Male
        <input type="radio" name="gender" value="female"> Female<br><br>
        <input type="text" name="faculty" placeholder="Faculty" required><br><br>
        <button type="submit" name="register">Register</button>
    </form>
</body>
</html>
