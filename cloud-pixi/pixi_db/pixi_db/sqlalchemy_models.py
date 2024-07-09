from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, MetaData, UniqueConstraint, DateTime, func, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import bcrypt
import hashlib
import datetime


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    userid_uuid = Column(String(50), primary_key=True)  # Assuming UUID format
    email_id = Column(String(100), nullable=False, unique=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(64), nullable=False)  # Assuming hashed password (SHA-256)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    role_uuid = Column(Integer, ForeignKey('roles.role_uuid'))
    permission_uuid = Column(String(150), ForeignKey('permissions.permission_uuid'))
    csim_status = Column(String(20))  # Assuming a field for entry list (csim or Active)

    # Define relationship to roles table
    role = relationship('Roles', back_populates='users')

    # Define relationship to permissions table
    permission = relationship('Permissions', back_populates='users')

    def set_password(self, password):
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()


class Roles(Base):
    __tablename__ = 'roles'

    role_uuid = Column(Integer, primary_key=True)
    role_name = Column(String(100), nullable=False, unique=True)
    
    # Define relationship to users table
    users = relationship('Users', back_populates='role')


class Permissions(Base):
    __tablename__ = 'permissions'

    permission_uuid = Column(String(150), primary_key=True)  # Assuming UUID format
    permission_name = Column(String(100), nullable=False, unique=True)
    
    # Define relationship to users table
    users = relationship('Users', back_populates='permission')


class SQLAlchemyConnectNE(Base):
    __tablename__ = 'connectne'

    connect_ne_uuid = Column(String(150), primary_key=True)  # Assuming UUID format
    handle = Column(String(100))
    username = Column(String(100), default="temp")
    password = Column(String(64))  # Assuming hashed password (SHA-256)
    hostname = Column(String(100))
    port = Column(Integer, default=22)
    interface = Column(String(50), default="CLI")
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    connection_status = Column(String(1), default="p")  # 'p' for pending, 'f' for failed

    def set_password(self, password):
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()


class SQLAlchemyDisconnectNE(Base):
    __tablename__ = 'disconnectne'

    disconnect_ne_uuid = Column(String(150), primary_key=True)  # Assuming UUID format
    handle = Column(String(100), default='', nullable=True)
    username = Column(String(100), default="temp")
    password = Column(String(64))  # Assuming hashed password (SHA-256)
    hostname = Column(String(100))
    port = Column(Integer, default=22)
    interface = Column(String(50), default="CLI")
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    disconnect_status = Column(String(1), default="p")  # 'p' for pending, 'f' for failed

    def set_password(self, password):
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()


class TestExecution(Base):
    __tablename__ = 'test_execution'

    execution_uuid = Column(String(50), primary_key=True)
    environment_details = Column(String(255))
    userid_uuid = Column(String(150), ForeignKey('users.userid_uuid'))
    test_suite_uuid = Column(Integer)
    test_suite_name = Column(String(100))
    test_case_uuid = Column(Integer)
    test_case_name = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    executed_at = Column(DateTime)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    time_taken = Column(String(20))
    result = Column(String(20))
    sw_package = Column(String(100))
    logs_path = Column(String(255))

    user = relationship('Users', backref='test_execution')


class TestStepsResults(Base):
    __tablename__ = 'teststeps_results'

    log_id_uuid = Column(String(50), primary_key=True)  # Assuming UUID format
    log_path = Column(String(255))
    execution_uuid = Column(String(50), ForeignKey('test_execution.execution_uuid'))
    test_result_status = Column(String(1))  # 'p' for pending, 'f' for failed
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    test_suite_uuid = Column(String(250))  # ForeignKey('test_execution.test_suite_id') if needed
    userid_uuid = Column(String(50), ForeignKey('users.userid_uuid'))

    # Define relationship to TestExecution table
    execution = relationship('TestExecution', backref='teststeps_results')

    # Define relationship to Users table
    user = relationship('Users', backref='teststeps_results')


class TestExecutionMetrics(Base):
    __tablename__ = 'test_execution_metrics'

    matric_uuid = Column(String(50), primary_key=True)
    execution_uuid = Column(String(50), ForeignKey('test_execution.execution_uuid'))
    execution_table = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    execution_count = Column(Integer)
    each_execution_status = Column(JSON)

    # Define relationship to TestExecution table
    test_execution = relationship('TestExecution', backref='metrics')

    def __repr__(self):
        return f"<TestExecutionMetrics(matric_uuid='{self.matric_uuid}', execution_uuid='{self.execution_uuid}', created_at='{self.created_at}', execution_count='{self.execution_count}')>"


class TestMetadataTable(Base):
    __tablename__ = 'TestMetadata'

    metadata_uuid = Column(String(50), primary_key=True)
    owner = Column(String(255))
    doa = Column(String(20))  # Assuming date format mm/dd/yyyy
    with_tgen = Column(String(3))  # Assuming Yes/No
    status = Column(String(20))
    product = Column(String(50))
    interface = Column(String(50))
    script_id = Column(String(10))
    title = Column(String(255))
    software_version = Column(String(20))
    simulator_compatible = Column(String(3))

    def __repr__(self):
        return f"<Metadata(id={self.id}, title='{self.title}', owner='{self.owner}', doa='{self.doa}')>"


# class SQLAlchemySendRCV(Base):
#     __tablename__ = 'sendrcv'

#     sendRcv_uuid = Column(String(150), primary_key=True)
#     handle = Column(String(100), nullable=False, default="CLI")
#     command = Column(String(500), nullable=True)


# class SQLAlchemyComparePairs(Base):
#     __tablename__ = 'compare_pairs'

#     compare_pair_uuid = Column(String(150), primary_key=True)
#     stash = Column(String(100), nullable=True, default="notStash")
#     compare_input = Column(String(250), nullable=True, default=None)
#     compare_result = Column(String(250), nullable=True, default=None)


# class CPixiUserTable(Base):
#     __tablename__ = 'c_pixi_data_table'

#     uuid = Column(String(150), primary_key=True)  # Assuming UUID format
#     username = Column(String(100), nullable=False, unique=True, index=True)  # Non-nullable, unique, indexed column
#     filename1 = Column(String(255))
#     file1path = Column(String(255))
#     filename2 = Column(String(255))
#     file2path = Column(String(255))


# SQLAlchemy engine creation
DATABASE_NAME = 'Pixi_DB'
DATABASE_USER = 'temproot'
DATABASE_PASSWORD = 'infinera'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'  # default PostgreSQL port

# Construct the database URL for SQLAlchemy
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
engine = create_engine(DATABASE_URL)

# Create tables defined by Base
# Define your MetaData object and reflect existing tables
metadata = MetaData()

# Bind metadata to the engine
metadata.bind = engine

# Reflect existing tables (if needed)

Base.metadata.reflect(bind=engine)

