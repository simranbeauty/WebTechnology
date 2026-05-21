import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# q21
write_file('q21/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Lok Sewa Aayog Registration</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="card">
        <h2 class="title">LOK SEWA AAYOG REGISTRATION</h2>
        
        <form>
            <div class="form-group">
                <label>Full Name (In Block Letters)</label>
                <input type="text" value="simran">
            </div>
            
            <div class="form-group">
                <label>Email Address</label>
                <input type="email" value="example@domain.com">
            </div>
            
            <div class="form-group">
                <label>Citizenship Number</label>
                <input type="text" placeholder="e.g., 27-01-72-XXXXX">
            </div>
            
            <div class="form-group">
                <label>Applied Post</label>
                <select>
                    <option>-- Select Post --</option>
                </select>
            </div>
            
            <div class="form-group">
                <label>Gender</label>
                <div class="radio-group">
                    <input type="radio" name="gender" id="male" checked> <label for="male">Male</label>
                    <input type="radio" name="gender" id="female"> <label for="female">Female</label>
                    <input type="radio" name="gender" id="others"> <label for="others">Others</label>
                </div>
            </div>
            
            <button type="submit" class="submit-btn">Register User</button>
        </form>
    </div>
</body>
</html>''')
write_file('q21/style.css', '''body {
    background-color: #f4f6f8;
    font-family: sans-serif;
    display: flex;
    justify-content: center;
    padding: 50px;
    margin: 0;
}
.card {
    background-color: white;
    width: 600px;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    border-top: 5px solid #0056b3;
}
.title {
    text-align: center;
    color: #0056b3;
    margin-top: 0;
    margin-bottom: 30px;
}
.form-group {
    margin-bottom: 20px;
}
label {
    display: block;
    font-weight: bold;
    margin-bottom: 8px;
    color: #333;
}
input[type="text"], input[type="email"], select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    font-size: 16px;
    color: #555;
}
select {
    background-color: #eee;
}
.radio-group {
    display: flex;
    gap: 20px;
    align-items: center;
}
.radio-group label {
    margin-bottom: 0;
    font-weight: bold;
}
.submit-btn {
    width: 100%;
    padding: 15px;
    background-color: #0056b3;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    margin-top: 10px;
}
''')

# q22
write_file('q22/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Mobile First Layout</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div class="header">Header</div>
        <div class="main">Main</div>
        <div class="left">Left</div>
        <div class="right">Right</div>
        <div class="footer">Footer</div>
    </div>
</body>
</html>''')
write_file('q22/style.css', '''body { margin: 20px; font-family: sans-serif; display: flex; justify-content: center; }
.container { width: 100%; max-width: 400px; display: flex; flex-direction: column; gap: 10px; }
.container > div {
    padding: 20px;
    text-align: center;
    font-weight: bold;
    border-radius: 5px;
}
.header { background-color: #f06a6a; color: #333; }
.main { background-color: white; border: 1px solid #ccc; height: 100px; display: flex; align-items: center; justify-content: center; }
.left { background-color: #e6c55c; }
.right { background-color: #a4e673; }
.footer { background-color: #6bb9ed; }
''')

# q23
write_file('q23/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Grade Sheet</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="grade-sheet">
        <div class="header">
            <h1>TRIBHUVAN UNIVERSITY</h1>
            <p>Institute of Science and Technology</p>
            <h2 class="subtitle"><u>GRADE SHEET</u></h2>
        </div>
        
        <div class="student-info">
            <div class="info-left">
                <p><strong>Name of Student:</strong> Simran Thapa</p>
                <p><strong>Roll No:</strong> 2045/081</p>
                <p><strong>Exam Roll No:</strong> 280451</p>
            </div>
            <div class="info-right">
                <p><strong>Semester:</strong> 2nd Semester</p>
                <p><strong>Year:</strong> 2026</p>
                <p><strong>Course:</strong> B.Sc. CSIT</p>
            </div>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th>COURSE CODE</th>
                    <th>COURSE TITLE</th>
                    <th>CREDIT<br>HOURS</th>
                    <th>GRADE<br>OBTAINED</th>
                    <th>GRADE POINT</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>CSC160</td><td>Discrete Structure</td><td>3</td><td>A</td><td>4.0</td></tr>
                <tr><td>CSC161</td><td>Object Oriented Programming</td><td>3</td><td>A-</td><td>3.7</td></tr>
                <tr><td>MTH163</td><td>Mathematics II</td><td>3</td><td>B+</td><td>3.3</td></tr>
                <tr><td>PHY164</td><td>Physics</td><td>3</td><td>A</td><td>4.0</td></tr>
                <tr><td>CSC165</td><td>Digital Logic</td><td>3</td><td>A-</td><td>3.7</td></tr>
            </tbody>
        </table>
        
        <div class="footer">
            <span><strong>Total Credits: 15</strong></span>
            <span><strong>SGPA: 3.74</strong></span>
            <span><strong>Result: PASS</strong></span>
        </div>
    </div>
</body>
</html>''')
write_file('q23/style.css', '''body { font-family: "Segoe UI", sans-serif; background-color: #f0f4f4; padding: 20px; display: flex; justify-content: center; }
.grade-sheet { background-color: white; border: 2px solid #2b455b; border-radius: 5px; width: 900px; padding: 40px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
.header { text-align: center; color: #2b455b; margin-bottom: 30px; }
.header h1 { margin: 0; font-size: 24px; letter-spacing: 1px; }
.header p { margin: 5px 0; color: #7f8c8d; }
.subtitle { margin-top: 15px; font-size: 18px; }
.student-info { display: flex; justify-content: space-between; background-color: #f8f9fa; padding: 20px; border-left: 5px solid #2b455b; margin-bottom: 20px; color: #2c3e50; }
.student-info p { margin: 5px 0; }
.info-right { text-align: right; }
table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
th, td { border: 1px solid #ddd; padding: 12px; text-align: center; }
td:nth-child(2) { text-align: left; }
th { background-color: #34495e; color: white; font-weight: bold; font-size: 14px; }
td { color: #555; }
.footer { background-color: #34495e; color: white; padding: 15px 20px; display: flex; justify-content: flex-end; gap: 40px; border-radius: 3px; font-size: 16px; }
''')

# q24
write_file('q24/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Image Card</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="card">
        <img src="https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=400&q=80" alt="Tree">
        <div class="card-content">
            <h2>Card Title</h2>
            <p>This is a sample card description</p>
            <a href="#" class="btn">Read More</a>
        </div>
    </div>
</body>
</html>''')
write_file('q24/style.css', '''body { background-color: #6d8e9e; display: flex; justify-content: center; padding: 50px; font-family: sans-serif; margin: 0; }
.card {
    width: 300px;
    height: 400px;
    border-radius: 10px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
.card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.card-content {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 20px;
    background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
    color: white;
}
.card-content h2 {
    margin: 0 0 10px 0;
    font-size: 24px;
}
.card-content p {
    margin: 0 0 20px 0;
    font-size: 14px;
}
.btn {
    display: inline-block;
    background-color: white;
    color: black;
    text-decoration: none;
    padding: 8px 20px;
    border-radius: 20px;
    font-weight: bold;
    font-size: 14px;
}
''')

# q25
write_file('q25/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Team Members</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div class="header">
            <span class="subtitle">Experts</span>
            <h2>Our Team Members</h2>
        </div>
        <div class="team-grid">
            <div class="member-card">
                <img src="https://via.placeholder.com/120/8b5cf6/ffffff?text=Noman" alt="Noman">
                <h3>Noman</h3>
                <p>Programmer</p>
                <div class="socials">
                    <span>FB</span> <span>YT</span> <span>IG</span>
                </div>
            </div>
            <div class="member-card">
                <img src="https://via.placeholder.com/120/4b5563/ffffff?text=Aasim" alt="Aasim">
                <h3>Aasim</h3>
                <p>CEO</p>
                <div class="socials">
                    <span>FB</span> <span>YT</span> <span>IG</span>
                </div>
            </div>
            <div class="member-card">
                <img src="https://via.placeholder.com/120/1e293b/ffffff?text=Jhanzaib" alt="Jhanzaib">
                <h3>Jhanzaib</h3>
                <p>WordPress</p>
                <div class="socials">
                    <span>FB</span> <span>YT</span> <span>IG</span>
                </div>
            </div>
            <div class="member-card">
                <div class="placeholder-img">Faheem</div>
                <h3>Faheem</h3>
                <p>Youtuber</p>
                <div class="socials">
                    <span>FB</span> <span>YT</span> <span>IG</span>
                </div>
            </div>
        </div>
    </div>
</body>
</html>''')
write_file('q25/style.css', '''body { background-color: #ececec; font-family: sans-serif; margin: 0; padding: 40px; }
.container { max-width: 1000px; margin: 0 auto; }
.header { text-align: center; margin-bottom: 40px; }
.subtitle { color: #888; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
h2 { font-size: 32px; margin: 10px 0; }
.team-grid { display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; }
.member-card { background-color: white; border-radius: 10px; padding: 30px 20px; text-align: center; width: 200px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
.member-card img { width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin-bottom: 20px; }
.placeholder-img { width: 120px; height: 120px; margin: 0 auto 20px auto; display: flex; align-items: center; justify-content: center; color: transparent; } /* Hidden text, transparent bg */
.member-card h3 { margin: 0 0 5px 0; font-size: 18px; }
.member-card p { margin: 0 0 20px 0; color: #888; font-size: 14px; }
.socials { background-color: #f4f4f4; border-radius: 20px; padding: 8px 15px; display: inline-flex; gap: 15px; }
.socials span { font-size: 12px; font-weight: bold; color: #555; }
''')

# q26
write_file('q26/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Polaroid Gallery</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="gallery">
        <div class="polaroid">
            <img src="https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=300" alt="Dog">
            <p>Julie's Rabbit Ears</p>
        </div>
        <div class="polaroid">
            <img src="https://images.unsplash.com/photo-1552053831-71594a27632d?w=300" alt="Dog">
            <p>The Innocent Look</p>
        </div>
        <div class="polaroid">
            <img src="https://images.unsplash.com/photo-1517849845537-4d257902454a?w=300" alt="Dog">
            <p>Big Eyed Buggy</p>
        </div>
        <div class="polaroid">
            <div class="img-placeholder">Labrador</div>
            <p>The Saint Doggo</p>
        </div>
        
        <div class="polaroid">
            <img src="https://images.unsplash.com/photo-1517849845537-4d257902454a?w=300" alt="Dog">
            <p>Big Eyed Buggy</p>
        </div>
        <div class="polaroid">
            <img src="https://images.unsplash.com/photo-1552053831-71594a27632d?w=300" alt="Dog">
            <p>The Innocent Look</p>
        </div>
        <div class="polaroid">
            <div class="img-placeholder">Labrador</div>
            <p>The Saint Doggo</p>
        </div>
        <div class="polaroid">
            <img src="https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=300" alt="Dog">
            <p>Julie's Rabbit Ears</p>
        </div>
    </div>
</body>
</html>''')
write_file('q26/style.css', '''body { background-color: #e5e5e5; padding: 40px; font-family: monospace; display: flex; justify-content: center; }
.gallery { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; max-width: 1200px; }
.polaroid { background-color: white; padding: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 1px solid #ccc; }
.polaroid img { width: 100%; aspect-ratio: 1/1; object-fit: cover; display: block; }
.img-placeholder { width: 100%; aspect-ratio: 1/1; border: 1px solid #eee; padding: 10px; box-sizing: border-box; }
.polaroid p { text-align: center; margin: 15px 0 0 0; font-size: 16px; }
''')

# q27
write_file('q27/index.html', '''<!DOCTYPE html>
<html>
<head>
    <title>Invoice</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="invoice">
        <div class="header">
            <div class="company-info">
                <div class="logo">LOGO</div>
                <div class="details">
                    <h2>Apex Tech Solutions Inc.</h2>
                    <p>450 Innovation Way, Suite 200<br>San Francisco, CA 94107 | contact@apextech.com</p>
                </div>
            </div>
            <div class="invoice-details">
                <h1>INVOICE</h1>
                <p><strong>DATE</strong><br>May 21, 2026</p>
                <p><strong>INVOICE NO.</strong><br>INV-2026-8941</p>
            </div>
        </div>
        
        <div class="payment-terms">
            <p><em>Payment terms: Due on receipt (Net 15 days)</em></p>
        </div>
        
        <div class="addresses">
            <div class="bill-to">
                <h3>BILL TO</h3>
                <p>Jane Rowen<br>Acme Global Corporation<br>123 Business Rd, Building A<br>+1 (555) 019-2834<br>j.rowen@acmeglobal.com</p>
            </div>
            <div class="ship-to">
                <h3>SHIP TO</h3>
                <p>Receiving Dept / Dock 4<br>Acme Global Corporation<br>888 Logistics Blvd<br>+1 (555) 019-2839</p>
            </div>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th>DESCRIPTION</th>
                    <th>QTY</th>
                    <th>UNIT PRICE</th>
                    <th>TOTAL</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>Enterprise Software License Tier-1 (Annual)</td><td>2</td><td>1,200.00</td><td>2,400.00</td></tr>
                <tr><td>Cloud Database Storage Allocation Add-on (500GB)</td><td>5</td><td>150.00</td><td>750.00</td></tr>
                <tr><td>Premium Technical Onboarding & Integration Support</td><td>1</td><td>850.00</td><td>850.00</td></tr>
                <tr><td>Hardware Terminal Interfaces (Model v4)</td><td>4</td><td>250.00</td><td>1,000.00</td></tr>
                <tr><td>&nbsp;</td><td></td><td></td><td></td></tr>
                <tr><td>&nbsp;</td><td></td><td></td><td></td></tr>
                <tr><td>&nbsp;</td><td></td><td></td><td></td></tr>
                <tr><td>&nbsp;</td><td></td><td></td><td></td></tr>
                <tr><td>&nbsp;</td><td></td><td></td><td></td></tr>
                <tr><td>&nbsp;</td><td></td><td></td><td></td></tr>
                <tr><td>&nbsp;</td><td></td><td></td><td></td></tr>
            </tbody>
        </table>
        
        <div class="footer">
            <div class="remarks">
                <strong>Remarks / Payment Instructions:</strong>
                <p>Please include Invoice Number <strong>INV-2026-8941</strong> on all wire transfer documents.<br>Bank routing information is listed in your vendor onboarding portal.</p>
            </div>
            <div class="totals">
                <div class="row"><span><strong>SUBTOTAL</strong></span><span>5,000.00</span></div>
                <div class="row"><span><strong>DISCOUNT (10%)</strong></span><span>500.00</span></div>
                <div class="row final"><span><strong>SUBTOTAL LESS DISCOUNT</strong></span><span><strong>4,500.00</strong></span></div>
            </div>
        </div>
    </div>
</body>
</html>''')
write_file('q27/style.css', '''body { font-family: sans-serif; background-color: #f4f4f4; padding: 40px; display: flex; justify-content: center; }
.invoice { background-color: white; width: 850px; padding: 50px; box-shadow: 0 0 10px rgba(0,0,0,0.1); border-top: 10px solid #e25822; }
.header { display: flex; justify-content: space-between; border-bottom: 1px solid #eee; padding-bottom: 20px; background-color: #f9f9f9; padding: 20px; margin: -50px -50px 20px -50px; border-top-left-radius: 4px; border-top-right-radius: 4px; }
.company-info { display: flex; align-items: center; gap: 20px; }
.logo { width: 80px; height: 80px; background-color: #555; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; }
.details h2 { margin: 0 0 5px 0; color: #333; }
.details p { margin: 0; color: #666; font-size: 14px; line-height: 1.5; }
.invoice-details { text-align: right; }
.invoice-details h1 { margin: 0; color: #888; letter-spacing: 2px; }
.invoice-details p { margin: 10px 0 0 0; font-size: 14px; }
.invoice-details strong { color: #1c3664; }
.payment-terms { text-align: right; font-size: 12px; color: #555; margin-bottom: 20px; }
.addresses { display: flex; gap: 50px; margin-bottom: 30px; }
.bill-to, .ship-to { flex: 1; }
.bill-to h3, .ship-to h3 { color: #1c3664; border-bottom: 2px solid #1c3664; padding-bottom: 5px; margin-bottom: 15px; font-size: 16px; }
.bill-to p, .ship-to p { margin: 0; line-height: 1.6; color: #333; font-size: 14px; }
table { width: 100%; border-collapse: collapse; margin-bottom: 30px; }
th, td { border: 1px solid #ddd; padding: 12px; text-align: right; font-size: 14px; color: #333; }
th:first-child, td:first-child { text-align: left; }
th { background-color: #e25822; color: white; font-weight: bold; }
.footer { display: flex; justify-content: space-between; gap: 40px; }
.remarks { flex: 2; font-size: 13px; color: #555; }
.remarks strong { color: #333; }
.remarks p { line-height: 1.5; margin-top: 5px; }
.totals { flex: 1; }
.totals .row { display: flex; justify-content: space-between; border-bottom: 1px solid #ddd; padding: 8px 0; font-size: 14px; }
.totals .row span:first-child { color: #1c3664; }
.totals .row.final { border-bottom: 2px solid #e25822; }
.totals .row.final span:first-child { color: #e25822; }
''')
