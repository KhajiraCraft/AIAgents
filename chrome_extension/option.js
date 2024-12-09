window.addEventListener('DOMContentLoaded', function() {
    // your button here
    var link = document.getElementById('btnOpenNewTab');
    // onClick's logic below:
    link.addEventListener('click', function() {
        var newURL = "http://stackoverflow.com/";
        chrome.tabs.create({ url: newURL });
    });
});