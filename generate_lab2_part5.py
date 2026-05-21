import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')

# Q17
write_file('q17/sales.xsd', """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="sales">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="salesman" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="name">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="first" type="xs:string"/>
                    <xs:element name="middle" type="xs:string" minOccurs="0"/>
                    <xs:element name="last" type="xs:string"/>
                  </xs:sequence>
                  <xs:attribute name="title" type="xs:string" use="optional"/>
                </xs:complexType>
              </xs:element>
              <xs:element name="phone">
                <xs:complexType>
                  <xs:simpleContent>
                    <xs:extension base="xs:string">
                      <xs:attribute name="type" default="personal">
                        <xs:simpleType>
                          <xs:restriction base="xs:string">
                            <xs:enumeration value="work"/>
                            <xs:enumeration value="home"/>
                            <xs:enumeration value="personal"/>
                          </xs:restriction>
                        </xs:simpleType>
                      </xs:attribute>
                    </xs:extension>
                  </xs:simpleContent>
                </xs:complexType>
              </xs:element>
              <xs:element name="area" type="xs:string"/>
              <xs:element name="records">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="record" maxOccurs="unbounded">
                      <xs:complexType>
                        <xs:sequence>
                          <xs:element name="product">
                            <xs:complexType>
                              <xs:sequence>
                                <xs:element name="sku" type="xs:string"/>
                                <xs:element name="product_name" type="xs:string"/>
                              </xs:sequence>
                              <xs:attribute name="productid" type="xs:string" use="required"/>
                            </xs:complexType>
                          </xs:element>
                          <xs:element name="quantity" type="xs:positiveInteger"/>
                          <xs:element name="price">
                            <xs:complexType>
                              <xs:simpleContent>
                                <xs:extension base="xs:decimal">
                                  <xs:attribute name="currency" default="npr">
                                    <xs:simpleType>
                                      <xs:restriction base="xs:string">
                                        <xs:enumeration value="npr"/>
                                        <xs:enumeration value="inr"/>
                                        <xs:enumeration value="usd"/>
                                      </xs:restriction>
                                    </xs:simpleType>
                                  </xs:attribute>
                                </xs:extension>
                              </xs:simpleContent>
                            </xs:complexType>
                          </xs:element>
                          <xs:element name="date">
                            <xs:complexType>
                              <xs:simpleContent>
                                <xs:extension base="xs:string">
                                  <xs:attribute name="type" use="required">
                                    <xs:simpleType>
                                      <xs:restriction base="xs:string">
                                        <xs:enumeration value="ad"/>
                                        <xs:enumeration value="bs"/>
                                      </xs:restriction>
                                    </xs:simpleType>
                                  </xs:attribute>
                                </xs:extension>
                              </xs:simpleContent>
                            </xs:complexType>
                          </xs:element>
                        </xs:sequence>
                      </xs:complexType>
                    </xs:element>
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

write_file('q17/sales.xml', """<?xml version="1.0" encoding="UTF-8"?>
<sales xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="sales.xsd">
    <salesman>
        <name title="Mr.">
            <first>Hari</first>
            <middle>Kumar</middle>
            <last>Shrestha</last>
        </name>
        <phone>9851012345</phone>
        <area>Kathmandu</area>
        <records>
            <record>
                <product productid="P-9901">
                    <sku>SKU-LAP-01</sku>
                    <product_name>Pro Laptop 15</product_name>
                </product>
                <quantity>2</quantity>
                <price currency="usd">1199.99</price>
                <date type="ad">2026-05-21</date>
            </record>
            <record>
                <product productid="P-5542">
                    <sku>SKU-MOU-05</sku>
                    <product_name>Wireless Optical Mouse</product_name>
                </product>
                <quantity>15</quantity>
                <price>2500.00</price>
                <date type="bs">2083-02-07</date>
            </record>
        </records>
    </salesman>
    <salesman>
        <name title="Ms.">
            <first>Sita</first>
            <last>Thapa</last>
        </name>
        <phone type="work">01-4412345</phone>
        <area>Lalitpur</area>
        <records>
            <record>
                <product productid="P-1022">
                    <sku>SKU-KB-09</sku>
                    <product_name>Mechanical Keyboard</product_name>
                </product>
                <quantity>5</quantity>
                <price currency="inr">4200.00</price>
                <date type="ad">2026-04-10</date>
            </record>
        </records>
    </salesman>
</sales>""")

# Q18
write_file('q18/students_input.xml', """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="students_transform.xsl"?>
<students> 
    <student> 
        <name>Ram Thapa</name> 
        <reg_no>5454545</reg_no> 
        <symbol_number>87878</symbol_number> 
        <marks> 
            <web>54</web> 
            <sad>54</sad> 
            <dsa>54</dsa> 
            <java>54</java> 
            <stat>54</stat> 
        </marks> 
    </student> 
    <student> 
        <name>Rabina Giri</name> 
        <reg_no>21221</reg_no> 
        <symbol_number>7777</symbol_number> 
        <marks> 
            <web>65</web> 
            <sad>78</sad> 
            <dsa>78</dsa> 
            <java>98</java> 
            <stat>24</stat> 
        </marks> 
    </student> 
</students>""")

write_file('q18/students_transform.xsl', """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="yes" encoding="UTF-8"/>
    <xsl:template match="/">
        <students>
            <xsl:for-each select="students/student">
                <student reg_no="{reg_no}">
                    <name><xsl:value-of select="name"/></name>
                    <symbol_number><xsl:value-of select="symbol_number"/></symbol_number>
                    <marks>
                        <subject name="web"><xsl:value-of select="marks/web"/></subject>
                        <subject name="dsa"><xsl:value-of select="marks/dsa"/></subject>
                        <subject name="java"><xsl:value-of select="marks/java"/></subject>
                        <subject name="sad"><xsl:value-of select="marks/sad"/></subject>
                        <subject name="stat"><xsl:value-of select="marks/stat"/></subject>
                    </marks>
                    <xsl:variable name="total" select="marks/web + marks/sad + marks/dsa + marks/java + marks/stat"/>
                    <total_marks>
                        <xsl:value-of select="$total"/>
                    </total_marks>
                    <percentage>
                        <xsl:value-of select="$total div 5"/>
                    </percentage>
                </student>
            </xsl:for-each>
        </students>
    </xsl:template>
</xsl:stylesheet>""")
