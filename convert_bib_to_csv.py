#!/usr/bin/env python3


#Input is via standard input.
#Output is via standard output.


from os import getcwd
from os import listdir
from re import match
from re import search
from re import findall
from sys import stdin
from string import capwords

entries = []
entry = {}
keys= { "title",
        "journal", 
        "year",
        #"doi",
        #"author",
        "abstract",
        "url"
        #...
}

for line in stdin:
    #print(entry)
    if (match('^@', line.strip())):
        #print(line.strip())
        if entry != {}:
            entries.append(entry)
            entry = {}
    elif (search('=', line.strip())):
        key, value = [v.strip(" {},\n") for v in line.split("=")]
        entry[key] = value
        #print(value)

entries.append(entry)    

for item in entries:
    #print(entries)
    author = "Anonymous"
    if "author" in item:
        author = item["author"]
    elif "authors" in item:
        author = item["authors"]
    elif "editor" in item:
        author = item["editor"]
    item["author"] = author

    publish = "No publishing information"
    if "journal" in item:
        publish = item["journal"]
    if "journaltitle" in item:
        publish = item["journaltitle"]
    elif "booktitle" in item:
        publish = item["booktitle"]
    elif "howpublished" in item:
        publish = item["howpublished"]
    elif "type" in item:
        publish = item["type"]
    elif "url" in item:
        publish = "Website: {}".format(item["url"])
    elif "crossref" in item:
        publish = item["crossref"].replace("_", " ")
        publish = capwords(publish)
    elif "publisher" in item:
        publish = item["publisher"]
    item["publish"] = publish
    
    year = "Unknown year"
    if "year" in item:
        year = item["year"]
    item["year"] = year

    title = "Unknown title"
    if "title" in item:
        title = item["title"]
    item["title"] = title

    abstract = "Unknown abstract"
    if "abstract" in item:
        abstract = item["abstract"]
    item["abstract"] = abstract

    journal = "Unknown journal"
    if "journal" in item:
        journal = item["journal"]
    item["journal"] = journal

    string = ""
    for k in keys:
        string += item[k] + "; "
        
    print(string)