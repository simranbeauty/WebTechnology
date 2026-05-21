<?php
require_once '../db.php';

if (isset($_POST['delete'])) {
    $id = $_POST['id'];

    $stmt = $pdo->prepare("DELETE FROM books WHERE id = ?");
    if ($stmt->execute([$id])) {
        $msg = "Book deleted successfully!";
    }
}
?>
<!DOCTYPE html>
<html>
<head><title>Delete Book</title></head>
<body>
    <h2>Delete Book</h2>
    <?php if(isset($msg)) echo "<p style='color:red;'>$msg</p>"; ?>
    <form method="POST">
        <label>Select Book to Delete:</label>
        <select name="id" required>
            <?php
            $stmt = $pdo->query("SELECT id, title FROM books");
            while ($row = $stmt->fetch()) {
                echo "<option value='{$row['id']}'>{$row['title']}</option>";
            }
            ?>
        </select><br><br>
        <button type="submit" name="delete" onclick="return confirm('Are you sure?');">Delete Book</button>
    </form>
</body>
</html>
