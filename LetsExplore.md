## Let's Explore! - Episode Guide

**Let's Explore!** is a live streaming series that I host on Twitch where, each week, I set myself a testing mission and then stumble blindly towards completing the goal. There's no editing, and nowhere to hide - just raw unfiltered testing and exploration.

Here are a list of the episodes to date, together with links to useful resources and a quick write-up of the session.

### 23/08/2020: Episode 0 - Visualizing Fixtures
**Mission:** Use the Visualizer in Postman to display this season’s English Premier League fixtures. 

**Secret sub-mission:** Check Neil’s Twitch streaming setup is acceptable before Episode 1!

**Resources:**

 - [Postman](https://postman.com)
 - [Football Data API](https://football-data.org)
 - [Postman collection for this episode](https://github.com/neilstudd/neilstudd/blob/master/resources/LetsExplore/Episode0.postman_collection.json) (you'll need to sign up for a free Football Data API key, and setup a Postman global environment variable called **secretAuthHeader**)
 
**Neil's comments:** 

This one went almost entirely as I'd hoped, except for an issue at the beginning where Twitch silently stopped streaming after a minute (poor connection quality at my end, apparently). Luckily I had to switch back to Twitch Studio to change which screen I was sharing, so I noticed it without too much wasted effort (although that's why the intro on this video sounds a bit half-arsed; I'd already done it once!)

As for the testing mission, I certainly accomplished everything that I'd hoped to do. We took JSON data of Premier League teams/fixtures, and converted them into versions which were easier for the human eye to parse, including team logos. I also managed to run into a few of the current limitations around Postman's implementations of the Handlebars language (Handlebars relies on "helpers" for a lot of useful functionality, and without these it was hard to achieve a few of my mini-goals). I did manage to get some conditional code working though, and in doing so, demonstrated one of the benefits of testing both a "positive" and "negative" case (my tired eyes had made an incorrect assumption about the data which the Visualizer was able to clarify).

Onwards and upwards for episode 1! Expect things to remain mostly in the same format, although I'm going to setup a second monitor which will show the current live stream, so I can spot any future crashes...
