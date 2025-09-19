 async function getJsonFromUrl(url) {
        try {
            const response = await fetch(url); // Make the network request
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const jsonData = await response.json(); // Parse the response as JSON
            return jsonData; // Return the parsed JSON data
        } catch (error) {
            console.error("Error fetching JSON:", error);
            return null; // Handle errors gracefully
        }
    }
