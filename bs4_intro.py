from bs4 import BeautifulSoup

html_string = """
<!doctype html>
<html lang="ru">
<head>
    <title>Web developing road map</title>
    <style type="text/css">
        h1{
            color:brown;
            background:yellow
        }
        #py{
            color:blue
        }
        h2{
            color:salmon;
            background:aquamarine
        }
        .neo{
            color:red
        }

    </style>
</head>
<body>
    <h1>Programming languages for Web developing.</h1>
    <ol>
        <h2>Front-End pars:</h2>
        <li>HTML</li>
        <li>CSS</li>
        <li class="neo">Java Script</li>
    </ol>
    <ol>
        <h2>Back-End pars:</h2>
        <li id="py">Python</li>
        <li>Django</li>
    </ol>

</body>
</html>
"""






html_parsed = BeautifulSoup(html_string,'html.parser')

# print(html_parsed,type(html_parsed),sep="\n\n")

print(html_parsed.find_all('li')[3])
print(html_parsed.select('#py'))
print(html_parsed.select('.neo'))

















