<?xml version="1.0" encoding="UTF-8"?>
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
</xsl:stylesheet>
