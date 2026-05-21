<?php require_once '../db.php'; ?>
<!DOCTYPE html>
<html>
<head><title>Registration Form</title></head>
<body>
    <h2>User Registration</h2>
    <form method="POST">
        <input type="text" name="name" placeholder="Full Name" required><br><br>
        <input type="email" name="email" placeholder="Email" required><br><br>
        <input type="password" name="password" placeholder="Password" required><br><br>
        <input type="text" name="phone" placeholder="Phone" required><br><br>
        Gender: 
        <input type="radio" name="gender" value="male" required> Male
        <input type="radio" name="gender" value="female"> Female
        <input type="radio" name="gender" value="others"> Others<br><br>
        <select name="faculty" required>
            <option value="">Select Faculty</option>
            <option value="BCA">BCA</option>
            <option value="BIM">BIM</option>
            <option value="CSIT">CSIT</option>
        </select><br><br>
        <button type="submit" name="register">Register</button>
    </form>

    <?php
    if (isset($_POST['register'])) {
        $name = $_POST['name'];
        $email = $_POST['email'];
        $pass = password_hash($_POST['password'], PASSWORD_DEFAULT);
        $phone = $_POST['phone'];
        $gender = $_POST['gender'];
        $faculty = $_POST['faculty'];

        try {
            $stmt = $pdo->prepare("INSERT INTO registrations (name, email, password, phone, gender, faculty) VALUES (?, ?, ?, ?, ?, ?)");
            $stmt->execute([$name, $email, $pass, $phone, $gender, $faculty]);
            echo "<p style='color:green;'>Registration successful!</p>";
        } catch(PDOException $e) {
            echo "<p style='color:red;'>Error: " . $e->getMessage() . "</p>";
        }
    }
    ?>
</body>
</html>
