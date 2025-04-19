from django.core.exceptions import ValidationError

def validate_length(value):
    valid_lengths = [5, 6, 10]
    if len(value) not in valid_lengths:
        raise ValidationError(
            f'Field length must be one of the following lengths: {", ".join(map(str, valid_lengths))}.'
        )

def gender_validator(value):
    valid_genders = [0,1,2, None] 
    if value not in valid_genders:
        raise ValidationError(
            f'gendercode value must be one of the following number: {", ".join(map(str, valid_genders))}.'
        )
def age_validator(value):
    min_age = 1
    max_age = 100

    if value < min_age or value > max_age:
        raise ValidationError(
            f'age value must be betwwen 1 to 100 not {value}'
        )

def postal_code_validator(postal_code):
    """
    Validate if the input is a 10-digit postal code.

    Args:
    postal_code (str): The postal code to validate.

    Returns:
    bool: True if valid, False otherwise.
    """
    if not postal_code.isdigit():
        raise ValidationError(
            f'postal code should be digit, {postal_code}'
        )
    
    if not  len(postal_code) == 10:
        raise ValidationError(
            f'maximum lenfth for postal code is 10, {postal_code}'
        )
    