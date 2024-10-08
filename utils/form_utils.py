from flask import flash


def flash_form_errors(form):
    """
    Flash all errors from a form.

    :param form: The form containing errors
    """
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error in {field}: {error}", "error")
