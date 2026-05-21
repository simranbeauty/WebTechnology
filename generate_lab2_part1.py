import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

# Q1
write_file('q1/book_information.xml', """<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
    <book id="1">
        <title>The Pragmatic Programmer: Your Journey to Mastery</title>
        <author>Andrew Hunt</author>
        <isbn>978-0135166307</isbn>
        <publisher>Addison-Wesley Professional</publisher>
        <edition>2nd Edition</edition>
        <price currency="USD">45.99</price>
    </book>
    <book id="2">
        <title>Clean Code: A Handbook of Agile Software Craftsmanship</title>
        <author>Robert C. Martin</author>
        <isbn>978-0132350884</isbn>
        <publisher>Prentice Hall</publisher>
        <edition>1st Edition</edition>
        <price currency="USD">42.50</price>
    </book>
    <book id="3">
        <title>Introduction to Algorithms</title>
        <author>Thomas H. Cormen</author>
        <isbn>978-0262046305</isbn>
        <publisher>MIT Press</publisher>
        <edition>4th Edition</edition>
        <price currency="USD">95.00</price>
    </book>
</bookstore>""")

# Q2
write_file('q2/book_information.dtd', """<!ELEMENT bookstore (book+)>
<!ELEMENT book (title, author, isbn, publisher, edition, price)>
<!ATTLIST book id CDATA #REQUIRED>

<!ELEMENT title (#PCDATA)>
<!ELEMENT author (#PCDATA)>
<!ELEMENT isbn (#PCDATA)>
<!ELEMENT publisher (#PCDATA)>
<!ELEMENT edition (#PCDATA)>
<!ELEMENT price (#PCDATA)>
<!ATTLIST price currency CDATA #IMPLIED>""")

write_file('q2/book_information.xsd', """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="bookstore">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="book" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="title" type="xs:string"/>
              <xs:element name="author" type="xs:string"/>
              <xs:element name="isbn" type="xs:string"/>
              <xs:element name="publisher" type="xs:string"/>
              <xs:element name="edition" type="xs:string"/>
              <xs:element name="price">
                <xs:complexType>
                  <xs:simpleContent>
                    <xs:extension base="xs:decimal">
                      <xs:attribute name="currency" type="xs:string" use="optional"/>
                    </xs:extension>
                  </xs:simpleContent>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:integer" use="required"/>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>""")

# Q3
write_file('q3/playlist.xml', """<?xml version="1.0" encoding="UTF-8"?>
<playlist>
    <song>
        <name>Bohemian Rhapsody</name>
        <singer>Queen</singer>
        <composed_by>Freddie Mercury</composed_by>
        <length>5:55</length>
    </song>

    <song>
        <name>Shape of You</name>
        <singer>Ed Sheeran</singer>
        <composed_by>Ed Sheeran</composed_by>
        <length>3:53</length>
    </song>

    <song>
        <name>Thriller</name>
        <singer>Michael Jackson</singer>
        <composed_by>Rod Temperton</composed_by>
        <length>5:57</length>
    </song>

    <song>
        <name>Someone Like You</name>
        <singer>Adele</singer>
        <composed_by>Adele and Dan Wilson</composed_by>
        <length>4:45</length>
    </song>
</playlist>""")

# Q4
write_file('q4/bookstore.xsd', """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:complexType name="nameType">
    <xs:sequence>
      <xs:element name="first_name" type="xs:string"/>
      <xs:element name="middle_name" type="xs:string" minOccurs="0"/>
      <xs:element name="last_name" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="bookstore">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="book" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="title" type="xs:string"/>
              <xs:element name="author" maxOccurs="unbounded">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="name" type="nameType"/>
                  </xs:sequence>
                  <xs:attribute name="title" default="ms">
                    <xs:simpleType>
                      <xs:restriction base="xs:string">
                        <xs:enumeration value="mr"/>
                        <xs:enumeration value="ms"/>
                        <xs:enumeration value="mrs"/>
                      </xs:restriction>
                    </xs:simpleType>
                  </xs:attribute>
                  <xs:attribute name="phone" type="xs:string" use="required"/>
                  <xs:attribute name="email" type="xs:string" use="required"/>
                </xs:complexType>
              </xs:element>
              <xs:element name="page_no" type="xs:positiveInteger"/>
              <xs:element name="price">
                <xs:complexType>
                  <xs:simpleContent>
                    <xs:extension base="priceLimit">
                      <xs:attribute name="currency" use="required">
                        <xs:simpleType>
                          <xs:restriction base="xs:string">
                            <xs:enumeration value="NPR"/>
                            <xs:enumeration value="INR"/>
                            <xs:enumeration value="USD"/>
                          </xs:restriction>
                        </xs:simpleType>
                      </xs:attribute>
                    </xs:extension>
                  </xs:simpleContent>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
            <xs:attribute name="isbn" type="xs:string" use="required"/>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
    <xs:unique name="uniqueISBN">
      <xs:selector xpath="book"/>
      <xs:field xpath="@isbn"/>
    </xs:unique>
  </xs:element>
  <xs:simpleType name="priceLimit">
    <xs:restriction base="xs:decimal">
      <xs:maxInclusive value="600"/>
    </xs:restriction>
  </xs:simpleType>
</xs:schema>""")

write_file('q4/bookstore.xml', """<?xml version="1.0" encoding="UTF-8"?>
<bookstore xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="bookstore.xsd">
    <book isbn="978-3-16-148410-0">
        <title>The Tech Revolution</title>
        <author title="mr" phone="+1-555-0199" email="john.d@example.com">
            <name>
                <first_name>John</first_name>
                <middle_name>Robert</middle_name>
                <last_name>Doe</last_name>
            </name>
        </author>
        <author phone="+1-555-0143" email="jane.s@example.com">
            <name>
                <first_name>Jane</first_name>
                <last_name>Smith</last_name>
            </name>
        </author>
        <page_no>350</page_no>
        <price currency="USD">45.00</price>
    </book>
    <book isbn="978-0-545-01022-1">
        <title>Himalayan Trails</title>
        <author title="mrs" phone="+977-1-444444" email="anita@example.com.np">
            <name>
                <first_name>Anita</first_name>
                <last_name>Sharma</last_name>
            </name>
        </author>
        <page_no>210</page_no>
        <price currency="NPR">550.00</price>
    </book>
</bookstore>""")
