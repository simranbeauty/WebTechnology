import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

# Q13
write_file('q13/hospital.xsd', """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="hospital_records">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="patient" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="name">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="first_name" type="xs:string"/>
                    <xs:element name="middle_name" type="xs:string" minOccurs="0"/>
                    <xs:element name="last_name" type="xs:string"/>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
              <xs:element name="patient_number">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:pattern value="[0-9]{5}"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element name="doctor_name" type="xs:string"/>
              <xs:element name="disease" type="xs:string" maxOccurs="unbounded"/>
              <xs:element name="consultation_charge">
                <xs:simpleType>
                  <xs:restriction base="xs:decimal">
                    <xs:minInclusive value="500"/>
                    <xs:maxInclusive value="5000"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element name="lab_tests">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="test" type="xs:string" maxOccurs="unbounded"/>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>""")

write_file('q13/hospital.xml', """<?xml version="1.0" encoding="UTF-8"?>
<hospital_records xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="hospital.xsd">
    <patient>
        <name>
            <first_name>Robert</first_name>
            <middle_name>John</middle_name>
            <last_name>Miller</last_name>
        </name>
        <patient_number>45102</patient_number>
        <doctor_name>Dr. Alice Evans</doctor_name>
        <disease>Type 2 Diabetes</disease>
        <disease>Hypertension</disease>
        <consultation_charge>1500.00</consultation_charge>
        <lab_tests>
            <test>HbA1c Blood Test</test>
            <test>Lipid Panel</test>
            <test>Basic Metabolic Panel</test>
        </lab_tests>
    </patient>
    <patient>
        <name>
            <first_name>Sarah</first_name>
            <last_name>Connor</last_name>
        </name>
        <patient_number>91823</patient_number>
        <doctor_name>Dr. Raymond Holt</doctor_name>
        <disease>Acute Bronchitis</disease>
        <consultation_charge>500.00</consultation_charge>
        <lab_tests>
            <test>Chest X-Ray</test>
            <test>Complete Blood Count (CBC)</test>
        </lab_tests>
    </patient>
</hospital_records>""")

# Q14
write_file('q14/catalog.xml', """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="catalog.xsl"?>
<catalog>
    <book id="bk101">
        <author>Buneman</author>
        <title>XML Developer's Guide</title>
        <genre>Computer</genre>
        <price>129.95</price>
        <publish_date>1992-03-25</publish_date>
        <description>Kluwer Academic Publishers</description>
    </book>
    <book id="bk102">
        <author>Gambardella, Matthew</author>
        <title>Midnight Rain</title>
        <genre>Fantasy</genre>
        <price>44.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>An in-depth look at creating applications with XML.</description>
    </book>
    <book id="bk103">
        <author>Ralls, Kim</author>
        <title>Midnight Rain</title>
        <genre>Fantasy</genre>
        <price>5.95</price>
        <publish_date>2000-12-16</publish_date>
        <description>A former software engineer battles an ancient dread.</description>
    </book>
    <book id="bk104">
        <author>Corets, Eva</author>
        <title>Maeve Ascendant</title>
        <genre>Fantasy</genre>
        <price>5.95</price>
        <publish_date>2000-11-17</publish_date>
        <description>After the collapse of a minor kingdom, a new power arises.</description>
    </book>
    <book id="bk105">
        <author>Corets, Eva</author>
        <title>Oberon's Legacy</title>
        <genre>Fantasy</genre>
        <price>5.95</price>
        <publish_date>2001-03-10</publish_date>
        <description>In Ireland, an ancient druid stone is discovered.</description>
    </book>
</catalog>""")

write_file('q14/catalog.xsl', """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
<head>
    <title>Book Catalog Table</title>
    <style>
        table { border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; margin-top: 20px; }
        th, td { border: 1px solid #000000; padding: 10px; text-align: left; vertical-align: top; }
        th { font-weight: bold; font-size: 14px; background-color: #ffffff; }
        td { font-size: 13px; color: #000000; line-height: 1.4; }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Publish<br/>Date</th>
                <th>Author</th>
                <th>Genere</th>
                <th>Description</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <xsl:for-each select="catalog/book">
                <tr>
                    <td><xsl:value-of select="@id"/></td>
                    <td><xsl:value-of select="title"/></td>
                    <td><xsl:value-of select="publish_date"/></td>
                    <td><xsl:value-of select="author"/></td>
                    <td><xsl:value-of select="genre"/></td>
                    <td><xsl:value-of select="description"/></td>
                    <td><xsl:value-of select="price"/></td>
                </tr>
            </xsl:for-each>
        </tbody>
    </table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>""")

# Q15
write_file('q15/tu_directory.xsd', """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="TU">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="Employee" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="Post">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:minLength value="5"/>
                    <xs:maxLength value="8"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element name="Salary">
                <xs:simpleType>
                  <xs:restriction base="xs:integer">
                    <xs:minInclusive value="25000"/>
                    <xs:maxInclusive value="50000"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element name="Gender">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:enumeration value="male"/>
                    <xs:enumeration value="female"/>
                    <xs:enumeration value="others"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element name="UserName">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:minLength value="8"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element name="Password">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:pattern value="[a-zA-Z][a-zA-Z0-9!@#$%^&amp;*()_+\-=\[\]{};':&quot;\\|,&lt;&gt;/?]{7}"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>""")

write_file('q15/tu_directory.xml', """<?xml version="1.0" encoding="UTF-8"?>
<TU xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="tu_directory.xsd">
    <Employee>
        <Post>Officer</Post>
        <Salary>35000</Salary>
        <Gender>male</Gender>
        <UserName>harikumar99</UserName>
        <Password>P@ss1234</Password>
    </Employee>
    <Employee>
        <Post>Analyst</Post>
        <Salary>48500</Salary>
        <Gender>female</Gender>
        <UserName>sitasubedi</UserName>
        <Password>a1b2c3d4</Password>
    </Employee>
</TU>""")

# Q16
write_file('q16/transform_products.xsl', """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="yes" encoding="UTF-8"/>
    <xsl:key name="products-by-category" match="product" use="category" />
    <xsl:template match="/*">
        <root>
            <xsl:for-each select="product[quantity &gt;= 10][generate-id() = generate-id(key('products-by-category', category)[quantity &gt;= 10][1])]">
                <xsl:variable name="currentCategory" select="category"/>
                <category name="{$currentCategory}">
                    <xsl:for-each select="key('products-by-category', $currentCategory)[quantity &gt;= 10]">
                        <xsl:sort select="price" data-type="number" order="descending"/>
                        <product>
                            <xsl:attribute name="productname">
                                <xsl:value-of select="productname"/>
                            </xsl:attribute>
                            <price><xsl:value-of select="price"/></price>
                            <quantity><xsl:value-of select="quantity"/></quantity>
                            <total-price>
                                <xsl:value-of select="price * quantity"/>
                            </total-price>
                        </product>
                    </xsl:for-each>
                </category>
            </xsl:for-each>
        </root>
    </xsl:template>
</xsl:stylesheet>""")

write_file('q16/products.xml', """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="transform_products.xsl"?>
<products_list>
    <product>
        <productname>Laptop</productname>
        <category>Electronics</category>
        <price>1200</price>
        <quantity>15</quantity>
    </product>
    <product>
        <productname>Tablet</productname>
        <category>Electronics</category>
        <price>400</price>
        <quantity>5</quantity>
    </product>
    <product>
        <productname>Smartphone</productname>
        <category>Electronics</category>
        <price>800</price>
        <quantity>20</quantity>
    </product>
    <product>
        <productname>Desk Chair</productname>
        <category>Furniture</category>
        <price>150</price>
        <quantity>12</quantity>
    </product>
</products_list>""")
