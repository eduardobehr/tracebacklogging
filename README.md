# tracebacklogging
Developed by Eduardo Eller Behr with Python 3.8

## Purpose
This code is meant as a quick way to log errors from your code.

If you have a program that you don't want to halt uppon erros,
but still need to analyse them, why not just save it to a log file and read later for debugging?

## How to use
### Instructions
    1) create TracebackLogger object;
    2) call the method 'get_traceback' INSIDE the except clause; (this MUST be inside the except);
    3) call the method log_traceback().

### TLDR
```
# import class
from tracebacklogging import TracebackLogger

logger = TracebackLogger()
try:
    # try some code that may fail to finish
    x = 1/0  # this raises the ZeroDivisionError

except ZeroDivisionError:
    # log the traceback in the 'traceback.log'
    logger.log_traceback()

    # [optional]
    logger.print_traceback()
```

## License
MIT License

Copyright (c) 2020 Eduardo Eller Behr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
