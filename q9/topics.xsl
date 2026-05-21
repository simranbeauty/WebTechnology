<?xml version="1.0" encoding="UTF-8"?>
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
</xsl:stylesheet>
