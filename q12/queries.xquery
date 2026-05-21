(: a. Give the titles of all books sorted by price. :)
for $b in doc("bib.xml")/bib/book
order by xs:decimal($b/price)
return $b/title

(: b. How many books have been written by Abiteboul? :)
let $count := count(doc("bib.xml")/bib/book[author = "Abiteboul"])
return <result>{$count}</result>

(: c. Give for each author the number of books, which he has written. :)
for $author in distinct-values(doc("bib.xml")/bib/book/author)
let $books := doc("bib.xml")/bib/book[author = $author]
return 
  <author_metrics>
      <name>{$author}</name>
      <books_written>{count($books)}</books_written>
  </author_metrics>
