<?php require_once '../db.php'; ?>
<!DOCTYPE html>
<html>
<head>
    <title>Retrieve Books</title>
    <style>table, th, td { border: 1px solid black; border-collapse: collapse; padding: 8px; }</style>
</head>
<body>
    <h2>Books List</h2>
    <table>
        <tr>
            <th>ID</th><th>Title</th><th>Author</th><th>Publisher</th><th>Price</th><th>ISBN</th>
        </tr>
        <?php
        $stmt = $pdo->query("SELECT * FROM books");
        while ($row = $stmt->fetch()) {
            echo "<tr>
                <td>{$row['id']}</td>
                <td>{$row['title']}</td>
                <td>{$row['author']}</td>
                <td>{$row['publisher']}</td>
                <td>{$row['price']}</td>
                <td>{$row['isbn']}</td>
            </tr>";
        }
        ?>
    </table>
</body>
</html>
