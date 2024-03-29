## Let's Explore! - Episode Guide

**Let's Explore!** is a live streaming series that I host on Twitch where, each week, I set myself a testing mission and then stumble blindly towards completing the goal. There's no editing, and nowhere to hide - just raw unfiltered testing and exploration.

## Episode List

Here are a list of the episodes to date, together with links to useful resources and a quick write-up of the session.

* [Episode 0 - Visualizing Fixtures](#23082020-episode-0---visualizing-fixtures-watch-on-youtube)
* [Episode 1 - The Python Lottery](#27082020-episode-1---the-python-lottery-watch-on-youtube)
* [Episode 2 - API Challenge App](#02092020-episode-2---api-challenge-app-watch-on-youtube)
* [Episode 3 - API Exploratory Testing](#09092020-episode-3---api-exploratory-testing-watch-on-youtube)
* [Episode 4 - Exploring with TestBuddy](#15092020-episode-4---exploring-with-testbuddy-watch-on-youtube)
* [Episode 5 - Python Play Your Cards Right](#22092020-episode-5---python-play-your-cards-right-watch-on-youtube)
* [Episode 6 - Racket Search](#14072021-episode-6---racket-search-watch-on-youtube)

### 23/08/2020: Episode 0 - Visualizing Fixtures [[Watch on YouTube](https://www.youtube.com/watch?v=fjjqTvA_rgQ)]
**Mission:** Use the Visualizer in Postman to display this season’s English Premier League fixtures. 

**Secret sub-mission:** Check Neil’s Twitch streaming setup is acceptable before Episode 1!

**Resources:**

 - [Postman](https://postman.com)
 - [Football Data API](https://football-data.org)
 - [Postman collection for this episode](/resources/LetsExplore/Episode0/Episode0.postman_collection.json) (you'll need to sign up for a free Football Data API key, and setup a Postman global environment variable called **secretAuthHeader**)
 
**Neil's comments:** 

This one went almost entirely as I'd hoped, except for an issue at the beginning where Twitch silently stopped streaming after a minute (poor connection quality at my end, apparently). Luckily I had to switch back to Twitch Studio to change which screen I was sharing, so I noticed it without too much wasted effort (although that's why the intro on this video sounds a bit half-arsed; I'd already done it once!)

As for the testing mission, I certainly accomplished everything that I'd hoped to do. We took JSON data of Premier League teams/fixtures, and converted them into versions which were easier for the human eye to parse, including team logos. I also managed to run into a few of the current limitations around Postman's implementations of the Handlebars language (Handlebars relies on "helpers" for a lot of useful functionality, and without these it was hard to achieve a few of my mini-goals). I did manage to get some conditional code working though, and in doing so, demonstrated one of the benefits of testing both a "positive" and "negative" case (my tired eyes had made an incorrect assumption about the data which the Visualizer was able to clarify).

Onwards and upwards for episode 1! Expect things to remain mostly in the same format, although I'm going to setup a second monitor which will show the current live stream, so I can spot any future crashes...

### 27/08/2020: Episode 1 - The Python Lottery [[Watch on YouTube](https://www.youtube.com/watch?v=DW3dRznL4N8)]
**Mission:** Write a Python script which runs a series of fake lottery draws (6 random numbers) and compares it against the user's chosen numbers. Run many simulations and see if we can "win" the jackpot!

**Resources:**

 - [Python](https://python.org)
 - [The script created in this episode](/resources/LetsExplore/Episode1/Episode1.py)
 - [The updated script that Neil went away and refactored](/resources/LetsExplore/Episode1/Episode1_Refactored.py)
 - [A further version for checking multiple sets of numbers at once](/resources/LetsExplore/Episode1/Episode1_MultipleContestants.py)

**Neil's comments:**

Mission accomplished, although we didn't win the jackpot in FIFTY MILLION attempts during the video! Of course, the very next time that I ran the script, we won the jackpot five times... it just goes to show, probability isn't to be messed with.

![](/resources/LetsExplore/Episode1/Episode1_JackpotWins.png)

As for the episode itself, it went pretty much as I'd hoped (except for forgetting to select my Yeti microphone as the source, meaning that all of the episode's audio came from my tinny Mac). It's a real odd experience trying to explain code that you're about to write; particularly near the start, I found myself saying "here, let me just show you" a lot! And I liked the way that I was able to demonstrate that the biggest performance improvements can come from the unlikeliest of sources (in this case, commenting-out some log messages).

As promised in the video, I went away and refactored my two functions into one-liners, and you can find both the original and refactored scripts in the links above. I like the new version of GetDrawNumbers - it utilises one of the functions that I spotted when browsing the Python docs on-stream - but the refactored CheckNumbers has lost a lot in readability, in exchange for not much peformance gain.

### 02/09/2020: Episode 2 - API Challenge App [[Watch on YouTube](https://www.youtube.com/watch?v=zSHLYayjb5w)]
**Mission:** Download Alan Richardson's API Challenges app, and complete 3-4 of the challenges in Postman.

**Bonus Mission:** Complete a challenge on the hosted version of the app (which requires extra authentication).

**Resources:**

 - [API Challenges homepage](eviltester.com/apichallenges)
 - [Hosted version of API Challenges app (resets data every 10 minutes)](https://apichallenges.herokuapp.com)
 - [Postman](https://postman.com)
 - [Neil's challenge status page](https://apichallenges.herokuapp.com/gui/challenges/13af3358-b16c-4077-bc46-c3f3a10e15dc)

**Neil's comments:**

Plain sailing! I knew there shouldn't be too much for me to be fearful of here, as I work with APIs on a daily basis, and I'd pre-downloaded Alan's app to make sure that I didn't have setup problems during the session. In fact I ended up completing a few more challenges than expected, after discovering by happy accident that some of Postman's default settings (e.g. always sending an Accept header) meant that I was able to tick-off multiple challenges with a single request. And I did unexpectedly learn something - I've never had reason to use the HEAD verb before, but can now already think of some very useful scenarios where I might choose to apply it in the future.

The only thing I noticed (and commented on) was my own habit for "shortcutting": I declared that I was going to create a new Postman request for each challenge (the awfully-named Challenge 1, Challenge 2 etc) and yet quickly fell into the habit of just modifying the already-opened request. I think I might have been less lazy if I'd used better naming for these requests - my brain was probably saying it "doesn't matter" if Challenge 2 points to something different now - but as the collection was basically temporary, it didn't seem like a big deal.

There was only one technical snafu in the episode, where my webcam preview froze for no apparent reason. Thankfully I noticed the problem a lot quicker than I'd feared; it's probably something to do with the weird way in which I'm capturing my screen and webcam simultaneously (the webcam is basically a QuickTime 'New Movie Recording' window, set to float on top, but not actually recording). 


### 09/09/2020: Episode 3 - API Exploratory Testing [[Watch on YouTube](https://www.youtube.com/watch?v=m6bYQQOCiWM)]

**Mission:** Brainstorm a list of possible tests for a real API endpoint, and (if time) run as many as possible.

**Resources:**

 - [Football Data API](https://football-data.org)
 - [Postman](https://postman.com)
 - [Mindmup](https://mindmup.com)
 - [Test Heuristics Cheat Sheet (PDF)](https://testobsessed.com/wp-content/uploads/2011/04/testheuristicscheatsheetv1.pdf)
 - [Big List of Naughty Strings](https://github.com/minimaxir/big-list-of-naughty-strings/blob/master/blns.txt)

**Neil's comments:**

I really enjoyed this one! It's weird how quickly your ideas can dry up when you're under pressure, and it perfectly illustrated the benefits of having something like Elizabeth Hendrickson's cheat sheet to hand. And we found one genuine server error along the way (even if it was primarily due to an error in the user input).

It was also my first time using new recording software ([OBS Studio](https://obsproject.com/)) which was recommended to me by Alan Richardson. It worked pretty much as hoped, although it's inconvenient that there's no way of viewing the webcam overlay while you're recording: there were a couple of moments during the video where I suddenly realised that I was probably typing in an area which wouldn't have been visible to the user. OBS is primarily designed for live streaming, especially of games, so I'm not massively surprised by this - the recording experience was more seamless than before, so I'm happy to learn to adapt.

The only noteworthy thing that's missing from this episode: it's the first one which doesn't include human-transcribed subtitles. Subtitling is EXPENSIVE; [Rev](https://www.rev.com) is great, but when transcriptions are $1.25 per minute and you're recording a 47-minute video which is unlikely to reach 100 viewers in its first week, the costs mount up really quickly. If the series takes off, or I'm able to find some way to cover the costs of these, I'll backdate the subtitling at the earliest opportunity.

### 15/09/2020: Episode 4 - Exploring with TestBuddy [[Watch on YouTube](https://www.youtube.com/watch?v=a0DWifILUCE)]

**Mission:** Use TestBuddy to plan and execute a 15-minute recon session on the registration page for The StoryGraph.

**Resources:**

 - [TestBuddy](https://testbuddy.co)
 - [The StoryGraph](https://thestorygraph.com)
 - [PDF of Neil's test session](/resources/LetsExplore/Episode4/TestBuddy_Report.pdf)

**Neil's comments:**

This was an interesting challenge, because I was testing two things at once! Firstly, the website for The StoryGraph, which I hadn't even opened prior to starting the session, so I was going in completely blind. Secondly, I was running the session using TestBuddy, which I'd signed-up for that morning, and had yet to run any test sessions using the tool. Lots to learn, and so perhaps it wasn't a surprise that (although the recon session was only the advertised 15 minutes) the video ran to 45 minutes. I think I demonstrated that prior preparation (utilising the Planning section within TestBuddy) makes for a more focused testing session.

I picked the registration page of The StoryGraph for my test as it seemed the most obvious - after all, I would have to register for an account before I could start to build a profile. However, in hindsight it's perhaps not a surprise that the registration process seemed to be a little rough: I talked in the video about 'product value', and a frictionless registration process isn't where The StoryGraph is striving to build its value. If I ran another session with The StoryGraph, I would probably focus on one of their headline features, such as the recommendations/filtering system which they're promoting on the homepage.

As for TestBuddy: I found it an incredibly slick experience. I mentioned a few possible UX improvements at points where I'd been confused when first using the tool, but they're aspects which I'd learn to forget very quickly (such as the need to click "Finish" before being able to access the summary section). It's a tool that I'm certainly planning to share with colleagues, as I'm sure some of them are working within teams who would appreciate having test notes shared with them in this fashion.

### 22/09/2020: Episode 5 - Python Play Your Cards Right [[Watch on YouTube](https://www.youtube.com/watch?v=C1rHzXRYPfk)]

**Mission:** Write some code which shuffles a deck of cards, and allows the user to guess whether the next card is higher or lower.

**Bonus Mission:** Try to correctly guess ten in a row!

**Resources:**

 - [Python](https://python.org)
 - [The script created in this episode](/resources/LetsExplore/Episode5/Episode5_Original.py)
 - [The updated script that Neil went away and refactored](/resources/LetsExplore/Episode5/Episode5_Refactored.py)

**Neil's comments:**

My second blind Python coding session of the series, and it shared a lot of parallels with the first! Most notably, it seems that I'm very good at setting overly ambitious "Bonus Mission" goals which are impossible to meet live on-stream, so (with a little bit of additional refactoring also visible) here's proof that I eventually managed to accomplish the 10-in-a-row feat:

![](/resources/LetsExplore/Episode5/Screenshot.png)

I was happy with how the script progressed throughout the video: my use of "todo" statements certainly paid-off, allowing me to focus on the piece of functionality that I was working on in the moment, before returning to add/improve extra features later. I only fell into a couple of language traps: firstly, the fact that `random.shuffle` modifies the original variable (causing some confusion when I was calling variables which I expected to be unshuffled) and some headaches around array-splitting of strings (for all the nice things that I have to say about Python, the fact that you have to do `foo[-1]` rather than some variant of `right(foo)` isn't brilliant).

I'll probably park Python for a bit until we're in the double-figures, but I've got a few ideas of other things that I could try to code live, possibly more testing-focused. (Loading JSON data from a URL, and then traversing it, is something I've had to do a few times in the course of my testing, it'd be good to see how much I can remember when put on the spot!)

### 14/07/2021: Episode 6 - Racket Search [[Watch on YouTube](https://www.youtube.com/watch?v=Xp1N7aAEYHA)]

**Mission:** Explore the new Search feature on Racket, to determine whether its results match expectations.

**Resources:**

 - [Racket](https://www.racket.com)
 - [PDF of the mind map created in this episode](/resources/LetsExplore/Episode6/Racket%20Search.pdf)

**Neil's comments:**

Time to blow off the cobwebs! Since I last recorded an episode, I've bought a new house and converted myself a dedicated studio space in the garden, complete with acoustic panelling and a bonus ultrawide UHD monitor. It's great that I don't have to record in the kitchen any more! Primarily this episode was a way of getting back into the swing of things, and making sure my laptop was set up to record and screen-share reasonably well, something which will be vital for upcoming conferences and live streams.

This was a true "testing something new" experience, as the feature I was testing only went live today (it hadn't officially been announced to Racket's "What's New" page at this point). This made it a very good candidate for demonstrating how we occasionally find ourselves having to reverse-engineer behaviours (if we don't have access to the original specification or user story), and how it can be sometimes difficult to determine whether an observation is a "problem" or it can be brushed off as "as designed".
