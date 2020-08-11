import re


nospace = re.compile(r'[^\s][\S]*')


quotation = re.compile(r'\"[\S]*[\s]?[\S]*\"')


twonum = re.compile(r'(-?(\d+)(\.)?(\d+)?)(,|, | )(-?(\d+)(\.)?(\d+)?)')