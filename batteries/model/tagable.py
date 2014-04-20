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
    import pdb; pdb.set_trace()
    tags = relationship('Tag', secondary='{}_tag'.format(),
                        collection_class=set)

    # object name, lowercase'd, underscored
    

    # tagging table

    # index both ways
