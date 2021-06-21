from mailman.interfaces.domain import IDomainManager
from zope.component import getUtility

def init_dev():
    """
        Initializes a basic dev install of Mailman.

        This does the following:

        - Add example.com domain if it's missing
    """
    domain_manager = getUtility(IDomainManager)

    if not domain_manager.get('example.com', None):
        print('Adding example domain')
        domain_manager.add('example.com')