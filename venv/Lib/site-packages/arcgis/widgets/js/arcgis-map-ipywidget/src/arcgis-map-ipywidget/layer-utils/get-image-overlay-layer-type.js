var getEsriLoader = require("../loaders/get-esri-loader");
var config = require("config");
var esriLoader = getEsriLoader(config);
var options = config.EsriLoaderOptions;

var getImageOverlayLayerType = function(){
    return new Promise(function(resolve, reject) {
    esriLoader.loadModules(["esri/layers/GraphicsLayer",
                            "esri/views/2d/layers/BaseLayerView2D",
                            "esri/geometry/Extent",
                            "esri/geometry/SpatialReference",
                            "esri/geometry/projection",
                            "esri/core/watchUtils",
                            "esri/core/Collection"],
    options).then(([GraphicsLayer,
                    BaseLayerView2D,
                    Extent,
                    SpatialReference,
                    projection,
                    watchUtils,
                    Collection]) => {
        var ImageOverlayLayerView2D = BaseLayerView2D.createSubclass({
            constructor: function(){
                var requestUpdate = () => {
                    this.requestRender();}
                this.watcher = watchUtils.on(
                    this,
                    "layer._imagesToOverlay",
                    "change",
                    requestUpdate,
                    requestUpdate,
                    requestUpdate);},

            render: function(renderParameters) {
                var state = renderParameters.state;
                var pixelRatio = state.pixelRatio;
                var width = state.size[0];
                var height = state.size[1];
                var context = renderParameters.context;

                if (state.rotation !== 0) {
                    context.translate(width * pixelRatio * 0.5, height * pixelRatio * 0.5);
                    context.rotate((state.rotation * Math.PI) / 180);
                    context.translate(- width * pixelRatio * 0.5, -height * pixelRatio * 0.5);}

                var i;
                for(i=0;i<this.layer._imagesToOverlay.length; i++){
                    var imgToOverlay = this.layer._imagesToOverlay.getItemAt(i);
                    var min = [0,0];
                    min = state.toScreenNoRotation(min, 
                                                   imgToOverlay.extent.xmin, 
                                                   imgToOverlay.extent.ymax);
                    var max = [0,0];
                    max = state.toScreenNoRotation(max,
                                                   imgToOverlay.extent.xmax,
                                                   imgToOverlay.extent.ymin);

                    var screenScale = pixelRatio;
                    context.save();
                    context.globalAlpha = imgToOverlay.opacity;
                    context.drawImage(imgToOverlay.imgEl,
                                      min[0], min[1],
                                      (max[0]-min[0]), 
                                      (max[1]-min[1]));
                    context.restore();}}});

        var ImageOverlayLayer = GraphicsLayer.createSubclass({
            constructor: function(){
                this._imagesToOverlay = new Collection();},

            createLayerView: function(view) {
                if (view.type === "2d") {
                    return new ImageOverlayLayerView2D({
                        view: view,
                        layer: this});}},

            tryRemoveImageOverlays: function(imageOverlaysToRemove){
                var i;
                for(i=0;i<this._imagesToOverlay.length; i++){
                    var existingOverlay = this._imagesToOverlay.getItemAt(i);
                    if(imageOverlaysToRemove.includes(existingOverlay.id)){
                        this._imagesToOverlay.removeAt(i);
                    }
                }
            },

            tryOverlayImage: function(image){
            return new Promise((resolve, reject) => {
            projection.load().then(() => {
            var randQuery = "?" + Math.random().toString(36).substring(2);
            var imageOverlaySrc = image["src"] + randQuery; //Force no browser cache hit
            fetch(imageOverlaySrc).then((resp) => {
                // Check that we can fetch the URL before trying to draw it
                // (CORs errors & network errors are commonplace, this causes
                // errors to bubble up to the widget display screen
                if(!(resp.ok)){
                    class BadHTTPStatusError extends Error {
                        constructor(message){
                            super(message);
                            this.name = "BadHTTPStatusError";
                            this.status = resp.status;}}
                    reject(new BadHTTPStatusError(
                    "Web request to '" + resp.url + "' returned status " +
                    resp.status + " with message '" + resp.statusText + "'."));}
                // If we're here, the image can be loaded correctly -- continue
                var imgEl = new Image();
                imgEl.onload = () => {
                    var sr = SpatialReference.fromJSON(
                        image["extent"]["spatialReference"]);
                    var extent = Extent.fromJSON(image["extent"])
                    extent = projection.project(extent,
                                                SpatialReference.WebMercator);
                    var opacity = image["opacity"];
                    var id = image["id"];
                    this._imagesToOverlay.add({
                        id: id,
                        imgEl: imgEl,
                        extent: extent,
                        opacity: opacity});}
                imgEl.src = imageOverlaySrc;
            }).catch((err) => {
                reject(err);});
            }).catch((err) => {
                reject(err);})});
            }});
        resolve(ImageOverlayLayer);
    }).catch((err) => {
        reject(err);
    });
    });
}

module.exports = getImageOverlayLayerType;
