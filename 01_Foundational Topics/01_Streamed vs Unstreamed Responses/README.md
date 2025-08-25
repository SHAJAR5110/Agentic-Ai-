

# 📘 Streamed vs Unstreamed Responses

When working with the **OpenAI SDK**, responses can be delivered in two modes: **Unstreamed** and **Streamed**. Understanding the difference helps in choosing the right approach depending on your application.



## 🔹 Unstreamed Responses

* The model **generates the full response internally** before sending it back.
* The user/application **receives the complete output at once**.
* Simpler to implement but may feel slow for longer outputs.

**Use Case Examples:**

* Getting a final summarized report.
* One-shot answers (e.g., math solution, SQL query).



## 🔹 Streamed Responses

* The model **sends chunks of the response as they are generated**.
* The user/application **receives output in real time**, like a typing effect.
* Provides a faster, more interactive experience for longer replies.

**Use Case Examples:**

* Chatbots where users see answers appear live.
* Code generation where step-by-step output is useful.



## 📊 Comparison Table

| Feature             | Unstreamed Response                 | Streamed Response                      |
| ------------------- | ----------------------------------- | -------------------------------------- |
| **Delivery**        | Full output at once                 | Sent in chunks (real-time)             |
| **User Experience** | Wait until complete answer          | Immediate feedback, typing-like effect |
| **Implementation**  | Easy to set up                      | Requires handling streaming events     |
| **Best For**        | Short/simple queries, final reports | Chatbots, long texts, interactive apps |
| **Performance**     | Slower perceived response           | Faster, continuous response flow       |


