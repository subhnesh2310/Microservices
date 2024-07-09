import os
import sys
from sqlalchemy import engine_from_config, pool
from alembic import context

# Add the path to the root directory of your project
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
print(f"Root path: {root_path}")
sys.path.append(root_path)

# Import SQLAlchemy Base object from pixi_db module
from pixi_db.sqlalchemy_models import Base
from pixi_db.settings import DATABASES

# Use Django database settings
DATABASE_NAME = DATABASES['default']['NAME']
DATABASE_USER = DATABASES['default']['USER']
DATABASE_PASSWORD = DATABASES['default']['PASSWORD']
DATABASE_HOST = 'localhost'  # Service name in docker-compose.yml
DATABASE_PORT = DATABASES['default']['PORT']

# Construct the database URL for SQLAlchemy
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'

# Configure SQLAlchemy engine
config = context.config
config.set_main_option('sqlalchemy.url', DATABASE_URL)

# Bind engine to the Base object
engine = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix='sqlalchemy.',
    poolclass=pool.NullPool
)
Base.metadata.bind = engine

# Function for running migrations online
def run_migrations_online():
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Base.metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Check if Alembic is in offline or online mode and run migrations accordingly
if context.is_offline_mode():
    raise NotImplementedError("Offline mode not supported for Django-based Alembic migrations")
else:
    # Run migrations online
    run_migrations_online()
