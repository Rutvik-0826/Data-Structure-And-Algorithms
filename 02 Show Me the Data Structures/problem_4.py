class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not isinstance(group, Group):
        return False
    if user in group.get_users():
        return True
    if not group.get_groups():
        return False

    for group in group.get_groups():
        return is_user_in_group(user, group)


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# =====================================================================
# TESTS
# =====================================================================
root = Group('root')
root.add_user('john')
assert is_user_in_group('john', root)
assert not is_user_in_group('jane', root)

company = Group('root')
department = Group('marketing')
department.add_user('john')
company.add_group(department)
assert is_user_in_group('john', company)
assert not is_user_in_group('jane', company)

# Non-existent group
assert not is_user_in_group('john', None)
