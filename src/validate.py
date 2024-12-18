import datetime
from repositories.references_repository import get_reference_id


class UserInputError(Exception):
    pass


def should_be_str(param_name, value):
    if not value or not isinstance(value, str) or len(value) < 1:
        raise UserInputError(f"{param_name} is too short or invalid.")


def should_be_valid_positive_int(param_name, value):
    if value and not value.isnumeric():
        raise UserInputError(f"{param_name} must be a positive integer.")


def year_check(year):
    should_be_valid_positive_int("year", year)
    if int(year) > datetime.date.today().year:
        raise UserInputError(
            "year must be a valid integer between 1 and current year.")


def reference_id_should_be_unique(value):
    references = get_reference_id()
    if value in references:
        raise UserInputError(
            "reference ID already exists in the database."
        )


def month_check(month):
    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]
    if month:
        should_be_str("month", month)
    if month and (month.lower() not in months):
        raise UserInputError(f"month must be one of: {', '.join(months)}.")


def validate_article(
        reference_id,
        author,
        title,
        journal,
        year,
        volume,
        number,
        pages,
        month,
        note):
    # mandatory fields
    reference_id_should_be_unique(reference_id)
    should_be_str("reference_id", reference_id)
    should_be_str("author", author)
    should_be_str("title", title)
    should_be_str("journal", journal)
    year_check(year)
    should_be_valid_positive_int("volume", volume)

    # optional fields
    for field_name, value in [
        ("volume", volume),
        ("number", number),
        ("pages", pages),
        ("note", note)
    ]:
        if value:
            should_be_str(field_name, value)
    if month:
        month_check(month)


def validate_book(
    reference_id,
    author,
    year,
    title,
    publisher,
    address
):
    # all fields are mandatory
    reference_id_should_be_unique(reference_id)
    should_be_str("reference_id", reference_id)
    should_be_str("author", author)
    year_check(year)
    should_be_str("title", title)
    should_be_str("publisher", publisher)
    should_be_str("address", address)


def validate_inproceedings(
    reference_id,
    author,
    title,
    booktitle,
    year,
    editor,
    volume,
    number,
    series,
    pages,
    address,
    month,
    organization,
    publisher
):
    reference_id_should_be_unique(reference_id)
    should_be_str("reference_id", reference_id)
    should_be_str("author", author)
    should_be_str("title", title)
    should_be_str("booktitle", booktitle)
    should_be_valid_positive_int("volume", volume)
    year_check(year)

    for field_name, value in [
        ("editor", editor),
        ("volume", volume),
        ("number", number),
        ("series", series),
        ("pages", pages),
        ("address", address),
        ("organization", organization),
        ("publisher", publisher),
    ]:
        if value:
            should_be_str(field_name, value)
    if month:
        month_check(month)
