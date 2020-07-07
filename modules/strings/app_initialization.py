init = '"""\nFile: {}.py\nMain application entry point\n"""\n' \
       'from src.utilities.configuration import configuration\n' \
       'from src.utilities.logger import *\n' \
       'from src import app\n' \
       'import traceback\n\n\n' \
       '# main program definition\n' \
       'if __name__ == \'__main__\':\n' \
       '    try:\n' \
       '        HOST = \n' \
       '        PORT = \n' \
       '        DEBUG = \n' \
       '        app.run(host=HOST, port=PORT, debug=DEBUG)\n' \
       '    except Exception as e:\n' \
       '        log_fatal(message=str(e), description=traceback.format_exc())\n'
