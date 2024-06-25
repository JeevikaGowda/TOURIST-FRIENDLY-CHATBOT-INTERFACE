document.addEventListener("DOMContentLoaded", function () {
  const chatbotToggler = document.querySelector(".chatbot-toggler");
  const chatbot = document.querySelector(".chatbot");
  const closeBtn = document.querySelector(".chatbot header .close-btn");
  const chatbox = document.querySelector(".chatbox");
  const chatInput = document.querySelector(".chat-input textarea");
  const sendBtn = document.getElementById("send-btn");

  let responses = []; // Array to store responses from JSON

  // Fetch responses from JSON
  fetch("../static/responses.json")
    .then((response) => response.json())
    .then((data) => {
      responses = data.responses;

      // Open/close chatbot
      chatbotToggler.addEventListener("click", function () {
        document.body.classList.toggle("show-chatbot");
      });

      closeBtn.addEventListener("click", function () {
        document.body.classList.remove("show-chatbot");
      });

      // Send message
      sendBtn.addEventListener("click", function () {
        sendMessage();
      });

      chatInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
          event.preventDefault();
          sendMessage();
        }
      });
    })
    .catch((error) => console.error("Error fetching responses:", error));

  // Function to send user message
  function sendMessage() {
    const userMessage = chatInput.value.trim();
    if (userMessage === "") return;

    appendMessage("outgoing", userMessage);

    // Send user input to Flask server
    fetch("/chatbot/chatbot", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ userInput: userMessage }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.image_url) {
          appendMessage("incoming", null, data.image_url);
        }
        appendMessage("incoming", data.answer);
      })
      .catch((error) => {
        console.error("Error:", error);
        appendMessage("incoming", "I'm sorry, an error occurred.");
      });

    chatInput.value = "";
  }

  // Function to find response in JSON
  function findResponse(userInput) {
    let maxSimilarity = 0;
    let bestResponse = null;

    for (const pair of responses) {
      if (pair && pair.question) {
        const similarity = similarityScore(userInput, pair.question);

        // Exact match
        if (similarity === 1) {
          bestResponse = pair;
          break;
        }

        // Check if the similarity is higher than the threshold
        if (similarity > 0.6) {
          // Adjust the threshold as needed
          maxSimilarity = similarity;
          bestResponse = pair;
        }
      }
    }

    return bestResponse;
  }

  function similarityScore(str1, str2) {
    // Remove repeated characters and punctuation from the input strings
    const cleanStr1 = str1
      .toLowerCase()
      .replace(/mysore/gi, "mysuru")
      .replace(/(.)\1+/g, "$1")
      .replace(/[^a-z0-9\s]/g, "");
    const cleanStr2 = str2
      .toLowerCase()
      .replace(/mysore/gi, "mysuru")
      .replace(/(.)\1+/g, "$1")
      .replace(/[^a-z0-9\s]/g, "");

    const words1 = cleanStr1.split(/\s+/);
    const words2 = cleanStr2.split(/\s+/);

    let intersection = 0;
    const uniqueWords = new Set([...words1, ...words2]);

    for (const word of uniqueWords) {
      const count1 = words1.filter((w) => w === word).length;
      const count2 = words2.filter((w) => w === word).length;
      intersection += Math.min(count1, count2);
    }

    const unionLength = words1.length + words2.length - intersection;

    // Give higher similarity score for exact phrase matches
    if (cleanStr1 === cleanStr2) {
      return 1;
    }

    // Check if the shorter string is a subset of the longer string
    const shorterWords = words1.length < words2.length ? words1 : words2;
    const longerWords = words1.length < words2.length ? words2 : words1;
    let isSubset = true;
    for (const word of shorterWords) {
      if (!longerWords.includes(word)) {
        isSubset = false;
        break;
      }
    }

    if (isSubset) {
      return 0.8; // Adjust the similarity score for subset matches as needed
    }

    // Calculate word order similarity
    let wordOrderSimilarity = 0;
    const maxLength = Math.max(words1.length, words2.length);
    for (let i = 0; i < maxLength; i++) {
      const word1 = words1[i] || "";
      const word2 = words2[i] || "";
      if (word1 === word2) {
        wordOrderSimilarity += 1;
      } else {
        wordOrderSimilarity += 0.5; // Partial match for similar words
      }
    }
    wordOrderSimilarity /= maxLength;

    // Calculate the ratio of common words to the total number of unique words
    const commonWordRatio = intersection / uniqueWords.size;

    // Combine the common word ratio, word order similarity, and intersection/union similarity
    const combinedSimilarity =
      (commonWordRatio + intersection / unionLength + wordOrderSimilarity) / 3;

    return combinedSimilarity;
  }

  // Function to append message to chatbox
  function appendMessage(type, message, imageUrl = null) {
    const listItem = document.createElement("li");
    listItem.classList.add("chat", type);

    if (imageUrl) {
      listItem.innerHTML = `
        <span class="material-symbols-outlined">smart_toy</span>
        <img src="${imageUrl}" alt="Image" class="chat-image">
      `;
    } else {
      listItem.innerHTML = `
        <span class="material-symbols-outlined">smart_toy</span>
        <p>${message || ""}</p>
      `;
    }

    chatbox.appendChild(listItem);
    chatbox.scrollTop = chatbox.scrollHeight;
  }
});
