import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

# Q5
write_file('q5/students.xsd', """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="student_records">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="student" maxOccurs="unbounded">
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
              <xs:element name="email">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:pattern value="[^@]+@[^\.]+\..+"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element name="phone">
                <xs:simpleType>
                  <xs:restriction base="xs:string">
                    <xs:pattern value="(98|97)[0-9]{8}"/>
                  </xs:restriction>
                </xs:simpleType>
              </xs:element>
              <xs:element name="address" maxOccurs="2">
                <xs:complexType>
                  <xs:simpleContent>
                    <xs:extension base="xs:string">
                      <xs:attribute name="type" use="required">
                        <xs:simpleType>
                          <xs:restriction base="xs:string">
                            <xs:enumeration value="permanent"/>
                            <xs:enumeration value="temporary"/>
                          </xs:restriction>
                        </xs:simpleType>
                      </xs:attribute>
                    </xs:extension>
                  </xs:simpleContent>
                </xs:complexType>
              </xs:element>
              <xs:element name="DOB">
                <xs:complexType>
                  <xs:simpleContent>
                    <xs:extension base="datePattern">
                      <xs:attribute name="type" use="required">
                        <xs:simpleType>
                          <xs:restriction base="xs:string">
                            <xs:enumeration value="AD"/>
                            <xs:enumeration value="BS"/>
                          </xs:restriction>
                        </xs:simpleType>
                      </xs:attribute>
                    </xs:extension>
                  </xs:simpleContent>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
            <xs:attribute name="rollno" type="xs:string" use="required"/>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
    <xs:unique name="uniqueRollNo">
      <xs:selector xpath="student"/>
      <xs:field xpath="@rollno"/>
    </xs:unique>
  </xs:element>
  <xs:simpleType name="datePattern">
    <xs:restriction base="xs:string">
      <xs:pattern value="[0-9]{4}-[0-9]{2}-[0-9]{2}"/>
    </xs:restriction>
  </xs:simpleType>
</xs:schema>""")

write_file('q5/students.xml', """<?xml version="1.0" encoding="UTF-8"?>
<student_records xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="students.xsd">
    <student rollno="S101">
        <name>
            <first_name>Rohan</first_name>
            <middle_name>Kumar</middle_name>
            <last_name>Sharma</last_name>
        </name>
        <email>rohan.sharma@example.com</email>
        <phone>9841234567</phone>
        <address type="permanent">Kathmandu, Nepal</address>
        <address type="temporary">Lalitpur, Nepal</address>
        <DOB type="AD">2004-05-14</DOB>
    </student>
    <student rollno="S102">
        <name>
            <first_name>Aayusha</first_name>
            <last_name>Shrestha</last_name>
        </name>
        <email>aayusha@domain.org</email>
        <phone>9745678901</phone>
        <address type="permanent">Pokhara, Nepal</address> 
        <DOB type="BS">2061-02-25</DOB>
    </student>
</student_records>""")

# Q6
write_file('q6/university.xsd', """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:complexType name="addressType">
    <xs:sequence>
      <xs:element name="street" type="xs:string"/>
      <xs:element name="suburb" type="xs:string"/>
      <xs:element name="postcode" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="staffType">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="title" type="xs:string" minOccurs="0"/>
      <xs:element name="category">
        <xs:simpleType>
          <xs:restriction base="xs:string">
            <xs:enumeration value="academic"/>
            <xs:enumeration value="general"/>
            <xs:enumeration value="technical"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      <xs:element name="address" type="addressType" maxOccurs="unbounded"/>
    </xs:sequence>
    <xs:attribute name="staff_id" type="xs:string" use="required"/>
  </xs:complexType>
  <xs:simpleType name="capacityLimit">
    <xs:restriction base="xs:integer">
      <xs:minInclusive value="6"/>
      <xs:maxInclusive value="400"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:element name="university">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="school" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="name" type="xs:string"/>
              <xs:element name="location" type="xs:string" maxOccurs="unbounded"/>
              <xs:element name="staff_members">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="staff" type="staffType" maxOccurs="unbounded"/>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
              <xs:element name="subjects">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="subject" maxOccurs="unbounded">
                      <xs:complexType>
                        <xs:sequence>
                          <xs:element name="name" type="xs:string"/>
                          <xs:element name="description" type="xs:string"/>
                          <xs:element name="capacity" type="capacityLimit"/>
                          <xs:element name="taught_by" maxOccurs="unbounded">
                            <xs:complexType>
                              <xs:attribute name="staff_ref" type="xs:string" use="required"/>
                            </xs:complexType>
                          </xs:element>
                        </xs:sequence>
                        <xs:attribute name="subject_code" type="xs:string" use="required"/>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
            <xs:attribute name="school_id" type="xs:string" use="required"/>
          </xs:complexType>
          <xs:key name="staffKey">
            <xs:selector xpath="staff_members/staff"/>
            <xs:field xpath="@staff_id"/>
          </xs:key>
          <xs:keyref name="taughtByStaffRef" refer="staffKey">
            <xs:selector xpath="subjects/subject/taught_by"/>
            <xs:field xpath="@staff_ref"/>
          </xs:keyref>
          <xs:key name="subjectKey">
            <xs:selector xpath="subjects/subject"/>
            <xs:field xpath="@subject_code"/>
          </xs:key>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
    <xs:unique name="uniqueSchoolId">
      <xs:selector xpath="school"/>
      <xs:field xpath="@school_id"/>
    </xs:unique>
  </xs:element>
</xs:schema>""")

write_file('q6/university.xml', """<?xml version="1.0" encoding="UTF-8"?>
<university xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="university.xsd">
    <school school_id="SCI-01">
        <name>School of Computer Science</name>
        <location>Building A, North Campus</location>
        <staff_members>
            <staff staff_id="STF101">
                <name>Dr. Alan Turing</name>
                <title>Senior Lecturer</title>
                <category>academic</category>
                <address>
                    <street>123 Computing Way</street>
                    <suburb>Binary Hills</suburb>
                    <postcode>2000</postcode>
                </address>
                <address>
                    <street>456 Innovation Blvd</street>
                    <suburb>Silicon Valley</suburb>
                    <postcode>94043</postcode>
                </address>
            </staff>
            <staff staff_id="STF102">
                <name>Grace Hopper</name>
                <category>technical</category>
                <address>
                    <street>789 Compiler Lane</street>
                    <suburb>Data Core</suburb>
                    <postcode>4000</postcode>
                </address>
            </staff>
        </staff_members>
        <subjects>
            <subject subject_code="COMP101">
                <name>Introduction to Programming</name>
                <description>Foundational concepts of software development.</description>
                <capacity>150</capacity> 
                <taught_by staff_ref="STF101"/>
            </subject>
            <subject subject_code="COMP402">
                <name>Advanced Quantum Computing</name>
                <description>Exploring quantum algorithms and architectures.</description>
                <capacity>12</capacity> 
                <taught_by staff_ref="STF101"/>
                <taught_by staff_ref="STF102"/>
            </subject>
        </subjects>
    </school>
</university>""")

# Q7
write_file('q7/movies.xsd', """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="movies">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="Movie" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="title" type="xs:string"/>
              <xs:element name="year" type="xs:string"/>
              <xs:element name="_director">
                <xs:complexType>
                  <xs:simpleContent>
                    <xs:extension base="xs:string">
                      <xs:attribute name="name" type="xs:string" use="optional"/>
                    </xs:extension>
                  </xs:simpleContent>
                </xs:complexType>
              </xs:element>
              <xs:choice maxOccurs="unbounded">
                <xs:element name="comment">
                  <xs:complexType>
                    <xs:simpleContent>
                      <xs:extension base="xs:string">
                        <xs:attribute name="lang" type="xs:string" use="optional"/>
                      </xs:extension>
                    </xs:simpleContent>
                  </xs:complexType>
                </xs:element>
                <xs:element name="newcomment" type="xs:string"/>
              </xs:choice>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="required"/>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>""")

write_file('q7/movies.xml', """<?xml version="1.0" encoding="UTF-8"?>
<movies xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="movies.xsd">
    <Movie id="m101">
        <title>Inception</title>
        <year>2010</year>
        <_director name="Christopher Nolan">Director Information</_director>
        <comment lang="en">A masterpiece of modern sci-fi.</comment>
        <comment lang="fr">Absolument brillant.</comment>
    </Movie>
    <Movie id="m102">
        <title>Spirited Away</title>
        <year>2001</year>
        <_director>Hayao Miyazaki</_director>
        <comment>Beautifully animated.</comment>
        <newcomment>An incredible theatrical re-release experience!</newcomment>
        <comment lang="jp">すばらしい映画です。</comment>
    </Movie>
</movies>""")

# Q8
write_file('q8/oceans.xml', """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/css" href="oceans.css"?>
<document>
    <title_banner>Oceans</title_banner>
    <oceans_container>
        <ocean>
            <name>Arctic</name>
            <metric>Area: 13,000 million km²</metric>
            <metric>Mean depth: 1,200 m</metric>
        </ocean>
        <ocean>
            <name>Atlantic</name>
            <metric>Area: 87,000 million km²</metric>
            <metric>Mean depth: 3,900 m</metric>
        </ocean>
        <ocean>
            <name>Pacific</name>
            <metric>Area: 180,000 million km²</metric>
            <metric>Mean depth: 4,000 m</metric>
        </ocean>
        <ocean>
            <name>Indian</name>
            <metric>Area: 73,000 million km²</metric>
            <metric>Mean depth: 3,900 m</metric>
        </ocean>
        <ocean>
            <name>Southern</name>
            <metric>Area: 20,000 million km²</metric>
            <metric>Mean depth: 4,500 m</metric>
        </ocean>
    </oceans_container>
</document>""")

write_file('q8/oceans.css', """/* Document Layout Container setup */
document {
    display: block;
    font-family: "Times New Roman", Times, serif;
    margin: 40px;
    padding: 0;
    position: relative;
}
oceans_container {
    display: block;
    border: 1px solid #a4bde2;
    padding: 35px 25px 20px 25px;
    margin-top: 15px;
    background-color: #ffffff;
}
title_banner {
    display: block;
    position: absolute;
    top: -4px;
    left: 0px;
    background-color: #cbdcfc;
    color: #000000;
    font-size: 18px;
    font-weight: bold;
    padding: 4px 45px 4px 12px;
    border-top: 1px solid #a4bde2;
    border-left: 1px solid #a4bde2;
    border-right: 1px solid #a4bde2;
    z-index: 10;
}
ocean {
    display: block;
    margin-bottom: 20px;
}
name {
    display: block;
    font-size: 16px;
    font-weight: bold;
    color: #000000;
    margin-bottom: 2px;
}
metric {
    display: block;
    font-size: 12px;
    color: #333333;
    margin-left: 2px;
    line-height: 1.4;
}""")
