import taskManager as tM
import eel


eel.init('front', allowed_extensions=['.js', '.html'])

@eel.expose                         # Expose this functiocompagnon/stats/n to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('index.html')             # Start (this blocks and enters loop)

