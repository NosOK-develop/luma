import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

SqlAlchemyBase = orm.declarative_base()
__factory = None


def global_init(db_url):  # Изменили параметр с db_file на db_url
    global __factory

    if __factory:
        return

    if not db_url or not db_url.strip():
        raise Exception('Необходимо указать строку подключения к базе данных.')

    # Исправляем формат строки для SQLAlchemy + PostgreSQL драйвера psycopg2
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql+psycopg2://", 1)
    elif db_url.startswith("postgresql://"):
        db_url = db_url.replace("postgresql://", "postgresql+psycopg2://", 1)

    # Убрали sqlite-специфичные параметры. Оставляем чистый engine.
    engine = sa.create_engine(db_url, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models
    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
