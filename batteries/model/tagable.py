from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey

from batteries.model.types import Ascii
from sqlalchemy.types import Unicode

# only define a Tag model if the project using Tagable
# doesn't have one. Needed? At least for isolated tests 
# here in batteries
if 'Tag' not in locals() or 'Tag' not in globals():
    from batteries.model import Model
    from batteries.model.hashable import Hashable
    class Tag(Model, Hashable):
        __tablename__ = 'tag'
        __identifiers__ = ('slug', 'name')
        _key = Column('key', Ascii(40), primary_key=True)
        serializable = ('slug', 'name')
        slug = Column(Ascii(40), unique=True, nullable=False)
        name = Column(Unicode(40), nullable=False)


class Tagable(object):
    def _get_subclass_name(self):
        return self.__class__.__name__

    @property
    def tags(self):
        return Tag.query.join('{}_tag'.format(self._get_subclass_name())),
                     collection_class=set)


    # tagging table. How to create when child class is getting defined?

    # index both ways
