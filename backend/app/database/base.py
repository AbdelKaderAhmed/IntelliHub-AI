"""
IntelliHub AI - Declarative Base Class Configuration
Dynamically registers domain entities for transactional reflection.
"""
from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    """
    Architectural base containing dynamic table naming mechanisms and common structural abstractions.
    """
    @declared_attr
    def __tablename__(cls) -> str:
        # Generates snake_case names implicitly from class layouts
        return cls.__name__.lower()