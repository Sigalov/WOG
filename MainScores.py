from Score import read_score_from_file
def score_server():
    try:
        score = read_score_from_file()
    except Exception as e:
        return f"""
            <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <body>
            <h1><div id="score" style="color:red">{e}</div></h1>
            </body>
            </html>        
        """
    return f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>    
    """