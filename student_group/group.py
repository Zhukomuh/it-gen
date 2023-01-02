"""class for add or del students to students group and output inform about group"""


class Group:
    """create group object with 'group_name' param"""
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.group_members = []

    def add_student(self, student):
        """method for add students in to group"""
        if len(self.group_members) >= 10:
            raise Exception('Group is already full')
        if student in self.group_members:
            raise Exception('Student is already in a group')
        self.group_members.append(student)

    def del_student(self, student):
        """method for del students from the group"""
        if student not in self.group_members:
            raise Exception('Student is not in a group')
        self.group_members.remove(student)

    def __str__(self):
        """reformat __str__ method for better output inform about object"""
        return f'{self.group_name}: ' + ','.join(map(str, self.group_members))
