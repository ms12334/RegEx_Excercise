## RegEx_Excercise

Extract information within xml tags using *non-capturing* patterns and *re.DOTALL*.  This is for very simple XML files.

In Python, non-capturing patterns are indicated with **(?:_______)**.

**(?P\<name\>_______)** is a pattern for a named group.

sample1.py will extract names of publisher.

sample2.py will extract genres.

sample3.py will extract book titles, author names, and published years.

sample4.py will generate books_updated.xml. This doesn't use re.DOTALL or re.S option. Instead, (?s) was added at the beginning of RegEx. Also this example shows how to use group name as a reference.
