<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>Book Report</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 30px; }
          table { border-collapse: collapse; width: 100%; }
          th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
          th { background: #1d3557; color: #fff; }
          .expensive { background: #ffe8d6; }
        </style>
      </head>
      <body>
        <h1>Book Report</h1>
        <p>Total books: <xsl:value-of select="count(/catalog/book)"/></p>
        <table>
          <tr><th>#</th><th>Title</th><th>Author</th><th>Category</th><th>Price (Rs.)</th></tr>
          <xsl:for-each select="/catalog/book">
            <xsl:sort select="price" data-type="number" order="descending"/>
            <tr>
              <xsl:if test="price &gt; 2000">
                <xsl:attribute name="class">expensive</xsl:attribute>
              </xsl:if>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="title"/></td>
              <td><xsl:value-of select="author"/></td>
              <td>
                <xsl:choose>
                  <xsl:when test="@category='database'">Database</xsl:when>
                  <xsl:when test="@category='programming'">Programming</xsl:when>
                  <xsl:otherwise>Other</xsl:otherwise>
                </xsl:choose>
              </td>
              <td><xsl:value-of select="price"/></td>
            </tr>
          </xsl:for-each>
        </table>
        <p>Total value: Rs. <xsl:value-of select="sum(/catalog/book/price)"/></p>
        <p>Average price: Rs. <xsl:value-of select="round(sum(/catalog/book/price) div count(/catalog/book))"/></p>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
