import os

def write_file(path, content):
    if os.path.dirname(path): os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

# Q6: Session Data
write_file('q6/session.php', """<?php
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
</html>""")

# Q7: Cookies Data
write_file('q7/cookie.php', """<?php
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
</html>""")

# Q8: Complete Authentication
write_file('q8/index.php', """<?php
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
</html>""")

write_file('q8/login.php', """<?php
require_once '../../db.php';
session_start();

if (isset($_POST['login'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];

    $stmt = $pdo->prepare("SELECT * FROM registrations WHERE email = ?");
    $stmt->execute([$email]);
    $user = $stmt->fetch();

    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['auth_user'] = $user['name'];
        header("Location: index.php");
        exit();
    } else {
        $error = "Invalid credentials.";
    }
}
?>
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Auth - Login</h2>
    <?php if(isset($error)) echo "<p style='color:red;'>$error</p>"; ?>
    <form method="POST">
        <input type="email" name="email" placeholder="Email" required><br><br>
        <input type="password" name="password" placeholder="Password" required><br><br>
        <button type="submit" name="login">Login</button>
    </form>
    <p>No account? <a href="register.php">Register</a></p>
</body>
</html>""")

write_file('q8/register.php', """<?php
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
</html>""")

write_file('q8/logout.php', """<?php
session_start();
session_destroy();
header("Location: login.php");
exit();
?>""")

# Q9: Store Books
write_file('q9/add_book.php', """<?php
require_once '../db.php';

if (isset($_POST['add_book'])) {
    $title = $_POST['title'];
    $publisher = $_POST['publisher'];
    $author = $_POST['author'];
    $edition = $_POST['edition'];
    $pages = $_POST['no_of_page'];
    $price = $_POST['price'];
    $date = $_POST['publish_date'];
    $isbn = $_POST['isbn'];

    try {
        $stmt = $pdo->prepare("INSERT INTO books (title, publisher, author, edition, no_of_page, price, publish_date, isbn) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
        $stmt->execute([$title, $publisher, $author, $edition, $pages, $price, $date, $isbn]);
        $msg = "Book added successfully!";
    } catch(PDOException $e) {
        $msg = "Error: " . $e->getMessage();
    }
}
?>
<!DOCTYPE html>
<html>
<head><title>Add Book</title></head>
<body>
    <h2>Store Book Data</h2>
    <?php if(isset($msg)) echo "<p>$msg</p>"; ?>
    <form method="POST">
        <input type="text" name="title" placeholder="Title" required><br><br>
        <input type="text" name="publisher" placeholder="Publisher" required><br><br>
        <input type="text" name="author" placeholder="Author" required><br><br>
        <input type="text" name="edition" placeholder="Edition" required><br><br>
        <input type="number" name="no_of_page" placeholder="No. of Pages" required><br><br>
        <input type="number" step="0.01" name="price" placeholder="Price" required><br><br>
        <input type="date" name="publish_date" required><br><br>
        <input type="text" name="isbn" placeholder="ISBN" required><br><br>
        <button type="submit" name="add_book">Save Book</button>
    </form>
</body>
</html>""")
