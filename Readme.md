# RTEIndexer
by Cathal Garvey, Copyright 2016, Released under the AGPLv3 or later

### TL;DR
This is a [Scrapy](https://scrapy.org/) project that indexes all
available episodes for all shows on RTE.ie player, including key
metadata that's provided by RTÉ for each item. Right now, it's
a barebones project, but it would make a good back-end to a free/libre
RTÉ Player alternative as a web-app or mobile app.

### The Longer Version
[RTÉ offers an online player][rteplayer] for many broadcast programmes,
which in theory allows you to watch those programmes in-browser from any
Irish IP address (or VPN exit), ad-free and on-demand. At least, until
they de-list the shows after some expiry date.

This would be great, except that they require you to install Adobe Flash
in order to view the videos. Not only is this a nuisance, it's actively
harmful to your privacy and security; next to Java and Internet Explorer,
Flash is one of the most vulnerable-to-everything ways to interact with
the world, and nearly guarantees you a virus if you use it for more than
a small span. In fact, it's so bad, that all major browsers will soon be
dropping default support for Flash entirely and will require users to
manually install it henceforth at their own risk.

Well, you shouldn't have to install malware to enjoy the programmes that
RTÉ make using the Television Levy. Fortunately for you RTÉ player
is supported by [Youtube-DL][ytdl], so you can take the URL of any show
or episode and download it to your computer, for viewing with any other
less-evil player! Great!

The only annoyance, then, is that doing this means manually visiting
each URL and calling Youtube-DL on it by hand, which is irritating if
you just want to binge-watch three or more shows in a row.

This is my attempt to put things another step in the right direction.
This is a Python 3 Scrapy project to index RTÉ Player, outputting
metadata and URLs for all shows currently available to view.
When I run this locally it takes about an hour with some polite
rate-limiting settings.

Using this data and a tool to filter the output like [JLTool][jltool],
you can then construct lists of URLs to pass to [Youtube-DL][ytdl] to
download for local viewing.

This would also make an interesting back-end for a Free/Libre RTÉ app
or web-app, to allow people to browse and view things comfortably
like RTÉ player, but without Flash. It is ready to deploy locally
using Scrapy or remotely [as a web-scraper on Scrapinghub][shub]*.

*Disclosure: I currently work for Scrapinghub

[rteplayer]: https://www.rte.ie/player/ie/
[ytdl]: https://rg3.github.io/youtube-dl/
[jltool]: https://github.com/cathalgarvey/jltool
[shub]: https://scrapinghub.com
