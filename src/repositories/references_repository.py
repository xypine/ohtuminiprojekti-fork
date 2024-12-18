from config import db
from sqlalchemy import text

from entities.references import References


def get_references():
    result = db.session.execute(
        text(
            """
            SELECT id, reference_id, reference_type, created_at, title, author, year, publisher, 
                   address, journal, volume, number, pages, month, note, booktitle, editor, 
                   series, organization
            FROM reference
        """
        )
    )
    references_result = result.fetchall()
    return [
        References(
            id=reference.id,
            reference_id=reference.reference_id,
            reference_type=reference.reference_type,
            created_at=reference.created_at,
            author=reference.author,
            title=reference.title,
            booktitle=reference.booktitle,
            year=reference.year,
            editor=reference.editor,
            volume=reference.volume,
            number=reference.number,
            series=reference.series,
            pages=reference.pages,
            address=reference.address,
            month=reference.month,
            organization=reference.organization,
            publisher=reference.publisher,
            journal=reference.journal,
            note=reference.note,
        )
        for reference in references_result
    ]


def create_reference(
    reference_id,
    reference_type,
    title,
    author,
    year,
    booktitle=None,
    editor=None,
    volume=None,
    number=None,
    series=None,
    pages=None,
    address=None,
    journal=None,
    month=None,
    note=None,
    organization=None,
    publisher=None,
):

    sql = text(
        """INSERT INTO reference (reference_id, reference_type, title,
        author, year, publisher, address, journal, volume, number, pages,
        month, note, booktitle, editor, series, organization) 
        VALUES (:reference_id, :reference_type, :title, :author, :year,
        :publisher, :address, :journal, :volume, :number, :pages, :month,
        :note, :booktitle, :editor, :series, :organization)"""
    )
    db.session.execute(
        sql,
        {
            "reference_id": reference_id,
            "reference_type": reference_type,
            "title": title,
            "author": author,
            "year": int(year),
            "publisher": publisher,
            "address": address,
            "journal": journal,
            "volume": volume,
            "number": number,
            "pages": pages,
            "month": month,
            "note": note,
            "booktitle": booktitle,
            "editor": editor,
            "series": series,
            "organization": organization,
        },
    )
    db.session.commit()


def get_reference_id():
    result = db.session.execute(text("SELECT reference_id FROM reference"))
    references = result.fetchall()
    return [item[0] for item in references]

def delete_reference(reference):
    sql = text("""
        DELETE FROM Reference
        WHERE id = :reference_id
    """)
    db.session.execute(sql, {"reference_id":reference})
    db.session.commit()
