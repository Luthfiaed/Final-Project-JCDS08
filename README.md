<h1>Content-Based Movie Recommender</h1>
<hr>

<b>Objective:</b> Recommend movies by matching the plot/description of the movie being input by user.

<b>Dataset:</b>
For this project, I use the IMDb movie dataset from kaggle, accessible <a href="https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset?select=IMDb+movies.csv">here</a>.

<b>Model:</b>
I use natural language processing (NLP) technique, specifically the <b>spacy</b> python module.

<b>Steps Taken in the Project</b>:
<ol>
<li>Upload csv file to MySql, the query can be found in this repository under the name <b>mysql_query.txt</b></li>
<li>Import data from MySql to pandas Data Frame</li>
<li>Clean the dataset</li>
<li>Tokenize and lemmatize movie description using spacy in English</li>
<li>Calculate the similarity distance between each description using the <b>cosine_similarity</b> function</li>
<li>Build a recommendation function using the cosine_similarity function</li>
<li>Deploy the recommender using flask</li>
</ol>
