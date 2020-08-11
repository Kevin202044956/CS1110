import re
import urllib.request
import html


def report(identifier):
    '''
    the function is to transform the type of the name, join the '-' in to the name and search the job rank title trough the website by
    using regex
    :param identifier: the name you input
    :return: people's salary job and rank you want
    '''
    a = re.compile(r"^([\w\-]+ ?)+$")
    b = re.compile(r"^([\w\-]+), (\w+)$")
    c = re.compile(r"^(\d{9})$")
    d = re.compile(r"^([\w\-]+)$")

    if (a.match(identifier)):
        result = identifier.split()
        ret = "-".join(result).lower()
    elif (b.match(identifier)):
        result = b.match(identifier)
        ret = result.group(2).lower() + "-" + result.group(1).lower()
    elif (c.match(identifier)):
        ret = identifier
    elif (d.match(identifier)):
        ret = identifier
    try:
        conn = urllib.request.urlopen("http://cs1110.cs.virginia.edu/files/uva2016/" + ret)
    except:
        return None, 0, 0
    else:
        data = conn.read().decode("utf-8")

        e = re.compile(r"\<span.*id=\"personjob\"\>([^<]+)\<\/span\>")
        f = re.compile(r"<h2.*id=\"paytotal\">\$([\d,]+)<\/h2>")
        g = re.compile(r"<tr><td>University of Virginia rank<\/td><td>([\d,]+) of 7,927<\/td><\/tr>")

        t = html.unescape(e.findall(data)[0])

        result = f.findall(data)
        compensation = float(result[0].replace(",", ""))
        rk = 0
        if (g.findall(data)):
            rk = int(g.findall(data)[0].replace(",", ""))

        return (t, compensation, rk)


