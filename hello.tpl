<html>
    <body>
        %if extra != None : 
        <h2>Hello, {{name}}! {{extra.upper()}}</h2>
        %else: 
        <h2>Hello, {{name.upper()}}!</h2>
        %end
        <br>
        -From the template
    </body>
</html>