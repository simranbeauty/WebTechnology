<!DOCTYPE html>
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
</html>
