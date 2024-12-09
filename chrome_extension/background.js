//
//console.log("JS is active")
//chrome.action.onClicked.addListener((tab) => {
//  // Log the captured URL for debugging purposes
//  console.log("Captured URL: ", tab.url);
//
//  // Save the URL to local storage
//  chrome.storage.local.set({ currentUrl: tab.url }, function() {
//    console.log("URL saved to local storage.");
//  });
//
//  // Send the URL to the Flask backend for processing
//  sendUrlToBackend(tab.url);
//});
//
//function sendUrlToBackend(url) {
//  const backendUrl = "http://localhost:5000/analyze";  // Flask server URL
//
//  // Send a POST request to the Flask server
//  fetch(backendUrl, {
//    method: 'POST',
//    headers: {
//      'Content-Type': 'application/json',
//    },
//    body: JSON.stringify({ url: url }),
//  })
//  .then(response => response.json())
//  .then(data => {
//    console.log("Received data from backend:", data);
//
//    // Optionally, you can store or display the results in the extension.
//    chrome.storage.local.set({ analysisResult: data }, function() {
//      console.log("Analysis result saved.");
//    });
//
//    // You can also show the result in a popup or console for debugging
//    alert("Summary: " + data.summary);  // Show summary as an alert
//  })
//  .catch(error => {
//    console.error("Error sending URL to backend:", error);
//  });
//}

console.log("JS is active");

chrome.action.onClicked.addListener((tab) => {
  console.log("Captured URL: ", tab.url);

  // Save the URL to local storage
  chrome.storage.local.set({ currentUrl: tab.url }, function() {
    console.log("URL saved to local storage.");
  });
});
