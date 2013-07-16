Title: GSoC 2013 Weeks 3 and 4 Review
Date: 2013-07-08 22:23
Tags: gsoc, sdl
Category: GSoC 2013
Slug: gsoc-2013-weeks-3-and-4
Author: Apoorv Upreti

I wasn't able to post my updates last week, so I'm going to bunch them together with this week's updates.

- The build system for Linux is now ready. The setup I'd made in week 2 didn't compile on Cygwin and MingW because I hadn't used the output from sdl2-config to configure the library paths and compiler flags. After some help from the SDL wiki and some Googling on my own I managed to configure autotools to use sdl2-config correctly. I haven't been able to test the new setup on Cygwin/MinGW yet but it works just fine on Ubuntu and Linux Mint.
- I've implemented the process API for Linux.
- Implemented parsing for arguments passed to the test harness and for config files. The way this works is quite similar to the way SDLTest_CommonArg() works.
- Implemented a tokenizer to break the arguments string to the SUT into an argv-style array. This was required because all the calls in the exec() family expect a list of arguments while Windows' CreateProcess() expects a single arguments string.
- Added a timer to kill the SUT after a maximum timeout.
- I've started working on parsing a config file that describes what kind of options an SUT application can take. The idea so far is that the file will be represented in JSON where each option will be a JSON object. JSON is an ideal choice because it's easy to write, light weight and easy to parse.

This week I completed the design and core infrastructure theme and began work on the next one, which deals with varying the SUT command line options.