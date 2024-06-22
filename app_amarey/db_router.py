class AmareyDBRouter:
    """
    A router to control all database operations on models in the
    amarey application.
    """

    route_app_labels = {'app_amarey'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read amarey models go to amarey_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'amarey_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write amarey models go to amarey_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'amarey_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the amarey app is involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the amarey app's models get created on the right database.
        """
        if app_label in self.route_app_labels:
            return db == 'amarey_db'
        return None
