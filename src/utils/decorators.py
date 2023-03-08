def skip_nones_in_kwargs(func):
    def _(*args, **kwargs):
        keys_to_delete = []
        for key, val in kwargs.items():
            if val is None:
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del kwargs[key]

        return func(*args, **kwargs)

    return _
