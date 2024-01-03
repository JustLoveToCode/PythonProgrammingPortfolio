# Function with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    first = f_name.title()
    last = l_name.title()
    return f"{first} {last}"


print(format_name(input('What is your first name?'),
                  input('What is your last name?')))
