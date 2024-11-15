class inproceedings:
    def __init__(
        self,
        id,
        created_at,
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
        publisher,
    ):
        self.id = id
        self.created_at = created_at
        self.author = author
        self.title = title
        self.booktitle = booktitle
        self.year = year
        self.editor = editor
        self.volume = volume
        self.number = number
        self.series = series
        self.pages = pages
        self.address = address
        self.month = month
        self.organization = organization
        self.publisher = publisher

    def __str__(self):
        return f"{self.title}, {self.author}"
