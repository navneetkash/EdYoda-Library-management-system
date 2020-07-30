from Catalog import Catalog

class IssueReturn:

    def issue_book(name, student_id, book_title, days):
        for book in Catalog.books_list:
            if book.title == book_title and len(book.book_item) != 0:
                book_item = book.book_item.pop()
                book.total_count -= 1
                Catalog.update_member_issue_info(book_item, name, student_id, days)
                Catalog.add_to_issue_list(book_item)
                return book_item
        else:
            print(f"{book_title} is currently not available in the library")

    def return_book(return_book_item):
        for book in Catalog.books_list:
            if book == return_book_item:
                book.book_item.append(return_book_item)
                book.total_count += 1
        Catalog.clear_member_issue_info(return_book_item)
        Catalog.remove_from_issue_list(return_book_item)