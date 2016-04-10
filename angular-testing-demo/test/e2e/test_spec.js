describe("e2e demo", function() {

    describe('Inactive with web pages', function() {

        // This one got error
        // it('should access google', function() {
        //     browser.driver.get('https://www.google.com');
        //     expect(browser.getTitle()).toEqual('Google');

        //     browser.driver.sleep(3000);
        // });

        it('should have a title', function() {
            browser.get('/angular-testing-demo/app/');
            expect(browser.getTitle()).toEqual('This is a angular testing page');
        });

        it('shoul get correct full name', function() {
            browser.get('/angular-testing-demo/app/');

            var firstName = element(by.model("firstName"));
            var lastName = element(by.id("input_lastName"));

            var button = element(by.id("button_getFullName"));

            firstName.sendKeys('lazy');
            lastName.sendKeys('gang');
            button.click();

            var fullName = element(by.id("input_fullName"));
            fullNameStr = fullName.getAttribute('value')
            expect(fullNameStr).toEqual('lazy gang');

            browser.driver.sleep(3000);
        });
    });
});