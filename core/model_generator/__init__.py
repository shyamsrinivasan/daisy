import sys
from sqlmodel import create_engine, MetaData
from sqlacodegen_v2.generators import SQLModelGenerator, TablesGenerator


def get_engine(db_url):
    return create_engine(db_url)


def get_metadata(engine):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    return metadata


def get_engine_metadata(db_url):
    engine = get_engine(db_url)
    metadata = get_metadata(engine)
    return engine, metadata


def generate_sqlmodels(db_url, file_name):
    engine, metadata = get_engine_metadata(db_url)
    generator = SQLModelGenerator(metadata=metadata, bind=engine, options=[])
    models = generator.generate()    
    with open(file_name, 'w') as sys.stdout:
        print(models)


def generate_sqla_models(db_url, file_name):
    engine, metadata = get_engine_metadata(db_url)
    generator = TablesGenerator(metadata=metadata, bind=engine, options=[])
    models = generator.generate_models()
    with open(file_name, 'w') as sys.stdout:
        print(models)