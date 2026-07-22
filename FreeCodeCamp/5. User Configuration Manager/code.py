def add_setting(settings, tuple_setting):
    tuple_key = tuple_setting[0].lower()
    tuple_value = tuple_setting[1].lower()

    if tuple_key in settings: 
        return f"Setting '{tuple_key}' already exists! Cannot add a new setting with this name."
    else:
        settings.update({tuple_key:tuple_value})
        return f"Setting '{tuple_key}' added with value '{tuple_value}' successfully!"

def update_setting(settings, tuple_setting):
    tuple_key = tuple_setting[0].lower()
    tuple_value = tuple_setting[1].lower()
    if tuple_key in settings:
        settings.update({tuple_key:tuple_value})
        return f"Setting '{tuple_key}' updated to '{tuple_value}' successfully!"
    else:
        return f"Setting '{tuple_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, tuple_key):
    tuple_key = tuple_key.lower()
    if tuple_key in settings:
        settings.pop(tuple_key)
        return f"Setting '{tuple_key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings (settings):
    if not settings.items():
        return 'No settings available.'
    else:
        setting_str = 'Current User Settings:\n'

        for key_setting, value_settig in settings.items():
            setting_str += f"{key_setting.capitalize()}: {value_settig}\n"
        
        return setting_str

test_settings = {
}

setting_1 = ('theme','light') #tuple containing
setting_2 = ('THEME','dark') #tuple containing
setting_3 = ('notifications','enabled') #tuple containing
setting_4 = ('volume','high') #tuple containing 


print(add_setting(test_settings, setting_2))
print(update_setting(test_settings, setting_1))
print(update_setting(test_settings, setting_3))
print(delete_setting(test_settings, 'cv'))
print(view_settings(test_settings))