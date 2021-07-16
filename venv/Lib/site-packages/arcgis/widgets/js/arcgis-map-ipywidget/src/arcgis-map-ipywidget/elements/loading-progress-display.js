//modifies the passed in element's textContent to mimic an animation until
//stop() is called

var baseText = " Loading ";
var cyclingIcon = "🗺️";
var cyclingCount = 0;
var intervalIds = [];
var element = document.createElement("div");
element.id = 'loadingTextDiv';
element.style.textAlign = "center";
element.style.verticalAlign = "text-top";
//element.style.top = "0%";

var start = function(){
    element.textContent = baseText;
    if(intervalIds.length === 0){
        intervalIds.push(setInterval(intervalCallback, 700));
    }
}

var intervalCallback = function(){
    if (cyclingCount++ % 4 == 0){
        element.textContent = baseText;
    }else{
        element.textContent = cyclingIcon + element.textContent + cyclingIcon;
    }
}

var stop = function(){
    while((id=intervalIds.pop()) != null){
        clearInterval(id);
    }
    element.textContent = "";
}

module.exports = { start: start,
                   stop: stop,
                   element: element}
