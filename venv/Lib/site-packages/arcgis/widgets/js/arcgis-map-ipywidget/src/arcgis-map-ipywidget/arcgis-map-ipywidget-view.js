//The main module that exports the javascript widget class

//import all external modules
const widgets = require('@jupyter-widgets/base');
const _ = require('lodash');

//import all helper functions
var createElements = require('./elements/create-elements');
var displayPureJSErrorBox = require('./elements/display-purejs-error-box');
var loadingProgressDisplay = require('./elements/loading-progress-display');
var inferNoTypeLayer = require('./layer-utils/infer-no-type-layer');
var getImageOverlayLayerType = require('./layer-utils/get-image-overlay-layer-type');
var images = require('./images/images');
var mainCssString = require('../css/main.css').toString();
var configureCDN = require("../config/configure-cdn");

//import the configuration and the specific esri-loader based off the config
var config = require("config")
var getEsriLoader = require('./loaders/get-esri-loader');
var esriLoader = getEsriLoader(config);
var options = config.EsriLoaderOptions;

console.log("Using this config:");
console.log(config);

//Apply the mainCssString defined in ../css/main.css
var _applyCssString = function(cssString){
    var style = document.createElement("style");
    style.innerHTML = cssString;
    document.head.appendChild(style);
}
_applyCssString(mainCssString);

//Apply the ArcGIS JS API's main.css to the document
var _applyCssFromUrl = function(url){
    var link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = url
    document.head.appendChild(link);
}
_applyCssFromUrl(config.CdnMainCssUrl);

//The arbitrary layer ID for all layers that we only want 1 instance of
const graphicsLayerId = "graphicsLayerId31195";
const imageOverlayLayerId = "imageOverlayLayerId551883";

// Each new widget instantiated on the Python side has a uuid field
// If a python widget displays in a notebook twice, there will be two
// instances of the JS widget with the same uuid, but still the 1 python inst.
// This global dictionary will have each key be the uuid, and each value
// be the token associated with the portal. This is needed due to security 
// concerns of not storing the token in the model (which can be persisted on 
// disk), and due to the unpredictable nature of traitlets/backbone.
// TODO: find a more elegant solution to this
var globalTokenLookup = {};

var ArcGISMapIPyWidgetView = widgets.DOMWidgetView.extend({
    render: function() {
    ///This is called once the first time the widget is drawn in the notebook
    this._override_right_click_menu();
    this._setup_js_cdn();
    this._setup_elements();
    this.model.set("jupyter_target", config.JupyterTarget);
    loadingProgressDisplay.start();
    esriLoader.loadModules(['esri/Map',
                            'esri/views/MapView',
                            'esri/WebMap',
                            'esri/WebScene',
                            'esri/views/SceneView',
                            'esri/core/watchUtils',
                            'esri/widgets/Compass',
                            'esri/widgets/Legend',
                            'esri/widgets/TimeSlider'], options).then((
                            [Map,
                             MapView,
                             WebMap,
                             WebScene,
                             SceneView,
                             watchUtils,
                             Compass,
                             Legend,
                             TimeSlider]) => {
        loadingProgressDisplay.stop();
        this._setup_custom_buttons();
        this._instantiate_esri_components(Map, WebMap, WebScene, 
                                          MapView, SceneView,
                                          Compass, Legend, TimeSlider);
        this._miscellanous_setup();
        //All model specific change functions. These functions are called
        //whenever that attribute on the model is updated, whether that update
        //comes from Python, from the UI, etc. The callback function is called on change
        //start map specific draw state
        this.model.on('change:mode', this.mode_changed, this);
        this.model.on('change:_basemap', this.basemap_changed, this);
        this.model.on('change:_zoom', this.zoom_changed, this);
        this.model.on('change:_scale', this.scale_changed, this);
        this.model.on('change:_snap_to_zoom', this.snap_to_zoom_changed, this);
        this.model.on('change:_rotation', this.rotation_changed, this);
        this.model.on('change:_link_writeonly_rotation', this.link_rotation_changed, this);
        this.model.on('change:_heading', this.heading_changed, this);
        this.model.on('change:_link_writeonly_heading', this.link_heading_changed, this);
        this.model.on('change:_tilt', this.tilt_changed, this);
        this.model.on('change:_link_writeonly_tilt', this.link_tilt_changed, this);
        this.model.on('change:_extent', this.extent_changed, this);
        this.model.on('change:_link_writeonly_extent', this.link_extent_changed, this);
        this.model.on('change:_center', this.center_changed, this);
        this.model.on('change:_center_long_lat', this.center_long_lat_changed, this);
        //start layer specific model types
        this.model.on('change:_func_chains', this.func_chains_changed, this);
        this.model.on('change:_add_this_notype_layer', this.add_this_notype_layer_changed, this);
        this.model.on('change:_layers_to_remove', this.layers_to_remove_changed, this);
        this.model.on('change:_add_this_graphic', this.graphics_changed, this);
        //end layer specific model types
        //start webmap/websceme section
        this.model.on('change:_webmap', this.webmap_changed, this);
        this.model.on('change:_webscene', this.webscene_changed, this);
        this.model.on('change:_trigger_webscene_save_to_this_portal_id', this.save_webscene, this);
        //end webmap/webscene section

        //start screenshot section
        this.model.on('change:_trigger_screenshot_with_args', this._trigger_screenshot_with_args_changed, this);
        //end screenshot section

        //start image overlay section
        this.model.on('change:_overlay_this_image', this.overlay_image_changed, this);
        this.model.on('change:_image_overlays_to_remove', this.image_overlays_to_remove_changed, this);
        //end image overlay section

        //start time section
        this.model.on('change:time_slider', this.time_slider_prop_changed, this);
        this.model.on('change:time_mode', this.time_mode_changed, this);
        this.model.on('change:_time_info', this.time_info_changed, this);
        this.model.on('change:_writeonly_start_time', this.start_time_changed, this);
        this.model.on('change:_writeonly_end_time', this.end_time_changed, this);
        //end time section

        //start miscellanous model section
        this.model.on('change:_portal_token', this.portal_token_changed, this);
        this.model.on('change:_custom_msg', this.custom_msg_changed, this);
        this.model.on('change:hide_mode_switch', this.hide_mode_switch_changed, this);
        this.model.on('change:_trigger_interactive_draw_mode_for', this.interactive_draw_shape, this);
        this.model.on('change:_trigger_new_jlab_window_with_args', this.trigger_jlab_window_changed, this);
        this.model.on('change:_js_cdn_override', this.js_cdn_changed, this);
        this.model.on('change:legend', this.legend_prop_changed, this);
        this.model.on('change:_trigger_print_js_debug_info', this.trigger_print_js_debug_info_changed, this);
        //end miscellanous model section

        //Last thing to do: update the widget state from the model's
        this.update_widget_from_model().then(() => {
            this._postLoadSetup(watchUtils);
        });
    }).catch((err) => {
       this._displayErrorBox();
       console.warn("Error on render: "); console.warn(err);
        });
    },

    update_widget_from_model: function(){
        return new Promise((resolve, reject) => {
            //start map specific draw state
            this.mode_changed();
            this.basemap_changed();
            this.zoom_changed();
            this.scale_changed();
            this.snap_to_zoom_changed();
            this.rotation_changed();
            this.heading_changed();
            this.tilt_changed();
            this.center_long_lat_changed();
            this.center_changed();
            this.extent_changed();
            //end map specific draw state
            //start miscellanous model section
            this.hide_mode_switch_changed();
            this.portal_token_changed();
            this.authenticate_to_portal().then((_) => {
                //Authenticate to the portal before attempting to load anything
                //end miscellanous model section
                //start layer specific model calls
                this.draw_these_notype_layers_on_widget_load();
                this.draw_these_graphics_on_widget_load();
                this.overlay_these_images_on_widget_load();
                //end layer specific model calls
                //start webmap/webscene section
                this.webmap_changed();
                this.webscene_changed();
                //end webmap/webscene section
                this.legend_prop_changed();
                //start time section
                this.time_slider_prop_changed();
                this.time_mode_changed();
                this.time_info_changed();
                //end time section

                resolve();
            }).catch((err) => {
                this._displayErrorBox("Error while authenticating to portal on first load.");
                console.warn("Error during portal auth"); console.warn(err);
                reject(err);
            });
        })
    },


    _displayErrorBox: function(msg, browser_console_message = true){
        ///A simple message box display mechanism
        if (!msg){
            msg = "Unhandled Error! See the browser console for more info.";
        }
        else if (browser_console_message) {
            msg += " See the browser console for more info.";
        }
        loadingProgressDisplay.stop();
        if (!document.getElementById(this.elements.errorTextBox.id)){
            //If everything has failed to load, add the error box so it displays
            this.el.appendChild(this.elements.errorTextBox);
        }
        if(!this.elements.errorTextBox.textContent){
            //If there's no current message box open
            displayPureJSErrorBox(msg, this.elements); 
        } else {
            //There's another message still open: save all messages
            //to browser console and alert user
            var multiple_messages_info = "Multiple messages attempted to " + 
                "display. See browser console to view all messages";
            if(this.elements.errorTextBox.textContent !== multiple_messages_info){
                console.warn("*****MESSAGE_BOX: " +
                    this.elements.errorTextBox.textContent);
            }
            console.warn("*****MESSAGE_BOX: " + msg);
            displayPureJSErrorBox(multiple_messages_info, this.elements);
        }
    },

    _setup_elements: function(){
        this.uuid = this.model.get('_uuid');
        this.elements = createElements(this.uuid);
        this.el.className = "arcgisMapIPyWidgetDiv";
        this.el.style.height = "100%";
        this.el.style.width = "100%";
        this.el.appendChild(this.elements.viewdivElement);
    },

    _setup_custom_buttons: function(){
        ///Now that we're loaded, add the 2D/3D switch, new window button, etc
        //2D/3D switch setup
        this.elements.infodivElement.appendChild(this.elements.switchButton);
        this.elements.switchButton.onclick = () => {
            if(this.model.get("mode") === "3D"){
                this.model.set("mode", "2D");
                this.touch();
            } else {
                this.model.set("mode", "3D");
                this.touch();
            }
        }
        //jupyterlab new window button setup
        if(config.JupyterTarget === "lab"){
            this.elements.infodivElement.appendChild(this.elements.newWindowButton);
            this.elements.newWindowButton.onclick = () => {
                this.move_to_new_jlab_window({title: "ArcGIS Map"});
            }
        }
    },

    _setup_2d_stationary_callback: function(watchUtils){
        //The moment the mouse enters the arcgis js api 2d view (not parent element),
        //Set up responses to the 'stationary' callback (i.e., what logic to run
        //when the user clicks the map, zooms, changes extent, etc.). Only set this up once
        this._MapView._pointerMoveHandler = this._MapView.on(
            ['pointer-move', 'key-down'], (event) => {
                console.log("Started interacting with the 2D map, " + 
                    "setting up stationary callback...");
                watchUtils.when(this._MapView, "stationary", this._2dStationaryCallback)
                this._MapView._pointerMoveHandler.remove();
        });
    },

    _setup_3d_stationary_callback: function(watchUtils){
        //Same as above, but for the 3D SceneView
        this._SceneView._pointerMoveHandler = this._SceneView.on(
            ['pointer-move', 'key-down'], (event) => {
                console.log("Started interacting with the 3D map, " + 
                    "setting up stationary callback...");
                watchUtils.when(this._SceneView, "stationary", this._3dStationaryCallback)
                this._SceneView._pointerMoveHandler.remove();
        });
    },

    _2dStationaryCallback: function(){
        ///Do 2D specific stationary callbacks before common stuff
        var widget_inst = this._parentIPyWidget;

        var rotation = this.rotation;
        if(rotation >= 0){
            widget_inst.model.set("_readonly_rotation", rotation);
            var heading = 360 - rotation;
            widget_inst.model.set("_readonly_heading", heading);
            widget_inst.apply_heading_to_view(heading);
        }

        widget_inst._commonStationaryCallback(widget_inst);
    },

    _3dStationaryCallback: function(){
        ///Do 3D specific stationary callbacks before common stuff
        var widget_inst = this._parentIPyWidget;

        var camera = this.camera;
        if(camera){
            widget_inst.model.set("_readonly_heading", camera.heading);
            var rotation = 360 - camera.heading;
            widget_inst.model.set("_readonly_rotation", rotation);
            widget_inst.apply_rotation_to_view(rotation);
            widget_inst.model.set("_readonly_tilt", camera.tilt);
        }

        widget_inst._commonStationaryCallback(widget_inst);
    },

    _commonStationaryCallback: function(widget_inst){
        ///This function is a callback for the 'stationary' event on the activeView
        ///('stationary' is when the map stops moving on a zoom, a pan, etc.)
        ///Since it is a callback, 'this' is actually the instance of either the
        ///the 2d MapView or 3D SceneView
        var zoom = widget_inst.activeView.zoom;
        if(zoom >= 0){
            //this callback is sometimes errenously called, displaying nonexistant values
            widget_inst.model.set("_readonly_zoom", zoom);}

        var scale = widget_inst.activeView.scale;
        if(scale >= 1){
            widget_inst.model.set("_readonly_scale", scale);}

        var center = widget_inst.activeView.center;
        if(center){
            widget_inst.model.set("_readonly_center", JSON.parse(JSON.stringify(center)));}

        var extent = widget_inst.activeView.extent;
        if(extent){
            widget_inst.model.set("_readonly_extent", JSON.parse(JSON.stringify(extent)));}

        widget_inst.model.save_changes();
    },

    _miscellanous_setup: function(){
       ///Every time the 2d map changes a basemap/ground/layer, call this function
        this.map.allLayers.on('change', (event) => {
            this.update_readonly_webmap();
        });
    },

    _postLoadSetup: function(watchUtils){
        //Whenever either the 2d or 3d view loads, set model var 'ready' to
        //true for python to consume
        console.log("Running post load setup for " + config.JSOutputContext);
        this._MapView.when(() => {
            console.log("2D map ready");
            this.model.set('ready', true)
            this.model.set('_readonly_extent', this._MapView.extent);
            this.model.set('_readonly_center', this._MapView.center);
            this.model.save_changes();
            this.zoom_changed(); //Fixes quick redraw bug of zoom not honored
            this._setup_2d_stationary_callback(watchUtils);
        });

        this._SceneView.when(() => {
            console.log("3D map ready");
            this.model.set('ready', true)
            this.model.set('_readonly_extent', this._SceneView.extent);
            this.model.set('_readonly_center', this._SceneView.center);
            this.model.save_changes();
            this.zoom_changed(); //Fixes quick redraw bug of zoom not honored
            this.tilt_changed(); //'' '' '' '' '' '' ''' ''  tilt not honored
            this._setup_3d_stationary_callback(watchUtils);
        });

        //Whenever you click on the map, send an event for python to listen to
        this._MapView.on(['click'], (event_) => {
            this.send({ event: 'mouseclick', message: event_.mapPoint });
        });

        this._SceneView.on(['click'], (event_) => {
            this.send({ event: 'mouseclick', message: event_.mapPoint });
        });

        // Apply CSS to hide any image preview and HTML embed preview in the 
        // live notebook (but keep it in the underlying notebook file)
        //
        // Don't do this when this JS code is called from the embedded
        // widget itself (i.e. when MapView.embed() or MapView.export_to_html()
        // is called)
        if(config.JSOutputContext === "default"){
            this._hidePreviewEls();}

        // Add screenshot keyboard shortcut
        this._set_screenshot_keyboard_shortcut();
    },

    _hidePreviewEls: function(){
        console.log("Hiding preview elements for " + this.uuid);
        var cssEl = document.createElement('style');
        cssEl.type = 'text/css';
        cssEl.innerHTML = 'div.map-static-img-preview-' +
            this.uuid + ' { display: none }\n' + 
            'div.map-html-embed-preview-' +
            this.uuid + ' { display: none }';
        document.head.appendChild(cssEl);
    },

    _setup_js_cdn: function(){
        //set up any CDN override before we call esri modules
        this.model.on('change:_js_cdn_override', this.js_cdn_changed, this);
        this.js_cdn_changed();
    },

    _instantiate_esri_components: function(Map, WebMap, WebScene, MapView, SceneView,
                                           Compass, Legend, TimeSlider){
        this.container = this.elements.mapElement;
        var mode = this.model.get("mode").toLowerCase();
        if(mode === "2d"){
            this.map = new WebMap({ground: "world-elevation"});
            this._MapView = new MapView({
                map: this.map,
                container: this.container});
            this.activeView = this._MapView;
            this._SceneView = new SceneView({map: this.map});
        } else if(mode === "3d"){
            this.map = new WebScene({ground: "world-elevation"});
            this._SceneView = new SceneView({
                map: this.map,
                container: this.container});
            this.activeView = this._SceneView;
            this._MapView = new MapView({map: this.map});}
        this._MapView._parentIPyWidget = this
        this._SceneView._parentIPyWidget = this;

        //Set the default zoom to a model-less number that looks a bit nicer
        this._MapView.zoom = 2;
        this._SceneView.zoom = 2;

        // Set up widgets like compass and legend
        this._MapView.ui.add(new Compass({view: this._MapView}), "top-left");
        this._time_slider = new TimeSlider({
            view: this.activeView,
            container: document.createElement("div"),
            mode: "time-window"});
        this._time_slider.watch('values', (values) => {
            this.time_slider_values_changed(values);});
        this._legend = new Legend({
            view: this.activeView,
            layerInfos: []});
   },

    _override_right_click_menu: function(){
        //JupyterLab has a right click menu we don't want displaying
        //when the map is right clicked to rotate
        this.el.addEventListener('contextmenu', function(e) {
            e.preventDefault();
            e.stopPropagation();
            return false;
        }, false);
    },

    _set_screenshot_keyboard_shortcut: function(){
        this.el.addEventListener('keydown', (e) => {
            if (e.shiftKey && e.key ==="P"){
                this.model.set("_trigger_screenshot_with_args",
                    {"_" : this._get_uuidv4(),
                     "set_as_preview": true,
                     "output_in_cell": false,
                     "file_path": false});
                this.model.save_changes();
            }
        });
    },

    _get_uuidv4: function() {
      return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, 
          function(c) {
            var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
          });
    },

    custom_msg_changed: function(){
        var _custom_msg = this.model.get("_custom_msg");
        if(_custom_msg){
            this._displayErrorBox(_custom_msg,
                                  browser_console_message = false);
        }
    },

    basemap_changed: function () {
        esriLoader.loadModules(['esri/Basemap'],
        options).then(([Basemap]) => {
            console.log("updating basemap...");
            var basemapStr = this.model.get('_basemap');
            var galleryBasemaps = this.model.get('_gallery_basemaps');
            if (basemapStr in galleryBasemaps){
                //If the basemap passed in is in the gallery, use it
                var basemapJSON = galleryBasemaps[basemapStr];
                var basemap = Basemap.fromJSON(basemapJSON);
                this.map.basemap = basemap;
            } else {
                //Else, just pass the str to the map (it can autocast)
                this.map.basemap = basemapStr
            }
        }).catch((err) => {
            this._displayErrorBox("Error while changing basemap.");
            console.warn("Error on basemap_change: "); console.warn(err)
        });
    },

    trigger_print_js_debug_info_changed: function(){
        console.log("Widget = ");
        console.log(this);
        console.log("Global token lookup = ");
        console.log(globalTokenLookup);
    },

    mode_changed: function(){
    esriLoader.loadModules(['esri/WebMap', 'esri/WebScene'],
    options).then(([WebMap, WebScene]) => { 
        console.log("updating mode...");
        var mode = this.model.get("mode").toLowerCase();
        if(mode === "3d"){
            this.elements.switchButton.src = images.sceneToMapEncoded;
            if(this.activeView.viewpoint){
                this._SceneView.viewpoint = this.activeView.viewpoint.clone();
                this.activeView.container = null;}
            this._SceneView.container = this.container;
            this.activeView = this._SceneView;
            this.map = new WebScene({ground: this.map.ground,
                                     basemap: this.map.basemap,
                                     layers: this.map.layers});
            this._SceneView.map = this.map
            this._MapView.map = null;
        } else {
            this.elements.switchButton.src = images.mapToSceneEncoded;
            if(this.activeView.viewpoint){
                this._MapView.viewpoint = this.activeView.viewpoint.clone();
                this.activeView.container = null;}
             this._MapView.container = this.container;
             this.activeView = this._MapView;
             this.map = new WebMap({ground: this.map.ground,
                                    basemap: this.map.basemap,
                                    layers: this.map.layers});
             this._MapView.map = this.map;
             this._SceneView.map = null;
             //Set the 'tilt' to 0 whenever switching to 2D mode
             this.model.set("tilt", 0);
             this.model.save_changes();}
        this.legend_prop_changed(); //Needed to reset the legend's view
        this.time_slider_prop_changed();
        this.map.allLayers.on('change', (event) => {
            this.update_readonly_webmap();}); 
    }).catch((err) => {
        this._displayErrorBox();
        console.warn("Error on mode_changed"); console.warn(err); 
    });},

    zoom_changed: function(){
        try{
            var zoom = this.model.get("_zoom");
            this.model.set("_readonly_zoom", zoom);
            if(zoom >= 0){
                this.activeView.zoom = zoom;}
            this.model.save_changes();
        } catch(err){
            this._displayErrorBox("Error while modifying zoom.");
            console.warn("Error on zoom"); console.warn(err);
        }
    },

    scale_changed: function(){
        try{
            var scale = this.model.get("_scale");
            this.model.set("_readonly_scale", scale);
            this.model.save_changes();
            if(scale >= 1){
                this.activeView.scale = scale;
            }
        } catch(err) {
            this._displayErrorBox("Error while modifying scale");
            console.warn("Error on scale"); console.warn(err);
        }
    },

    snap_to_zoom_changed: function(){
        try{
            var mode = this.model.get("mode")
            var snapToZoom = this.model.get("_snap_to_zoom");
            if(mode === "2D"){
                this.activeView.constraints.snapToZoom = snapToZoom;}
        } catch(err) {
            this._displayErrorBox("Error while modifying snap to zoom");
            console.warn("Error on snap to zoom"); console.warn(err);
        }
    },

    rotation_changed: function(){
        try{
            var rotation = this.model.get("_rotation");
            this.model.set("_readonly_rotation", rotation);
            this.model.save_changes();
            this.apply_rotation_to_view(rotation);
        } catch(err){
            this._displayErrorBox("Error while modifying rotation");
            console.warn("Error on rotation"); console.warn(err);
        }
    },

    link_rotation_changed: function(){
        var rotation = this.model.get("_link_writeonly_rotation");
        this.apply_rotation_to_view(rotation);
    },

    apply_rotation_to_view: function(rotation){
        this._MapView.rotation = rotation;
    },

    heading_changed: function(){
        var heading = this.model.get("_heading");
        this.model.set("_readonly_heading", heading);
        this.model.save_changes();
        this.apply_heading_to_view(heading);
    },

    link_heading_changed: function(){
        var heading = this.model.get("_link_writeonly_heading");
        this.apply_heading_to_view(heading);
    },

    apply_heading_to_view: function(heading){
        var _applyHeading = () => {
            //The actual function that is eventually called to apply the heading
            this._SceneView.goTo({center: this._SceneView.center,
                              heading: heading},
                             {animate: false});
        };
        esriLoader.loadModules(["esri/core/watchUtils"],
        options).then(([watchUtils]) => {
            if(this._SceneView.camera){
                //If the map is already initialized
                _applyHeading();
            } else{
                //set up the callback when the camera is ready for consumption
                watchUtils.once(this._SceneView, "camera", () => {
                    _applyHeading();
               })
            }
        }).catch((err) =>{
            this._displayErrorBox("Error while modifying heading");
            console.warn("Error on heading"); console.warn(err);
        });

    },

    tilt_changed: function(){
        var tilt = this.model.get("_tilt");
        this.model.set("_readonly_tilt", tilt);
        this.model.save_changes();
        this.apply_tilt_to_view(tilt);
    },

    link_tilt_changed: function(){
        var tilt = this.model.get("_link_writeonly_tilt");
        this.apply_tilt_to_view(tilt);
    },

    apply_tilt_to_view: function(tilt){
        var _applyTilt = () => {
            this._SceneView.goTo({center: this._SceneView.center,
                              tilt: tilt},
                             {animate: false});
         };
        esriLoader.loadModules(["esri/core/watchUtils"],
        options).then(([watchUtils]) => {
            if(this._SceneView.camera){
                //If the map is already initialized
                _applyTilt();
           } else {
                //Set up the callback when the camera is ready for consuption
                watchUtils.once(this._SceneView, "camera", () => {
                    _applyTilt();
                });
            }
        }).catch((err) =>{
            //TODO: Figure out why the 'h is null' error happens, fix it
            //For now, don't display an error box, just log to console
            //this._displayErrorBox("Error while modifying tilt");
            console.warn("Error on tilt"); console.warn(err);
        });
    },

    extent_changed: function(){
        var extent = this.model.get("_extent");
        this.apply_extent_to_view(extent);
    },

    link_extent_changed: function(){
        var extent = this.model.get("_link_writeonly_extent");
        this.apply_extent_to_view(extent);
    },

    apply_extent_to_view: function(extent){
        esriLoader.loadModules(['esri/geometry/Extent',
                                "esri/geometry/SpatialReference",
                                "esri/geometry/projection"],
        options).then(([Extent,
                        SpatialReference,
                        projection]) => {
            if(extent.xmin){
                //Prevents an error about a bad extent
                this.activeView.extent = new Extent(extent);
                projection.load().then(() => {
                    this.activeView.extent = projection.project(
                        new Extent(extent),
                        SpatialReference.WebMercator);
                });
            }
        }).catch((err) => {
            this._displayErrorBox("Error while modifying extent.");
            console.warn("Error on extent"); console.warn(err);
        });
    },

    center_long_lat_changed: function(){
        ///When the center is passed in as a [long,lat] list, add it to the view
        ///Then watch the view until it changes center into the correct format,
        ///which we will then update correctly via the _center model attribute
        esriLoader.loadModules(["esri/core/watchUtils"],
        options).then(([watchUtils]) => {
            var _center_long_lat = this.model.get("_center_long_lat");
            if(_center_long_lat.length === 2){
                console.log("Converting [long, lat] center to standard center...");
                //Set up the callback when the view's center is ready for consuption
                watchUtils.once(this.activeView, "center", () => {
                    console.log("Center is converted");
                    var view_center = JSON.parse(JSON.stringify(this.activeView.center));
                    this.model.set("_center", view_center);
                    this.model.set("_center_long_lat", []);
                    this.model.save_changes();
                })
                //Actually update the center on the activeView to trigger the above
                this.activeView.center = _center_long_lat
            }
       }).catch((err) =>{
            this._displayErrorBox("Error while modifying center_long_lat.");
            console.warn("Error on center_long_lat"); console.warn(err);
        });
 
    },

    center_changed: function(){
        ///this function is called when _center is in the correct format
        try{
            var _center = this.model.get("_center");
            if('x' in _center && 'y' in _center){
                this.activeView.center = _center;
            }
        }catch(err){
            this._displayErrorBox("Error while modifying center");
            console.warn("Error on center"); console.warn(err);
        }
    },

    webmap_changed: function(){
    esriLoader.loadModules(['esri/WebMap']).then(([WebMap]) => {
        console.log("Updating webmap...");
        var webmap_from_python = this.model.get("_webmap");
        if(Object.keys(webmap_from_python).length !== 0){
            this.map = WebMap.fromJSON(webmap_from_python);
            this._MapView.map = this.map;}
    }).catch((err) => {
        this._displayErrorBox("Error on loading webmap from portal");
        console.warn("Error on loading webmap"); console.warn(err);
    });
    },

    update_readonly_webmap: function() {
        ///Whenever a layer/basemap/ground is changed, OR whenever the webmap
        ///is directly changed, update an esri JSON representation of the webmap
        ///for readonly consumption on the python side of things
        try{
            var map;
            if(this._MapView.map){
                map = this._MapView.map}
            else {
                map = this._SceneView.map
            }
            var layers_json = []
            for(var i in map.layers.toArray()){
                //TODO: Implement WebMap.toJSON() when it's added to JS API
                var layer = map.layers.toArray()[i]
                var layer_json = { id : layer.id,
                                   normalization : layer.normalization,
                                   refreshInterval : layer.refreshInterval,
                                   url : layer.url };
                if (layer.graphics){
                    layer_json.graphics = [];
                    for(var i in layer.graphics.toArray()){
                        var graphic = layer.graphics.toArray()[i];
                        var graphic_json = graphic.toJSON();
                        graphic_json.shape = graphic.shape;
                        layer_json.graphics.push(graphic_json);
                    }
                }
                if (layer.renderer){
                    layer_json.renderer = layer.renderer.toJSON();
                    layer_json.rendererType = layer.renderer.declaredClass;}
                layers_json.push(layer_json) }
            var ground_json = map.ground ? map.ground.toJSON() : {}
            var basemap_json = map.basemap ? map.basemap.toJSON() : {}
            var wm = { layers : layers_json,
                       ground : ground_json,
                       basemap : basemap_json };
            this.model.set('_readonly_webmap_from_js', wm);
            this.model.save_changes();
        } catch(err){
            this._displayErrorBox("Error updating readonly webmap json.");
            console.warn("Error updating readonly webmap"); console.warn(err); }
    },

    webscene_changed: function(){
        esriLoader.loadModules(['esri/WebScene',
                                'esri/Viewpoint',
                                'esri/webscene/InitialViewProperties']).then(
        ([WebScene, ViewPoint, InitialViewProperties]) => {
        console.log("Updating webscene...");
        console.log(this.model.get("_webscene"))
        var webscene_from_python = this.model.get("_webscene");
        if(Object.keys(webscene_from_python).length !== 0){
            this.authenticate_to_portal().then((portal) => {
                webscene_from_python.portalItem.portal = portal;
                var webscene = new WebScene(webscene_from_python);
                webscene.load().then((webscene) => {
                    this._SceneView.map = webscene;
                    this.map = webscene;
                }).catch((err) => {
                    this._displayErrorBox("Error on loading webscene item");
                    console.warn("Error on loading webscene"); console.warn(err);
                });
            }).catch((err) => {
                this._displayErrorBox("Error on loading portal for webscene");
                console.warn("Error loading portal"); console.warn(err);
                
            });
        }
    }).catch((err) => {
        this._displayErrorBox("Error on loading webscene from portal");
        console.warn("Error on loading webscene"); console.warn(err);
    });
    },

    save_webscene: function(){
        esriLoader.loadModules(['esri/WebScene',
                                'esri/Ground',
                                'esri/Basemap']).then(
        ([WebScene,
          Ground,
          Basemap]) => {
            this.authenticate_to_portal().then((portal) => {
                var scene;
                if(this._SceneView.map.declaredClass == "WebScene"){
                    scene = new WebScene(this._SceneView.map.toJSON())}
                else{
                    scene = new WebScene({layers : this._SceneView.map.layers,
                        ground : Ground.fromJSON(this._SceneView.map.ground.toJSON()),
                        basemap : Basemap.fromJSON(this._SceneView.map.basemap.toJSON())});}
                var portal_item_id = this.model.get("_trigger_webscene_save_to_this_portal_id");
                console.log("Starting to save webscene to portal item " + portal_item_id); 
                scene.portalItem = {
                        id: portal_item_id,
                        portal: portal};
                scene.load().then(() => {
                    scene.ground = Ground.fromJSON(this._SceneView.map.ground.toJSON());
                    scene.basemap = Basemap.fromJSON(this._SceneView.map.basemap.toJSON());
                    scene.updateFrom(this._SceneView);
                    scene.save({ignoreUnsupported: true}).then((item) => {
                        console.log("The following item was saved:");
                        console.log(item.toJSON());
                   }).catch((err) => {
                        this._displayErrorBox("Error saving webscene");
                        console.warn("Error saving webscene"); console.warn(err);
                    });
                    //TODO: clean up, figure out why layers are deleted on save
                    this.reload_all_layers();
                    this._SceneView.map = scene;
                    this.map = scene;

                }).catch((err) => {
                    this._displayErrorBox("During load, error on loading webscene save");
                    console.warn("Error loading web scene"); console.warn(err);
                })
            }).catch((err) => {
                this._displayErrorBox("During portal auth, error on webscene save");
                console.warn("Error portal auth on webscene save"); console.warn(err);});
        }).catch((err) => {
            this._displayErrorBox("Error on saving the web scene");
            console.warn("Error saving web scene"); console.warn(err);
        });
    },

    reload_all_layers: function(){
        console.log("TODO: CHECK IF I'M BROKEN");
        this.draw_these_notype_layers_on_widget_load();
    },

    func_chains_changed: function(){
            console.log("Updating func_chains...");
            console.log(this.model.get("_func_chains"));
    },

    draw_these_notype_layers_on_widget_load: function(){
        var layers = this.model.get('_draw_these_notype_layers_on_widget_load');
        console.log("Drawing these layers on load... ");
        console.log(layers);
        for(var i in layers){
            var noTypeLayer = layers[i];
            this.add_notype_layer(noTypeLayer);
        }
    },

    add_this_notype_layer_changed: function(){
        var noTypeLayer = this.model.get("_add_this_notype_layer");
        if(Object.keys(noTypeLayer).length !== 0){
            this.add_notype_layer(noTypeLayer);
       }
   },

    add_notype_layer: function(noTypeLayer){
        var layersToInfer = [];
        if (noTypeLayer.layers){
            for(var i = 0; i < noTypeLayer.layers.length; i++){
                var layer = noTypeLayer.layers[i];
                layer.options = noTypeLayer.options;
                layersToInfer.push(layer);
            }
        } else {
            layersToInfer.push(noTypeLayer);
        }
        for(var i = 0; i<layersToInfer.length; i++){
           var layerToInfer = layersToInfer[i];
           inferNoTypeLayer(layerToInfer, this).then((typedLayer) => {
                console.log("Adding Layer " + noTypeLayer._hashFromPython + " " +
                    "to map.");
                this.map.add(typedLayer);
            }).catch((err) => {
                this._displayErrorBox("Could not update layer. " + err);
                console.warn("Could not update layer"); console.warn(err);
            });
       }
    },

    layers_to_remove_changed: function(){
        try{
            console.log("Called layer to remove changed...");
            var _layers_to_remove = this.model.get("_layers_to_remove");
            for(var i in _layers_to_remove){
                var layerId = _layers_to_remove[i];
                do {
                    var layer = this.map.findLayerById(layerId);
                    var layerExistsOnMap = Boolean(layer);
                    if(layerExistsOnMap){
                        console.log("Attempting to remove layer" + layer.id);
                        this.map.remove(layer);
                    }
                } while(layerExistsOnMap);
            }
        } catch(err){
            this._displayErrorBox("Error removing layer");
            console.warn("Error removing layer"); console.warn(err);
        }
    },

    hide_mode_switch_changed: function(){
        //NOTE: it is only possible to remove this element
        //To 'recreate', you must instantiate a whole new object
        if(this.model.get("hide_mode_switch")){
            console.log("Removing the mode switch...");
            this.elements.switchButton.remove();
        }
    },

    getGraphicsLayer: function(GraphicsLayer){
        ///All graphics are drawn on 1 layer: return it if it's been made,
        ///Make it if it hasn't
        var graphicsLayer = this.map.findLayerById(graphicsLayerId);
        if(typeof graphicsLayer === "undefined"){
            graphicsLayer = new GraphicsLayer({
                id: graphicsLayerId});
            this.map.add(graphicsLayer);
        }
        return graphicsLayer
    },

    draw_these_graphics_on_widget_load: function(){
        var graphics = this.model.get('_draw_these_graphics_on_widget_load');
        console.log("Drawing these layers on load... ");
        console.log(graphics);
        for(var i in graphics){
            var graphic_json = graphics[i];
            this.add_graphic(graphic_json);
        }
    },

    graphics_changed: function(){
        var graphic_json = this.model.get("_add_this_graphic");
        if(Object.keys(graphic_json).length !== 0){
            this.add_graphic(graphic_json);
       }
    },

    add_graphic: function(graphic_json){
        esriLoader.loadModules(['esri/layers/GraphicsLayer',
                                'esri/Graphic',
                                'esri/geometry/Geometry',
                                'esri/symbols/support/jsonUtils'],
        options).then(([GraphicsLayer,
                        Graphic,
                        Geometry,
                        symbolJsonUtils]) => {
            var gfx = new Graphic(graphic_json);
            if(gfx.symbol == null) {
                console.log(gfx.geometry);
                if (/polyline/i.test(gfx.geometry.type)) {
                    gfx.symbol = { type: 'simple-line' }
                } else if (/polygon/i.test(gfx.geometry.type)) {
                    gfx.symbol = { type: "simple-fill" };
                } else if (/point/i.test(gfx.geometry.type)) {
                    gfx.symbol = { type: 'simple-marker' }
                } else if (/multipoint/i.test(gfx.geometry.type)) {
                    gfx.symbol = { type: 'simple-marker' }
                }
            }
            if('symbol' in graphic_json){
                var symbol = symbolJsonUtils.fromJSON(graphic_json.symbol);
                if(symbol != null){
                    gfx.symbol = symbol
                }
            }
            var graphicsLayer = this.getGraphicsLayer(GraphicsLayer);
            graphicsLayer.add(gfx);
        }).catch((err) => {
            this._displayErrorBox("Error on updating graphics.");
            console.warn("Error on updating graphics"); console.warn(err);
        });
    },

    interactive_draw_shape: function(){
        esriLoader.loadModules(['esri/widgets/Sketch/SketchViewModel',
                                'esri/layers/GraphicsLayer',
                                'esri/Graphic'],
        options).then(([SketchViewModel,
                        GraphicsLayer,
                        Graphic]) => {
            console.log("Entering interactive draw shape mode.");
            var shape = this.model.get("_trigger_interactive_draw_mode_for");
            if(shape){
                var view = this.activeView;
                var graphicsLayer = this.getGraphicsLayer(GraphicsLayer);
                var sketch = new SketchViewModel({
                  layer: graphicsLayer,
                  view: view,
                });
                sketch.create(shape);
                sketch.on("create", (event) => {
                    if(event.state == "complete"){
                        this.send({ event: 'draw-end',
                                    message: event.graphic.geometry.toJSON() });
                    }
                });
            }
        }).catch((err) => {
            this._displayErrorBox("Error on drawing interactive shape");
            console.warn("Error on interactive shape"); console.warn(err);
        });
   },

    trigger_jlab_window_changed: function(){
        var args = this.model.get("_trigger_new_jlab_window_with_args");
        console.log("new_jlab_window triggered with:");
        console.log(args);
        if(Object.keys(args).length !== 0){
            this.move_to_new_jlab_window(args)
        }
    },

    move_to_new_jlab_window: function(args){
        if(config.JupyterTarget !== "lab"){
            this._displayErrorBox("Can only move to new window in a " + 
                                  "JupyterLab env");
            console.warn("Can't move to new window: JupyterTarget = " + 
                          config.JupyterTarget);
            return
        }
        console.log("Attempting to move map to new jlab window...");
        var childMapElement = this.el.childNodes[0];
        console.log(childMapElement);
        if(childMapElement != null){
            //Element is currently in the notebook; so, move it to a new window
            var window_title = args.title;
            var tab_mode;
            if ("tab_mode" in args){
                tab_mode = args.tab_mode
            } else {
                tab_mode = this.model.get("tab_mode"); }
            window.newJLabWindow({title: window_title,
                                  element: childMapElement,
                                  tab_mode: tab_mode});
            //hide the icon when you're in seperate window mode
            this.elements.newWindowButton.src = images.toOriginalWindowEncoded;
            //Store the previous height of the element
            this.prevElementHeight = this.el.style.height;
            this.el.style.height = "0px";
        } else {
            //element is currently in a new window (or is somewhere else)
            //So, move it back to the notebook
            var activeMapElement = document.getElementById(
                this.elements.viewdivElement.id);
            window.closeJLabWindow({element: activeMapElement});
            this.elements.newWindowButton.src = images.toNewWindowEncoded;
            this.el.style.height = this.prevElementHeight;
        }
    },

    portal_token_changed: function(){
    try{
        var _portal_token = this.model.get("_portal_token");
        if(_portal_token){
            console.log("updating _portal_token...");
            this._portalToken = _portal_token;
            globalTokenLookup[this.uuid] = _portal_token;
            this.model.set("_portal_token", "");
            this.model.save_changes();
        }
    } catch (err) {
        this._displayErrorBox("Error storing token.");
        console.warn("Error storing token."); console.warn(err);
    }
    },

    get_portal_token: function(){
        // The portal token doesn't exist in the model for long due to security
        // concerns: this function should return the string of any token,
        // regardless of what state the token transfer is in
        if(this._portalToken){
            return this._portalToken;
        } else if (this.uuid in globalTokenLookup){
            return globalTokenLookup[this.uuid];
        } else {
            return this.model.get("_portal_token");
        }
    },

    authenticate_to_portal: function(){
        ///Given all relevant information in the model, attempt to authenticate
        ///to the portal, then return the portal. Then, resolve the portal obj
        ///On any error, reject the Promise
        ///The _portal_token should be deleted and set to this before this
        ///function is called if you're planning on using auth
    return new Promise((resolve, reject) => {
        esriLoader.loadModules(['esri/config',
                                'esri/identity/ServerInfo',
                                'esri/identity/IdentityManager',
                                'esri/portal/Portal'],
        options).then(([esriConfig,
                        ServerInfo,
                        IdentityManager,
                        Portal]) => {
            var _auth_mode = this.model.get("_auth_mode");
            if(('_portal' in this) && (this._portal.loaded)){
                //If we've previously set up a portal & its loaded, resolve it
                resolve(this._portal);
            } else if(_auth_mode.toLowerCase() === "anonymous"){
                //If we specified an anonymous connection, load it and resolve
                var _portal_url = this.model.get("_portal_url");
                if(_portal_url !== ""){
                    esriConfig.portalUrl = _portal_url;
                }
                this._portal = new Portal({authMode: 'anonymous'});
                this._portal.load().then(() => {
                    resolve(this._portal);
                }).catch((err) => {
                    reject(err);
                });
            } else if (_auth_mode.toLowerCase() === "tokenbased"){
                //If we specified token based authentication, attempt to resolve it
                var _portal_url = this.model.get("_portal_url");
                var _portal_sharing_rest_url = this.model.get("_portal_sharing_rest_url");
                var _portal_token = this.get_portal_token();
                if(!(_portal_url && _portal_sharing_rest_url && _portal_token)){
                    var rejMsg = "_portal_url, _portal_sharing_rest_url, and _portal_token " + 
                        "must be specified to authenticate in 'tokenBased' auth mode. " +
                        "_portal_url = " + _portal_url + ", _portal_sharing_rest_url = " +
                        _portal_sharing_rest_url + ", _portal_token = " + this._portalToken;
                    reject(rejMsg);
                } else {
                    var serverInfo = new ServerInfo();
                    serverInfo.server = _portal_sharing_rest_url;
                    serverInfo.tokenServiceUrl = _portal_sharing_rest_url + 'generateToken';
                    IdentityManager.registerServers([serverInfo]);
                    IdentityManager.registerToken({"server": _portal_sharing_rest_url,
                                                  "userId": this.model.get("_username"),
                                                  "token": _portal_token});
                    //Needed for IWA authentication in DSX mode - dv
                    esriConfig.request.trustedServers.push(_portal_url);
                    console.log("esriConfig.request.trustedServers = ");
                    console.log(esriConfig.request.trustedServers);
                    //End IWA workaround section
                    this._portal = new Portal({
                        url: _portal_url});
                    this._portal.load().then(() => {
                        resolve(this._portal);
                    }).catch((err) => {
                        reject(err);
                    });
                }
            } else if (_auth_mode.toLowerCase() === "prompt"){
                var _portal_url = this.model.get("_portal_url");
                if(_portal_url !== ""){
                    esriConfig.portalUrl = _portal_url;
                }
                this._portal = new Portal({
                    authMode: 'immediate',
                    allSSL: false,
                    canSignInArcGIS: true,
                    canSignInIDP: true,
                    authorizedCrossOriginDomains: [esriConfig.portalUrl,]});
                this._portal.load().then(() => {
                    resolve(this._portal);
                }).catch((err) => {
                    reject(err);
                });
             } else {
                reject("You must specify the '_auth_mode' model variable to " + 
                       "either 'anonymous', 'tokenbased', or 'prompt'");
            }
        }).catch((err) => {
                reject(err);
            });
    })},

    js_cdn_changed: function() {
        var fallback_cdn = this.model.get("_js_cdn_override");
        if(fallback_cdn !== ""){
            configureCDN(config, fallback_cdn);
            console.log("CDN changed: new config = ");
            console.log(config);
            options = config.EsriLoaderOptions;
            this._check_js_api_version_loaded(fallback_cdn);
            css_url = fallback_cdn + "esri/css/main.css"
            if(config.JupyterTarget === "notebook"){
                esriLoader.setRequireJSConfig(config.BaseRequireJSConfig);
                //TODO: remove this jquery for notebook css adding
                $('head').append($('<link rel="stylesheet" type="text/css" />'
                    ).attr('href', css_url));
            } else if(config.JupyterTarget === "lab"){
                esriLoader.loadCss(css_url)
            }
            esriLoader.loadModules(['esri/config'],
            options).then(([esriConfig,]) => {
                esriConfig.request.corsEnabledServers.push(fallback_cdn)
            }).catch((err) => {
                console.log("Error while setting fallback cdn");
                console.log(err);
            });
        }
    },

    legend_prop_changed: function() {
        try{
            console.log("legend changed");
            var widgetCorner = "bottom-right";
            var legendProp = this.model.get("legend");
            if(legendProp){
                this.activeView.ui.empty(widgetCorner);
                this._legend.view = this.activeView;
                this.activeView.ui.add(this._legend, widgetCorner);
            } else {
                this.activeView.ui.empty(widgetCorner);
            }
        } catch(err) {
            console.log("Error while trying to show legend.");
            console.log(err);
        }
    },

    time_slider_prop_changed: function(){
        try{
            console.log("time slider changed");
            var widgetCorner = "bottom-left";
            var timeSliderProp = this.model.get("time_slider");
            if(timeSliderProp){
                this.activeView.ui.empty(widgetCorner);
                this._time_slider.view = this.activeView;
                this.activeView.ui.add(this._time_slider, widgetCorner);
            } else {
                this.activeView.ui.empty(widgetCorner);}
        } catch(err) {
            this._displayErrorBox("Error while updating time slider");
            console.warn("Error while trying to show time slider");
            console.warn(err);}
    },

    time_mode_changed: function(){
        try{
            var timeSlider = this.model.get("time_slider");
            if(timeSlider){
                console.log("time mode changed");
                var timeMode = this.model.get("time_mode");
                var values = this._time_slider.values;
                this._time_slider.mode = timeMode;
                if(values.length > 0){
                    if(timeMode === "instant"){
                        this._time_slider.values = [values[0],];}
                    if(timeMode === "time-window"){
                        if(values.length == 1){
                            this._time_slider.values = [
                                values[0],
                                values[0]];}}
                    if(timeMode === "cumulative-from-start"){
                        this._time_slider.values = [values[0],];}
                    if(timeMode === "cumulative-from-end"){
                        this._time_slider.values = [values[0],];}}}}
        catch(err){
            this._displayErrorBox("Error while updating time mode");
            console.warn("Error while trying updating time mode"); console.warn(err);}
    },

    time_slider_values_changed: function(values){
        if(values.length == 2){
            this.model.set("_readonly_start_time", values[0].toISOString());
            this.model.set("_readonly_end_time", values[1].toISOString());}
        if(values.length == 1){
            this.model.set("_readonly_start_time", values[0].toISOString());}
        this.model.save_changes();
    },

    time_info_changed: function(){
    esriLoader.loadModules(['esri/TimeExtent',
                            'esri/TimeInterval'],
    options).then(([TimeExtent, TimeInterval]) => {
        var timeInfo = this.model.get("_time_info");
        console.log("Time Info changed");
        console.log(timeInfo);
        if('time_extent' in timeInfo){
            var start = new Date(timeInfo.time_extent[0]);
            var end = new Date(timeInfo.time_extent[1]);
            this._time_slider.fullTimeExtent = new TimeExtent({
                                               start: start,
                                               end: end});}
        var intervalValue = 1;
        var intervalUnit = 'milliseconds';
        if('interval' in timeInfo){
            intervalValue = timeInfo.interval;}
        if('unit' in timeInfo){
            intervalUnit = timeInfo.unit;}
        this._time_slider.stops = {"interval" : new TimeInterval({
            value: intervalValue,
            unit: intervalUnit})};
    }).catch((err) => {
        this._displayErrorBox("Error while changing the time info");
        console.warn("Error while trying to change the time info");
        console.warn(err);});
    },

    start_time_changed: function(){
        try{
            console.log("start time changed");
            var startTimeStr = this.model.get("_writeonly_start_time");
            var startTime = new Date(startTimeStr);
            if(this._time_slider.values.length == 1){
                this._time_slider.values = [startTime,];}
            if(this._time_slider.values.length == 2){
                var endTime = this._time_slider.values[1];
                this._time_slider.values = [startTime, endTime];}}
        catch(err){
            this._displayErrorBox("Error while changing `start_time`");
            console.warn("Error while changing start_time");
            console.warn(err);}
    },

    end_time_changed: function(){
        try{
            console.log("end time changed");
            var endTimeStr = this.model.get("_writeonly_end_time");
            var endTime = new Date(endTimeStr);
            var startTime = this._time_slider.values[0];
            this._time_slider.values = [startTime, endTime];}
        catch(err){
            this._displayErrorBox("Error while changing `end_time`");
            console.warn("Error while changing `end_time`");
            console.warn(err);}
    },

    // Start screenshot section
    _trigger_screenshot_with_args_changed: function() {
        var args = this.model.get('_trigger_screenshot_with_args');
        console.log("Triggering Screenshot with args ");
        console.log(args);
        modelStrsToSendTo = [];
        if(args.set_as_preview){
            modelStrsToSendTo.push('_preview_screenshot_callback_resp');
        }
        if(args.output_in_cell){
            modelStrsToSendTo.push("_cell_output_screenshot_callback_resp");
        }
        if(args.file_path){
            modelStrsToSendTo.push("_file_output_screenshot_callback_resp");
        }
        this._capture_screenshot_send_to(modelStrsToSendTo);
    },

    _capture_screenshot_send_to: function(modelStrsToSendTo) {
        var mode = this.model.get('mode');
        var funcToCall = "";
        if(mode === "3D"){
            funcToCall = this._get_3d_screenshot;
        } else if(mode === "2D"){
            funcToCall = this._get_2d_screenshot;
        }
        funcToCall(this).then((base64Str) => {
            for(var i in modelStrsToSendTo){
                var modelStr = modelStrsToSendTo[i];
                this.model.set(modelStr, base64Str);
            }
            this.touch();
        }).catch((err) => {
            console.log("Could not take screenshot"); console.log(err);
            this._displayErrorBox("Could not take screenshot.");
            for(var i in modelStrsToSendTo){
                console.log("sending " + modelStr + " to ");
                var modelStr = modelStrsToSendTo[i];
                this.model.set(modelStr, images.screenshotErrorEncoded);
            }
            this.touch();
        });
    },

    _get_2d_screenshot: function(widget_inst) {
        return new Promise((resolve, reject) => {
            widget_inst._MapView.takeScreenshot({format:"png"}).then((screenshot) => {
                resolve(screenshot.dataUrl);
            }).catch((err) => {
                reject(err);
            });
        });
    },

    _get_3d_screenshot: function(widget_inst) {
        return new Promise((resolve, reject) => {
            widget_inst._SceneView.takeScreenshot({format:"png"}).then((screenshot) => {
                resolve(screenshot.dataUrl);
            }).catch((err) => {
                reject(err);
           });
        });
    },

    // End screenshot section

    // Start image overlay section

    overlay_these_images_on_widget_load: function(){
        var images = this.model.get("_overlay_these_images_on_widget_load");
        for(var i=0; i<images.length; i++){
            var image = images[i];
            this.overlay_this_image(image);
        }
    },

    overlay_image_changed: function(){
        var image = this.model.get("_overlay_this_image");
        this.overlay_this_image(image);
    },

    getActiveImageOverlayLayer: function(ImageOverlayLayer){
        ///All graphics are drawn on 1 layer: return it if it's been made,
        ///Make it if it hasn't
        var imageOverlayLayer = this.map.findLayerById(imageOverlayLayerId);
        if(typeof imageOverlayLayer === "undefined"){
            imageOverlayLayer = new ImageOverlayLayer({
                id: imageOverlayLayerId});
            this.map.add(imageOverlayLayer);}
        return imageOverlayLayer;
    },

    overlay_this_image: function(image){
    if(Object.keys(image).length !== 0){
        if(config.JupyterTarget === "lab"){
            //JupyterLab handles URLs differently than classic notebook server.
            //Change the image path to the full path prepended by `/tree/`
            //See: https://jupyterlab.readthedocs.io/en/stable/user/urls.html
            //TODO: consider using `ContentsManager` from `@jupyterlab/services`
            //Ref: https://jupyterlab.github.io/jupyterlab/services/index.html
            var nbPath = this.model.widget_manager.context.session.path;
            var nbName = this.model.widget_manager.context.session.name;
            var nbDir = nbPath.substring(0, nbPath.lastIndexOf(nbName));
            image.src = "/tree/" + nbDir + image.src;}

        getImageOverlayLayerType().then((ImageOverlayLayer) => {
            var imageOverlayLayer = this.getActiveImageOverlayLayer(ImageOverlayLayer);
            imageOverlayLayer.tryOverlayImage(image).catch((err) => {
                if(err.message.includes("NetworkError")){
                    this._displayErrorBox("Error overlaying image (uhandled "+
                        "NetworkError). You probably specified an image URL "+
                        "that violate browser security rules (CORs, etc).");
                } else if(err.name.includes("BadHTTPStatusError")) {
                    this._displayErrorBox("Error overlaying image (URL " + 
                        "return status " + err.status + "). ");
                } else {
                    this._displayErrorBox("Error on overlaying image.");}
                console.warn("Error on overlaying image"); console.warn(err);
            });
        }).catch((err) => {
            this._displayErrorBox("Error getting ImageOverlayLayer type:");
            console.log("Error getting ImageOverlayLayer type"); console.log(err);
        });
        }
    },

    image_overlays_to_remove_changed: function(){
        var overlaysToRemove = this.model.get('_image_overlays_to_remove')
        getImageOverlayLayerType().then((ImageOverlayLayer) => {
            var imageOverlayLayer = this.getActiveImageOverlayLayer(ImageOverlayLayer);
            imageOverlayLayer.tryRemoveImageOverlays(overlaysToRemove);
        }).catch((err) => {
            this._displayErrorBox("Error getting ImageOverlayLayer type:");
            console.log("Error getting ImageOverlayLayer type:"); console.log(err);
        });
    },

    // End image overlay section

    _check_js_api_version_loaded: function(fallback_cdn){
        this._httpGetAsync(fallback_cdn).then((response) => {
            //TODO: find better parsing logic for finding out what version
            var lines = response.split("\n");
            var copyrightLine = null; //copyright.txt line link contains version #
            for(var i = 0; i < lines.length; i++){
                var line = lines[i];
                if((line.indexOf("js.arcgis.com") !== -1) && 
                   (line.indexOf("copyright.txt") !== -1)){
                    copyrightLine = line;
                    break;
                }
            }
            if(copyrightLine !== null){
                console.log("Copyright line = '" + copyrightLine + "'");
                var versionNum = copyrightLine.split(
                    "js.arcgis.com/")[1].split("/esri")[0];
                if (versionNum < config.minJSAPIVersion){
                    console.warn("JS API " + versionNum + " < " + config.minJSAPIVersion);
                    this._displayErrorBox("Warning: the ArcGIS API for JavaScript " + 
                        "being loaded at " + fallback_cdn + " does not appear to be " +
                        ">=" + config.minJSAPIVersion + ". Widget may not function " + 
                        "properly.", browser_console_message=false);
                }
            } else {
                console.warn("Could not infer javascript version");
                this._displayErrorBox("Warning: Could not infer version of any " +
                    "loaded ArcGIS API for JavaScript. Widget may not function " +
                    "properly.", browser_console_message=false);
            }
        }).catch((err) => {
            console.log("Could not reach the fallback cdn...");
            console.log(err);
        });
    },

    _httpGetAsync : function(theUrl){
        return new Promise((resolve, reject) => {
            fetch(theUrl, {mode: 'cors'}).then((response) => {
                if (response.status >= 200 && response.status < 300){
                    response.text().then((data) => {
                        resolve(data);
                    }).catch((err) => {
                        reject(err);
                    });
                } else {
                    reject("HTTP request on " + theUrl + 
                           " returned code " + status);
                }
            })
        })
    },
});

module.exports = ArcGISMapIPyWidgetView;

