import os

def write_file(path, content):
    if os.path.dirname(path): os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

# Q10: Retrieve Books
write_file('q10/list_books.php', """<?php require_once '../db.php'; ?>
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
</html>""")

# Q11: Modify Books
write_file('q11/edit_book.php', """<?php
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
</html>""")

# Q12: Delete Books
write_file('q12/delete_book.php', """<?php
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
</html>""")

# Q13: File Upload
write_file('q13/upload.php', """<?php
if (isset($_POST['upload'])) {
    $target_dir = "uploads/";
    if (!is_dir($target_dir)) {
        mkdir($target_dir, 0777, true);
    }
    
    $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
    
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        $msg = "The file ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " has been uploaded.";
    } else {
        $msg = "Sorry, there was an error uploading your file.";
    }
}
?>
<!DOCTYPE html>
<html>
<head><title>File Upload</title></head>
<body>
    <h2>Upload a File</h2>
    <?php if(isset($msg)) echo "<p>$msg</p>"; ?>
    <form method="POST" enctype="multipart/form-data">
        Select image to upload:
        <input type="file" name="fileToUpload" required><br><br>
        <button type="submit" name="upload">Upload File</button>
    </form>
</body>
</html>""")

# Q14: File Operations
write_file('q14/file_ops.php', """<?php
$filename = "data.txt";
$msg = "";

if (isset($_POST['write'])) {
    $file = fopen($filename, "w") or die("Unable to open file!");
    fwrite($file, $_POST['content'] . "\\n");
    fclose($file);
    $msg = "File written successfully.";
}

if (isset($_POST['append'])) {
    $file = fopen($filename, "a") or die("Unable to open file!");
    fwrite($file, $_POST['content'] . "\\n");
    fclose($file);
    $msg = "Content appended successfully.";
}

$file_contents = "";
if (file_exists($filename)) {
    $file = fopen($filename, "r");
    if (filesize($filename) > 0) {
        $file_contents = fread($file, filesize($filename));
    }
    fclose($file);
}
?>
<!DOCTYPE html>
<html>
<head><title>File Operations</title></head>
<body>
    <h2>Read, Write, and Append</h2>
    <?php if($msg) echo "<p style='color:green;'>$msg</p>"; ?>
    
    <form method="POST">
        <textarea name="content" rows="4" cols="50" required placeholder="Enter text here..."></textarea><br><br>
        <button type="submit" name="write">Write (Overwrite)</button>
        <button type="submit" name="append">Append</button>
    </form>

    <h3>Current File Contents (Read Operation):</h3>
    <pre style="background:#eee; padding:10px; width:400px;"><?php echo htmlspecialchars($file_contents); ?></pre>
</body>
</html>""")
