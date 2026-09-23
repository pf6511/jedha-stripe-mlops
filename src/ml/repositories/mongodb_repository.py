class MongoDbRepository:

    def update_field(
        self,
        collection: str,
        document_id: str,
        field_name: str,
        field_value: dict,
    ) -> None:
        """
        Update field in a document.
        """
        ...