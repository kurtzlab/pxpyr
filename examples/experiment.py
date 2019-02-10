'''
Experiment
	press 'escape' to escape the experiment
'''

## Python Standard Library
import sys
import os
import datetime
import time

## external dependencies
from psychopy import visual

## Internal Dependencies
sys.path.append(os.path.abspath(os.path.join(__file__, '../../')))
import utils
from events import initializer, instructions, forced_choice_classification




##--------------------------------------------------
## SETUP
experiment_time = '-'.join([str(d) for d in datetime.datetime.now().timetuple()][:6])

initial_info = initializer.run(conditions=[1,2])

# Define Subject Dictionary (this is where we'll store all the information about the subject)
subject = {
	'id': str(initial_info[0]),
	'condition': int(initial_info[1]),
	'datafile_path': os.path.join('./data.csv')
}

win = visual.Window(fullscr = True, units = 'pix', color = [1,1,1])



##--------------------------------------------------
## RUN EXPERIMENT
##__init instructions
instructions.run(
	window = win,
    text_file = './materials/train_instructions.txt',
    continue_option = 'click',
)


##__train phase
forced_choice_classification.run(
	['./materials/stim1.png', './materials/stim2.png'],
	labels = ['A', 'B'],
	stim_position = [0,100],

	supervised = True,
	randomize_presentation = True,
	num_blocks = 5,

	window = win,
	experiment_id = 'example',
	subject_info = subject,
	save_data = True,
)


##__ test instructions
instructions.run(
	window = win,
    text_file = './materials/test_instructions.txt',
    continue_option = 'click',
)


##__test phase
forced_choice_classification.run(
	['./materials/stim1.png', './materials/stim2.png'],
	labels = ['A', 'B'],
	stim_position = [0,100],

	supervised = False,
	randomize_presentation = True,
	num_blocks = 1,

	window = win,
	experiment_id = 'example',
	subject_info = subject,
	save_data = True,
)




