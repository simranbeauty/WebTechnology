<?php
require_once '../db.php';

if (isset($_POST['update'])) {
    $id = $_POST['id'];
    $price = $_POST['price'];

    $stmt = $pdo->prepare("UPDATE books SET price = ? WHERE id = ?");
    if ($stmt->execute([$price, $id])) {
        $msg = "Book price updated successfully!";
    }
}
?>
<!DOCTYPE html>
<html>
<head><title>Modify Book</title></head>
<body>
    <h2>Update Book Price</h2>
    <?php if(isset($msg)) echo "<p style='color:green;'>$msg</p>"; ?>
    <form method="POST">
        <label>Select Book to Update:</label>
        <select name="id" required>
            <?php
            $stmt = $pdo->query("SELECT id, title, price FROM books");
            while ($row = $stmt->fetch()) {
                echo "<option value='{$row['id']}'>{$row['title']} (Current: {$row['price']})</option>";
            }
            ?>
        </select><br><br>
        <input type="number" step="0.01" name="price" placeholder="New Price" required><br><br>
        <button type="submit" name="update">Update Price</button>
    </form>
</body>
</html>
