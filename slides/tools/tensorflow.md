# <logos-tensorflow /> TensorFlow

From Wikipedia:
- free and open-source software library for machine learning and artificial intelligence. 
- developed by the [Google Brain](https://en.wikipedia.org/wiki/Google_Brain) team
- can be used across a range of tasks but has a particular focus on training and 
  inference of **deep neural networks**
- usable in many different languages
  * primarily Python
  * has bindings for other mainstream languages 
    <span class="bg-gray-100 p-2 rounded-3xl">
      <logos-javascript /> <logos-c-plusplus /> <logos-java /> <logos-scala />
      <logos-c-sharp /> <logos-r-lang /> <logos-ruby /> <logos-rust />
    </span>
- TF 2.0 is tightly integrated with [Keras](https://keras.io/)
  * common to see code like
    ```py
    tf.keras.models.Sequential
    ```
  * high-level neural networks API, written in <logos-python />
  * supports rapid experimentation, prototyping, and has a developer-friendly API
    + 👎 comes up with the cost of losing access to the inner details of TensorFlow
