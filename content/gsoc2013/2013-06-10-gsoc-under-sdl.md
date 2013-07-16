Title: Google Summer of Code 2013 under SDL
Date: 2013-06-10 17:00
Tags: gsoc, sdl
Category: GSoC 2013
Slug: gsoc-2013-sdl
Author: Apoorv Upreti
Summary: I got selected for Google's Summer of Code program with SDL as my mentoring organization.

SDL or Simple DirectMedia Layer is a low-level, cross-platform multimedia library that provides access to keyboard, mouse, audio and video hardware. It's available for Windows, Linux, OS X, iOS, Android, and many other platforms.

My GSoC project concerns a test in the SDL test suite called testsprite2. This test simply launches a window and moves sprites around the screen as fast as possible. The basic objective of the test is to answer three questions:

1. Is the window being created by the window manager as expected? (correct title, resolution, window state, etc.)
2. Is mouse behavior being detected correctly?
3. Are the sprites inside the window rendered correctly?

The goal of this GSoC project is to automate this process. There are two major challenges to overcome. Firstly, testsprite2 takes 26 parameters as input with thousands of valid combinations. Success would mean testing as many valid combinations as possible. Secondly, verifying the success of the test is inherently hard to automate - it's much easier for a human to answer the above questions than for a computer to. By automating testsprite2, I hope to make it easier to detect certain kinds of bugs in SDL's code, ones that were missed out previously.

I started using SDL years ago when I was still in high school. I fondly remember following lazy_foo's tutorials and struggling with concepts like blitting, double buffering and alpha blending. This is why the opportunity to make SDL better means a lot to me. I'm looking forward to working towards a top quality SDL 2.0 release this summer.

Useful Links:

- [GSoC Ideas Page](http://www.libsdl.org/gsoc.php "SDL GSoC Ideas Page")
- [Project Wiki](https://github.com/nerdap/autotestsprite2/wiki "Project Wiki on GitHub")
- [Application on Melange](http://www.google-melange.com/gsoc/proposal/review/google/gsoc2013/nerdap/10001 "Application on Melange")