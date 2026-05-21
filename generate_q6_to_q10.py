import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# q6
write_file('q6/index.html', '''<!DOCTYPE html>
<html>
<head><title>Text Formatting</title></head>
<body>
    <p><b>Bold text (b)</b> and <strong>Strong text (strong)</strong></p>
    <p><i>Italic text (i)</i> and <em>Emphasized text (em)</em></p>
    <p>Short quote: <q>This is a short quote (q)</q></p>
    <blockquote>This is a blockquote, used for longer quotations.</blockquote>
    <p>Price: <del>$50</del> <ins>$40</ins> (del & ins)</p>
    <p><font color="blue">This is colored text (font)</font></p>
    <pre>Preformatted text (pre)
preserves spaces
and line breaks.</pre>
    <p><code>console.log('Hello'); (code)</code></p>
    <p><tt>Teletype text (tt)</tt></p>
    <p>HTML Entities: &lt; (less than), &gt; (greater than), &amp; (ampersand)</p>
    <p>Water is H<sub>2</sub>O (sub) and Area is &pi;r<sup>2</sup> (sup)</p>
</body>
</html>''')

# q7
write_file('q7/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Tribhuvan University</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h2>Tribhuvan University (TU)</h2>
    <ul>
        <li><strong>Faculty of Management</strong>
            <ul style="list-style-type: circle;">
                <li>BBA (Bachelor of Business Administration)</li>
                <li>BBS (Bachelor of Business Studies)</li>
                <li>MBS (Master of Business Studies)</li>
            </ul>
        </li>
        <li><strong>Institute of Science and Technology</strong>
            <ul style="list-style-type: circle;">
                <li>B.Sc. CSIT (Computer Science & IT)</li>
                <li>B.Sc. (General Science)</li>
                <li>M.Sc. Physics</li>
            </ul>
        </li>
        <li><strong>Faculty of Humanities and Social Sciences</strong>
            <ul style="list-style-type: circle;">
                <li>BA (Bachelor of Arts)</li>
                <li>BCA (Bachelor of Computer Application)</li>
                <li>MA (Master of Arts)</li>
            </ul>
        </li>
    </ul>
</body>
</html>''')
write_file('q7/style.css', '''body { font-family: "Times New Roman", Times, serif; }
h2 { font-family: serif; }''')

# q8
write_file('q8/index.html', '''<!DOCTYPE html>
<html>
<head><title>Interactive Image Map Example</title></head>
<body>
    <h2>Interactive Image Map Example</h2>
    <p>Hover and click on different shapes in the image below to visit different pages.</p>
    <img src="../images/l1q8.png" usemap="#workmap" alt="Colorful Gradient">
    <map name="workmap">
        <area shape="rect" coords="0,0,200,200" alt="Rectangle" href="#">
        <area shape="circle" coords="300,150,50" alt="Circle" href="#">
        <area shape="poly" coords="400,300,500,200,600,300" alt="Polygon" href="#">
    </map>
</body>
</html>''')

# q9
write_file('q9/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Class Routine</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h2 style="text-align: center;">Weekly Class Routine</h2>
    <table>
        <thead>
            <tr>
                <th>Day / Time</th>
                <th>10:00 AM - 11:30 AM</th>
                <th>11:30 AM - 01:00 PM</th>
                <th>01:00 PM - 01:30 PM</th>
                <th>01:30 PM - 03:00 PM</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>Monday</th>
                <td>Web Technology</td>
                <td>Database Systems</td>
                <td rowspan="3" class="break">B<br>R<br>E<br>A<br>K</td>
                <td>Mathematics</td>
            </tr>
            <tr>
                <th>Tuesday</th>
                <td>Java Programming</td>
                <td>Web Technology</td>
                <td>Operating Systems</td>
            </tr>
            <tr>
                <th>Wednesday</th>
                <td>Database Systems</td>
                <td>Java Programming</td>
                <td>Mathematics</td>
            </tr>
            <tr>
                <th>Thursday</th>
                <td colspan="2">Project Lab Work</td>
                <td class="break" style="font-weight: bold;">BREAK</td>
                <td>Operating Systems</td>
            </tr>
        </tbody>
    </table>
</body>
</html>''')
write_file('q9/style.css', '''table { width: 100%; border-collapse: collapse; text-align: center; font-family: serif; }
th, td { border: 1px solid #333; padding: 15px; }
th { background-color: #003366; color: white; }
tbody th { background-color: #f2f2f2; color: black; }
.break { background-color: #ffcccc; font-weight: bold; }''')

# q10
write_file('q10/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Time Table</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <table>
        <tr>
            <th colspan="6" class="title">Time Table</th>
        </tr>
        <tr>
            <th rowspan="6">Hours</th>
            <th>Mon</th>
            <th>Tue</th>
            <th>Wed</th>
            <th>Thu</th>
            <th>Fri</th>
        </tr>
        <tr>
            <td>Math</td>
            <td>Science</td>
            <td>Math</td>
            <td>Science</td>
            <td>Arts</td>
        </tr>
        <tr>
            <td>Math</td>
            <td>Science</td>
            <td>Math</td>
            <td>Science</td>
            <td>Arts</td>
        </tr>
        <tr>
            <th colspan="5">Lunch</th>
        </tr>
        <tr>
            <td>Math</td>
            <td>Science</td>
            <td>Math</td>
            <td colspan="2" rowspan="2" class="project">Project</td>
        </tr>
        <tr>
            <td>Math</td>
            <td>Science</td>
            <td>Math</td>
        </tr>
    </table>
</body>
</html>''')
write_file('q10/style.css', '''table { border-collapse: collapse; margin: 20px auto; font-family: serif; border: 2px solid grey; }
th, td { border: 1px solid grey; padding: 10px; text-align: center; }
.title { font-size: 24px; font-weight: bold; padding: 20px; }
.project { font-weight: bold; }''')
