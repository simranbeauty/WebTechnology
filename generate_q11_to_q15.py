import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# q11
write_file('q11/index.html', '''<!DOCTYPE html>
<html>
<head><title>Frameset Example</title></head>
<!-- Note: Frameset is not supported in HTML5, using older doctype or just basic frameset -->
<frameset rows="20%, 80%">
    <frame src="header.html" name="header">
    <frameset cols="25%, 75%">
        <frame src="menu.html" name="menu">
        <frame src="main.html" name="main">
    </frameset>
</frameset>
</html>''')
write_file('q11/header.html', '<!DOCTYPE html><html><body style="background-color: lightblue;"><h2>Header Frame</h2></body></html>')
write_file('q11/menu.html', '<!DOCTYPE html><html><body style="background-color: lightgreen;"><h2>Menu Frame</h2></body></html>')
write_file('q11/main.html', '<!DOCTYPE html><html><body style="background-color: lightyellow;"><h2>Main Content Frame</h2></body></html>')

# q12
write_file('q12/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Types of CSS</title>
    <!-- External CSS -->
    <link rel="stylesheet" href="style.css">
    
    <!-- Internal CSS -->
    <style>
        .internal-style {
            color: green;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <h2>CSS Types Demonstration</h2>
    
    <!-- Inline CSS -->
    <p style="color: blue; font-weight: bold;">This is Inline CSS.</p>
    
    <p class="internal-style">This is Internal CSS.</p>
    
    <p class="external-style">This is External CSS.</p>
</body>
</html>''')
write_file('q12/style.css', '''.external-style {
    color: red;
    text-decoration: underline;
}''')

# q13
write_file('q13/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Photo Gallery</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h2 style="text-align: center;">Photo Gallery</h2>
    <div class="gallery">
        <div class="gallery-item">
            <img src="https://via.placeholder.com/300x200" alt="Forest Trees">
            <div class="desc">Forest Trees</div>
        </div>
        <div class="gallery-item">
            <img src="https://via.placeholder.com/300x200" alt="Ocean Waves">
            <div class="desc">Ocean Waves</div>
        </div>
        <div class="gallery-item">
            <img src="https://via.placeholder.com/300x200" alt="Mountain Peak">
            <div class="desc">Mountain Peak</div>
        </div>
        <div class="gallery-item">
            <img src="https://via.placeholder.com/300x200" alt="Laptop & Coffee">
            <div class="desc">Laptop & Coffee</div>
        </div>
        <div class="gallery-item">
            <img src="https://via.placeholder.com/300x200" alt="Desert Dunes">
            <div class="desc">Desert Dunes</div>
        </div>
        <div class="gallery-item">
            <img src="https://via.placeholder.com/300x200" alt="City Street">
            <div class="desc">City Street</div>
        </div>
    </div>
</body>
</html>''')
write_file('q13/style.css', '''body { font-family: serif; }
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    padding: 20px;
}
.gallery-item {
    width: 300px;
    border: 1px solid #ccc;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
}
.gallery-item img {
    width: 100%;
    height: auto;
    display: block;
}
.desc {
    padding: 15px;
    text-align: left;
    background: white;
}''')

# q14
write_file('q14/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Simran Thapa CV</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="cv-container">
        <h1>Simran Thapa</h1>
        <p class="contact-info">Kathmandu, Nepal | +977-98XXXXXXXX | simranthapa@email.com</p>
        <p class="links"><a href="#">LinkedIn Profile</a> | <a href="#">GitHub Profile</a></p>
        
        <hr>
        
        <h2>Professional Summary</h2>
        <p>A motivated and detail-oriented computer science student with foundational skills in web development, database management, and software design. Eager to contribute to a dynamic team through an entry-level position or internship.</p>
        
        <hr>
        
        <h2>Education</h2>
        <ul>
            <li><strong>BCA</strong><br>Tribhuvan University &mdash; 2024 - Present</li>
            <li><strong>+2 Science</strong><br>ABC Higher Secondary School &mdash; 2021 - 2023</li>
        </ul>
        
        <hr>
        
        <h2>Technical Skills</h2>
        <ul>
            <li><strong>Languages:</strong> HTML, CSS, JavaScript, C, Java</li>
            <li><strong>Databases:</strong> MySQL</li>
            <li><strong>Tools & Frameworks:</strong> Git, VS Code</li>
        </ul>
        
        <hr>
        
        <h2>Academic Projects</h2>
        <ul>
            <li><strong>E-Commerce Web Application</strong><br>Developed a fully responsive frontend bookstore website using HTML and CSS. Features include a product catalog, functional navigation link mapping, and a styled contact form.</li>
        </ul>
        
        <hr>
        
        <h2>References</h2>
        <p>Available upon request.</p>
    </div>
</body>
</html>''')
write_file('q14/style.css', '''body { font-family: "Times New Roman", Times, serif; background-color: white; color: black; line-height: 1.6; }
.cv-container { max-width: 800px; margin: 0 auto; padding: 20px; }
h1 { font-size: 32px; margin-bottom: 5px; }
.contact-info { margin: 0; }
.links a { color: blue; text-decoration: underline; }
hr { border: 0; border-top: 1px solid black; margin: 20px 0; }
h2 { font-size: 20px; margin-top: 0; margin-bottom: 15px; }
ul { list-style-type: disc; padding-left: 20px; margin-bottom: 0; }
li { margin-bottom: 10px; }''')

# q15
write_file('q15/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Menu/Navbar</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav class="navbar">
        <a href="#" class="active">Home</a> | 
        <a href="#">About</a> | 
        <a href="#">Services</a> | 
        <a href="#">Gallery</a> | 
        <a href="#">Contact</a>
    </nav>
</body>
</html>''')
write_file('q15/style.css', '''body { font-family: serif; margin: 0; padding: 20px; }
.navbar {
    background-color: #ffff66;
    padding: 10px 20px;
    font-size: 20px;
    color: #6633cc;
    display: inline-block;
    width: 100%;
    box-sizing: border-box;
}
.navbar a {
    text-decoration: none;
    color: #6633cc;
    padding: 5px 15px;
}
.navbar a.active {
    background-color: #6633cc;
    color: white;
}''')
