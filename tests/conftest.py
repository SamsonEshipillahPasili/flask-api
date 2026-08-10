import pytest
from app.app_factory import create_app
from app.extensions import db
from app.schemas import TodoCreate
import faker

fake = faker.Faker()

@pytest.fixture
def app():
    app = create_app(config_object='app.config.TestingConfig')

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(autouse=True)
def app_context(app):
    with app.app_context():
        yield

@pytest.fixture
def new_todo_create_schema():
    yield TodoCreate(
        title=fake.sentence(),
        description=fake.paragraph(),
        completed=False,
    )
