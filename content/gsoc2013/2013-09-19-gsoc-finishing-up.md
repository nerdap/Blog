Title: GSoC End Term Review
Date: 2013-10-01 10:42
Tags: gsoc, sdl
Category: GSoC 2013
Slug: gsoc-2013-finishing-up
Author: Apoorv Upreti

GSoC officially ended on the 27th of this month. I've been a little late in finishing this blog post because I had exams from the 28th.

Since this is probably my final GSoC blog post, I'm going to discuss how to setup and try out the test harness so members of the SDL community can use the test harness themselves and give comments or suggestions.

### What we have so far
We've got a test harness that can run a system under test (SUT) executable for various combinations of command line parameters, take screenshots of the SUT windows and compare these screenshots with a repository of verification images.

I've made available verification images for two configs that you can find below.

### Trying out the automated testing

- Start off by cloning the [repository](https://bitbucket.org/nerdap/sdlvisualtest).
- Build using the instructions in `visualtest/README.txt`.
- If you're using the Makefile to build, copy `testsprite2` and `icon.bmp` to the test harness executable directory. The VS solution does this automatically.
- Download the verification images for one of the configs:
    - [testsprite2_blendmodes](https://www.dropbox.com/s/nm02aem76m812ng/testsprite2_blendmodes.zip)
    - [testsprite2_geometry](https://www.dropbox.com/s/csypwryopaslpaf/testsprite2_geometry.zip)
- Extract the directory of verification images. The path to this directory should be passed to the test harness as `verify_dir`.
- Copy the `*.config`, `*.parameters` and `*.actions` files to the test harness executable directory.
- Run `testharness --config testsprite2_XXX.config --verify-dir /path/to/verify_dir`, where `testsprite2_XXX.config` is the name of the config file you want to use.
- If all goes well, all tests should pass and you should get a message like "X/X tests passed".

That's about it. If any of the tests fail, do let me know. Take a look at `README.txt` for more detailed usage instructions and contact information.

### What's next
Lots of tasks still remain. A more complete list is in README.txt, which I'll keep updating as time goes on. At the moment, the following are priorities:

- Implementing the SCREENSHOT action on Linux
- Fixing a bug with the SCREENSHOT action on Windows: it doesn't work when --fullscreen is passed to testsprite2
- Adding actions to inject mouse/keyboard events
- Adding actions to manipulate the SUT windows. E.g., minimize, maximize, resize, etc.

### Conclusion
It's been a lot of fun working on this project over the summer. I'm really grateful to Andreas and the rest of the SDL community in making my first significant open source contribution a success. I plan to stay actively involved in the project and the SDL community in the future and to contribute often.

Thanks for reading and goodbye!