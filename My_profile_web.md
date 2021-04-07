# My profile website

![Profile web](https://user-images.githubusercontent.com/60378207/113810797-f4f49600-97a5-11eb-931e-96eff0d96bcf.png)

## Code:
### HTML
```.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="MyProfileStyleSheet.css">
    <title>About Me</title>
</head>
<body>
    <img src="Backgroung_img.jpg" alt="" id="backgroung-img">
    <div>
        <div class="heading">
            <h1 id="Greating">Hi, I am </h1>
            <h1 id="My-name">Timur</h1>
        </div>
        <img id="self-portrait" src="self-portrait.png" alt="">
    </div>
</body>
</html>
```
### CSS
```.html
/*mystyle.css*/
/*css stands for Cascade Stylesheet*/


h1{
    /*any proporties for all h1*/
    color: white;
    font-family: sans-serif;
    font-size: 100px;
    margin: 10px;
}
#backgroung-img{
    alignment: center;
    width: 100%;
    max-width: 1800px;
    height: auto;
    max-height: 850px;
}
.heading{
    position: absolute;
    top: 50%;
    left: 40%;
    transform: translate(-50%, -50%);
}
#My-name{
    color: #f05945;
}
#self-portrait{
    width: 100%;
    max-width: 200px;
    height: auto;
    max-height: 200px;

    position: absolute;
    top: 50%;
    left: 20%;
    transform: translate(-50%, -50%);

}
div{
    display: inline-block;
}
#Greating{
    font-size: 60px;
}
```
