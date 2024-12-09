


// Fetch the stored analysis result
//chrome.storage.local.get(['analysisResult'], function(result) {
//  if (result.analysisResult) {
//    document.getElementById('summary').textContent = "Summary: " + result.analysisResult.summary;
//    document.getElementById('risks').textContent = "Risks: " + result.analysisResult.risks;
//    document.getElementById('recommendations').textContent = "Recommendations: " + result.analysisResult.recommendations;
//  } else {
//    document.getElementById('summary').textContent = "No result available";
//  }
//});


// document.getElementById('summarizeBtn').addEventListener('click', function() {
//   // Get the active tab's URL
//   chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//     if (tabs && tabs[0]) {
//       const currentUrl = tabs[0].url;  // The URL of the active tab

//       // Call the function to send URL to the backend for analysis
//       sendUrlToBackend(currentUrl);
//     } else {
//       alert('No active tab found.');
//     }
//   });
// });

// // Function to send URL to backend and display the result
// function sendUrlToBackend(url) {
//   const backendUrl = "http://localhost:5000/analyze";  // Flask server URL

//   // Send a POST request to the Flask server
//   fetch(backendUrl, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({ url: url }),
//   })
//   .then(response => response.json())
//   .then(data => {
//     console.log("Received data from backend:", data);

//     // Store the result in local storage
//     chrome.storage.local.set({ analysisResult: data }, function() {
//       console.log("Analysis result saved.");
//     });

//     // Display the results in the popup
//     document.getElementById('summary').textContent = "Summary: " + data.summary;
//     document.getElementById('risks').textContent = "Risks: " + data.risks;
//     document.getElementById('recommendations').textContent = "Recommendations: " + data.recommendations;
//   })
//   .catch(error => {
//     console.error("Error sending URL to backend:", error);
//     alert("Failed to fetch analysis. Please try again.");
//   });
//   chrome.tabs.create({ url: 'https://www.google.com' });
// }




// document.getElementById('summarizeBtn').addEventListener('click', function() {
//   // Get the active tab's URL
//   chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//     if (tabs && tabs[0]) {
//       const currentUrl = tabs[0].url;  // The URL of the active tab

//       // Call the function to send URL to the backend for analysis
//       sendUrlToBackend(currentUrl);
      
//       // Open the results page (results.html)
//       chrome.tabs.create({ url: chrome.runtime.getURL('results.html') });
//     } else {
//       alert('No active tab found.');
//     }
//   });
// });

// // Function to send URL to backend and display the result
// function sendUrlToBackend(url) {
//   const backendUrl = "http://localhost:5000/analyze";  // Flask server URL

//   // Send a POST request to the Flask server
//   fetch(backendUrl, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({ url: url }),
//   })
//   .then(response => response.json())
//   .then(data => {
//     console.log("Received data from backend:", data);

//     // Store the result in local storage
//     chrome.storage.local.set({ analysisResult: data }, function() {
//       console.log("Analysis result saved.");
//     });

//     // Optional: If you want to directly pass the data through URL parameters
//     const params = new URLSearchParams({
//       summary: data.summary,
//       risks: data.risks,
//       recommendations: data.recommendations
//     }).toString();

//     // Open the results page with URL parameters
//     chrome.tabs.create({
//       url: chrome.runtime.getURL(`results.html?${params}`)
//     });
//   })
//   .catch(error => {
//     console.error("Error sending URL to backend:", error);
//   });
// }




// document.getElementById('summarizeBtn').addEventListener('click', function() {
//   // Get the active tab's URL
//   chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//     if (tabs && tabs[0]) {
//       const currentUrl = tabs[0].url;  // The URL of the active tab

//       // Call the function to send URL to the backend for analysis
//       sendUrlToBackend(currentUrl);
      
//       // Open the results page (results.html)
//       chrome.tabs.create({ url: chrome.runtime.getURL('results.html') });
//     } else {
//       alert('No active tab found.');
//     }
//   });
// });

// // Function to send URL to backend and display the result
// function sendUrlToBackend(url) {
//   const backendUrl = "http://localhost:5000/analyze";  // Flask server URL

//   // Send a POST request to the Flask server
//   fetch(backendUrl, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({ url: url }),
//   })
//   .then(response => response.json())
//   .then(data => {
//     console.log("Received data from backend:", data);

//     // Store the result in local storage
//     chrome.storage.local.set({ analysisResult: data }, function() {
//       console.log("Analysis result saved.");
//     });

//     // Open the results page (results.html)
//     chrome.tabs.create({ url: chrome.runtime.getURL('results.html') });
//   })
//   .catch(error => {
//     console.error("Error sending URL to backend:", error);
//   });
// }




// document.getElementById('summarizeBtn').addEventListener('click', function() {
//   chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//     if (tabs && tabs[0]) {
//       const currentUrl = tabs[0].url;

//       // Send the URL to the backend
//       sendUrlToBackend(currentUrl);

//       // Notify the user
//       document.getElementById('status').textContent = "Processing... please wait.";
//     } else {
//       alert('No active tab found.');
//     }
//   });
// });

// function sendUrlToBackend(url) {
//   const backendUrl = "http://localhost:5000/analyze";

//   fetch(backendUrl, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({ url }),
//   })
//     .then(response => response.json())
//     .then(data => {
//       console.log("Received data from backend:", data);

//       // Store the analysis results in local storage
//       if (data.distinct_json_objects) {
//         chrome.storage.local.set({ analysisResult: data.distinct_json_objects }, function() {
//           console.log("Analysis result saved.");
//           // Open the results page to display data
//           chrome.tabs.create({ url: chrome.runtime.getURL('results.html') });
//         });
//       } else {
//         console.error("No distinct_json_objects found in response.");
//         document.getElementById('status').textContent = "Error: Invalid response.";
//       }
//     })
//     .catch(error => {
//       console.error("Error sending URL to backend:", error);
//       document.getElementById('status').textContent = "Error occurred. Try again.";
//     });
// }

document.getElementById('summarizeBtn').addEventListener('click', function() {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    if (tabs && tabs[0]) {
      const currentUrl = tabs[0].url;

      // Send the URL to the backend
      sendUrlToBackend(currentUrl);
    } else {
      alert('No active tab found.');
    }
  });
});

function sendUrlToBackend(url) {
  const backendUrl = "http://localhost:5000/analyze";

  fetch(backendUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url }),
  })
    .then(response => response.json())
    .then(data => {
      if (data.message) {
        console.log("Processing started:", data.message);
        // Redirect user to the results page
        chrome.tabs.create({ url: "http://localhost:5000/results" });
      } else {
        console.error("Error:", data.error || "Unexpected response.");
      }
    })
    .catch(error => {
      console.error("Error sending URL to backend:", error);
    });
    chrome.tabs.create({ url: 'http://localhost:5000/results' });
}
