#!/usr/bin/env python3
'''
@author: David Shaw, shawd@vmware.com

Inspired by EAS Inspector for Fiddler
https://easinspectorforfiddler.codeplex.com

----- The MIT License (MIT) ----- 
Filename: ASWBXML.py
Copyright (c) 2014, David P. Shaw

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
import logging
from PyWBXMLDecoder import ASCommandResponse

if __name__ == "__main__":
        import os
        logging.basicConfig(level=logging.INFO)

        projectDir = os.path.dirname(os.path.realpath("PyWBXMLDecoder"))
        samplesDir = os.path.join(projectDir, "wbxml_samples/")
        listOfSamples = os.listdir(samplesDir)

        for filename in listOfSamples:
                byteWBXML = open(samplesDir + os.sep + filename, "rb").read()

                logging.info("-"*100)
                logging.info(filename)
                logging.info("-"*100)
                instance = ASCommandResponse.ASCommandResponse(byteWBXML)
                logging.info(instance.xmlString)
