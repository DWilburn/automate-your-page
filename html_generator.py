def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept
        

TEST_TEXT = """TITLE: Programming Language
DESCRIPTION: Programming languages are used by programmers to tell a computer what to do. Python is one example of a programming language.
TITLE: Python
DESCRIPTION: When you write Python code and "Run" the code, a Python Interpreter converts the written code into a set of instructions that the computer can understand and execute.
TITLE: Python Expressions
DESCRIPTION: In Python an "expression" is a legal Python statement. For example: print 2 + 2 is a valid expression, but print 2 + (without a number at the end) is not.
TITLE: What is a variable in Python?
DESCRIPTION: Variables give programmers a way to give names to values. If my_variable is a variable with a value of 2, then the following code would print out 0:
print my_variable - my_variable """


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(TEST_TEXT)