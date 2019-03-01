def is_isbn_or_key(word):
    # isbn  isbn13 13个0到9的数字组成
    # isbn10 10个0到9的数字组成，含有一些'-'

    if len(word) == 13 and word.isdigit():
        return 'isbn'
    if '-' in word and len(word.replace('-', '')) == 10:
        # isbn10
        return 'isbn'
    return 'keyword'
