#!  python3
#mad_libs_2.0.py is a madlib game.

import pyinputplus as pyip
import re
import os
from pathlib import Path as p
import pyperclip as p

MADLIB = []

MAD_TEXT = """The ADJECTIVE panda walked to the NOUN and then VERB-ENDING-WITH: '-ED'. A nearby NOUN was
unaffected by these events. However, upon VERB-ENDING-WITH: '-ING' in the NOUN, the panda decided it
was time to go VERB.
"""

NEW_MAD_TEXT = ''

search_keywords = [r'\bNOUN(?=\s|\.|\,)', r'\bADJECTIVE(?=\s|\.|\,)', r'\bVERB(?=\s|\.|\,)',
r'\bADVERB(?=\s|\.|\,)', r'\bVERB-ENDING-WITH: \'-ING\'(?=\s|\.|\,)', r'\bADVERB-ENDING-WITH: \'-LY\'(?=\s|\.|\,)',
r'\bVERB-ENDING-WITH: \'-ED\'(?=\s|\.|\,)']

TOT_KW_NUM = 0
NUM_RUN = 0

def update_text(kw_index, key_regx, user_in):
    if kw_index == 0:
            update_mad = re.sub(key_regx, user_in, MAD_TEXT, 1)
    else:
        update_mad = re.sub(key_regx, user_in, NEW_MAD_TEXT, 1)
    return update_mad

for i, regx in enumerate(search_keywords):
    found_keyword = re.findall(regx, MAD_TEXT, re.DOTALL)

    for j in range(len(found_keyword)):
        pr_1 = f'Please enter a {found_keyword[j]}. '
        pr_2 = f'Please enter an {found_keyword[j]}. '
        pr_3 = f'Please enter a {found_keyword[j]} ending in \"ing\". '
        pr_4 = f'Please enter an {found_keyword[j]} ending in \"ly\". '

        if found_keyword[j] == 'NOUN' or found_keyword[j] == 'VERB':
            user_input = pyip.inputStr(prompt=pr_1,
                                        blockRegexes=[r'\d+']).lower()
            NEW_MAD_TEXT = update_text(NUM_RUN, regx, user_input)

        if found_keyword[j] == 'ADJECTIVE' or found_keyword[j] == 'ADVERB':
            user_input = pyip.inputStr(prompt=pr_2,
                                        blockRegexes=[r'\d+']).lower()
            NEW_MAD_TEXT = update_text(NUM_RUN, regx, user_input)

        if found_keyword[j] == "VERB-ENDING-WITH: '-ING'":
            user_input = pyip.inputStr(prompt=pr_3,
                                        blockRegexes=[r'\d+'],
                                        allowRegexes=[r'\w+ing']).lower()
            NEW_MAD_TEXT = update_text(NUM_RUN, regx, user_input)

        if found_keyword[j] == "ADVERB-ENDING-WITH: '-LY'":
            user_input = pyip.inputStr(prompt=pr_4,
                                        blockRegexes=[r'\d+'],
                                        allowRegexes=[r'\w+ly']).lower()
            NEW_MAD_TEXT = update_text(NUM_RUN, regx, user_input)
        if found_keyword[j] == "VERB-ENDING-WITH: '-ED'":
            user_input = pyip.inputStr(prompt=pr_4,
                                        blockRegexes=[r'\d+'],
                                        allowRegexes=[r'\w+ed']).lower()
            NEW_MAD_TEXT = update_text(NUM_RUN, regx, user_input)
        NUM_RUN += 1

print(NEW_MAD_TEXT)
p.copy(NEW_MAD_TEXT)
print("Press CTRL-V to paste your mad-lib anywhere you like!")

