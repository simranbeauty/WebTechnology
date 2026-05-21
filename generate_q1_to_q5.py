import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# q1
write_file('q1/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Q1: Mockup Layouts</title>
</head>
<body>
    <h1>Design 5 page layout using any of mockup tools</h1>
    <p>This question requires a mockup tool (Figma, Balsamiq, Canva) to design the layouts. No HTML code is required here.</p>
</body>
</html>''')

# q2
write_file('q2/index.html', '''<!-- HTML 4 Structure -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <title>HTML 4 Document</title>
</head>
<body>
    <h1>This is an HTML 4 Document</h1>
</body>
</html>

<!-- HTML 5 Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML 5 Document</title>
</head>
<body>
    <h1>This is an HTML 5 Document</h1>
</body>
</html>''')

# q3
write_file('q3/index.html', '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <ul>
            <li><a href="#about">About Us</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#gallery">Gallery</a></li>
            <li><a href="#contact">Contact Us</a></li>
        </ul>
    </nav>
    <section id="about">
        <h2>About Us</h2>
        <p>Welcome to our company. We provide top-notch services to our clients worldwide.</p>
    </section>
    <section id="services">
        <h2>Services</h2>
        <ul>
            <li>Web Development</li>
            <li>Graphic Design</li>
            <li>Digital Marketing</li>
        </ul>
    </section>
    <section id="gallery">
        <h2>Gallery</h2>
        <img src="https://via.placeholder.com/150" alt="Gallery Image 1">
        <img src="https://via.placeholder.com/150" alt="Gallery Image 2">
    </section>
    <section id="contact">
        <h2>Contact Us</h2>
        <form>
            <label>Name: <input type="text" name="name"></label><br>
            <label>Email: <input type="email" name="email"></label><br>
            <button type="submit">Submit</button>
        </form>
    </section>
</body>
</html>''')
write_file('q3/style.css', '''body { font-family: sans-serif; margin: 0; padding: 0; }
nav { background-color: #333; }
nav ul { list-style: none; padding: 0; margin: 0; display: flex; }
nav ul li a { color: white; padding: 15px 20px; text-decoration: none; display: block; }
nav ul li a:hover { background-color: #555; }
section { padding: 20px; min-height: 50vh; }
#about { background-color: #f9f9f9; }
#services { background-color: #e9e9e9; }
#gallery { background-color: #f9f9f9; }
#contact { background-color: #e9e9e9; }''')

# q4
write_file('q4/index.html', '''<!DOCTYPE html>
<html>
<head><title>Lists</title></head>
<body>
    <h2>Ordered List</h2>
    <ol>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ol>
    <h2>Unordered List</h2>
    <ul>
        <li>Item A</li>
        <li>Item B</li>
        <li>Item C</li>
    </ul>
</body>
</html>''')

# q5
write_file('q5/index.html', '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nested Lists</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div class="left">
            <h2>Nested Unordered List</h2>
            <p>GeeksforGeeks courses list:</p>
            <ul>
                <li>DSA
                    <ul style="list-style-type: circle;">
                        <li>Array</li>
                        <li>Linked List</li>
                        <li>Stack</li>
                        <li>Queue</li>
                    </ul>
                </li>
                <li>Web Technologies
                    <ul style="list-style-type: circle;">
                        <li>HTML</li>
                        <li>CSS</li>
                        <li>JavaScript</li>
                    </ul>
                </li>
                <li>Aptitude</li>
                <li>Gate</li>
                <li>Placement</li>
            </ul>
        </div>
        <div class="right">
            <h2>Learning Web Development</h2>
            <ol type="I">
                <li>Background Skills
                    <ol type="A">
                        <li>Unix Commands</li>
                        <li>Vim Text Editor</li>
                    </ol>
                </li>
                <li>HTML
                    <ol type="A">
                        <li>Minimal Page</li>
                        <li>Headings</li>
                        <li>Tags</li>
                        <li>Lists
                            <ol type="i">
                                <li>Unordered</li>
                                <li>Ordered</li>
                                <li>Definition</li>
                                <li>Nested</li>
                            </ol>
                        </li>
                        <li>Links
                            <ol type="i">
                                <li>Absolute</li>
                                <li>Relative</li>
                            </ol>
                        </li>
                        <li>Images</li>
                    </ol>
                </li>
                <li>CSS
                    <ol type="A">
                        <li>Anatomy</li>
                        <li>Basic Selectors
                            <ol type="i">
                                <li>Element</li>
                                <li>Class</li>
                                <li>ID</li>
                                <li>Group</li>
                            </ol>
                        </li>
                        <li>The DOM</li>
                        <li>Advanced Selectors</li>
                        <li>Box Model</li>
                    </ol>
                </li>
                <li>Programming
                    <ol type="A">
                        <li>Python</li>
                        <li>JavaScript</li>
                    </ol>
                </li>
                <li>Database</li>
            </ol>
        </div>
    </div>
</body>
</html>''')
write_file('q5/style.css', '''body { font-family: "Times New Roman", Times, serif; }
.container { display: flex; border: 1px solid black; }
.left, .right { padding: 20px; width: 50%; box-sizing: border-box; }
.left { border-right: 1px solid black; }
h2 { font-family: serif; }''')
