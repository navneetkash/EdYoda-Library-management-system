from User import Member, Librarian


lib = Librarian("Sumit yadav", "Mumbai", 30, "PUNE199", "JSPM1111")
print(lib)
lib.addBook("Crack IELTS", "Pravin Choudhari", "2015")
lib.addBookItem("Crack IELTS", "001aa", "B1")
lib.addBookItem("Crack IELTS", "002aa", "B2")
lib.addBook("Crack coding round", "Saurabh Jadhav", "2002")
lib.addBookItem("Crack coding round", "001ab", "C1")
lib.addBookItem("Crack coding round", "002ab", "C2")
lib.addBook("Theory of everything", "Stephen hawking", "2012")
lib.addBookItem("Theory of everything", "001ac", "D1")
lib.addBookItem("Theory of everything", "002ac", "D2")
lib.addBookItem("Theory of everything", "003ac", "D2")
lib.viewBooks()
lib.removeBookItem("001ac")
lib.viewBooks()
lib.removeBook("Crack coding round")
lib.viewBooks()


member1 = Member("Ashwani Devesh Kashyap", "Mumbai", 23, "ADK4321", "NESS4321")
member2 = Member("Shivani Kashyap", "Surat", 19, "SK1234", "MSU8765")
member3 = Member("Navneet Kashyap", "Patna", 21, "NK9876", "JSPM1715")
print(member1)
print(member2)
print(member3)
member1.viewBooks()
member1.search_by_book_name("Theory of everything")
member1.search_by_book_name("The magic of thinking big")
member1.search_by_author_name("Stephen Hawking")
member1.search_by_author_name("JK rowling")
member1.issue_book("Theory of everything", 8)
member2.issue_book("Crack IELTS", 10)
member1.viewBooks()

lib.view_issued_books()

member1.return_book("001ac")
member1.viewBooks()

member2.issue_book("Crack IELTS")

lib.viewMembers()

lib.removeMember("Navneet")
member1.issue_book("Crack IELTS")
lib.viewMembers()
lib.view_issued_books()