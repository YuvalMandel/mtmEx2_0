#!/bin/bash

echo === === HW2 Test Script === === 
echo This script will compile your code using the commands as given in the PDF.
echo Then it will run tests 1 and 2 by the course staff, and an additional test.
echo Good Luck!
read -p "Press enter to start: "
echo === === 

echo === Compiling...
swig -python Survey.i 
gcc -std=c99 -fPIC -c Survey_wrap.c -I/usr/local/include/python3.6m 
ld -shared Survey.o Survey_wrap.o -L/usr/local/include/python3.6m/ -o _Survey.so

echo === Running tests given by course staff...
python3.6 main1.py > out1 
python3.6 main2.py > out2 
diff exp1 out1 
diff exp2 out2

echo === Running Guy\'s test for file correction...
python3.6 correct_guy.py > survey_guy_corrected
diff survey_guy_corrected exp_survey_guy_corrected

echo === Running Guy\'s test for histograms...
python3.6 main_guy.py > out_guy
diff out_guy exp_guy

echo === === === === 
echo All Done! If diff didn\'t shout at you, congratulations!