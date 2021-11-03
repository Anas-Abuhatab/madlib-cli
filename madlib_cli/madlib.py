
welcome_massage = """
#######################################
    Welcome to the Madlids Creator
#######################################
"""
def welcome():
    print(welcome_massage)

def read_template(path_text):
    try:
        file  = open(path_text)
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        raise FileNotFoundError("Flie not found")
   

def parse_template(text):
    word = ""
    parsed_word = []
    parsed_text = ""
    state = 0 # outside of curly braces
    for ch in text:
        if ch == "{":
            state = 1
            parsed_text =parsed_text + ch
        elif ch == "}":
            state = 0
            parsed_text =parsed_text +ch
            parsed_word.append(word)
            word = ""
        elif state == 0:
            parsed_text =parsed_text +ch
        else:
            word =word + ch
    return parsed_text,tuple(parsed_word)

def merge(text,inputs):

    new_text =  text.format(*inputs)

    with open("madlib_cli/assets/dark_and_stormy_night_template_output.txt","w") as file :
        file.write(new_text)
    return new_text

def start(text ,inputs):
    welcome()
    input_new_list = []
    for i in inputs:
        inputs_user = input(f"inter an {i} ")
        input_new_list.append(inputs_user)
    return merge(text,input_new_list)

   

if __name__=="__main__":
    read_text = read_template("madlib_cli/assets/dark_and_stormy_night_template.txt")
    text,excluded = parse_template(read_text)
    print(start(text,excluded))

