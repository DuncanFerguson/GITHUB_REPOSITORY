import { IJupyterWidgetRegistry} from '@jupyter-widgets/base';
import { ArcGISMapIPyWidgetModel, ArcGISMapIPyWidgetView } from './arcgis-map-ipywidget/arcgis-map-ipywidget.js';
import { version } from '../package.json';
import { Widget } from "@lumino/widgets";
import { toNewWindowEncoded } from './arcgis-map-ipywidget/images/images';

import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { ICommandPalette } from '@jupyterlab/apputils';

class IPythonExtensionWidgetContainer extends Widget{
    ///The jupyterlab container class that seperates the 
    ///widget from the notebook for you to view it side-by-side 
    originalParentElement: any;
    ipywidgetElement: any;
    constructor(element, title) {
        super();
        this.ipywidgetElement = element;
        this.originalParentElement = element.parentElement
        this.originalParentElement.removeChild(element);
        this.node.appendChild(element);
        this.id = "ipywidget-external-window-container-" + Math.random().toString(36).substring(7);
        this.title.label = title;
        this.title.closable = true;
        this.addClass('IPythonExtensionWidgetContainer');
    }

    restoreToOriginalParentElement(msg){
        this.originalParentElement.appendChild(this.ipywidgetElement);
        while(this.node.hasChildNodes()){
            this.node.removeChild(this.node.lastChild);
            }
        //TODO: find more elegant solution to this ugly hack
        this.mapForAllChildrenOfIPyWidgetElement((childNode) => {
            if(childNode.id && /.*new.*window/i.test(childNode.id)){
                ///For the icon that was previously hidden, redisplay it
                childNode.src = toNewWindowEncoded;
                this.ipywidgetElement.style.height = this.ipywidgetElement.prevElementHeight;
                }
        });
    }

    mapForAllChildrenOfIPyWidgetElement(func){
        var recursiveChildDescend = function(node){
            for(var i=0; i < node.childElementCount; i++){
                var child = node.childNodes[i];
                recursiveChildDescend(child);
                func(child);}};
        recursiveChildDescend(this.ipywidgetElement);}};

/**
 * Actually create the FrontEndPlugin to export, read by the
 * appropriate JupyterLab labextension manager
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'arcgis-map-ipywidget',
  autoStart: true,
  requires: [ICommandPalette, 
             IJupyterWidgetRegistry],
  activate: (
    app: JupyterFrontEnd,
    palette: ICommandPalette,
    widgets: IJupyterWidgetRegistry
  ) => {

    //Activate the base ipywidget to work in a notebook
    const { commands, shell } = app;

    widgets.registerWidget({
        name: 'arcgis-map-ipywidget',
        version: version,
        exports: { ArcGISMapIPyWidgetModel : ArcGISMapIPyWidgetModel,
                    ArcGISMapIPyWidgetView : ArcGISMapIPyWidgetView }
    });

    //Create the commands to move that map to an external window
    //via class we've previously defined
    const newWindowCommand = 'arcgis-map-ipywidget:new-window';
    commands.addCommand(newWindowCommand, {
      label: 'Move Existing ArcGIS Map IPyWidget to Seperate Window',
      caption: '',
      execute: (args : any) => {
          if(!('element' in args)){
              alert("Do not call this command from the command window UI, " + 
                    "it is called indirectly on the Python ipywidget instance.");
          } else {
                ///TODO: Find more elegant, less global way to do this
                console.log("Attempting to create new window with these args:");
                console.log(args);
                var ipyExtWinCon = new IPythonExtensionWidgetContainer(args.element, args.title);
                shell.activateById(ipyExtWinCon.id);

                if(args.tab_mode === "auto"){
                    autoPlaceInMainArea(app, ipyExtWinCon);
                }
                else{
                    shell.add(ipyExtWinCon, "main", { mode: args.tab_mode });}}}
    });
    palette.addItem({ command: newWindowCommand, category: 'ArcGIS Map IPywidget'});
    (<any>window).newJLabWindow = (args) => {
        //Global function called by the `arcgis-map-ipywidget-view.js` file
        app.commands.execute("arcgis-map-ipywidget:new-window", args);};
    
    //Create the commands to close that map to its original location
    const closeWindowCommand = 'arcgis-map-ipywidget:close-window';
    commands.addCommand(closeWindowCommand, {
      label: 'Close Existing ArcGIS Map IPyWidget to Original Location',
      caption: '',
      execute: (args : any) => {
          if(!('element' in args)){
              alert("Do not call this command from the command window UI, " + 
                    "it is called indirectly on the Python ipywidget instance.");
          } else {
            console.log("Attempting to close window with these args:");
            console.log(args);
            var phosphorWidgets = getAllPhosphorWidgets();
                for(var j in phosphorWidgets){
                    var pwidget = phosphorWidgets[j];
                    if(pwidget.node != null){
                        for(var k in pwidget.node.children){
                            var child = pwidget.node.children[k];
                            if(child.id == args.element.id){
                                pwidget.restoreToOriginalParentElement();
                                pwidget.close();
                                break;}}}}}}
    });
    palette.addItem({ command: closeWindowCommand, category: 'ArcGIS Map IPywidget'});
    (<any>window).closeJLabWindow = function(args){
        //Global function called by the `arcgis-map-ipywidget-view.js` file
        app.commands.execute('arcgis-map-ipywidget:close-window', args);};

    //Miscellaneous helper functions
    const autoPlaceInMainArea = function(app, ipyExtWinCon){
    try{
        var numPhosphorWidgetsInMain = 0;
        var widgets = app.shell.widgets("main");
        var widget;
        while (widget = widgets.next()){
                numPhosphorWidgetsInMain++;}
        var numWidgetsInCurrentTab = app.shell._currentTabBar().titles.length;
        var numActiveWindows = numPhosphorWidgetsInMain - numWidgetsInCurrentTab + 1;
        console.log("Attempting to autoplace widget among " + numActiveWindows + 
            " other active widgets.");
        if(numActiveWindows <= 1){
            app.shell.add(ipyExtWinCon, "main", {mode: "split-right"});
        } else {
            app.shell.add(ipyExtWinCon, "main", {mode: "tab-after"});
        }
    } catch(err) {
        console.log("Unhandled error while 'auto' mode of placing tabs" + 
            ". Just adding this widget in 'tab-after' mode");
        console.log(err);
        app.shell.add(ipyExtWinCon, "main", {mode: "tab-after"});}};

    const getAllPhosphorWidgets = function(){
        var outputWidgets = []
        var areas = ['main', 'left', 'right', 'top', 'bottom'];
        for(var i in areas){
            var area = areas[i];
            try{
                var widgets = app.shell.widgets(area);
                var widget;
                while (widget = widgets.next()){
                    outputWidgets.push(widget);}
        } catch(err) {
            //ignore errors, since not all jlab instances have all of
            //left, right, top, bottom, etc.
        }}
    return outputWidgets;}}

};

export default extension;