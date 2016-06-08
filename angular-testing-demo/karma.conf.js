module.exports = function(config) {
    config.set({
        basePath: '.',
        frameworks: ['jasmine'],
        files: [
            "../bower_components/angular/angular.js",
            '../bower_components/angular-route/angular-route.js',
            '../bower_components/angular-mocks/angular-mocks.js',
            
            'app/js/*.js',
            'test/unit/*_spec.js'
        ],
        exclude: [
        ],
        plugins: [
            'karma-chrome-launcher',
            'karma-jasmine',
        ],
        browsers: ['Chrome'],
        autoWatch: true,
        reporters: ['progress'],
        // Continuous Integration mode
        // if true, it capture browsers, run tests and exit
        singleRun: true,
        // enable / disable colors in the output (reporters and logs)
        colors: true,
    })
}