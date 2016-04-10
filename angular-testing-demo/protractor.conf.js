exports.config = {

    allScriptsTimeout: 11000,
    specs: [
        'test/e2e/*.js'
    ],

    capabilities: {
        'browserName': 'chrome'
    },

    chromeOnly: true,

    baseUrl: 'http://127.0.0.1:8080',

    framework: 'jasmine',
    jasmineNodeOpts: {
        defaultTimeoutInterval: 30000
    }
};

