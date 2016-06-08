describe("Hello", function() {
    it("says hello", function() {
        expect(sayHello()).toBe("Hello, world!");
    });
});


describe("A suite of basic functions", function() {
    it("reverse word",function(){
        expect(add(1,2)).toEqual(3);
    });

    it("reverse word",function(){
        expect(add(3,2)).toEqual(6);
    });
});