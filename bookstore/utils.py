from rest_framework.utils.model_meta import get_field_info


def get_modal_fields(modal):
    data = get_field_info(modal).fields
    fields = [key for i, (key, value) in enumerate(data.items())]
    data = get_field_info(modal).relations
    [fields.append(key) for i, (key, value) in enumerate(data.items())]
    return fields
