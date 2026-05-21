import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

# Q9
write_file('q9/topics.xml', """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="topics.xsl"?>
<course_directory>
    <main_heading>Hello Everyone! Welcome to XML to CSS</main_heading>
    <category name="Algo">
        <item>Greedy Algo</item>
        <item>Randomized Algo</item>
        <item>Searching Algo</item>
        <item>Sorting Algo</item>
    </category>
    <category name="Data Structures">
        <item>Array</item>
        <item>Stack</item>
        <item>Queue</item>
        <item>Linked List</item>
    </category>
    <category name="Web Technology">
        <item>HTML</item>
        <item>CSS</item>
        <item>Java Script</item>
        <item>Php</item>
    </category>
    <category name="Languages">
        <item>C/C++</item>
        <item>Java</item>
        <item>Python</item>
        <item>Ruby</item>
    </category>
    <category name="DBMS">
        <item>Basics</item>
        <item>ER Diagram</item>
        <item>Normalization</item>
        <item>Transaction Concepts</item>
    </category>
</course_directory>""")

write_file('q9/topics.xsl', """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
<head>
    <title>XML to XSLT Transformation</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #fcfcfc; }
        .header-banner { background-color: #008000; color: #ffffff; text-align: center; font-size: 22px; font-weight: bold; padding: 10px 0; border-bottom: 2px solid #004d00; }
        .category-row { text-align: center; padding: 15px 0; border-bottom: 1px solid #d3d3d3; background-color: #fdfdfd; }
        .category-title { color: #008000; font-size: 18px; font-weight: bold; text-decoration: underline; margin-bottom: 5px; }
        .topic-item { font-size: 12px; font-weight: bold; margin: 3px 0; }
        .color-1 { color: #008000; } /* Green */
        .color-2 { color: #cc0000; } /* Red */
        .color-3 { color: #0000ff; } /* Blue */
        .color-4 { color: #ff9900; } /* Orange */
    </style>
</head>
<body>
    <div class="header-banner">
        <xsl:value-of select="course_directory/main_heading"/>
    </div>
    <xsl:for-each select="course_directory/category">
        <div class="category-row">
            <div class="category-title">
                <xsl:value-of select="@name"/>
            </div>
            <xsl:for-each select="item">
                <xsl:variable name="colorPos" select="(position() - 1) mod 4 + 1"/>
                <div class="topic-item color-{$colorPos}">
                    <xsl:value-of select="."/>
                </div>
            </xsl:for-each>
        </div>
    </xsl:for-each>
</body>
</html>
</xsl:template>
</xsl:stylesheet>""")

# Q10
write_file('q10/books.xml', """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="books.xsl"?>
<bookstore>
    <main_title>Book List</main_title>
    <book>
        <title>Web Programming</title>
        <author>Chrisbates</author>
        <publisher>Wiley</publisher>
        <edition>3</edition>
        <price>300</price>
    </book>
    <book>
        <title>Internet world-wide-web</title>
        <author>Ditel</author>
        <publisher>Pearson</publisher>
        <edition>3</edition>
        <price>400</price>
    </book>
    <book>
        <title>Computer Networks</title>
        <author>Forouzan</author>
        <publisher>Mc Graw Hill</publisher>
        <edition>5</edition>
        <price>700</price>
    </book>
    <book>
        <title>DBMS Concepts</title>
        <author>Navath</author>
        <publisher>Oxford</publisher>
        <edition>5</edition>
        <price>600</price>
    </book>
    <book>
        <title>Linux Programming</title>
        <author>Subhitab Das</author>
        <publisher>Oxford</publisher>
        <edition>8</edition>
        <price>300</price>
    </book>
</bookstore>""")

write_file('q10/books.xsl', """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
<head>
    <title>Book List Table Transformation</title>
    <style>
        body { font-family: "Times New Roman", Times, serif; margin: 30px; background-color: #ffffff; }
        h1 { font-size: 28px; font-weight: bold; color: #000000; margin-bottom: 20px; margin-top: 0; }
        table { border-collapse: separate; border-spacing: 2px; border: 2px solid #888888; background-color: #fcfcfc; }
        th { border: 1px solid #888888; padding: 4px 10px; font-weight: bold; font-size: 16px; text-align: center; background-color: #ffffff; }
        td { border: 1px solid #888888; padding: 4px 8px; font-size: 15px; color: #333333; background-color: #ffffff; }
        .text-left { text-align: left; }
        .text-center { text-align: center; }
    </style>
</head>
<body>
    <h1><xsl:value-of select="bookstore/main_title"/></h1>
    <table>
        <thead>
            <tr>
                <th>Title</th>
                <th>Author</th>
                <th>Publisher</th>
                <th>Edition</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <xsl:for-each select="bookstore/book">
                <tr>
                    <td class="text-left"><xsl:value-of select="title"/></td>
                    <td class="text-left"><xsl:value-of select="author"/></td>
                    <td class="text-left"><xsl:value-of select="publisher"/></td>
                    <td class="text-center"><xsl:value-of select="edition"/></td>
                    <td class="text-center"><xsl:value-of select="price"/></td>
                </tr>
            </xsl:for-each>
        </tbody>
    </table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>""")

# Q11
write_file('q11/students.xsd', """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="students">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="student" maxOccurs="unbounded" minOccurs="0">
          <xs:complexType>
            <xs:simpleContent>
              <xs:extension base="xs:string">
                <xs:attribute name="regid" type="xs:integer" use="required"/>
                <xs:attribute name="firstName" type="xs:string" use="required"/>
                <xs:attribute name="lastName" type="xs:string" use="required"/>
                <xs:attribute name="age" type="xs:positiveInteger" use="required"/>
                <xs:attribute name="university" type="xs:string" use="required"/>
              </xs:extension>
            </xs:simpleContent>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>""")

write_file('q11/students.xml', """<?xml version="1.0" encoding="UTF-8"?>
<students xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="students.xsd">
    <student regid="125" firstName="Hari" lastName="Kumar" age="20" university="TU"/>
</students>""")

# Q12
write_file('q12/bib.xsd', """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="bib">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="book" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="title" type="xs:string"/>
              <xs:choice>
                <xs:element name="author" type="xs:string" maxOccurs="unbounded"/>
                <xs:element name="editor">
                  <xs:complexType>
                    <xs:simpleContent>
                      <xs:extension base="xs:string">
                        <xs:attribute name="affiliation" type="xs:string" use="optional"/>
                      </xs:extension>
                    </xs:simpleContent>
                  </xs:complexType>
                </xs:element>
              </xs:choice>
              <xs:element name="publisher" type="xs:string"/>
              <xs:element name="price" type="xs:decimal"/>
            </xs:sequence>
            <xs:attribute name="year" type="xs:gYear" use="required"/>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>""")

write_file('q12/bib.xsl', """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
<head>
    <title>Bibliography Collection</title>
    <style>
        table { border-collapse: collapse; width: 100%; font-family: sans-serif; }
        th, td { border: 1px solid #dddddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>Title</th>
                <th>Year</th>
                <th>Author</th>
                <th>Editor</th>
                <th>Publisher</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <xsl:for-each select="bib/book">
                <tr>
                    <td><xsl:value-of select="title"/></td>
                    <td><xsl:value-of select="@year"/></td>
                    <td>
                        <xsl:for-each select="author">
                            <xsl:value-of select="."/>
                            <xsl:if test="position() != last()">, </xsl:if>
                        </xsl:for-each>
                    </td>
                    <td><xsl:value-of select="editor/text()"/></td>
                    <td><xsl:value-of select="publisher"/></td>
                    <td><xsl:value-of select="price"/></td>
                </tr>
            </xsl:for-each>
        </tbody>
    </table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>""")

write_file('q12/queries.xquery', """(: a. Give the titles of all books sorted by price. :)
for $b in doc("bib.xml")/bib/book
order by xs:decimal($b/price)
return $b/title

(: b. How many books have been written by Abiteboul? :)
let $count := count(doc("bib.xml")/bib/book[author = "Abiteboul"])
return <result>{$count}</result>

(: c. Give for each author the number of books, which he has written. :)
for $author in distinct-values(doc("bib.xml")/bib/book/author)
let $books := doc("bib.xml")/bib/book[author = $author]
return 
  <author_metrics>
      <name>{$author}</name>
      <books_written>{count($books)}</books_written>
  </author_metrics>""")
