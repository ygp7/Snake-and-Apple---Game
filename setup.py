import cx_Freeze

executables = [cx_Freeze.Executable("snakegame.py")]

cx_Freeze.setup(
    name = "SNAKESSS",
    options = {"build_exe":{"packages":["pygame"],"include_files":["chhotuapple.png","snakehead.png"]}},

    description = "First game ^_^ Soo happy",
    executables = executables
)
