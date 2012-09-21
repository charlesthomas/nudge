nudge
=====

FitBit API Module in Python

http://storify.com/crthomas42/fitbit-s-os-x-software-stops-working-after-a-time

FitBit's OS X app is completely broken. It stops syncing after a random amount
of time, and will only ever sync again after reinstalling the app. I have
officially requested that FitBit Support delete my account. I therefore will no
longer be working on the FitBit module. Feel free to pick up where I left off,
if you're using Windows to sync, or they eventually correct whatever is causing
this in the OS X app.

I am new to Python, and I want to automate some stuff with my FitBit account.
I looked for a Python API module, and I couldn't find one, so I decided to make
one myself.

Current functionality:

    * Initial authentication is mostly functional.
    CAVET: As a desktop application, not a webservice.
    What does this mean?
    Desktop applications direct you to the FitBit website where you authenticate
    and are then given a pin to paste back into the application. Webservice
    applications instead redirect users from the FitBit website to the client
    website, and everything is automatic.

To do:

    * Figure out how to authenticate again, after the initial auth.
    Will I need to go through the whole process again, or will the token
    received be permanent?

    * All actual API functionality
    Now that I can get an auth token, I can start building out actual
    functionality.

Requirements:
(See requirements.txt for more details. Produced with pip freeze.)

    * oauth
