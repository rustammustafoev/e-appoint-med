from django.db import DatabaseError, IntegrityError


COMMON_MODEL_EXCEPTIONS = (
    TypeError, ValueError,
    DatabaseError, IntegrityError,
)
