# Parameters
ID_INDEX = 0
EH_INDEX = 1
AGE_INDEX = 2
GENDER_INDEX = 3
SCORES_INDEX = 4
ID_LEGAL_LENGTH = 8
AGE_LEGAL_MAX = 100
AGE_LEGAL_MIN = 10
SCORE_LEGAL_MAX = 10
SCORE_LEGAL_MIN = 1
MAN_BOOL_VAL = True
WOMAN_BOOL_VAL = False
VEGAN_INT_VAL = 0
VEGETARIAN_INT_VAL = 1
OMNIVORE_INT_VAL = 2
QUERY_INT_LENGTH = 10


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

    scores = line_char_params[SCORES_INDEX:]

    identification = line_char_params[ID_INDEX]

    age = line_char_params[AGE_INDEX]

    if check_id(identification) and check_age(age) and check_scores(scores):

        return True

    else:

        return False


# checks the user id
def check_id(identification):

    if len(identification) is not ID_LEGAL_LENGTH or identification.isdigit() is not True:

        return False

    else:

        return True


# checks the user age
def check_age(age):

    if AGE_LEGAL_MAX >= int(age) >= AGE_LEGAL_MIN:

        return True

    else:

        return False


# checks the user age
def check_scores(scores):

    for score in scores:

        if not SCORE_LEGAL_MAX >= int(score) >= SCORE_LEGAL_MIN:

            return False

    return True


def add_line_to_array(line_array, line):

    identification = line.split()[ID_INDEX]

    for current_line in line_array:

        current_line_id = current_line.split()[ID_INDEX]

        if identification == current_line_id:

            line_array.remove(current_line)

    line_array.append(line)

    line_array.sort()


# Returns a new Survey item with the data of a new survey file:
# survey_path: The path to the survey
def scan_survey(survey_path):

    from Survey import SurveyCreateSurvey, SurveyAddPerson, SurveyCreateIntAr, SurveySetIntArIdxVal, SurveyDestoryIntAr

    survey = SurveyCreateSurvey()

    survey_file = open(survey_path, "r")

    # Go through each line.
    for line in survey_file:

        line_char_params = line.split()
        identification = int(line_char_params[ID_INDEX])
        age = int(line_char_params[AGE_INDEX])
        scores = [int(i) for i in line_char_params[SCORES_INDEX:]]
        gender = True if line_char_params[GENDER_INDEX] == "Man" else False

        # send array and details to survey
        score_arr = SurveyCreateIntAr(len(scores))

        for index, score in enumerate(scores):
            SurveySetIntArIdxVal(score_arr, index, score)

        eating_habits = return_eating_habits_int(line_char_params[EH_INDEX])

        SurveyAddPerson(survey, identification, age, gender, eating_habits, score_arr)

        SurveyDestoryIntAr(score_arr)

    return survey


def return_eating_habits_int(eating_habits_char):
    if eating_habits_char == "Vegan":
        eating_habits = VEGAN_INT_VAL
    elif eating_habits_char == "Vegetarian":
        eating_habits = VEGETARIAN_INT_VAL
    else:
        eating_habits = OMNIVORE_INT_VAL

    return eating_habits


# Prints a python list containing the number of votes for each rating of a group according to the arguments
# s: the data of the Survey object
# choc_type: the number of the chocolate (between 0 and 4)
# gender: the gender of the group (string of "Man" or "Woman"
# min_age: the minimum age of the group (a number)
# max_age: the maximum age of the group (a number)
# eating_habits: the eating habits of the group (string of "Omnivore", "Vegan" or "Vegetarian")
def print_info(s, choc_type, gender, min_age, max_age, eating_habits):

    from Survey import SurveyQuerySurvey, SurveyGetIntArIdxVal, SurveyQueryDestroy

    eating_habits_to_transfer = return_eating_habits_int(eating_habits)

    gender_to_transfer = MAN_BOOL_VAL if gender == "Man" else WOMAN_BOOL_VAL

    # get array according to Query
    int_arr = SurveyQuerySurvey(s, choc_type, gender_to_transfer, min_age, max_age, eating_habits_to_transfer)

    output_list = []

    for i in range(QUERY_INT_LENGTH):

        # translate 'c' array to python list
        output_list.insert(i, SurveyGetIntArIdxVal(int_arr, i))

    print(output_list)

    SurveyQueryDestroy(int_arr)


# Clears a Survey object data
# s: the data of the Survey object
def clear_survey(s):

    from Survey import SurveyDestroySurvey

    SurveyDestroySurvey(s)
