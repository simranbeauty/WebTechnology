<?php
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
</html>
