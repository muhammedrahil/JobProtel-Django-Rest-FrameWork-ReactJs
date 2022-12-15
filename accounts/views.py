# from django.shortcuts import render

# # Create your views here.
#   print(request)
#   print(request.META)
#   print(request.META.get('HTTP_X_FORWARDED_FOR'))
#   print(request.META.get('REMOTE_ADDR'))

# <rest_framework.request.Request: POST '/api/accounts/registration/'>
# {'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\best\\AppData\\Roaming', 'CHROME_CRASHPAD_PIPE_NAME': 
#   '\\\\.\\pipe\\LOCAL\\crashpad_16980_MBBHPPVRBZBWMDZW', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 
#   'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 
#   'COMPUTERNAME': 'RAHIL-759297813', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA':
#     'C:\\Windows\\System32\\Drivers\\DriverData', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\best',
#     'INTELLIJ IDEA': 'C:\\Program Files\\JetBrains\\IntelliJ IDEA 2022.1.2\\bin;', 'LOCALAPPDATA':
#       'C:\\Users\\best\\AppData\\Local', 'LOGONSERVER': '\\\\RAHIL-759297813', 'NUMBER_OF_PROCESSORS': 
#         '8', 'ONEDRIVE': 'C:\\Users\\best\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\best\\OneDrive',
#         'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'OS': 'Windows_NT', 
#         'PATH': 'C:\\Users\\best\\brocamp projects\\My Website\\env\\Scripts;C:\\Windows\\system32;C:\\Windows;C:
#         \\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;
#         C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:
#         \\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS
#         \\\System32\\OpenSSH\\;C:\\FLUTTER\\flutter\\bin;C:\\Program Files\\Git\\cmd;C:\\Program Files\\Git\\bin;C:\\Users\\best
#         \\Downloads\\jdk-18_windows-x64_bin\\jdk-18.0.1.1\\bin;C:\\Users\\best\\Python\\Python310\\Scripts;C:\\Users\\best\\Python
#         \\Python310;C:\\xampp\\php;C:\\ProgramData\\ComposerSetup\\bin;C:\\Users\\best\\AppData\\Local\\Pub\\Cache\\bin;C:\\MinGW\\
#           bin;C:\\Users\\best\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files\\PostgreSQL\\14\\bin;C:\\Program
#           Files\\Redis\\;C:\\Program Files\\nodejs\\;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Windows\\system32;C:\\
#             Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:
#             \\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:
#             \\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:
#             \\WINDOWS\\System32\\OpenSSH\\;C:\\FLUTTER\\flutter\\bin;C:\\Program Files\\Git\\cmd;C:\\Program Files\\Git\\bin;
#             C:\\Users\\best\\Downloads\\jdk-18_windows-x64_bin\\jdk-18.0.1.1\\bin;C:\\Windows\\system32;C:\\Windows;C:\\Windows
#             \\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files
#             (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\WINDOWS\\system32;
#             C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\
#               ;C:\\FLUTTER\\flutter\\bin;C:\\Program Files\\Git\\cmd;C:\\Program Files\\Git\\bin;C:\\Users\\best\\Downloads\\
#                 jdk-18_windows-x64_bin\\jdk-18.0.1.1\\bin;C:\\Windows\\system32;C:;;C:\\Users\\best\\AppData\\Local\\Programs
#                 \\Microsoft VS Code\\bin;C:\\Users\\best\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;
#                 .JS;.JSE;.WSF;.WSH;.MSC;.CPL', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 
#                 6 Model 140 Stepping 1, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '8c01', 'PROGRAMDATA': 
#                   'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)',
#                   'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Users\\best\\OneDrive\\Documents\\WindowsPowerShell\\
#                     Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules'
#                     , 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS'
#                     , 'TEMP': 'C:\\Users\\best\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\best\\AppData\\Local\\Temp', 
#                     'USERDOMAIN': 'RAHIL-759297813', 'USERDOMAIN_ROAMINGPROFILE': 'RAHIL-759297813', 'USERNAME': 'best', 
#                     'USERPROFILE': 'C:\\Users\\best', 'VIRTUAL_ENV': 'C:\\Users\\best\\brocamp projects\\My Website\\env', 
#                     'VIRTUAL_ENV_PROMPT': 'env', 'WINDIR': 'C:\H\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;
#                     C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32
#                     \\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\FLUTTER\\flutter
#                     \\bin;C:\\Program Files\\Git\\cmd;C:\\Program Files\\Git\\bin;C:\\Users\\best\\Downloads\\jdk-18_windows-x64_bin
#                     \\jdk-18.0.1.1\\bin;C:\\Windows\\system32;C:;;C:\\Users\\best\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\best\\AppData\\Roaming\\npm', 'DJANGO_SETTINGS_MODULE': 'Backend.settings', 'RUN_MAIN': 'true', 'SERVER_NAME': 'kubernetes.docker.internal', 
#                     'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '398', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'POST', 'PATH_INFO': '/api/accounts/registration/', 'QUERY_STRING': '',
#                     'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'application/json', 'HTTP_USER_AGENT': 'PostmanRuntime/7.29.2', 'HTTP_ACCEPT': '*/*', 'HTTP_POSTMAN_TOKEN': 'cdf866c0-8f09-4c9f-a63d-c5fdd956a166', 'HTTP_HOST': '127.0.0.1:8000', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_CONNECTION': 'keep-alive',
#                     'HTTP_COOKIE': 'csrftoken=sZQ1c5MBV8N0YFWQF8JJokl1poo1ikGU', 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x000001B75FA67AF0>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>, 'wsgi.version': (1, 0),
#                     'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 'CSRF_COOKIE': 'sZQ1c5MBV8N0YFWQF8JJokl1poo1ikGU'}      
# None
# 127.0.0.1