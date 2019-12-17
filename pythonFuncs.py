# Filters a survey and prints to screen the corrected answers:
# old_survey_path: The path to the unfiltered survey
def correct_myfile(old_survey_path):
    # Open a file
    old_survey_file = open(old_survey_path, "r")

    good_lines = []

    # Go through each line.
    for line in old_survey_file:

        # If the data is good, we will add it to the array.
        if check_good_line(line):

            add_line_to_array(good_lines, line)

    # print our array.
    for line in good_lines:
        print(line[:-1])


# Checks If the line is good.
def check_good_line(line):

    line_char_params = line.split()

    scores = line_char_params[4:]

    id = line_char_params[0]

    age = line_char_params[2]

    if check_id(id) and check_age(age) and check_scores(scores):

        return True

    else:

        return False


# checks the user id
def check_id(id):

    if len(id) is not 8 or id.isdigit() is not True:

        return False

    else:

        return True


# checks the user age
def check_age(age):

    if 100 >= int(age) >= 10:

        return True

    else:

        return False


# checks the user age
def check_scores(scores):

    for score in scores:

        if not 10 >= int(score) >= 1:

            return False

    return True


def add_line_to_array(line_array, line):

    id = line.split()[0]

    for current_line in line_array:

        current_line_id = current_line.split()[0]

        if id == current_line_id:

            line_array.remove(current_line)

    line_array.append(line)

    line_array.sort()


# Returns a new Survey item with the data of a new survey file:
# survey_path: The path to the survey
def scan_survey(survey_path):

    from Survey import SurveyCreateSurvey, SurveyAddPerson

    Survey = SurveyCreateSurvey()

    survey_file = open(survey_path, "r")

    # Go through each line.
    for line in survey_file:

        line_char_params = line.split()

        id = int(line_char_params[0])

        age = int(line_char_params[2])

        print("line char params:", line_char_params)

        scores = [int(i) for i in line_char_params[4:]]

        gender = True if line_char_params[3] == "Man" else False

        if line_char_params[1] == "Vegan":
            eating_habits = 0
        elif line_char_params[1] == "Vegaterian":
            eating_habits = 1
        else:
            eating_habits = 2

        print("scores", scores)

        SurveyAddPerson(Survey,
                        id,
                        age,
                        gender,
                        eating_habits,
                        scores)

    return Survey


# Prints a python list containing the number of votes for each rating of a group according to the arguments
# s: the data of the Survey object
# choc_type: the number of the chocolate (between 0 and 4)
# gender: the gender of the group (string of "Man" or "Woman"
# min_age: the minimum age of the group (a number)
# max_age: the maximum age of the group (a number)
# eating_habits: the eating habits of the group (string of "Omnivore", "Vegan" or "Vegetarian")
def print_info(s, choc_type, gender, min_age, max_age, eating_habits):
    # TODO
    pass


# Clears a Survey object data
# s: the data of the Survey object
def clear_survey(s):
    # TODO
    pass
