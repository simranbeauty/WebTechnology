<?xml version="1.0" encoding="UTF-8"?>
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
</xsl:stylesheet>
