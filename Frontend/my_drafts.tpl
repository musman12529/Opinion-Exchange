<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="styles.css">
    <title>Forum Home</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="/home">Home</a></li>
                <li><a href="/mydrafts">My Drafts</a></li>
                <li><a href="/">Logout</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>My Drafts</h1>
        <div class="search-bar">
            <input type="text" id="searchInput" placeholder="Search drafts by topic or author..." />
        </div>
        <div id="container">
            % for review in reviews:
            %if review.get_draft():
            <div class="post">
                <h2><a href="/post/${data[i]['getID']}" contenteditable="true">{{review.get_topic()}}</a></h2>
                <div class="author" style="display: flex; align-items: center; gap: 10px;">
                    <img
                        width="40px"
                        src="https://api.dicebear.com/7.x/bottts-neutral/svg?seed={{review.get_author()['id']}}"
                        alt="avatar"
                    />
                    {{review.get_author()["username"]}}
                </div>
                <p contenteditable="true">{{review.get_body()}}</p>
                <button>Update Draft</button>
                <button>Post Draft</button>
                <button>Delete Draft</button>
            </div>
            % end
            % end
        </div>
    </main>

    <script>


        const searchInput = document.getElementById("searchInput");
        searchInput.addEventListener("input", function () {
            const searchTerm = searchInput.value.toLowerCase();
            const allDrafts = document.querySelectorAll(".post");
            allDrafts.forEach((draft) => {
                const topic = draft.querySelector("h2 a").textContent.toLowerCase();
                const author = draft.querySelector("p").textContent.toLowerCase();
                if (topic.includes(searchTerm) || author.includes(searchTerm)) {
                    draft.style.display = "block";
                } else {
                    draft.style.display = "none";
                }
            });
        });
    </script>
</body>

</html>