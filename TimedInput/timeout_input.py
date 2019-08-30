#!/usr/bin/env python3

# "Nobody dies a virgin... Life fucks us all." ~ Kurt Cobain

import threading as th

class TimeoutInput(th.Thread):
    """ Timed input reader """

    def get_input(self):
        """ Actual function for reading the input """
        self.input = input(self.prompt)

    def __init__(self, timout, prompt="", default=None, *args, **kwargs):
        """
        TimoutInput(
            timeout -> amount of seconds to wait for the input,
            prompt -> optionl prompt to display while asking for input,
            default -> string to return in case of timeout,
            *args/**args -> any additional arguments are passed down to Thread
                            constructor
        )
        Creates an object reading input, that times out after timeout amount of
        seconds.
        """
        self.timeout = timout
        self.prompt = prompt
        self.input = default
        super().__init__(target=self.get_input,*args,**kwargs)
        self.daemon = True

    def join(self):
        """ The actual timeout happens here """
        super().join(self.timeout)
        return self.input

    def read(self):
        """ Reads the input from the reader """
        self.start()
        return self.join()

# Sample usage:
if __name__ == "__main__":
    s = TimoutInput(5, "Enter name: ", "world").read()
    print("Hello %s!" % s)
