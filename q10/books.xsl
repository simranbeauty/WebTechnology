<?xml version="1.0" encoding="UTF-8"?>
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
</xsl:stylesheet>
