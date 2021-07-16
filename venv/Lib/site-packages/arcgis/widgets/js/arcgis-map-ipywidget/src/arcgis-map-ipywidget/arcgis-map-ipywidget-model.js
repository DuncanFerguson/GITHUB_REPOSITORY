//The main module that exports the javascript widget class

//import all external modules
const widgets = require('@jupyter-widgets/base');
const _ = require('lodash');
const version = require('../../package.json').version;

// The Model that stores state on the javascript side
var ArcGISMapIPyWidgetModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name : 'ArcGISMapIPyWidgetModel',
        _view_name : 'ArcGISMapIPyWidgetView',
        _model_module : 'arcgis-map-ipywidget',
        _view_module : 'arcgis-map-ipywidget',
        _model_module_version : version,
        _view_module_version : version,

        value : 'From Scene Model',

        //start map specific draw state
        _basemap: "topo",
        _gallery_basemaps: {},
        mode: "2D",
        _zoom: -1,
        _readonly_zoom: -1,
        _scale: -1,
        _snap_to_zoom: true,
        _readonly_scale: -1,
        _rotation: 0,
        _readonly_rotation: 0,
        _link_writeonly_rotation: 0,
        _heading: 0,
        _readonly_heading: 0,
        _link_writeonly_heading: 0,
        _tilt: 0,
        _readonly_tilt: 0,
        _link_writeonly_tilt: 0,
        _extent: {},
        _readonly_extent: {},
        _link_writeonly_extent: {},
        _center: {},
        _readonly_center: {},
        _center_long_lat: [],
        //end map specific draw state
        //start layer specific model state
        _func_chains: [],
        _add_this_notype_layer: {},
        _readonly_notype_layers: {},
        _draw_these_notype_layers_on_widget_load: {},
        _layers_to_remove: [],
        _add_this_graphic: {},
        _draw_these_graphics_on_widget_load: {},
        //end layer specific model state
        //start webmap/webscene state
        _webmap: {},
        _webscene: {},
        _trigger_webscene_save_to_this_portal_id: "",
        _readonly_webmap_from_js: {},
        //end webmap/webscene state

        //Start screenshot section
        _preview_screenshot_callback_resp: "",
        _cell_output_screenshot_callback_resp: "",
        _file_output_screenshot_callback_resp: "",
        _trigger_screenshot_with_args: {},
        //end screenshot section

        //start image overlay section
        _overlay_this_image: {},
        _overlay_these_images_on_widget_load: {},
        _image_overlays_to_remove: [],
        //end image overlay section

        //start time information
        time_slider: false,
        time_mode: "time-window",
        _time_info: {},
        _writeonly_start_time: "",
        _readonly_start_time: "",
        _writeonly_end_time: "",
        _readonly_end_time: "",
        //end time info

        //start miscellanous model state
        _portal_token: "",
        _auth_mode: "",
        _portal_url: "",
        _portal_sharing_rest_url: "",
        _username: "",
        _custom_msg: "",
        hide_mode_switch: false,
        _trigger_interactive_draw_mode_for: "",
        _trigger_new_jlab_window_with_args: {},
        jupyter_target: "",
        ready: false,
        tab_mode: "auto",
        _js_cdn_override: "",
        legend: false,
        _uuid: "",
        _trigger_print_js_debug_info: "",
        //end miscellanous modle state


    })
});

module.exports = ArcGISMapIPyWidgetModel;
