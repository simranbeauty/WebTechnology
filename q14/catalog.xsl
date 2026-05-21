<?xml version="1.0" encoding="UTF-8"?>
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
</xsl:stylesheet>
