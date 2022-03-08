class MailList:
    list_id = None
    list_name = None
    folder_name = None
    created = None
    updated = None

    def __init__(self, data_dict: dict):
        self.list_id = data_dict.get('list_id', None)
        self.list_name = data_dict.get('list_name', None)
        self.folder_name = data_dict.get('folder_name', None)
        self.created = data_dict.get('created', None)
        self.updated = data_dict.get('updated', None)

    @classmethod
    def from_dict(cls, json_dict):
        return cls(json_dict)
