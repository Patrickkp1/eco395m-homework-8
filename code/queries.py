-- 1. select COUNT(*) from "Artist" a 

select COUNT(*) from (select
	a."ArtistId" ,
	a."Name",
	a2."Title"
from
	"Artist" a
left outer join "Album" a2 on
	a2."ArtistId" = a."ArtistId") e
where e."Title" is null 

select COUNT(*) from (select
	a."ArtistId" ,
	a."Name",
	a2."Title"
from
	"Artist" a
right outer join "Album" a2 on
	a2."ArtistId" = a."ArtistId") e
where e."Title" is null 


select tt."Name" from (select t."Composer" , t."Name" from "Track" t 
group by t."Name", t."Composer") tt
where tt."Composer" = 'AC/DC'


--select sum(t."UnitPrice") from "Track" t 
--where t."Composer" = 'AC/DC'

select * from "InvoiceLine" i left outer join "Track" t on t."TrackId" = i."TrackId" 
where t."Composer" = 'AC/DC'

select * from "Invoice" i 

select * from (select * from "Track" t 
full outer join "InvoiceLine" l on t."TrackId" = l."TrackId") e
where e."Composer" = 'AC/DC'




# PROBLEM 1
# How many artists are there?
# Return a single column called "count" with a single row containing the count.
query_1 = """

    """

# PROBLEM 2
# How many Artists do not have an Album associated with them?
# Return a single column called "count" with a single row containing the count.
query_2 = """

"""

# PROBLEM 3
# How many Albums do not have an artist in the Artist table associated with them?
# Return a single column called "count" with a single row containing the count.
query_3 = """

"""

# PROBLEM 4
# List the tracks by "AC/DC"
# Return a single column called "AC/DC Tracks",
# in any order.
query_4 = """

"""

# PROBLEM 5
# Find the total sales of AC/DC Tracks.
# Return a single column called "Total Sales" with a single row containing the total.

query_5 = """

"""

# PROBLEM 6
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# for the artists with less than or equal to $5 in sales,
# in any order.

query_6 = """

"""

# PROBLEM 7
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# in descending order of "Total Sales".

query_7 = """

"""

# PROBLEM 8
# Find all of "Michael Mitchell"'s direct reports.
# Return 2 columns called "Name" and "Title".
# "Name" should have the employee's name in the form "last name, first name",
# for example, someone with the last name "Smith" and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_8 = """

"""

# PROBLEM 9
# Make a reporting chart. For each employee, find their name, title, manager's name and manager's title.
# Return 4 columns called "Employee Name" and "Employee Title", "Manager Name" and "Manager Title",
# "Employee Name" and "Manager Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_9 = """

"""

# PROBLEM 10
# Find the most recently hired employee(s) and their hire date(s)
# Return two columns called "Name" and "Hire Date",
# in any order.
# "Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Bob, Smith"

query_10 = """

"""

# PROBLEM 11
# Assume today is "2010-01-01", find every employee's tenure.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in any order.

query_11 = """

"""
# PROBLEM 12
# Assume today is 2010-01-01, find every employee with a tenure of less than 7 365-day years.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in ascending order of tenure.

query_12 = """

"""
