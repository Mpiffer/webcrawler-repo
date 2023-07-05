```javascript
// Fetch the data from the JSON file
fetch('scraper/data.json')
  .then(response => response.json())
  .then(data => {
    // Use the data to populate the website
    populateWebsite(data);
  })
  .catch(error => console.error('Error:', error));

// Function to populate the website with data
function populateWebsite(data) {
  // Get the HTML elements by their IDs
  const redditDataElement = document.getElementById('reddit-data');

  // Clear the existing content
  redditDataElement.innerHTML = '';

  // Add the new data
  data.forEach(item => {
    const itemElement = document.createElement('div');
    itemElement.classList.add('reddit-item');
    itemElement.innerHTML = `
      <h2>${item.title}</h2>
      <p>${item.content}</p>
    `;
    redditDataElement.appendChild(itemElement);
  });
}
```