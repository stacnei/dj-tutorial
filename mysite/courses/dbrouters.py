from courses.models import Courses

class CoursesRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'courses':
            return 'courses_db'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'courses':
            return 'courses_db'
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'courses':
            return db == 'courses_db'
        return None
