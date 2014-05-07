#!/usr/bin/env python

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
