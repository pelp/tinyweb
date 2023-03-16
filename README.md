# tinyweb

(super) tiny html file server in python

## How this all started

Once upon a time a wonderful friday night two friends set out on a journey to write really compact
python code. They started by taking the code their friend had written for a dice roller and
squished it down to just a few lines of unreadable code *(see: spawn of satan)*. They wrote the first
version of the `roller.py` program that you can find in this here repository, which ran continiously and
asked for user input instead of being served as a website in a single shot fashion.

This sparked interest deep within the two friends, they now had a new-found passion for writing terrible
code that no one could read. Code that broke all known laws of pep8 EXCEPT ONE! the single most important one,
the holiest of them all: the maximum line length of 79 characters.

Once they had defeated that beast, they wanted to take on the next challenge. Weilding
the power of nested (and recursive) lambda functions and walruss
assignments, they strode forth to overcome a new enemy: HTTP static serving.

## The beginning

As any sane person would, they started out by making part of the webserver by implementing it in readable code.
This way they could track down any bugs before it was too late. Little did they know at this point that they
would start to experience feature creep and would have to end up trying to implement things in the unreadable
code later anyways. But I'm getting ahead of myself.
The first version of the code can be [seen here](https://github.com/pelp/tinyweb/commit/69cf7c0fa79e203b379a1b9e7c9263674dde1b09).

## The great minifying

Once the two friends had gotten a lay of the land they got to work minifying the original code.
They immedietly noticed the abundance of `String.split()` calls, which they [replaced with a lambda function](https://github.com/pelp/tinyweb/commit/61b26df208d340d11fb1ea8f9a22fda92e9cf012).
They fought on, tackling the next foe: The nested lambda functions and recursion hell.
It's starting to become difficult for them to keep track of all the parentheses and
variable scopes. One second you thought you had the variable where you needed it,
only to turn out it was in the wrong lambda scope. They haven't yet started to worry about line length...

Once they finally got the script to run without errors they could tackle the next
issue, converting all this new fresh lambda code to compact tuples that they could
chop up between lines in whichever way they desired. By bending the rules of the walruss
operator (:=) they were able to put everything into tuples and not be restricted by the
fact that you aren't supposed to do variable assignment [inside a tuple](https://github.com/pelp/tinyweb/commit/745ff1dfa310aeb0e29a2d8929050e36507a4012).

Finally [the minimizing has begun](https://github.com/pelp/tinyweb/commit/4e807a10c7963555fd864f304530a694fc32dc8a), they have started to remove: whitespaces,
linebreaks, yes even all forms of indentation. Only a garbled mess of parentheses is left.
But the fight is far from over. The maximum line length is still to be dealt with.

The code is now starting to take the shape, the long lines are gone and [almost at the correct length](https://github.com/pelp/tinyweb/commit/7a07b77df1299f2bc6961a166b159d9a30464fbd).

The problem with the import line at the top of the code is that it leaves unused space where other
code can be written in it's place. The two friends felt like using semicolons and backslashes was
cheating, that would defeat half the challenge. After searching for answers in their previous attempt at this feat,
they found it in the form of `__import__`; They did unspeakable things to the poor dunder import method.
This might have increased the overall number of characters used for the import and following references but
this suddenly made the space on the first line usable for [code other than imports](https://github.com/pelp/tinyweb/commit/3fc1cd6320112bdfd6601a4e80087595fa166d59).

## The ending

Now with a working sort of minimized version of the code the feature creep began. The two friends thought it
would be a good idea to implement dynamic content by loading a python script that would return some dynamic content.
This "simple" idea turned out to add a lot more complexity to the project, and made the code even more confusing.

By using the extension of the requested file they made a condition that would return the contents of a file if it
ended with anything other than .py, [otherwise execute it](https://github.com/pelp/tinyweb/commit/8e1e142ef28716a573f5b4b849caaafdd8b8579d).

After some struggling the [implementation](https://github.com/pelp/tinyweb/commit/253ae1ec8f228821df10730cf85cca69f2287785) now works and the only
thing left is for the code to be form-fitted to the character limit. And be turned into a solid block.

Moving some things around, adding and removing some stuff made the code nearly fill neatly into a 79x9 block
but the only problem was that the last line wasn't long enough yet. Even with their signature within the
codebase it wasn't enough to fill the last line. They had mastered the skill of making things small and compact,
now they had to add something that wasn't strictly needed. After some thought, experimentation and discussion they decided on
a few improvements to the http headers. Adding a content encoding so that it could properly render utf-8 characters. As well as
adding the `Server: tw/v1` header. This was the final piece of the puzzle.

There they were, 9 lines, 79 characters each. 7 lambda functions, 13 walruss operators and several crimes against developers later, they had successfully made
a [working http server](https://github.com/pelp/tinyweb/commit/9c4d129a35801ebf454c7c4f335f74eb838e37db) that could serve static html files as well as
dynamic content rendered from python files.

## The revival

After 2 long years with no commits the two friends set out to improve their tiny webserver. They started by removing redundant split operations to 
save a few characters, they trimmed some minor details to save a few characters here and there. But when they realised that they could remove the whole 
`subprocess` import and just use the `os` modules `popen` funciton to run the python programs great steps towards minifying even further was made. While 
going over the code with fresh eyes and 2 more years of experience they realised that the recursive data receiving was unnecessary and they could just 
increase the receive buffer so that it would fit every possible request URL. This saved greatly on characters as well. As a final step, they removed 
their watermark to save even more and to their surprise now the program would fit in 7 lines perfectly, each line being 79 characters.

So, to correct the previos statement. There they were, 7 lines, 79 characters each. 5 lambda functions, 11 walruss operators and several crimes against developers later, they had successfully made a [working http server](https://github.com/pelp/tinyweb/commit/6ff00e4d422cf18f1d83e33e6f77700a0f9ca25e) that cold server static html files as well as dynamic content rendered from python files.
