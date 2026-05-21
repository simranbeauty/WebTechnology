import os

def write_file(path, content):
    if os.path.dirname(path): os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

# Q1: Dynamic Content Generation
write_file('q1/index.php', """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dynamic Content Generation</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f4f4f9; }
        .card { background: white; border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        table { border-collapse: collapse; width: 100%; margin-top: 10px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #007bff; color: white; }
    </style>
</head>
<body>
    <h2>1. HTML List from Array</h2>
    <ul>
        <?php
        $fruits = ["Apple", "Banana", "Cherry", "Mango"];
        foreach ($fruits as $fruit) {
            echo "<li>$fruit</li>";
        }
        ?>
    </ul>

    <h2>2. HTML Table from Multidimensional Array</h2>
    <table>
        <tr><th>ID</th><th>Name</th><th>Faculty</th></tr>
        <?php
        $students = [
            ["id" => 1, "name" => "Ram", "faculty" => "BCA"],
            ["id" => 2, "name" => "Sita", "faculty" => "BIM"],
            ["id" => 3, "name" => "Hari", "faculty" => "CSIT"]
        ];
        foreach ($students as $student) {
            echo "<tr><td>{$student['id']}</td><td>{$student['name']}</td><td>{$student['faculty']}</td></tr>";
        }
        ?>
    </table>

    <h2>3. Card Layout from Array</h2>
    <?php
    $products = [
        ["title" => "Laptop", "price" => "$1200", "desc" => "High performance laptop."],
        ["title" => "Smartphone", "price" => "$800", "desc" => "Latest model smartphone."]
    ];
    foreach ($products as $p) {
        echo "<div class='card'>";
        echo "<h3>{$p['title']}</h3>";
        echo "<p><strong>Price:</strong> {$p['price']}</p>";
        echo "<p>{$p['desc']}</p>";
        echo "</div>";
    }
    ?>
</body>
</html>""")

# Q2: Interest Calculator
write_file('q2/interest.php', """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Interest Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        form { margin-bottom: 20px; padding: 15px; border: 1px solid #ccc; width: 300px; }
        input, button { margin-top: 10px; width: 100%; padding: 8px; }
        .result { padding: 15px; background: #e9ecef; border-left: 5px solid #007bff; width: 300px; }
    </style>
</head>
<body>
    <h2>Interest Calculator</h2>
    <form method="POST">
        <label>Principal (P):</label>
        <input type="number" name="principal" required>
        <label>Rate (R) in %:</label>
        <input type="number" step="0.01" name="rate" required>
        <label>Time (T) in Years:</label>
        <input type="number" step="0.01" name="time" required>
        <button type="submit" name="calculate">Calculate</button>
    </form>

    <?php
    if (isset($_POST['calculate'])) {
        $p = $_POST['principal'];
        $r = $_POST['rate'];
        $t = $_POST['time'];

        $simple_interest = ($p * $t * $r) / 100;
        $compound_interest = $p * pow((1 + $r / 100), $t) - $p;

        echo "<div class='result'>";
        echo "<strong>Simple Interest:</strong> " . number_format($simple_interest, 2) . "<br>";
        echo "<strong>Compound Interest:</strong> " . number_format($compound_interest, 2);
        echo "</div>";
    }
    ?>
</body>
</html>""")

# Q3: Marksheet
write_file('q3/marksheet.php', """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dynamic Marksheet</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        form { margin-bottom: 20px; padding: 15px; border: 1px solid #ccc; width: 300px; }
        input, button { margin-top: 10px; width: 100%; padding: 8px; }
        table { border-collapse: collapse; width: 400px; margin-top: 20px; }
        th, td { border: 1px solid #000; padding: 10px; text-align: center; }
        th { background: #f0f0f0; }
    </style>
</head>
<body>
    <h2>Enter Marks</h2>
    <form method="POST">
        <input type="number" name="marks[]" placeholder="Web Tech Marks" required max="100">
        <input type="number" name="marks[]" placeholder="Java Marks" required max="100">
        <input type="number" name="marks[]" placeholder="DSA Marks" required max="100">
        <input type="number" name="marks[]" placeholder="SAD Marks" required max="100">
        <input type="number" name="marks[]" placeholder="Stats Marks" required max="100">
        <button type="submit" name="generate">Generate Marksheet</button>
    </form>

    <?php
    if (isset($_POST['generate'])) {
        $subjects = ["Web Technology", "Java Programming", "DSA", "SAD", "Statistics"];
        $marks = $_POST['marks'];
        $total = array_sum($marks);
        $percent = $total / 5;
        
        echo "<h2>Marksheet</h2>";
        echo "<table>";
        echo "<tr><th>Subject</th><th>Full Marks</th><th>Obtained Marks</th></tr>";
        for ($i = 0; $i < 5; $i++) {
            echo "<tr><td>{$subjects[$i]}</td><td>100</td><td>{$marks[$i]}</td></tr>";
        }
        echo "<tr><th colspan='2'>Total</th><th>{$total}</th></tr>";
        echo "<tr><th colspan='2'>Percentage</th><th>{$percent}%</th></tr>";
        echo "</table>";
    }
    ?>
</body>
</html>""")

# Database Connection Helper (used in 4, 5, 8, 9, 10, 11, 12)
db_code = """<?php
$host = '127.0.0.1';
$db   = 'webtech_lab';
$user = 'root';
$pass = '';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];
try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\\PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}
?>"""
write_file('db.php', db_code)

# Q4: Registration Form
write_file('q4/register.php', """<?php require_once '../db.php'; ?>
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
</html>""")

# Q5: Login Process
write_file('q5/login.php', """<?php 
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
</html>""")
