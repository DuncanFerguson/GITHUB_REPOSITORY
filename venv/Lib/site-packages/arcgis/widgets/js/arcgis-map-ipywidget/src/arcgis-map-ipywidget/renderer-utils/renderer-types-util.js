var isSmartMapRenderer = function(renderer){
    return isClassedSizeRenderer(renderer) ||
           isClassedColorRenderer(renderer)
}

var isHeatMapRenderer = function(renderer){
    return /.*heat.*/i.test(renderer);
}

var isClassBreaksRenderer = function(renderer){
    return /.*class.*break.*/i.test(renderer);
}

var isClassedSizeRenderer = function(renderer){
    return /.*class.*size.*/i.test(renderer);
}

var isClassedColorRenderer = function(renderer){
    return /.*class.*color.*/i.test(renderer);
}

var isSimpleRenderer = function(renderer){
    return /.*simple.*/i.test(renderer);
}

var isUniqueRenderer = function(renderer){
    return /.*unique.*/i.test(renderer);
}

var isDotDensityRenderer = function(renderer){
    return /.*dot.*density.*/i.test(renderer);
}

var userSpecifiedAutocastRenderer = function(renderer){
    return /.*auto.*cast.*/i.test(renderer);
}

module.exports = { isSmartMapRenderer: isSmartMapRenderer,
                   isHeatMapRenderer: isHeatMapRenderer,
                   isClassedColorRenderer: isClassedColorRenderer,
                   isClassBreaksRenderer: isClassBreaksRenderer,
                   isClassedSizeRenderer: isClassedSizeRenderer,
                   isSimpleRenderer: isSimpleRenderer,
                   isUniqueRenderer: isUniqueRenderer,
                   isDotDensityRenderer: isDotDensityRenderer,
                   userSpecifiedAutocastRenderer: userSpecifiedAutocastRenderer,};
