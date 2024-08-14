from abc import ABC, abstractmethod  # Importing Abstract Base Class and abstractmethod for creating abstract classes

# Abstract Product
class Document(ABC):
    @abstractmethod
    def create(self):
        # Abstract method that must be implemented by all subclasses
        pass

# Concrete Products
class WordDocument(Document):
    def create(self):
        # Implementation of the create method for Word documents
        return "Word document created."

class PDFDocument(Document):
    def create(self):
        # Implementation of the create method for PDF documents
        return "PDF document created."

class ExcelDocument(Document):
    def create(self):
        # Implementation of the create method for Excel documents
        return "Excel document created."

# Factory
class DocumentFactory:
    @staticmethod
    def get_document(doc_type):
        # Static method to get the appropriate document type based on the input string
        if doc_type == "Word":
            # If the document type is 'Word', return an instance of WordDocument
            return WordDocument()
        elif doc_type == "PDF":
            # If the document type is 'PDF', return an instance of PDFDocument
            return PDFDocument()
        elif doc_type == "Excel":
            # If the document type is 'Excel', return an instance of ExcelDocument
            return ExcelDocument()
        else:
            # If an unknown document type is provided, raise an error
            raise ValueError(f"Unknown document type: {doc_type}")

if __name__ == "__main__":
    # Usage
    factory = DocumentFactory()  # Create an instance of DocumentFactory

    doc = factory.get_document("PDF")  # Get a PDF document instance from the factory
    print(doc.create())  # Output: PDF document created.

    doc = factory.get_document("Word")  # Get a Word document instance from the factory
    print(doc.create())  # Output: Word document created.
