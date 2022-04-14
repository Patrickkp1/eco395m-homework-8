# PROBLEM 1
# How many artists are there?
# Return a single column called "count" with a single row containing the count.
query_1 = """
select COUNT(*) from "Artist" a 
    """

# PROBLEM 2
# How many Artists do not have an Album associated with them?
# Return a single column called "count" with a single row containing the count.
query_2 = """
select COUNT(*) from (select
	a."ArtistId" ,
	a."Name",
	a2."Title"
from
	"Artist" a
left outer join "Album" a2 on
	a2."ArtistId" = a."ArtistId") e
where e."Title" is null 
"""

# PROBLEM 3
# How many Albums do not have an artist in the Artist table associated with them?
# Return a single column called "count" with a single row containing the count.
query_3 = """
select COUNT(*) from (select
	a."ArtistId" ,
	a."Name",
	a2."Title"
from
	"Artist" a
right outer join "Album" a2 on
	a2."ArtistId" = a."ArtistId") e
where e."Title" is null 
"""

# PROBLEM 4
# List the tracks by "AC/DC"
# Return a single column called "AC/DC Tracks",
# in any order.
query_4 = """
select tt."AC/DC Tracks" from (select t."Composer" , t."Name" "AC/DC Tracks" from "Track" t 
group by t."Name", t."Composer") tt
where tt."Composer" = 'AC/DC' or tt."Composer" = 'Angus Young, Malcolm Young, Brian Johnson'

"""

# PROBLEM 5
# Find the total sales of AC/DC Tracks.
# Return a single column called "Total Sales" with a single row containing the total.

query_5 = """
select sum(il."UnitPrice") as "Total Sales"
from "InvoiceLine" il 
left outer join "Track" t 
on il."TrackId" = t."TrackId" 
where t."TrackId" in (select t2."TrackId" from "Track" t2 where t2."Composer" = 'AC/DC' or 
t2."Composer" = 'Angus Young, Malcolm Young, Brian Johnson')
"""

# PROBLEM 6
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# for the artists with less than or equal to $5 in sales,
# in any order.

query_6 = """
select aa."Name" as "Artist", sum(il."UnitPrice") as "Total Sales" from  "InvoiceLine" il 
inner join "Track" t on il."TrackId" = t."TrackId" 
inner join "Album" a on t."AlbumId" = a."AlbumId"
inner join "Artist" aa on aa."ArtistId" = a."ArtistId" group by aa."Name" 
having sum(il."UnitPrice") <= 5


"""

# PROBLEM 7
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# in descending order of "Total Sales".

query_7 = """
select * from (select aa."Name" as "Artist", sum(il."UnitPrice") as "Total Sales" from  "InvoiceLine" il 
inner join "Track" t on il."TrackId" = t."TrackId" 
inner join "Album" a on t."AlbumId" = a."AlbumId"
inner join "Artist" aa on aa."ArtistId" = a."ArtistId" group by aa."Name") e
order by e."Total Sales" desc

"""

# PROBLEM 8
# Find all of "Michael Mitchell"'s direct reports.
# Return 2 columns called "Name" and "Title".
# "Name" should have the employee's name in the form "last name, first name",
# for example, someone with the last name "Smith" and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_8 = """
select e."Name", e."Title" from (select concat(e."LastName", ', ', e."FirstName") "Name", e."Title", e2."LastName" as "manager" from "Employee" e 
join "Employee" e2  on e."ReportsTo" = e2."EmployeeId") e
where e."manager" = 'Mitchell'
"""

# PROBLEM 9
# Make a reporting chart. For each employee, find their name, title, manager's name and manager's title.
# Return 4 columns called "Employee Name" and "Employee Title", "Manager Name" and "Manager Title",
# "Employee Name" and "Manager Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_9 = """
select concat(e."LastName", ', ', e."FirstName") as "Employee Name",  e."Title" as  "Employee Title", 
concat(e2."LastName", ', ', e."FirstName") as "Manager Name", e2."Title" as "Manager Title" 
from "Employee" e inner join "Employee" e2 on e."ReportsTo" = e2."EmployeeId"
"""

# PROBLEM 10
# Find the most recently hired employee(s) and their hire date(s)
# Return two columns called "Name" and "Hire Date",
# in any order.
# "Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Bob, Smith"

query_10 = """
select concat(e."LastName", ', ', e."FirstName") as "Name", e."HireDate" as "Hire Date"
from "Employee" as e
order by e."HireDate" desc 
"""

# PROBLEM 11
# Assume today is "2010-01-01", find every employee's tenure.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in any order.

query_11 = """
select e."FirstName" as "First Name", e."LastName" as "Last Name", 
('2010-01-01' - e."HireDate") as "Tenure"
from "Employee" e
"""
# PROBLEM 12
# Assume today is 2010-01-01, find every employee with a tenure of less than 7 365-day years.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in ascending order of tenure.

query_12 = """
select e."FirstName" as "First Name", 
e."LastName" as "Last Name", 
('2010-01-01' - e."HireDate") as "Tenure"
from "Employee" e
where '2010-01-01' - date(e."HireDate") <= 7*365
order by "Tenure"
"""
