<!DOCTYPE html>
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
</html>
