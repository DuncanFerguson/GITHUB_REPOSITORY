const path = require('path');
const version = require('./package.json').version;
const merge = require('webpack-merge');
const nodeExternals = require('webpack-node-externals');
const common = require("./webpack.common.js");

//Use the config/notebook.js file for all "require('config')" statements
resolve = {
    alias: {
            config: path.join(__dirname, 'src', 'config', 'lab')
        }
}

module.exports = merge(common, {
// Bundle for the notebook that's compatible with jupyterlab
     //
     // This bundle contains the implementation for the custom widget views and
     // custom widget.
     // It must be an amd module
     //
        entry: './src/labplugin.ts',
        target: 'node',
        externals: [nodeExternals()],
        output: {
            filename: 'arcgis-map-ipywidget-jupyterlab.js',
            path: path.resolve(__dirname, 'dist'),
            libraryTarget: 'amd'
        },
        resolve: resolve
    });
