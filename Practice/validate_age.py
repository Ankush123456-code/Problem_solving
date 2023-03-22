def validateAge(age):
    if age < 0:
        raise ValueError("Age must be greater than 0")
    return age
