import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# q16
write_file('q16/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Dropdown Menu</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="menu-container">
        <ul class="nav">
            <li><a href="#">Home &#709;</a></li>
            <li class="dropdown">
                <a href="#" class="active">Services &#708;</a>
                <ul class="dropdown-content">
                    <li><a href="#">Design</a></li>
                    <li><a href="#" class="highlight">Development</a></li>
                    <li><a href="#">Accessibility</a></li>
                    <li><a href="#">Content Strategy</a></li>
                    <li><a href="#">Training</a></li>
                </ul>
            </li>
            <li><a href="#">Portfolio &#709;</a></li>
            <li><a href="#">About &#709;</a></li>
        </ul>
    </div>
</body>
</html>''')
write_file('q16/style.css', '''body {
    background: linear-gradient(to bottom right, #800080, #4b0082);
    height: 100vh;
    margin: 0;
    font-family: sans-serif;
    padding-top: 50px;
}
.menu-container {
    width: 80%;
    margin: 0 auto;
    background: #f4f4f4;
    border-radius: 4px;
}
.nav {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-around;
}
.nav > li {
    position: relative;
    padding: 15px 20px;
}
.nav a {
    text-decoration: none;
    color: black;
    font-weight: bold;
}
.dropdown-content {
    display: block; /* to show it open as per image */
    position: absolute;
    top: 100%;
    left: 0;
    background-color: #f4f4f4;
    min-width: 200px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    list-style: none;
    padding: 10px 0;
    margin: 0;
    border-radius: 0 0 4px 4px;
}
.dropdown-content li {
    padding: 10px 20px;
}
.dropdown-content a {
    font-weight: normal;
}
.dropdown-content a.highlight {
    font-weight: bold;
}
.dropdown-content li:nth-child(2) {
    background-color: #ffffff;
}
''')

# q17
write_file('q17/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Responsive Navigation</title>
    <link rel="stylesheet" href="style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <nav class="navbar">
        <div class="logo">Mystery Code</div>
        <button class="menu-toggle">Menu</button>
        <ul class="nav-links">
            <li><a href="#">Home</a></li>
            <li><a href="#">About Us</a></li>
            <li><a href="#">Service</a></li>
            <li><a href="#">Portfolio</a></li>
            <li><a href="#">Blog</a></li>
            <li><a href="#">Contact Us</a></li>
        </ul>
    </nav>
</body>
</html>''')
write_file('q17/style.css', '''body {
    margin: 0;
    font-family: sans-serif;
    background-color: #e0e0e0;
}
.navbar {
    background-color: #1a3b5c;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 30px;
}
.logo {
    font-size: 24px;
    font-weight: bold;
}
.nav-links {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
}
.nav-links li {
    margin-left: 20px;
}
.nav-links a {
    color: white;
    text-decoration: none;
}
.menu-toggle {
    display: none;
    background: transparent;
    border: 1px solid white;
    color: white;
    padding: 5px 10px;
    cursor: pointer;
}

@media screen and (max-width: 768px) {
    .navbar {
        flex-wrap: wrap;
        padding: 15px;
    }
    .menu-toggle {
        display: block;
    }
    .nav-links {
        flex-direction: column;
        width: 100%;
        background-color: #1a3b5c;
        margin-top: 15px;
        /* Simulated open state */
        display: flex; 
    }
    .nav-links li {
        margin: 0;
        border-bottom: 1px solid #2a4b6c;
    }
    .nav-links a {
        display: block;
        padding: 15px;
    }
}
''')

# q18
write_file('q18/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Registration Form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1 class="title">Registration Form</h1>
    <form>
        <fieldset>
            <legend>Personal Details</legend>
            
            <div class="form-group">
                <label>Name</label>
                <input type="text" placeholder="Enter Name">
            </div>
            
            <div class="form-group">
                <label>Address</label>
                <input type="text">
            </div>
            
            <div class="form-group">
                <label>Phone</label>
                <input type="text">
            </div>
            
            <div class="form-group">
                <label>Gender</label>
                <div class="radio-group">
                    <input type="radio" name="gender" id="male"> <label for="male">Male</label>
                    <input type="radio" name="gender" id="female"> <label for="female">Female</label>
                </div>
            </div>
            
            <div class="form-group">
                <label>Country</label>
                <select>
                    <option>Select Country</option>
                </select>
            </div>
            
            <div class="form-group align-top">
                <label>Message</label>
                <textarea rows="4"></textarea>
            </div>
            
            <div class="form-group">
                <label>Image</label>
                <input type="file">
            </div>
            
            <div class="checkbox-group">
                <input type="checkbox" id="terms">
                <label for="terms">I Accept Term & Condition</label>
            </div>
            
            <div class="button-group">
                <button type="submit" class="btn-register">Register</button>
                <button type="reset" class="btn-clear">Clear</button>
            </div>
        </fieldset>
    </form>
</body>
</html>''')
write_file('q18/style.css', '''body {
    font-family: serif;
    padding: 20px;
}
.title {
    color: #ff6666;
}
fieldset {
    border: 1px solid #ccc;
    padding: 20px;
    max-width: 800px;
}
legend {
    font-weight: bold;
}
.form-group {
    display: flex;
    margin-bottom: 20px;
    align-items: center;
}
.form-group.align-top {
    align-items: flex-start;
}
.form-group > label:first-child {
    width: 150px;
    font-weight: bold;
}
input[type="text"], select, textarea {
    width: 400px;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 3px;
}
.radio-group {
    display: flex;
    align-items: center;
}
.radio-group label {
    font-size: 20px;
    margin-right: 15px;
    margin-left: 5px;
}
.checkbox-group {
    margin: 20px 0;
    margin-left: 150px;
}
.button-group {
    margin-left: 150px;
}
button {
    padding: 10px 20px;
    border: none;
    color: white;
    cursor: pointer;
    font-size: 16px;
}
.btn-register {
    background-color: #0066ff;
    margin-right: 10px;
}
.btn-clear {
    background-color: #ff3333;
}
''')

# q19
write_file('q19/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Registration / Login Form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="overlay">
        <h2>REGISTRATION / LOGIN FORM</h2>
        <div class="container">
            <div class="card">
                <h3 class="card-title">Register Form :</h3>
                <form>
                    <input type="text" value="simran" class="input-field">
                    <input type="email" placeholder="Email" class="input-field icon-field">
                    <div class="hint">Please enter a valid email address</div>
                    <input type="password" value="........" class="input-field highlight">
                    <div class="hint">Minimum of 6 characters</div>
                    <input type="password" placeholder="Confirm password" class="input-field">
                    
                    <div class="radio-row">
                        <input type="radio" name="gender" id="fem" checked> <label for="fem">Female</label>
                        <input type="radio" name="gender" id="mal"> <label for="mal">Male</label>
                    </div>
                    
                    <div class="check-row">
                        <input type="checkbox" id="terms"> <label for="terms">I have read and accept terms of use.</label>
                    </div>
                    
                    <button type="submit" class="submit-btn">SUBMIT</button>
                </form>
            </div>
            
            <div class="card">
                <h3 class="card-title">Login form :</h3>
                <form>
                    <input type="text" value="simran" class="input-field icon-field">
                    <input type="password" value="........" class="input-field highlight">
                    
                    <div class="check-row">
                        <input type="checkbox" id="remember"> <label for="remember">Remember me</label>
                    </div>
                    
                    <button type="submit" class="submit-btn">LOGIN</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>''')
write_file('q19/style.css', '''body {
    margin: 0;
    font-family: sans-serif;
    background: url('../images/l1q19.png') no-repeat center center fixed; 
    background-size: cover;
    color: white;
}
.overlay {
    background-color: rgba(0,0,0,0.5);
    min-height: 100vh;
    padding: 50px;
    box-sizing: border-box;
}
h2 {
    text-align: center;
    margin-bottom: 40px;
    letter-spacing: 1px;
}
.container {
    display: flex;
    justify-content: center;
    gap: 30px;
    max-width: 1000px;
    margin: 0 auto;
}
.card {
    background-color: rgba(40,40,40,0.9);
    padding: 30px;
    border-radius: 5px;
    flex: 1;
}
.card-title {
    color: #00ffff;
    margin-top: 0;
    margin-bottom: 20px;
}
.input-field {
    width: 100%;
    padding: 15px;
    margin-bottom: 5px;
    border: none;
    background-color: #444;
    color: white;
    border-radius: 3px;
    box-sizing: border-box;
}
.input-field.highlight {
    background-color: #ffffcc;
    color: black;
}
.hint {
    font-size: 11px;
    color: #aaa;
    margin-bottom: 15px;
}
.radio-row, .check-row {
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 14px;
}
.radio-row label {
    margin-right: 15px;
}
.submit-btn {
    width: 100%;
    padding: 15px;
    background-color: #cc9900;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 3px;
    cursor: pointer;
}
''')

# q20 layout 1
write_file('q20/layout1.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Div Layout 1</title>
    <link rel="stylesheet" href="layout1.css">
</head>
<body>
    <div class="header">Header</div>
    <div class="menu">menu</div>
    <div class="main-content">
        <div class="left">Left side</div>
        <div class="content">Content</div>
        <div class="right">Right</div>
    </div>
    <div class="footer">Footer</div>
</body>
</html>''')
write_file('q20/layout1.css', '''body { margin: 0; font-family: sans-serif; display: flex; flex-direction: column; height: 100vh; }
.header { background-color: #60648c; padding: 40px; text-align: center; }
.menu { background-color: #8fa08f; padding: 10px 20px; }
.main-content { display: flex; flex: 1; }
.left { background-color: #a85d58; flex: 1; padding: 20px; }
.content { background-color: #00bfff; flex: 2; padding: 20px; }
.right { background-color: #8c73ff; flex: 1; padding: 20px; }
.footer { background-color: #8c9096; padding: 20px; }
''')

# q20 layout 2
write_file('q20/layout2.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Div Layout 2</title>
    <link rel="stylesheet" href="layout2.css">
</head>
<body>
    <div class="container">
        <div class="header">Header</div>
        <div class="middle">
            <div class="sidebar">Side Bar</div>
            <div class="main-right">
                <div class="content1">Content 1</div>
                <div class="bottom-split">
                    <div class="content2">Content 2</div>
                    <div class="content3">Content 3</div>
                </div>
            </div>
        </div>
        <div class="footer">Footer</div>
    </div>
</body>
</html>''')
write_file('q20/layout2.css', '''body { margin: 20px; font-family: sans-serif; }
.container { display: flex; flex-direction: column; gap: 20px; }
.container > div { border: 2px solid black; background-color: #33ff33; font-weight: bold; text-align: center; }
.header { padding: 30px; }
.footer { padding: 30px; }
.middle { display: flex; gap: 20px; background-color: transparent !important; border: none !important; }
.sidebar { border: 2px solid black; background-color: #33ff33; flex: 1; display: flex; align-items: center; justify-content: center; min-height: 300px; }
.main-right { flex: 4; display: flex; flex-direction: column; gap: 20px; }
.content1 { border: 2px solid black; background-color: #33ff33; padding: 50px; display: flex; align-items: center; justify-content: center; }
.bottom-split { display: flex; gap: 20px; flex: 1; }
.content2, .content3 { border: 2px solid black; background-color: #33ff33; flex: 1; padding: 50px; display: flex; align-items: center; justify-content: center; }
''')
