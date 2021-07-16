var createDefaultPopup = function (layer) {
    //Pass in the PopupTemplate already loaded so we don't have to use Promises (overkill)
    var fieldInfos = [];
    for(var i in layer.fields){
        var field = layer.fields[i];
        fieldInfos.push({
            "fieldName": field.name,
            "label": field.alias,
            "visible": true
        });
    };
    return { //will autocast as a PopUpTemplate
        title: layer.title,
        content: [{
            type: "fields",
            fieldInfos: fieldInfos
        },]
    };
}

module.exports = createDefaultPopup;
