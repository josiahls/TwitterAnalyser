<h1>
Twitter Crawler
</h1>
<p>
<ul>
    <li>Author: Josiah Laivins
    <li>Date: 2/17/2018
    <li>Course: ITCS 6112
</ul>
</p>

<p>
Program uses the twitter API for accessing a large number of tweets.
They are mostly limited to about 2 weeks of tweets, however should be plently for this
small analyzer.
</p>

<h2>
Installation
</h2>
<p>
Note that the following needs to be applied in the twitter.py.
Got to: <a>https://apps.twitter.com/</a> to make an account to apply these links:
<ul>
    <li>ACCESS_TOKEN = ''
    <li>ACCESS_SECRET = ''
    <li>CONSUMER_KEY = ''
    <li>CONSUMER_SECRET = ''
</ul>
</p>
<p>
You should be set!
Just execute twitter.py either through an 
ide or via python3 twitter

The prompts should walk you through the rest. 
5 files will be generated.

output.txt contains the raw file output.
The next 4 will contian any interesting data as described by
their file titles. 
</p>

<h2>
Example Output:
</h2>

<h4>Input</h4>
<p>
'trump'<br>
'2018-01-01'<br>
'2018-02-17'<br>
80<br>
10<br>
</p>

<h4>Outputs for each file:</h4>
<p>
    <b>max retweets of tweets</b><br>
    Tweet: penleyvic [16/Feb/2018:23:59:59 ] Total reweets: 12242 <br>
    Tweet: MAGA4TRUMP2020 [16/Feb/2018:23:59:59 ] Total reweets: 10763<br>
    Tweet: mbrand2815 [16/Feb/2018:23:59:58 ] Total reweets: 7778<br>
    Tweet: johanwirfalt [16/Feb/2018:23:59:59 ] Total reweets: 7486<br>
    Tweet: paolo_sf [16/Feb/2018:23:59:57 ] Total reweets: 6398<br>
    Tweet: beinpulse [16/Feb/2018:23:59:59 ] Total reweets: 5685<br>
    Tweet: Rtfighter_MAGA [16/Feb/2018:23:59:59 ] Total reweets: 4048<br>
    Tweet: SumatraSue [16/Feb/2018:23:59:59 ] Total reweets: 3714<br>
    Tweet: AnsareSummers [16/Feb/2018:23:59:57 ] Total reweets: 3651<br>
    Tweet: theLegacyPrep [16/Feb/2018:23:59:57 ] Total reweets: 3525<br>
</p>

<p>
    <b>user max followers</b><br>
    User: rap0322 Total followers: 35838<br>
    User: stumblinginn Total followers: 35838<br>
    User: iateyourfrog Total followers: 29399<br>
    User: c2bryant Total followers: 27838<br>
    User: duckyjd Total followers: 27838<br>
    User: lauralazsewell Total followers: 27838<br>
    User: lynnepithecus Total followers: 27838<br>
    User: IDGomez_Austin Total followers: 24528<br>
    User: johanwirfalt Total followers: 15813<br>
    User: ElizabethHarris Total followers: 14333<br>
</p>

<p>
    <b>user total per hour</b><i> Note larger data sets yeild correct values</i><br>
    User: 99nole Max Total tweets for one hour: 1<br>
    User: AngryLogician Max Total tweets for one hour: 1<br>
    User: Anita_Wahine Max Total tweets for one hour: 1<br>
    User: AnsareSummers Max Total tweets for one hour: 1<br>
    User: BAttanasio Max Total tweets for one hour: 1<br>
    User: BeatleJeff Max Total tweets for one hour: 1<br>
    User: Bladeisspooky Max Total tweets for one hour: 1<br>
    User: Blake_R95 Max Total tweets for one hour: 1<br>
    User: Boggskm1 Max Total tweets for one hour: 1<br>
    User: BonnieJoy1159 Max Total tweets for one hour: 1<br>
</p>

<p>
    <b>user total tweets</b><i> Note larger data sets yeild correct values</i><br>
    User: 99nole Total tweets: 1<br>
    User: AngryLogician Total tweets: 1<br>
    User: Anita_Wahine Total tweets: 1<br>
    User: AnsareSummers Total tweets: 1<br>
    User: BAttanasio Total tweets: 1<br>
    User: BeatleJeff Total tweets: 1<br>
    User: Bladeisspooky Total tweets: 1<br>
    User: Blake_R95 Total tweets: 1<br>
    User: Boggskm1 Total tweets: 1<br>
    User: BonnieJoy1159 Total tweets: 1<br>
</p>
