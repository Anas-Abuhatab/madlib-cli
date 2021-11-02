
welcome_massage = """
#######################################
    Welcome to the Madlids Creator
#######################################
"""

def read_template(path):
    try:
        file  = open(path)
        content = file.read()
        file.close()
    except FileNotFoundError:
        contant = ("Flie not found")
    finally:
        return (content)


# def parse_template():



