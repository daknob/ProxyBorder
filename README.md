# ProxyBorder: A tool to check proxy lists and keep only the working ones

You usually find thousands of proxies all over the Internet that allow use from anyone.
Most of them do not make it over a few weeks. So if you have a huge list of proxies, you
sooner or later end up with a list than has less than 30% working rate. You either have
to look again for one, or have reduced performance for your cause.


## What is ProxyBorder?
ProxyBorder is a Python Command-Line Utility that accepts a proxy list in the form of

```
8.8.8.8:8888
8.8.4.4:8844
```
and checks every proxy in the list whether it works or not. It then stores in another file
a second list, containing only the proxies that were accessible and the request was made
without problems.


For an added bonus, ProxyBorder has multi-threading so you don't waste time and have
measurably faster performance while checking large proxy lists. 


## How it works?
You need to supply a text file that has a proxy list as the first argument and another
file that does not exist to be the output of ProxyBorder. In other words, the syntax
is as follows:

```
python proxyborder.py proxylist.txt output.txt
```


If you do not supply the proper arguments, the program will prompt the user to enter
the two files from `stdin` by writing the required messages on `stdout`.
