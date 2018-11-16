#Python 3
import traceback

try:

    def spam():
        bacon()
    def bacon():
        raise Exception('This is the error message')

    spam()

except:
        errorFile = open('errorFile.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was writtenn to errInfo.txt')