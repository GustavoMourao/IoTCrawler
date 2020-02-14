from dotenv import load_dotenv
import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    """
    Class that implements connection with database
    """
    def __init__(self):
        """
        Create engine and new database connection.
        """
        logging.basicConfig(
            filename='LogDatabaseEvents.log',
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.log = logging.getLogger('LogDatabaseEvents.log')

        load_dotenv()
        try:
            engine_name = os.getenv('DB_TYPE') + \
                '://' + os.getenv('DB_USER') + \
                ':' + os.getenv('DB_PASS') + \
                '@' + os.getenv('DB_HOST') + \
                ':' + os.getenv('DB_PORT') + \
                '/' + os.getenv('DB_NAME')

            self.engine = create_engine(engine_name)
            self.session = sessionmaker(bind=self.engine)
            self.base = declarative_base()

        except Exception as ex:
            self.log.warning(ex)

    def open_session(self):
        """
        Create and return new db session object.
        """
        self.base.metadata.create_all(self.engine)
        return self.session()

    def insert(self, bulkdata):
        """
        Inserts a bulk data into the database.

        Args:
        ---------
            bulkdata: bulk of data to be inserted on database
        """
        new_session = self.open_session()
        new_session.bulk_save_objects(bulkdata)
        new_session.commit()

    def read(self, table):
        """
        Read entire data and relationship between tables.

        Args:
        ---------
            table: name of table on database

        Returns:
        ---------
            values: values storage on database

        Obs:
        ---------
            Its recomended to implement a method with filter parameters
        """
        new_session = self.open_session()
        values = new_session.query(table).all()
        return values
