from .button_click_job import ButtonClickJob
from .job import Job
from .navigate_job import NavigateJob
from .select_job import SelectElementJob
from .type_input_job import TypeInputMaskJob

from pathlib import Path
if __name__ == '__main__':
    print('Running')
else:
    print('Importing', Path(__file__).resolve())
