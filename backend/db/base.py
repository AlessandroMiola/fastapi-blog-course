# make alembic aware of other models (not being the Base one) as well
from db.base_class import Base
from db.models.user import User
from db.models.blog import Blog
