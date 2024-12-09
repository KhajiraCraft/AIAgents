// // Fetch results from localStorage where it was saved by popup.js
// chrome.storage.local.get('analysisResult', function(result) {
//     const analysisResult = result.analysisResult;
//     const resultsContainer = document.getElementById('results-container');

//     if (analysisResult) {
//       resultsContainer.innerHTML = '';

//       // Loop through the sections of the result and display them
//       if (analysisResult.summary) {
//         const summarySection = document.createElement('div');
//         summarySection.classList.add('result-section');
//         const summaryTitle = document.createElement('div');
//         summaryTitle.classList.add('section-title');
//         summaryTitle.textContent = 'Summary';
//         summarySection.appendChild(summaryTitle);

//         const summaryContent = document.createElement('pre');
//         summaryContent.textContent = JSON.stringify(analysisResult.summary, null, 2);
//         summarySection.appendChild(summaryContent);
//         resultsContainer.appendChild(summarySection);
//       }

//       if (analysisResult.risks) {
//         const risksSection = document.createElement('div');
//         risksSection.classList.add('result-section');
//         const risksTitle = document.createElement('div');
//         risksTitle.classList.add('section-title');
//         risksTitle.textContent = 'Risks';
//         risksSection.appendChild(risksTitle);

//         const risksContent = document.createElement('pre');
//         risksContent.textContent = JSON.stringify(analysisResult.risks, null, 2);
//         risksSection.appendChild(risksContent);
//         resultsContainer.appendChild(risksSection);
//       }

//       if (analysisResult.recommendations) {
//         const recommendationsSection = document.createElement('div');
//         recommendationsSection.classList.add('result-section');
//         const recommendationsTitle = document.createElement('div');
//         recommendationsTitle.classList.add('section-title');
//         recommendationsTitle.textContent = 'Recommendations';
//         recommendationsSection.appendChild(recommendationsTitle);

//         const recommendationsContent = document.createElement('pre');
//         recommendationsContent.textContent = JSON.stringify(analysisResult.recommendations, null, 2);
//         recommendationsSection.appendChild(recommendationsContent);
//         resultsContainer.appendChild(recommendationsSection);
//       }
//     } else {
//       resultsContainer.innerHTML = '<p>No analysis results available.</p>';
//     }
//   });


chrome.storage.local.get('analysisResult', function(result) {
  const analysisResult = result.analysisResult;
  const resultsContainer = document.getElementById('results-container');

  if (analysisResult && Array.isArray(analysisResult)) {
    resultsContainer.innerHTML = '';

    // Iterate through distinct JSON objects and display them
    analysisResult.forEach((jsonObj, index) => {
      const section = document.createElement('div');
      section.classList.add('result-section');

      const title = document.createElement('div');
      title.classList.add('section-title');
      title.textContent = `Object ${index + 1}`;
      section.appendChild(title);

      const content = document.createElement('pre');
      content.textContent = JSON.stringify(jsonObj, null, 2);
      section.appendChild(content);

      resultsContainer.appendChild(section);
    });
  } else {
    resultsContainer.innerHTML = '<p>No analysis results available.</p>';
  }
});
