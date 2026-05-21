# Lab Report 3 - Server-Side Scripting (PHP)

**Course**: Web Technology  
**Submitted By**: [Your Name]  
**Roll No**: [Your Roll No]  
**Date**: [Submission Date]  

---

## 1. Dynamic Content Generation using Array and Loop

### 1.1 Lab Question
Write a server-side script to demonstrate the use of dynamic content generation using array and loop for HTML list, table and card layout with suitable examples.

### 1.2 Introduction & Topic Theory
PHP allows seamless integration with HTML to dynamically generate structural content such as lists, tables, and cards. By utilizing PHP arrays (indexed, associative, or multidimensional) and loop structures (like `foreach`), web pages can be populated with varying amounts of data dynamically without hardcoding each HTML element.

### 1.3 Syntax and Format
```php
foreach ($array as $element) {
    // HTML Output mixed with $element data
}
```

### 1.4 Code
**File**: `q1/index.php`
```php
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Dynamic Content</title>
    <style>
        .card { border: 1px solid #ddd; padding: 15px; margin: 10px 0; }
        table { border-collapse: collapse; width: 100%; margin-top: 10px; }
        th, td { border: 1px solid #ddd; padding: 8px; }
    </style>
</head>
<body>
    <h2>1. HTML List</h2>
    <ul>
        <?php
        $fruits = ["Apple", "Banana", "Cherry"];
        foreach ($fruits as $fruit) { echo "<li>$fruit</li>"; }
        ?>
    </ul>

    <h2>2. HTML Table</h2>
    <table>
        <tr><th>ID</th><th>Name</th></tr>
        <?php
        $students = [["id" => 1, "name" => "Ram"], ["id" => 2, "name" => "Sita"]];
        foreach ($students as $student) {
            echo "<tr><td>{$student['id']}</td><td>{$student['name']}</td></tr>";
        }
        ?>
    </table>
</body>
</html>
```

### 1.5 Output
> [INSERT SCREENSHOT OF LIST AND TABLE HERE]
> **GitHub URL**: `https://github.com/.../lab-unit-3/q1/index.php`

---

## 2. Simple and Compound Interest Calculator

### 2.1 Lab Question
Write a server-side script to create simple web form to take input of principle, rate and interest and calculate simple and compound interest based on the button click.

### 2.2 Introduction & Topic Theory
Forms in HTML allow users to input data which can be sent to the server using `GET` or `POST` methods. PHP retrieves this data via superglobals `$_GET` or `$_POST`. Mathematical calculations like Simple Interest (P*T*R/100) and Compound Interest (P(1+R/100)^T - P) can be computed and rendered directly.

### 2.3 Syntax and Format
```php
$value = $_POST['input_name'];
$result = $value * 10;
```

### 2.4 Code
**File**: `q2/interest.php`
```php
<form method="POST">
    Principal: <input type="number" name="p"><br>
    Rate (%): <input type="number" step="0.01" name="r"><br>
    Time (Yrs): <input type="number" step="0.01" name="t"><br>
    <button name="calc">Calculate</button>
</form>

<?php
if(isset($_POST['calc'])) {
    $p = $_POST['p']; $r = $_POST['r']; $t = $_POST['t'];
    $si = ($p * $t * $r) / 100;
    $ci = $p * pow((1 + $r/100), $t) - $p;
    echo "SI: $si <br> CI: $ci";
}
?>
```

### 2.5 Output
> [INSERT SCREENSHOT OF INTEREST FORM AND RESULT]
> **GitHub URL**: `https://github.com/.../lab-unit-3/q2/interest.php`

---

## 3. Dynamic Marksheet

### 3.1 Lab Question
Write a server-side script to take user input for five subject marks from user and display those marks into marksheet.

### 3.2 Introduction & Topic Theory
An HTML form can use array inputs (e.g., `name="marks[]"`) which PHP receives as an array. `array_sum()` quickly calculates totals, which are then injected into a clean HTML table structure replicating a standardized marksheet.

### 3.3 Syntax and Format
```html
<input name="marks[]" type="number">
```
```php
$marks = $_POST['marks'];
$total = array_sum($marks);
```

### 3.4 Code
**File**: `q3/marksheet.php`
```php
<form method="POST">
    <input type="number" name="marks[]" required max="100"> <!-- repeat 5 times -->
    <button name="gen">Generate</button>
</form>
<?php
if(isset($_POST['gen'])) {
    $marks = $_POST['marks'];
    $total = array_sum($marks);
    echo "<table><tr><th>Subject</th><th>Marks</th></tr>";
    foreach($marks as $m) { echo "<tr><td>Sub</td><td>$m</td></tr>"; }
    echo "<tr><th>Total</th><th>$total</th></tr></table>";
}
?>
```

### 3.5 Output
> [INSERT SCREENSHOT OF MARKSHEET]
> **GitHub URL**: `https://github.com/.../lab-unit-3/q3/marksheet.php`

---

## 4. User Registration into Database

### 4.1 Lab Question
Develop a simple web page that asks the users input for name, email, password, phone, gender, and faculty and validate, store into database project table registrations.

### 4.2 Introduction & Topic Theory
Connecting PHP to a MySQL database using PDO (PHP Data Objects) is the secure standard. Using prepared statements prevents SQL injection. User passwords must be securely hashed before storage using `password_hash()`.

### 4.3 Syntax and Format
```php
$stmt = $pdo->prepare("INSERT INTO table (col) VALUES (?)");
$stmt->execute([$val]);
```

### 4.4 Code
**File**: `q4/register.php`
```php
<?php
$pdo = new PDO("mysql:host=127.0.0.1;dbname=webtech_lab", "root", "");
if (isset($_POST['reg'])) {
    $pass = password_hash($_POST['pwd'], PASSWORD_DEFAULT);
    $stmt = $pdo->prepare("INSERT INTO registrations (name, email, password) VALUES (?, ?, ?)");
    $stmt->execute([$_POST['name'], $_POST['email'], $pass]);
}
?>
<form method="POST">
    <input name="name"><input name="email"><input type="password" name="pwd">
    <button name="reg">Register</button>
</form>
```

### 4.5 Output
> [INSERT SCREENSHOT OF DB RECORD OR SUCCESS MSG]
> **GitHub URL**: `https://github.com/.../lab-unit-3/q4/register.php`

---

## 5. Login Process

### 5.1 Lab Question
Write a server-side script for login process assume that your data is already store from previous question.

### 5.2 Introduction & Topic Theory
Authentication verifies user credentials. The entered email is queried in the database, and `password_verify()` checks if the entered plain-text password matches the stored hash.

### 5.3 Syntax and Format
```php
if (password_verify($input_pass, $db_hash)) { // Login success }
```

### 5.4 Code
**File**: `q5/login.php`
```php
<?php
$pdo = new PDO("mysql:host=127.0.0.1;dbname=webtech_lab", "root", "");
if(isset($_POST['login'])) {
    $stmt = $pdo->prepare("SELECT * FROM registrations WHERE email = ?");
    $stmt->execute([$_POST['email']]);
    $user = $stmt->fetch();
    if($user && password_verify($_POST['pwd'], $user['password'])) {
        echo "Login Success!";
    }
}
?>
<form method="POST">
    <input name="email"><input type="password" name="pwd">
    <button name="login">Login</button>
</form>
```

### 5.5 Output
> [INSERT SCREENSHOT OF LOGIN SUCCESS]
> **GitHub URL**: `https://github.com/.../lab-unit-3/q5/login.php`

---

## 6. Session Data (Store, Retrieve, Destroy)

### 6.1 Lab Question
Write a server-side script to store, retrieve and destroy session data.

### 6.2 Introduction & Topic Theory
Sessions store user data on the server for tracking state across multiple pages. `session_start()` must be called before accessing `$_SESSION`. `session_destroy()` clears the state.

### 6.3 Syntax and Format
```php
session_start();
$_SESSION['key'] = 'value'; // Store
unset($_SESSION['key']); // Destroy
```

### 6.4 Code
**File**: `q6/session.php`
```php
<?php
session_start();
if(isset($_POST['set'])) $_SESSION['user'] = 'Admin';
if(isset($_POST['destroy'])) session_destroy();
echo isset($_SESSION['user']) ? $_SESSION['user'] : 'No session';
?>
<form method="POST">
    <button name="set">Set</button><button name="destroy">Destroy</button>
</form>
```

### 6.5 Output
> [INSERT SCREENSHOT OF SESSION UI]
> **GitHub URL**: `https://github.com/.../lab-unit-3/q6/session.php`

---

## 7. Cookies Data (Store, Retrieve, Destroy)

### 7.1 Lab Question
Write a server-side script to store, retrieve and destroy cookies data.

### 7.2 Introduction & Topic Theory
Cookies store small pieces of data on the client's browser. `setcookie()` sets them with an expiration timestamp. Setting the time in the past destroys the cookie.

### 7.3 Syntax and Format
```php
setcookie("name", "value", time() + 3600); // Store 1hr
setcookie("name", "", time() - 3600); // Destroy
```

### 7.4 Code
**File**: `q7/cookie.php`
```php
<?php
if(isset($_POST['set'])) setcookie("theme", "dark", time() + 3600);
if(isset($_POST['destroy'])) setcookie("theme", "", time() - 3600);
echo isset($_COOKIE['theme']) ? $_COOKIE['theme'] : 'No cookie';
?>
<form method="POST">
    <button name="set">Set</button><button name="destroy">Destroy</button>
</form>
```

### 7.5 Output
> [INSERT SCREENSHOT OF COOKIE UI]
> **GitHub URL**: `https://github.com/.../lab-unit-3/q7/cookie.php`

---

## 8. Complete Authentication Process

### 8.1 Lab Question
Write a server-side script for complete authentication process.

### 8.2 Introduction & Topic Theory
Complete authentication binds Registration, Login, Session Management (Dashboard), and Logout processes to restrict unauthorized access to protected pages.

### 8.3 Code
**Files**: `q8/login.php`, `q8/dashboard.php`, `q8/logout.php`
```php
// logout.php
session_start();
session_destroy();
header("Location: login.php");
```

### 8.4 Output
> [INSERT SCREENSHOT OF PROTECTED DASHBOARD]
> **GitHub URL**: `https://github.com/.../lab-unit-3/q8/`

---

## 9-12. CRUD Operations on Books

### Lab Questions
9. Store books data.
10. Retrieve books data.
11. Modify books data.
12. Remove books data.

### Introduction & Topic Theory
CRUD stands for Create, Read, Update, Delete. These represent the fundamental operations of database management. Using SQL commands (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) executed via PDO, PHP dynamically manages data tables.

### Code
**Create (Add Book)**:
```php
$stmt = $pdo->prepare("INSERT INTO books (title, price) VALUES (?, ?)");
$stmt->execute([$title, $price]);
```
**Read (List Books)**:
```php
$stmt = $pdo->query("SELECT * FROM books");
while($row = $stmt->fetch()) { echo $row['title']; }
```
**Update (Edit Price)**:
```php
$stmt = $pdo->prepare("UPDATE books SET price=? WHERE id=?");
$stmt->execute([$new_price, $id]);
```
**Delete (Remove)**:
```php
$stmt = $pdo->prepare("DELETE FROM books WHERE id=?");
$stmt->execute([$id]);
```

### Output
> [INSERT SCREENSHOTS OF ADD, VIEW, EDIT, AND DELETE OPERATIONS]
> **GitHub URL**: `https://github.com/.../lab-unit-3/q9/` to `q12/`

---

## 13. File Upload

### 13.1 Lab Question
Write a server-side script to upload file using form.

### 13.2 Introduction & Topic Theory
Forms handling files require `enctype="multipart/form-data"`. PHP handles the incoming file via the `$_FILES` superglobal and saves it using `move_uploaded_file()`.

### 13.3 Code
**File**: `q13/upload.php`
```php
<?php
if(isset($_FILES['file'])) {
    move_uploaded_file($_FILES['file']['tmp_name'], "uploads/" . $_FILES['file']['name']);
    echo "Uploaded!";
}
?>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <button>Upload</button>
</form>
```

### 13.4 Output
> [INSERT SCREENSHOT OF FILE UPLOAD SUCCESS]
> **GitHub URL**: `https://github.com/.../lab-unit-3/q13/upload.php`

---

## 14. File Read, Write, and Append

### 14.1 Lab Question
Write a server-side script to perform file read, write and append operation.

### 14.2 Introduction & Topic Theory
PHP provides `fopen()` to open files in different modes: `w` (write/overwrite), `a` (append), and `r` (read). `fwrite()` and `fread()` are then used to manipulate file contents on the server.

### 14.3 Code
**File**: `q14/file_ops.php`
```php
<?php
$f = "data.txt";
if(isset($_POST['w'])) { $fp = fopen($f, 'w'); fwrite($fp, $_POST['data']); fclose($fp); }
if(isset($_POST['a'])) { $fp = fopen($f, 'a'); fwrite($fp, $_POST['data']); fclose($fp); }
echo file_exists($f) ? fread(fopen($f, 'r'), filesize($f)) : "";
?>
<form method="POST">
    <textarea name="data"></textarea>
    <button name="w">Write</button> <button name="a">Append</button>
</form>
```

### 14.4 Output
> [INSERT SCREENSHOT OF FILE READ/WRITE]
> **GitHub URL**: `https://github.com/.../lab-unit-3/q14/file_ops.php`
