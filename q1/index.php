<!DOCTYPE html>
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
</html>
