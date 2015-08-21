"""
fb_parse.py
@author: Suyash Kumar
"""
import re

def parse(comment_input):
    """
    Parses emails from a traditional netid comment thread on facebook (or text with netids). For when studens comment
    with their netid expressing interest in a group and a list of emails must be compiled to be added to a list. 

    Args:   
        comment_input:  raw comment thread sting (copy & pasted from facebook)
    Returns:    
        emails: a list of strings representing the netid based emails captured in the input comment string
    """
    result=re.findall(r'[a-z,A-Z][a-z][a-z]?\d+',comment_input) # Find traditional netid matches
    result_mrg=re.findall(r' [a-z,A-Z][a-z][a-z]?$',comment_input, flags=re.MULTILINE) # Edge case for 'mrg' type netids
    result.extend(result_mrg) # add edge case netids to result
    emails=[netid.strip()+"@duke.edu" for netid in result] # Make list of emails
    return emails

if __name__=="__main__":
    # Main thread
    inputFile=open("comments.txt","rb")
    comment_input=inputFile.read()
    inputFile.close()
    emails=parse(comment_input) 
    for email in emails:
        print email

