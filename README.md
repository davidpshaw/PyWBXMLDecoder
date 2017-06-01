PyWBXMLDecoder
==============

A WAP Binary XML (WBXML) Decoder Written in Python

Written by David Shaw, shawd AT vmware.com

Inspired by EAS Inspector for Fiddler
https://easinspectorforfiddler.codeplex.com

Updates
==============
Updated for Python 3 for compatibility with mitmproxy 2.0 and later

Description
==============
I was writing an Exchange ActiveSync client and found it very difficult to troubleshoot because the WBXML format is not human-readable.  I found a nice open source plugin for the Fiddler proxy, but because I use a Mac for development, Fiddler wasn't a good option.

I then found a really great open-source proxy at:  http://mitmproxy.org

It was really good and did most of what I needed, but it was written in Python and did not handle WBXML decoding.  

I wrote this code with significant inspiration from the C# code used in Fiddler, and crafted it as a plug-in to the mitmproxy project. I have submitted it for inclusion in a future release, but I felt that it was useful code on its own, so I am releasing it separately as well.

If you have any questions or comments, feel free to email me at the address above.
