#BEWARE OF TAB SPACING WHILE WRITING IN PYCHARM(4 SPACES)

.PHONY: help messages ahoj mypy lint test venv test t lint_f mypy_f all_f clear_console

# CONSTANTS -----------------------------------------

include make_config.mk

# UTILS ---------------------------------------------
hello:
	@echo "Hello World!!"

# FILE MAKES -------------------------------------

.DEFAULT: mypy_f
mypy_f:
	@echo "# MYPY SOURCE FILE##";\
	echo "   - File Name: $(FILE_NAME)";\
	echo "   - File Folder: $(FILE_FOLDER)";\
	echo "###################################################################################################";\
	mypy --strict $(FILE_FOLDER)/$(FILE_NAME).py --config-file mypy.ini;\
	echo "# MYPY TEST FILE ###################################################################################";\
	echo "   - File Name: $(FILE_NAME)";\
	echo "   - File Folder: $(FILE_FOLDER)";\
	echo "###################################################################################################";\
	mypy --strict tests/t_$(FILE_FOLDER)/test_$(FILE_NAME).py --config-file mypy.ini;\

.DEFAULT: lint_f
lint_f:
	@echo "# LINT SOURCE FILE ################################################################################";\
	echo "   - File Name: $(FILE_NAME)";\
	echo "   - File Folder: $(FILE_FOLDER)";\
	echo "###################################################################################################";\
	pylint $(FILE_FOLDER)/$(FILE_NAME).py --rcfile .pylintrc;\
	echo "# LINT TEST FILE ###################################################################################";\
		echo "   - File Name: $(FILE_NAME)";\
	echo "   - File Folder: $(FILE_FOLDER)";\
	echo "###################################################################################################";\
	pylint tests/t_$(FILE_FOLDER)/test_$(FILE_NAME).py --rcfile .pylintrc;\

.DEFAULT: test_f
test_f:
	@echo "# PYTEST AND DOCTEST ##############################################################################";\
	echo "   - File Name: $(FILE_NAME)";\
	echo "   - File Folder: $(FILE_FOLDER)";\
	echo "###################################################################################################";\
	python -m pytest tests/t_$(FILE_FOLDER)/test_$(FILE_NAME).py;\
	python -m pytest tests/t_$(FILE_FOLDER)/test_$(FILE_NAME).txt;\

all_f_no_clear_console:  mypy_f lint_f test_f

.DEFAULT: all_f
all_f: clear_console all_f_no_clear_console

# GLOBAL CODE MAKES EXCEPT NOTEBOOKS -----------------------------------------------------------------------------------

mypy_no_clear_console:
	@echo "###################################################################################################";\
	echo "# TYPE CHECKING IN SRC PIPELINE AND TESTS FOLDER ##################################################";\
	echo "###################################################################################################";\
	mypy --strict src/Utils tests --config-file mypy.ini;\

.DEVAULT: mypy
mypy: clear_console mypy_no_clear_console

lint_no_clear_console:
	@echo "###################################################################################################";\
	echo "# LINTING ALL FILES IN SRC PIPELINE AND TESTS FOLDER ##############################################";\
	pylint src --rcfile .pylintrc;\

.DEFAULT: lint
lint: lint_no_clear_console

lint_dup_no_clear_console:
	@echo "###################################################################################################";\
	echo "# LINTING ALL FILES IN SRC PIPELINE AND TESTS FOLDER, CHECK DUPLICITIES ###########################";\
	echo "###################################################################################################";\
	pylint src test Data pipelines tests --rcfile .pylintrc_dup;\

lint_dup: lint_dup_no_clear_console

test_no_clear_console:
	@echo "###################################################################################################";\
	echo "# PYTEST AND DOCTEST FOR ALL FILES ################################################################";\
	echo "###################################################################################################";\
	echo "";\
	echo "";\
	python -m pytest --ignore=tests/t_Utils/test_Cronus.py;\

.DEFAULT: test
test: test_no_clear_console

#  TEST COVERAGE -----------------------------------------------------------------------------------

cover:
	@echo "##################################################################################################";\
	echo "# PYTEST COVERAGE STATISTICS FOR ALL TEST FILES & REPORT GENERATION IN HTML FORMAT#################";\
	echo "# FIND YOUR REPORT IN HTML FORMAT IN YOUR DIRECTORY INSIDE THE FOLDER coverage#####################";\
	echo "###################################################################################################";\
	echo "";\
	echo "";\
	pytest --cov-report html:coverage --cov-branch --cov=tests

.DEFAULT: coverage
coverage: cover

log_coverage:
	@echo "###################################################################################################";\
	echo "# TOTAL COVERAGE RATIO WILL BE BACKLOGGED INTO coverage_log.csv FILE###############################";\
	echo "###################################################################################################"
ifdef comment
	@python ./src/Utils/CoverageLogger.py $(comment)
else
	python ./src/Utils/CoverageLogger.py
endif
	@echo "# TOTAL COVERAGE RATIO IS BACKLOGGED INTO coverage_log.csv FILE####################################"

.DEFAULT: log_cov
log_cov: log_coverage

all: mypy_no_clear_console lint_no_clear_console test_no_clear_console

# FOR BENCHMARKING -----------------------------------------------------------------------------------------------------

cronus_test:
	@echo "######";\
	echo "# BENCHMARK #######################################################################################";\
	echo "###################################################################################################";\
	echo "";\
	echo "Default benchmarking parameters:";\
	echo "    - Minimum running time per test = 0.000005";\
    echo "    - Maximum running time per test = 1.0";\
    echo "    - Minimum number of rounds per test = 10";\
    echo "    - Warm up run to calibrate the benchmarker = True";\
    echo "    - Number of warm up iterations = 10000";\
	echo "";\
	echo "";\
	python -m pytest tests/t_Utils/test_Cronus.py;\

.DEFAULT: cronus
cronus: cronus_test

#FOR DATA UPDATE AND ARCHIVING
#FIX HERE##########################
archive:
	@echo "Archive is being done.";\
	python -m src/Utils/Saver.py;\
	echo "Archive Done!"
.DEFAULT: archive
#FIX HERE##########################


# FOR FIXING -----------------------------------------------------------------------------------------------------------

#activate virtual environment
act_venv:
	@echo "Archive is being done.";\
	source venv/bin/activate
	echo "Archive Done!"
.DEFAULT: act_venv



#Create virtual environment
make_venv:
	@echo "Virtual environment is being created.";\
	python -m venv venv2 --prompt setup.py;\
	echo "Done";\

#venv/bin/activate: requirements.txt
#	test -d .venv || virtualenv .venv
#	. .venv/Scripts/activate; pip install -r requirements.txt
#	. .venv/Scripts/activate


# python -m venv venv --promt tasks_proj 


#.DEFAULT: t
#t:#
#	touch .venv/Scripts/activate
#	activate

# TESTS --------------------------------------------------------------------------------------

messages:
	$(info Info message)
	# $(warning Warning message)
	# $(error Error message)
	$(info Info message)

.DEFAULT: help
help:
	$(info ******HELP*******)
	$(info     Please fill in help)
	