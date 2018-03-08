from .auth import (IndexView, StudentRegisterView, LoginView, HomeworkListPage)
from .info_detail import (InfoDetailBase, StudentInfoDetail)
from .info_update import (StudentInfoUpdate, )

__all__ = [
    'IndexView', 'StudentRegisterView', 'LoginView', 'InfoDetailBase',
    'StudentInfoDetail', 'StudentInfoUpdate', 'HomeworkListPage'
]
