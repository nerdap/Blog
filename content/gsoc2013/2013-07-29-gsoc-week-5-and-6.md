Title: GSoC 2013 Weeks 5 and 6 Review
Date: 2013-07-29 11:19
Tags: gsoc, sdl
Category: GSoC 2013
Slug: gsoc-2013-weeks-5-and-6
Author: Apoorv Upreti

I've been working on Theme 2 for the last two weeks, which is about varying the SUT command line options.

The first task was to come up with a format to describe the options to the SUT and the kinds of input they would accept. After considering XML, JSON and CSV as possible options, I decided to go with CSV since it's easy to parse without any external dependencies. I've described the encoding in detail and also provided a sample encoding for testsprite2 on the [wiki](https://github.com/nerdap/autotestsprite2/wiki/SUT-Command-Line-Options-Encoding). 

Andreas suggested using SDL_RWops for reading from the CSV file instead of FILE for better compatibility with platforms like Android. This created a bit of a problem because the SDL_RWops library doesn't have an equivalent for fgets(). I had to implement a ReadLine() function using SDL_RWread() which proved to be an interesting exercise.

The CSV file is parsed into a struct that is used by "variators" to generate variations of SUT command line options. The test harness tests the SUT with each such variation.

A variator is quite simply an iterator that iterates through different variations of command line options. I've written briefly about variators in the [wiki](https://github.com/nerdap/autotestsprite2/wiki/Variators).

The test harness will call the variator, launch the SUT with the arguments string from the variator, wait for a specified time period, then kill the SUT and report its return code. This process is repeated until there are no more variations left.

With this part done by the end week 7, we will have a base for the testing framework. The next step would be to add the ability to inject actions while the SUT is running; to take a screenshot or click a mouse button, for example.