<h1>A tool to check proxy lists and keep only the working ones</h1>

You usually find thousands of proxies all over the Internet that allow use from anyone.
Most of them do not make it over a few weeks. So if you have a huge list of proxies, you
sooner or later end up with a list than has less than 30% working rate. You either have
to look again for one, or have reduced performance for your cause.
<br/><br/>
<h2>What is ProxyBorder?</h2>
ProxyBorder is a Python Command-Line Utility that accepts a proxy list in the form of
```
8.8.8.8:8888
8.8.4.4:8844
```
and checks every proxy in the list whether it works or not. It then stores in another file
a second list, containing only the proxies that were accessible and the request was made
without problems.
<br/>
For an added bonus, ProxyBorder has multi-threading so you don't waste time and have
measurably faster performance while checking large proxy lists. 
<br/><br/>
<h2>How it works?</h2>
You need to supply a text file that has a proxy list as the first argument and another
file that does not exist to be the output of ProxyBorder. In other words, the syntax
is as follows:
```
python proxyborder.py proxylist.txt output.txt
```
<br/>
If you do not supply the proper arguments, the program will prompt the user to enter
the two files from STDIN by writing the required messages on STDOUT.

